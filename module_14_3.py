from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = "___"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

def get_mkb():
    button_calc = KeyboardButton('Рассчитать')
    button_info = KeyboardButton('Информация')
    button_buy = KeyboardButton('Купить')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button_calc, button_info)
    keyboard.add(button_buy)
    return keyboard

def get_buying_menu():
    inline_kb = InlineKeyboardMarkup(row_width=4)
    button1 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
    button2 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
    button3 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
    button4 = InlineKeyboardButton(text='Product4', callback_data='product_buying')
    inline_kb.add(button1, button2, button3, button4)
    return inline_kb

def get_ikb():
    inline_kb = InlineKeyboardMarkup(row_width=1)
    button_calories = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
    button_formulas = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
    inline_kb.add(button_calories, button_formulas)
    return inline_kb

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.\nНажми "Рассчитать", чтобы начать.', reply_markup=get_mkb())

@dp.message_handler(lambda message: message.text == 'Рассчитать')
async def main_menu(message: types.Message):
    await message.answer('Выберите опцию:', reply_markup=get_ikb())

@dp.message_handler(lambda message: message.text == 'Информация')
async def info(message: types.Message):
    await message.answer("Это бот, рассчитывающий дневную норму калорий")

@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    formula_text = ("Формула Миффлина-Сан Жеора для расчёта нормы калорий:\n"
                    "Для мужчин: 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(г) + 5\n"
                    "Для женщин: 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(г) - 161")
    await call.message.answer(formula_text)
    await call.answer()

@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_age(call: types.CallbackQuery):
    await call.message.answer("Введите свой возраст:")
    await call.answer()
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await message.answer("Введите свой рост (в сантиметрах):")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=int(message.text))
    await message.answer("Введите свой вес (в килограммах):")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=int(message.text))

    data = await state.get_data()
    age = data['age']
    growth = data['growth']
    weight = data['weight']

    # Расчет по формуле Миффлина-Сан Жеора (для мужчин):
    # Калории = 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (г) + 5
    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    # Отправляем результат пользователю
    await message.answer(f"Ваша норма калорий: {calories:.2f} ккал в день.")

    await state.finish()

@dp.message_handler(lambda message: message.text == 'Купить')
async def get_buying_list(message: types.Message):

    product_images = [
        'https://dieterra.ru/upload/iblock/37e/w5ffolok0f2tutg2ew4cb3y7uw65jh6v.png',
        'https://dieterra.ru/upload/iblock/66f/lmp88yw8lt059oxzc7hz8x7cvyz3xu6m.png',
        'https://dieterra.ru/upload/iblock/a12/hluo15c9s5l118h0npxgok1dlzjk8a87.jpg',
        'https://dieterra.ru/upload/iblock/bb3/mypey8p7qr056n18xnb7lnngxzvpb0lc.png'
    ]
    for i in range(1, 5):
        await message.answer(
            f'Название: Product{i} | Описание: описание {i} | Цена: {i * 100} рублей')
        # Отправка соответствующей картинки продукта
        await message.answer_photo(photo=product_images[i - 1])

    await message.answer('Выберите продукт для покупки:', reply_markup=get_buying_menu())

@dp.callback_query_handler(lambda call: call.data == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
