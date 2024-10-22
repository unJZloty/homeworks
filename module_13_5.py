from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = "___"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

def get_kb():
    button_calc = KeyboardButton(text='Рассчитать')
    button_info = KeyboardButton(text='Информация')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button_calc, button_info)
    return keyboard

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        'Привет! Я бот, помогающий твоему здоровью.\nНажми "Рассчитать", чтобы начать.',
        reply_markup=get_kb()
    )

@dp.message_handler(text='Рассчитать')
async def set_age(message: types.Message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()

@dp.message_handler(text='Информация')
async def show_info(message: types.Message):
    await message.answer("Этот бот помогает рассчитать вашу норму калорий.")

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

    # Завершаем состояние
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
