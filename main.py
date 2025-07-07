import logging
import threading
import asyncio
import os
from flask import Flask, jsonify
from pyrogram import Client
from pyrogram import utils as pyroutils
from config import BOT, API, OWNER

# ✅ Peer ID Fix (for large channel/group IDs)
pyroutils.MIN_CHAT_ID = -999999999999
pyroutils.MIN_CHANNEL_ID = -10099999999999

# ------------------ Logging Setup ------------------
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

# ------------------ Flask App for Health Check ------------------
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "running",
        "message": "Bot is running!",
        "bot_username": getattr(BOT, 'USERNAME', 'Not set')
    })

@app.route('/health')
def health_check():
    return jsonify({
        "status": "healthy",
        "timestamp": threading.current_thread().ident
    })

# ------------------ Bot Class ------------------
class MN_Bot(Client):
    def __init__(self):
        super().__init__(
            "MN-Bot",
            api_id=API.ID,
            api_hash=API.HASH,
            bot_token=BOT.TOKEN,
            plugins=dict(root="plugins"),
            workers=16,
        )

    async def start(self):
        """Start the bot and send startup notification"""
        try:
            await super().start()
            me = await self.get_me()
            BOT.USERNAME = f"@{me.username}"
            self.mention = me.mention
            self.username = me.username
            
            # Send startup notification to owner
            startup_message = f"🤖 {me.first_name} ✅✅ BOT started successfully ✅✅\n\n" \
                            f"🔹 Username: {BOT.USERNAME}\n" \
                            f"🔹 Bot ID: {me.id}\n" \
                            f"🔹 Workers: 16\n" \
                            f"🔹 Plugins: Loaded from plugins/"
            
            await self.send_message(
                chat_id=OWNER.ID,
                text=startup_message
            )
            
            logging.info(f"✅ {me.first_name} BOT started successfully")
            logging.info(f"🔹 Username: {BOT.USERNAME}")
            logging.info(f"🔹 Bot ID: {me.id}")
            
        except Exception as e:
            logging.error(f"❌ Error starting bot: {e}")
            raise

    async def stop(self, *args):
        """Stop the bot gracefully"""
        try:
            await super().stop()
            logging.info("🛑 Bot Stopped gracefully")
        except Exception as e:
            logging.error(f"❌ Error stopping bot: {e}")

# ------------------ Bot Instance ------------------
bot_instance = None

def create_bot():
    """Create and start the bot"""
    global bot_instance
    if not bot_instance:
        bot_instance = MN_Bot()
        bot_instance.run()

# ------------------ Main ------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    
    if os.environ.get("RENDER"):
        # Running on Render - start bot in background thread
        logging.info("🌐 Starting on Render platform")
        bot_thread = threading.Thread(target=create_bot, daemon=True)
        bot_thread.start()
        logging.info("🤖 Bot started in background thread")
        
        # Run Flask app on the PORT provided by Render
        app.run(host='0.0.0.0', port=port, debug=False)
    else:
        # Running locally
        try:
            # Start Flask in background thread
            def run_flask():
                app.run(host='0.0.0.0', port=8000, debug=False)
            
            flask_thread = threading.Thread(target=run_flask, daemon=True)
            flask_thread.start()
            logging.info("🌐 Flask health check server started on port 8000")
            
            # Start the bot in main thread
            create_bot()
            
        except KeyboardInterrupt:
            logging.info("🛑 Bot stopped by user")
        except Exception as e:
            logging.error(f"❌ Critical error: {e}")
            raise

# For gunicorn (used by Render)
def create_app():
    """Application factory for gunicorn"""
    if not bot_instance:
        bot_thread = threading.Thread(target=create_bot, daemon=True)
        bot_thread.start()
        logging.info("🤖 Bot started via gunicorn")
    return app