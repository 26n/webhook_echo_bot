from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os
import config


bot = Bot('TOKEN')
dp = Dispatcher(bot)

async def on_startup(dp):
    await bot.set_webhook(config.URL_APP)

async def on_shutdown(dp):
    await bot.delete_webhook()

@dp.message_handler()
async def echo_send(message : types.Message):
    await message.answer(message.text)
    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)



executor.start_webhook(
    dispatcher = dp,
    webhook_path ='',
    on_startup=on_startup,
    on_shutdown=on_shutdown,
    skip_updates = True,
    host = "0.0.0.0",
    port=int(os.environ.get("PORT", 5000)))