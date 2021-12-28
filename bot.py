from aiogram import types, executor, Dispatcher, Bot
from fake_useragent import UserAgent
import requests
import time

ua = UserAgent()
TOKEN = '5022622705:AAF-nLtYZr3mTCbo8OOrHhOqqzTek8B0630'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def parser(message: types.Message):
    back_code = None
    while True:
        response = requests.get(
            url='https://betgames9.betgames.tv/s/web/v1/game/results/testpartner?game_id=10&page=1&timezone=0',
            headers={'user-agent': f'{ua.random}'}
        )

        data = response.json()
        runs = data.get('runs')[0]
        code = runs.get('code')
        results = runs.get('results')
        redNumber = results[0].get('number')
        blueNumber = results[1].get('number')

        if back_code != code:
            if redNumber == blueNumber:
                await message.answer('Игра: Дуэль Костей 🎲\n\n' 'Тираж: 'f'{code}\n\n' 'Результат: 'f'{redNumber}' ' : ' f'{blueNumber}')
                back_code = code

        time.sleep(10)

if __name__ == '__main__':
    executor.start_polling(dp)