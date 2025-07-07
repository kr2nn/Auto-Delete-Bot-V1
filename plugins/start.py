from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from plugins.nikz import Translation
from plugins.logger import Logger
import logging
import time

@Client.on_message(filters.command("start") & filters.private)
async def start_command(client: Client, message: Message):
    """Handle /start command"""
    try:
        user = message.from_user
        bot_info = await client.get_me()
        
        await message.reply_photo(
            photo=Transition.START_PIC,
            caption=Translation.START_TEXT,
            reply_markup=START_BUTTONS
        )
        
        logging.info(Logger.START_SUCCESS)
        
    except Exception as e:
        logging.error(Logger.START_ERROR)
        await message.reply_text(Logger.START_WRING)

@Client.on_message(filters.command("start") & filters.group)
async def start_group_command(client: Client, message: Message):
    """Handle /start command in groups"""
    try:
        chat = message.chat
        user = message.from_user
        bot_info = await client.get_me()
        
        await message.reply_photo(
            photo=Transition.START_PIC,
            caption=Translation.GROUP_WELCOME_TEXT,
            reply_markup=START_BUTTONS
        )
        
        logging.info(Logger.GROUP_START_SUCCESS)
        
    except Exception as e:
        logging.error(Logger.GROUP_START_ERROR)
        await message.reply_text(Logger.GROUP_WRING)

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
        # Show ping result as alert (only answer once)
        await callback_query.answer(Translation.PING_TEXT, show_alert=True)
        
        logging.info(Logger.PING_LOG_SUCCESS)
        
    except Exception as e:
        logging.error(Logger.PING_ERROR)
        await callback_query.answer(Logger.PING_WRING, show_alert=True)

@Client.on_callback_query(filters.regex("chatid"))
async def chatid_callback(client: Client, callback_query: CallbackQuery):
    """Handle chatid button callback"""
    try:
        chat = callback_query.message.chat
        user = callback_query.from_user
        
        # Prepare detailed chat info
        # Show detailed chat info as alert
        await callback_query.answer(Translation.CHATID_TEXT, show_alert=True)
        
        logging.info(Logger.CHATID_SUCCESS)
        
    except Exception as e:
        logging.error(Logger.CHATID_ERROR)
        await callback_query.answer(Logger.CHATID_WRING, show_alert=True)
        
