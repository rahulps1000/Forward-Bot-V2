from pyrogram.filters import *
from Bot.config import Config


def is_sudo(_, __, update):
    try:
        user_id = update.from_user.id
    except:
        return False
    if str(user_id) in Config.SUDO_USERS:
        return True
    else:
        return False


admin = create(is_sudo)
