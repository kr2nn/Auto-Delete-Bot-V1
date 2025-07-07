from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import logging
import time

@Client.on_message(filters.command("start") & filters.private)
async def start_command(client: Client, message: Message):
    """Handle /start command"""
    try:
        user = message.from_user
        bot_info = await client.get_me()
        
        welcome_text = f"""
🪷 **Welcome {user.first_name}!**

🤖 I'm **{bot_info.first_name}**, auto-delete bot.

🗑️ **Features:**
• Auto-delete after 30 seconds
• Photos, videos, documents, messages
• Groups and channels

💡 **Setup:** Add me → Admin permissions → Done!

🔗 @{bot_info.username}
        """
        
        # Create inline keyboard
        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("🏓 Ping", callback_data="ping"),
                InlineKeyboardButton("🆔 Chat ID", callback_data="chatid")
            ]
        ])
        
        await message.reply_photo(
            photo="https://envs.sh/tjD.jpg",
            caption=welcome_text,
            reply_markup=keyboard
        )
        
        logging.info(f"✅ Start command executed for user {user.id} ({user.first_name})")
        
    except Exception as e:
        logging.error(f"❌ Error in start command: {e}")
        await message.reply_text(
            "⚠️ Sorry, there was an error processing your request. Please try again later."
        )

@Client.on_message(filters.command("start") & filters.group)
async def start_group_command(client: Client, message: Message):
    """Handle /start command in groups"""
    try:
        chat = message.chat
        user = message.from_user
        bot_info = await client.get_me()
        
        group_welcome_text = f"""
🪷 **Hello {chat.title}!**

🤖 **{bot_info.first_name}** - Auto-delete bot

🗑️ **30-second cleanup** active
⚠️ **Need admin permissions**

🔗 @{bot_info.username}
        """
        
        # Create inline keyboard for group
        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("🏓 Ping", callback_data="ping"),
                InlineKeyboardButton("🆔 Chat ID", callback_data="chatid")
            ]
        ])
        
        await message.reply_photo(
            photo="https://envs.sh/tjD.jpg",
            caption=group_welcome_text,
            reply_markup=keyboard
        )
        
        logging.info(f"✅ Start command executed in group {chat.id} ({chat.title}) by user {user.id}")
        
    except Exception as e:
        logging.error(f"❌ Error in group start command: {e}")
        await message.reply_text(
            "⚠️ Sorry, there was an error processing your request."
        )

@Client.on_callback_query(filters.regex("ping"))
async def ping_callback(client: Client, callback_query: CallbackQuery):
    """Handle ping button callback"""
    try:
        start_time = time.time()
        
        # Get bot info
        bot_info = await client.get_me()
        
        # Calculate response time
        end_time = time.time()
        response_time = round((end_time - start_time) * 1000, 2)
        
        # Prepare ping result
        ping_result = f"""🏓 Pong!

⚡ {response_time}ms
🤖 Status: ✅ Online
🕐 Time: {time.strftime('%H:%M:%S')}

📊 Info:
• @{bot_info.username}
• Workers: 16
• Health: ✅ Running"""
        
        # Show ping result as alert (only answer once)
        await callback_query.answer(ping_result, show_alert=True)
        
        logging.info(f"✅ Ping callback executed for user {callback_query.from_user.id} - Response time: {response_time}ms")
        
    except Exception as e:
        logging.error(f"❌ Error in ping callback: {e}")
        await callback_query.answer("⚠️ Error checking ping", show_alert=True)

@Client.on_callback_query(filters.regex("chatid"))
async def chatid_callback(client: Client, callback_query: CallbackQuery):
    """Handle chatid button callback"""
    try:
        chat = callback_query.message.chat
        user = callback_query.from_user
        
        # Prepare detailed chat info
        chat_info = f"""📍 Chat Info

🆔 ID: {chat.id}
📝 Type: {chat.type}
👥 Title: {chat.title if chat.title else "Private"}
👤 User: {user.id}

💡 Copy ID for configuration"""
        
        # Show detailed chat info as alert
        await callback_query.answer(chat_info, show_alert=True)
        
        logging.info(f"✅ ChatID callback executed by user {user.id} in chat {chat.id}")
        
    except Exception as e:
        logging.error(f"❌ Error in chatid callback: {e}")
        await callback_query.answer("⚠️ Error getting chat info", show_alert=True)

