import os


class Config(object):
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7270862829:AAFY2KNsTk2MnU2xrOvHochDsrdnyOkFW98")
    TELEGRAM_API = os.environ.get("TELEGRAM_API", "")
    OWNER = os.environ.get("OWNER", "7711039923")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "ftmdeveloper")
    PASSWORD = os.environ.get("PASSWORD", "@ftmdeveloper")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://ftm:ftm@cluster0.rhh9r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOGCHANNEL = os.environ.get("LOGCHANNEL", "")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    IS_PREMIUM = True
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
