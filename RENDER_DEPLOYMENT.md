# Deploy MN-Bot to Render

## Step-by-Step Deployment Guide

### 1. Prepare Your Code
- Ensure all files are in your GitHub repository
- Make sure `main.py`, `config.py`, and `plugins/` folder are included
- The `render.yaml` file is already configured

### 2. Create Render Account
1. Go to https://render.com and sign up
2. Connect your GitHub account

### 3. Deploy the Bot
1. Click "New +" → "Web Service"
2. Connect your GitHub repository
3. Choose your repository with the bot code
4. Configure the service:
   - **Name**: `mn-telegram-bot`
   - **Environment**: `Python`
   - **Build Command**: `pip install pyrogram flask tgcrypto`
   - **Start Command**: `RENDER=1 python main.py`

### 4. Set Environment Variables
In the Render dashboard, add these environment variables:
- `API_ID`: Your Telegram API ID
- `API_HASH`: Your Telegram API Hash  
- `BOT_TOKEN`: Your bot token from @BotFather
- `OWNER_ID`: Your Telegram user ID
- `DELETE_DELAY`: `30` (or your preferred delay in seconds)

### 5. Deploy
1. Click "Create Web Service"
2. Render will automatically build and deploy your bot
3. The bot will start running immediately

## Alternative: Docker Deployment

If you prefer Docker, use the included `Dockerfile`:

```bash
# Build the image
docker build -t mn-telegram-bot .

# Run with environment variables
docker run -d \
  -e API_ID=your_api_id \
  -e API_HASH=your_api_hash \
  -e BOT_TOKEN=your_bot_token \
  -e OWNER_ID=your_user_id \
  -e DELETE_DELAY=30 \
  --name mn-bot \
  mn-telegram-bot
```

## Configuration Notes

### Auto-Delete Settings
- The bot is configured to delete messages after 30 seconds
- Currently monitoring chat ID: `-1002799981051`
- To change monitored chats, edit `config.py` file

### Media Types Deleted
- ✅ Photos
- ✅ Videos  
- ✅ Documents
- ✅ Text messages
- ✅ Works in both groups and channels

### Health Check
- The Flask server runs on port 8000
- Health endpoint: `/` and `/health`
- Render will use this for monitoring

## Troubleshooting

### Common Issues
1. **Bot not starting**: Check environment variables are set correctly
2. **Not deleting messages**: Ensure the bot has admin permissions in the target chat
3. **Wrong chat ID**: Use `/chatid` command to get the correct chat ID

### Logs
Check Render logs for detailed information:
- Go to your service dashboard
- Click "Logs" tab
- Look for startup messages and any errors

### Support Commands
- `/config` - View current auto-delete settings (owner only)
- `/chatid` - Get current chat ID
- `/ping` - Check bot status
- `/help` - Show all commands

## Security Notes
- Never commit API keys to GitHub
- Use Render's environment variables for secrets
- The bot only responds to the configured owner for admin commands