import os

API_ID    = os.environ.get("API_ID", "2645474")
API_HASH  = os.environ.get("API_HASH", "6c9a5044d2f2c2350ac20b3838a7896e")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7595907385:AAFxOWCPWCa57YrHyS0THz6TbiNRZdY-GK4") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 6969))  # Default to 8000 if not set
