from os import environ

API_ID = int(environ.get("API_ID", "9328697"))
API_HASH = environ.get("API_HASH", "9844b5bade2267c9a175a1dc72952e76")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-1001536135490"))
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1001591180536"))
ADMINS = int(environ.get("ADMINS", "5935267941 1923770971"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "")
DB_NAME = environ.get("DB_NAME", "autoacceptbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', True))
