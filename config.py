import os
from typing import Optional

class API:
    """Telegram API configuration"""
    ID: int = int(os.getenv("API_ID", "0"))
    HASH: str = os.getenv("API_HASH", "")
    
    @classmethod
    def validate(cls):
        """Validate API credentials"""
        if not cls.ID or cls.ID == 0:
            raise ValueError("API_ID is required and must be a valid integer")
        if not cls.HASH:
            raise ValueError("API_HASH is required")

class BOT:
    """Bot configuration"""
    TOKEN: str = os.getenv("BOT_TOKEN", "")
    USERNAME: Optional[str] = None  # Will be set when bot starts
    
    @classmethod
    def validate(cls):
        """Validate bot token"""
        if not cls.TOKEN:
            raise ValueError("BOT_TOKEN is required")

class OWNER:
    """Owner configuration"""
    ID: int = int(os.getenv("OWNER_ID", "0"))
    
    @classmethod
    def validate(cls):
        """Validate owner ID"""
        if not cls.ID or cls.ID == 0:
            raise ValueError("OWNER_ID is required and must be a valid integer")

# Database configuration (optional)
class DATABASE:
    """Database configuration"""
    URL: str = os.getenv("DATABASE_URL", "")
    NAME: str = os.getenv("DATABASE_NAME", "AutoDelete")

# Validate all configurations on import
try:
    API.validate()
    BOT.validate()
    OWNER.validate()
except ValueError as e:
    print(f"❌ Configuration Error: {e}")
    print("Please set the required environment variables:")
    print("- API_ID: Your Telegram API ID")
    print("- API_HASH: Your Telegram API Hash")
    print("- BOT_TOKEN: Your Bot Token from @BotFather")
    print("- OWNER_ID: Your Telegram User ID")
    exit(1)

# Additional configuration
class CHATS:
    """Chat configuration for auto-delete feature"""
    # List of chat IDs where auto-delete should work (empty list means all groups/channels)
    IDS = [-1002799981051]  # Add chat IDs here like: [-1001234567890, -1001234567891]
    
    # Delay before deleting messages (in seconds)
    DELETE_DELAY = int(os.getenv("DELETE_DELAY", "30"))  # Default 30 seconds
    
    # Auto-delete specific media types
    DELETE_PHOTOS = True
    DELETE_VIDEOS = True
    DELETE_DOCUMENTS = True
    DELETE_TEXT_MESSAGES = True
    
    # Auto-delete in channels (in addition to groups)
    DELETE_IN_CHANNELS = True

class SETTINGS:
    """Additional bot settings"""
    # Command prefixes
    COMMAND_PREFIXES = ["/", "!", ".", "?"]
    
    # Plugin settings
    PLUGINS_DIR = "plugins"
    
    # Logging settings
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    
    # Rate limiting
    MAX_REQUESTS_PER_MINUTE = int(os.getenv("MAX_REQUESTS_PER_MINUTE", "20"))
    
    # Feature flags
    ENABLE_PRIVATE_CHATS = True
    ENABLE_GROUP_CHATS = True
    ENABLE_CHANNEL_POSTS = True
