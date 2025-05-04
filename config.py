from os import environ

API_ID = int(environ.get("API_ID", "24005775"))
API_HASH = environ.get("API_HASH", "e2593d8b0f5f52798926619defc21905")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-1001516086171"))
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002400433284"))
ADMINS = int(environ.get("ADMINS", "5935267941"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "")
DB_NAME = environ.get("DB_NAME", "MONTY")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', True))
