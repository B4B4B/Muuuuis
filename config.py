import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
MONGODB_URL = getenv("MONGODB_URL")
OWNER_NAME = getenv("OWNER_NAME")
ALIVE_NAME = getenv("ALIVE_NAME")
BOT_PHOTO = getenv("BOT_PHOTO")
DEV_PHOTO = getenv("DEV_PHOTO")
DEV_NAME = getenv("DEV_NAME")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "MOA_YAD")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "MOA_YAD")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "# $ / ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/MOA-YAD-06-08")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "70"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/noayad/-")
IMG_1 = getenv("IMG_1", "https://telegra.ph/MOA-YAD-06-08")
IMG_2 = getenv("IMG_2", "https://telegra.ph/MOA-YAD-06-08")
IMG_3 = getenv("IMG_3", "https://telegra.ph/MOA-YAD-06-08")
