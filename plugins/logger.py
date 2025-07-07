from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

class Logger(object):
  START_INFO = "✅ Start command executed for user {user.id} ({user.first_name})"
  START_ERROR = "❌ Error in start command: {e}"
  GROUP_START_LOG = "✅ Start command executed in group {chat.id} ({chat.title}) by user {user.id}"
  GROUP_START_ERROR_LOG = "❌ Error in group start command: {e}"
  GROUP_ERROR_LOG = "⚠️ Sorry, there was an error processing your request."
  PING_LOG_INFO = "✅ Ping callback executed for user {callback_query.from_user.id} - Response time: {response_time}ms"
  PING_ERROR_LOG = "❌ Error in ping callback: {e}"
  PING_WRING_LOG = "⚠️ Error checking ping"
  CHATID_LOG = "✅ ChatID callback executed by user {user.id} in chat {chat.id}"
  CHATID_ERROR_LOG = "❌ Error in chatid callback: {e}"
  CHATID_WRING = "⚠️ Error getting chat info"
  
