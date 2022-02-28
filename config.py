import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "MOATAZ")
ALIVE_NAME = getenv("ALIVE_NAME", "MOATAZ")
BOT_USERNAME = getenv("BOT_USERNAME", "XBA9BOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "XXSONGS")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "BAR_MOATAZ")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "SORMILAN")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "ف ب غ س ك و م ا ت / ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/1c41ded2dd871eb36bd7e.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/millaann/music")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/1c41ded2dd871eb36bd7e.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/1c41ded2dd871eb36bd7e.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/1c41ded2dd871eb36bd7e.png")
