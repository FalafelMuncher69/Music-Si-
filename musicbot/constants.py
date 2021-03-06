import os.path

MAIN_VERSION = '1.9.6'
SUB_VERSION = '-review'
VERSION = MAIN_VERSION + SUB_VERSION

AUDIO_CACHE_PATH = os.path.join(os.getcwd(), 'audio_cache')
DISCORD_MSG_CHAR_LIMIT = 2000

PLAY_HISTORY_FILE = 'config/play_history.txt' # Store the play history