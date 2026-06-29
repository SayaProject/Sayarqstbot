from os import path, getenv

class Config:
    API_ID = int(getenv("30422005", ""))
    API_HASH = getenv("5170ded206641d73215baf40175a6924", "")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("-1003894816847", "")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("5940554521", "").split()))
    MONGO_URI = getenv("MONGO_URI", "")
    
cfg = Config()
