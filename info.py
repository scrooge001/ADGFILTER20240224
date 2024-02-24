#Modified By scroogex
import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Movies_search')
API_ID = int(environ.get('API_ID', '29228879'))
API_HASH = environ.get('API_HASH', 'f8c420d7f974ef0a2bc23a9a4a0dc859')
BOT_TOKEN = environ.get('BOT_TOKEN', "6686728746:AAEVM6Wp0ptZR81uzMsWt7WIpSXAyYWM3pc")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS', 'https://telegra.ph/file/c721d579482ef6cfb0510.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5809081123').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001996814616').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '5809081123').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '-1001996814616')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://perera51:perera51@cluster0.c5kzo5m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'scroogex')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002021088905'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', '-1001552083767')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "🤩<b>ᴊᴏɪɴ [ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ](https://t.me/adgmovies)</b>😍\n\n📂𝙵𝙸𝙻𝙴 : <code>{file_name}</code>\n\n📼𝚂𝙸𝚉𝙴 : <i>{file_size}<i>\n\n😈𝙾𝚆𝙽𝙴𝚁 :<a href=https://t.me/adgmovies> ScroogeX</a>")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", "🤩<b>ᴊᴏɪɴ [ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ](https://t.me/adgmovies)</b>😍\n\n📂𝙵𝙸𝙻𝙴 : <code>{file_name}</code>\n\n📼𝚂𝙸𝚉𝙴 : <i>{file_size}<i>\n\n😈𝙾𝚆𝙽𝙴𝚁 :<a href=https://t.me/adgmovies> ScroogeX</a>")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "🤩ʜᴇʏ, {message.from_user.mention} 𝙱𝚁𝙾\n ᴀʀᴇ ʏᴏᴜ ʟᴏᴏᴋɪɴɢ ꜰᴏʀ ᴛʜɪꜱ ᴍᴏᴠɪᴇ?\n 👉 {query} 👈\n\n<b>♥️𝚃𝙸𝚃𝙻𝙴</b>: <a href={url}>{title}</a>\n🎭 𝙶𝙴𝙽𝚁𝙴𝚂: {genres}\n📆 𝚈𝙴𝙰𝚁: <a href={url}/releaseinfo>{year}</a>\n🌟 𝚁𝙰𝚃𝙸𝙽𝙶: <a href={url}/ratings>{rating}</a> / 10 (𝙱𝙰𝚂𝙴𝙳 𝙾𝙽 {votes} 𝚄𝚂𝙴𝚁 𝚁𝙰𝚃𝙸𝙽𝙶𝚂.)\n💽 𝚁𝚄𝙽𝚃𝙸𝙼𝙴: {runtime} Minutes\n📆 𝚁𝙴𝙻𝙴𝙰𝚂𝙴𝙳 : {release_date}\n🌍 𝙲𝙾𝚄𝙽𝚃𝚁𝙸𝙴𝚂 : <code>{countries}</code>\n\n☕𝙿𝙾𝚆𝙴𝚁𝙳 𝙱𝚈☕\n <a href=https://t.me/adgmovies>©️ADG MOVIES</a>\n <a href=https://t.me/adgmovies>©️ᴛᴇᴀᴍ ADG</a>")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "False"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

## EXTRA FEATURES

     # Auto Delete For Group Message (Self Delete) #
SELF_DELETE_SECONDS = int(environ.get('SELF_DELETE_SECONDS', 300))
SELF_DELETE = environ.get('SELF_DELETE', True)
if SELF_DELETE == "True":
    SELF_DELETE = True

     # Download Tutorial Button #
DOWNLOAD_TEXT_NAME = "📥 HOW TO DOWNLOAD 📥"
DOWNLOAD_TEXT_URL = "https://t.me/adgmovies"

     # Custom Caption Under Button #
CAPTION_BUTTON = "Follow"
CAPTION_BUTTON_URL = "https://t.me/adgmovies"
