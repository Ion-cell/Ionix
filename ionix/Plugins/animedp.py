#Plugin Made by @Helloji123bot

import requests , re , random 
import urllib , os 
from telethon.tl import functions
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from userbot.utils import admin_cmd
import asyncio
from time import sleep

COLLECTION_STRINGZ = [
  "dragon-ball-z",
  "pokemon",
  "pikachu",
  "beyblade",
  "death-note-anime",
  "naruto-anime-best-scenes",
  "pokemon-best-wallpapers",
  "pokemon-best-scenes",
  "best-beyblade-wallpaper",
  "ash-ketchum-emotional-scenes",
  "doraemon-best-4k-wallpaper",
  "Doraemon-last-episode"
]

async def animepp():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRINGZ) - 1)

    pack = COLLECTION_STRINGZ[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile('/\w+/full.+.jpg')

    f = f.findall(pc)

    fy = "http://getwallpapers.com"+random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve("http://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf","f.ttf")

    urllib.request.urlretrieve(fy,"donottouch.jpg")

@borg.on(admin_cmd(pattern="animedp ?(.*)"))

async def main(event):

    await event.edit("**Starting Anime profile picture generator!🕶️🕶️🌋🌋...\n\nDone !!! Check Your DP !! Made by @Helloji123bot ") #Owner @Helloji123bot

    while True:

        await animepp()

        file = await event.client.upload_file("donottouch.jpg")  

        await event.client(functions.photos.UploadProfilePhotoRequest( file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(60) #Edit this to your required needs
