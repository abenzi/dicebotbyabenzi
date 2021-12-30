from aiogram import types, executor, Dispatcher, Bot
from fake_useragent import UserAgent
import requests
import time

ua = UserAgent()
TOKEN = '5022622705:AAEbfEhtlr_PhNvtdDu45mZFmcyqTruqGkk'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def parser(message: types.Message):
    await message.answer('Добро пожоловать!\nБот начал работу!')
    back_code_0 = None
    back_code_1 = None
    back_code_2 = None
    back_code_3 = None
    back_code_4 = None
    while True:
        response = requests.get(
            url='https://betgames9.betgames.tv/s/web/v1/game/results/testpartner?game_id=10&page=1&timezone=0',
            headers={'user-agent': f'{ua.random}'}
        )

        data = response.json()

        runs_0 = data.get('runs')[0]
        runs_1 = data.get('runs')[1]
        runs_2 = data.get('runs')[2]
        runs_3 = data.get('runs')[3]
        runs_4 = data.get('runs')[4]

        code_0 = runs_0.get('code')
        code_1 = runs_1.get('code')
        code_2 = runs_2.get('code')
        code_3 = runs_3.get('code')
        code_4 = runs_4.get('code')

        results_0 = runs_0.get('results')
        results_1 = runs_1.get('results')
        results_2 = runs_2.get('results')
        results_3 = runs_3.get('results')
        results_4 = runs_4.get('results')

        redNumber_0 = results_0[0].get('number')
        redNumber_1 = results_1[0].get('number')
        redNumber_2 = results_2[0].get('number')
        redNumber_3 = results_3[0].get('number')
        redNumber_4 = results_4[0].get('number')

        blueNumber_0 = results_0[1].get('number')
        blueNumber_1 = results_1[1].get('number')
        blueNumber_2 = results_2[1].get('number')
        blueNumber_3 = results_3[1].get('number')
        blueNumber_4 = results_4[1].get('number')

        if code_0 != back_code_0 and code_1 != back_code_1 and code_2 != back_code_2 and code_3 != back_code_3 and code_4 != back_code_4:
            if redNumber_0 < blueNumber_0:
                time.sleep(1)
                back_code_0 = code_0
                if code_1 != back_code_1:
                    if redNumber_1 < blueNumber_1:
                        time.sleep(1)
                        back_code_1 = code_1
                        if code_2 != back_code_2:
                            if redNumber_2 < blueNumber_2:
                                time.sleep(1)
                                back_code_2 = code_2
                                if code_3 != back_code_3:
                                    if redNumber_3 < blueNumber_3:
                                        await message.answer('⚠️Приготовься Красный...')
                                        time.sleep(1)
                                        back_code_3 = code_3
                                        if code_4 != back_code_4:
                                            if redNumber_4 < blueNumber_4:
                                                time.sleep(1)
                                                back_code_4 = code_4
                                                await message.answer('➖➖➖➖➖➖➖➖➖➖➖\n'
                                                                     '✅ Прогноз: 🔴\n'
                                                                     f'🔻 Результат | Тираж 🔻\n'
                                                                     f'1️⃣  {redNumber_0} : {blueNumber_0}   |   {code_0}\n'
                                                                     f'2️⃣  {redNumber_1} : {blueNumber_1}   |   {code_1}\n'
                                                                     f'3️⃣  {redNumber_2} : {blueNumber_2}   |   {code_2}\n'
                                                                     f'4️⃣  {redNumber_3} : {blueNumber_3}   |   {code_3}\n'
                                                                     f'5️⃣  {redNumber_4} : {blueNumber_4}   |   {code_4}\n'
                                                                     '➖➖➖➖➖➖➖➖➖➖➖'
                                                                    )
            if redNumber_0 > blueNumber_0:
                time.sleep(1)
                back_code_0 = code_0
                if code_1 != back_code_1:
                    if redNumber_1 > blueNumber_1:
                        time.sleep(1)
                        back_code_1 = code_1
                        if code_2 != back_code_2:
                            if redNumber_2 > blueNumber_2:
                                time.sleep(1)
                                back_code_2 = code_2
                                if code_3 != back_code_3:
                                    if redNumber_3 > blueNumber_3:
                                        await message.answer('⚠️Приготовься Синий...')
                                        time.sleep(1)
                                        back_code_3 = code_3
                                        if code_4 != back_code_4:
                                            if redNumber_4 > blueNumber_4:
                                                time.sleep(1)
                                                back_code_4 = code_4
                                                await message.answer('➖➖➖➖➖➖➖➖➖➖➖\n'
                                                                     '✅ Прогноз: 🔵\n'
                                                                     f'🔻 Результат | Тираж 🔻\n'
                                                                     f'1️⃣  {redNumber_0} : {blueNumber_0}   |   {code_0}\n'
                                                                     f'2️⃣  {redNumber_1} : {blueNumber_1}   |   {code_1}\n'
                                                                     f'3️⃣  {redNumber_2} : {blueNumber_2}   |   {code_2}\n'
                                                                     f'4️⃣  {redNumber_3} : {blueNumber_3}   |   {code_3}\n'
                                                                     f'5️⃣  {redNumber_4} : {blueNumber_4}   |   {code_4}\n'
                                                                     '➖➖➖➖➖➖➖➖➖➖➖'
                                                                    )

        time.sleep(5)
if __name__ == '__main__':
    executor.start_polling(dp)