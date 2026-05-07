import asyncio
import os
from datetime import datetime
import pytz
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest

# گرفتن اطلاعات از متغیرهای محیطی
API_ID = int(os.getenv('API_ID', 0))
API_HASH = os.getenv('API_HASH', '')
TIMEZONE = os.getenv('TIMEZONE', 'Asia/Tehran')

if API_ID == 0 or API_HASH == '':
    print("❌ خطا: API_ID و API_HASH رو تنظیم کن")
    exit(1)

async def main():
    client = TelegramClient('session', API_ID, API_HASH)
    await client.start()
    print("✅ ربات روشن شد!")
    
    while True:
        tz = pytz.timezone(TIMEZONE)
        now = datetime.now(tz)
        time_str = now.strftime("%H:%M:%S")
        
        await client(UpdateProfileRequest(
            first_name="سعید",
            last_name=f"🕒 {time_str}",
            about=f"🕐 ساعت: {time_str}"
        ))
        
        print(f"✅ به‌روز شد: {time_str}")
        await asyncio.sleep(60)

with TelegramClient('session', API_ID, API_HASH) as client:
    client.loop.run_until_complete(main())
