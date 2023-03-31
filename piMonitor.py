import os
import asyncio
from dotenv import load_dotenv
from telegram import Bot

import psutil
import sensors

# Load environment variables
load_dotenv()
TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv("CHAT_ID")

async def main():
    # Create bot object
    bot = Bot(TOKEN)

    # Get system information
    cpu_percent = psutil.cpu_percent()
    ram_percent = psutil.virtual_memory().percent
    sensors.init()
    cpu_temp = sensors.get_cpu_temperatures()['coretemp-isa-0000'][0].current

    # Create message
    message = f"CPU usage: {cpu_percent}%\nRAM usage: {ram_percent}%\nCPU temperature: {cpu_temp}°C"

    # Send message
    await bot.send_message(chat_id=CHAT_ID, text=message)

if __name__ == '__main__':
    asyncio.run(main())
