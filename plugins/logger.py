from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

class Logger(object):
  START_SUCCESS = "✅ Start command executed for user {user.id} ({user.first_name})"
  START_ERROR = "❌ Error in start command: {e}"
  START_WRING = "⚠️ Sorry, there was an error processing your request. Please try again later."
  GROUP_START_SUCCESS = "✅ Start command executed in group {chat.id} ({chat.title}) by user {user.id}"
  GROUP_START_ERROR = "❌ Error in group start command: {e}"
  GROUP_WRING = "⚠️ Sorry, there was an error processing your request."
  PING_LOG_SUCCESS = "✅ Ping callback executed for user {callback_query.from_user.id} - Response time: {response_time}ms"
  PING_ERROR = "❌ Error in ping callback: {e}"
  PING_WRING = "⚠️ Error checking ping"
  CHATID_SUCCESS = "✅ ChatID callback executed by user {user.id} in chat {chat.id}"
  CHATID_ERROR = "❌ Error in chatid callback: {e}"
  CHATID_WRING = "⚠️ Error getting chat info"
  