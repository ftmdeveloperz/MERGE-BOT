import os


class Config(object):
    API_HASH = os.environ.get("API_HASH", "0c8f8bd171e05e42d6f6e5a6f4305389")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8079681536:AAH61qm5McvNIY0S2YVL-jFZPwmU_Pu4iwo")
    TELEGRAM_API = os.environ.get("TELEGRAM_API", "22141398")
    OWNER = os.environ.get("OWNER", "7744665378")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "ftmdeveloperz")
    PASSWORD = os.environ.get("PASSWORD", "@ftmbotz")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://ftm:ftm@cluster0.xotfi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOGCHANNEL = os.environ.get("LOGCHANNEL", "-1002283877325")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
