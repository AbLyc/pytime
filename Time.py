#AliTiTaniom
#@Darck_Tm
#@tmNull

from telethon.errors import FloodWaitError
from telethon import TelegramClient,functions
from datetime import datetime
import os
import pytz
import aiocron
import asyncio
os.system('pkg install python && pip install telethon && pip install asyncio && pip install aiocron && pip install pytz && clear') 

api_id = "" 
api_hash=""



client=TelegramClient("session name", api_id, api_hash)


@aiocron.crontab('*/1 * * * *')
async def clock():
	ir=pytz.timezone("Asia/Tehran")
	time=datetime.now(ir).strftime("»%H:%M«")
	font1="0❶❷❸❹❺❻❼❽❾"
	font2="𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"
	await client(functions.account.UpdateProfileRequest(last_name=time.translate(time.maketrans(font1,font2))))

client.start()
clock.start()
client.run_until_disconnected()
asyncio.get_event_loop().run_forever()
