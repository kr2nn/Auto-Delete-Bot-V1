from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

class Translation(object):
  START_PIC = "https://envs.sh/tjD.jpg"
  START_TEXT = """
  🪷 **Welcome {user.first_name}!**

🤖 I'm **{bot_info.first_name}**, auto-delete bot.

🗑️ **Features:**
• Auto-delete after 30 seconds
• Photos, videos, documents, messages
• Groups and channels

💡 **Setup:** Add me → Admin permissions → Done!

🔗 @{bot_info.username}
  """
  GROUP_WELCOME_TEXT = """
  🪷 **Hello {chat.title}!**

🤖 **{bot_info.first_name}** - Auto-delete bot

🗑️ **30-second cleanup** active
⚠️ **Need admin permissions**

🔗 @{bot_info.username}
  """
  
  PING_TEXT = """
  🏓 Pong!

⚡ {response_time}ms
🤖 Status: ✅ Online
🕐 Time: {time.strftime('%H:%M:%S')}

📊 Info:
• @{bot_info.username}
• Workers: 16
• Health: ✅ Running
  """
  CHATID_TEXT = """
  📍 Chat Info

🆔 ID: {chat.id}
📝 Type: {chat.type}
👥 Title: {chat.title if chat.title else "Private"}
👤 User: {user.id}

💡 Copy ID for configuration
  """
  START_BUTTONS = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("🏓 Ping", callback_data="ping"),
                InlineKeyboardButton("🆔 Chat ID", callback_data="chatid")
            ]
        ])