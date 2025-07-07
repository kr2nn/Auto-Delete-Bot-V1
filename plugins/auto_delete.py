# Auto-delete plugin for NikzPy
# Credit: @NikzPy

from pyrogram import Client, filters
import asyncio
import logging
from pyrogram.errors import FloodWait
from config import CHATS

@Client.on_message(filters.group | filters.channel)
async def auto_delete_handler(client, message):
    """Auto-delete messages in specified groups/channels after a delay"""
    try:
        # If CHATS.IDS is not empty and this chat ID is not in the list, skip
        if CHATS.IDS and message.chat.id not in CHATS.IDS:
            return

        # Check if we should delete in channels
        if message.chat.type == "channel" and not CHATS.DELETE_IN_CHANNELS:
            return

        # Get the delay from configuration
        delay = CHATS.DELETE_DELAY
        
        # Determine message type and check if we should delete it
        should_delete = False
        message_type = "text"
        
        if message.photo and CHATS.DELETE_PHOTOS:
            message_type = "photo"
            should_delete = True
        elif message.video and CHATS.DELETE_VIDEOS:
            message_type = "video"
            should_delete = True
        elif message.document and CHATS.DELETE_DOCUMENTS:
            message_type = "document"
            should_delete = True
        elif message.audio:
            message_type = "audio"
            should_delete = True
        elif message.voice:
            message_type = "voice"
            should_delete = True
        elif message.video_note:
            message_type = "video_note"
            should_delete = True
        elif message.sticker:
            message_type = "sticker"
            should_delete = True
        elif message.animation:
            message_type = "animation"
            should_delete = True
        elif message.text and CHATS.DELETE_TEXT_MESSAGES:
            message_type = "text"
            should_delete = True
        
        # Skip if this message type shouldn't be deleted
        if not should_delete:
            return
        
        # Log the scheduled deletion with message type
        chat_type = "channel" if message.chat.type == "channel" else "group"
        chat_name = message.chat.title or f"ID:{message.chat.id}"
        logging.info(f"🕐 {message_type.title()} message scheduled for deletion in {delay} seconds from {chat_type} {chat_name}")
        
        # Wait for the specified delay
        await asyncio.sleep(delay)

        # Attempt to delete the message
        try:
            await message.delete()
            logging.info(f"✅ {message_type.title()} message deleted successfully from {chat_type} {chat_name}")
            
        except FloodWait as fw:
            logging.warning(f"⚠️ FloodWait hit: sleeping for {fw.value} seconds")
            await asyncio.sleep(fw.value)
            try:
                await message.delete()
                logging.info(f"✅ {message_type.title()} message deleted successfully after FloodWait from {chat_type} {chat_name}")
            except Exception as e:
                logging.error(f"❌ Second attempt failed for {message_type}: {e}")
                
        except Exception as e:
            logging.error(f"❌ Failed to delete {message_type} message: {e}")
            
    except Exception as e:
        logging.error(f"❌ Error in auto_delete_handler: {e}")
