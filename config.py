import os


class Config(object):
    API_HASH = os.environ.get("API_HASH", "b3a786dce1f4e7d56674b7cadfde3c9d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8022217287:AAFawvEt5-R1igQx8bdOkMntWmmfR2NgjdU")
    TELEGRAM_API = os.environ.get("TELEGRAM_API", "28776072")
    OWNER = os.environ.get("OWNER", "7711039923")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "ftmdeveloper")
    PASSWORD = os.environ.get("PASSWORD", "@ftmbotz")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://ftm:ftm@cluster0.rhh9r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOGCHANNEL = os.environ.get("LOGCHANNEL", "-1002479719245")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    IS_PREMIUM = True
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
