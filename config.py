# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "14209057"))
API_HASH = getenv("API_HASH", "6143e2fdf0d99a8f6803bb0d42f0f8d6")
BOT_TOKEN = getenv("BOT_TOKEN", "7749294702:AAH-lmfdNcOZGqf_9UMXcCQLcVpYAwkkeus")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6564842820").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://ranaalex001:YdceMX2QwQvtfBDU@cluster0.hiy6v.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", "1002363907657"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "500"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "5000"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
