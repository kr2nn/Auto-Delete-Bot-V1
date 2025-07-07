"""
Plugin system for MN-Bot

This directory contains all the bot plugins/commands.
Each plugin should be a separate Python file with proper handlers.
"""

import logging

# Plugin metadata
PLUGIN_INFO = {
    "name": "MN-Bot Plugin System",
    "version": "1.0.0",
    "description": "Modular plugin system for Telegram bot commands",
    "author": "MN-Bot Team"
}

# Available plugins
AVAILABLE_PLUGINS = [
    "start",
    "auto_delete"
]

logging.info(f"📦 Loading {len(AVAILABLE_PLUGINS)} plugins...")
logging.info(f"🔌 Available plugins: {', '.join(AVAILABLE_PLUGINS)}")
