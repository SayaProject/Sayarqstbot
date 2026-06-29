from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "0"))
    API_HASH = getenv("API_HASH", "")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "0")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO_USERS", "0").split()))
    MONGO_URI = getenv("MONGO_URI", "")
    
cfg = Config()
