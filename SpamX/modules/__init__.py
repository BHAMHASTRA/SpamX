from SpamX.config import *
from SpamX.core.version import __version__
from SpamX import sudoser, RiZoeL 
from RiZoeLX import __version__ as pip_vr
from pyrogram import __version__ as pyro_vr
import platform

__version__ = __version__


ping_msg = PING_MSG if PING_MSG else "☆ 🇧𝗥𝗔𝗛𝗠𝗔🇸𝗧𝗥𝗔 ☆ 

 ➪ 𝗣ɨɳɠ: 588.001 ᴍs 
 ➪ 𝗨թƬɨмє: 18h:51m:25s 
 ➪ ⩔єяនɨ០ɳ: v0.6"
pic = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/82357702bbf37add6de97.jpg"
amsg = ALIVE_MSG if ALIVE_MSG else "☆ 🇧𝗥𝗔𝗛𝗠𝗔🇸𝗧𝗥𝗔 ☆ 

 ➪ 𝗣ɨɳɠ: 588.001 ᴍs 
 ➪ 𝗨թƬɨмє: 18h:51m:25s 
 ➪ ⩔єяនɨ០ɳ: v0.6"

try:
   sah = RiZoeL.get_users(OWNER_ID)
   owner_mention = sah.mention
except:
   owner_mention = f"[{OWNER_ID}](tg://user?id={OWNER_ID})"

class Alive:
     Pic = pic
     
     msg = f"""
**⁂ {amsg} ⁂**

━───────╯•╰───────━
☆ 🇧𝗥𝗔𝗛𝗠𝗔🇸𝗧𝗥𝗔 ☆ 

 ➪ 𝗣ɨɳɠ: 588.001 ᴍs 
 ➪ 𝗨թƬɨмє: 18h:51m:25s 
 ➪ ⩔єяនɨ០ɳ: v0.6

handler = HNDLR
Owner = int(OWNER_ID)
DATABASE_URL = DATABASE_URL
LOGS_CHANNEL = LOGS_CHANNEL

if DATABASE_URL:
   from SpamX.database import users_db
   Sudos = []
   All = users_db.get_all_sudos()
   for x in All:
     Sudos.append(x.user_id)
else:
   Sudos = sudoser
