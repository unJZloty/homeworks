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
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button_calc, button_info)
    return keyboard

def get_ikb():
    inline_kb = InlineKeyboardMarkup(row_width=1)
    button_calories = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
    button_formulas = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
    inline_kb.add(button_calories, button_formulas)
    return inline_kb

# Команда старт - отправляем обычную клавиатуру
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.\nНажми "Рассчитать", чтобы начать.', reply_markup=get_mkb())

# Хэндлер на кнопку "Рассчитать" - показывает Inline-клавиатуру
@dp.message_handler(lambda message: message.text == 'Рассчитать')
async def main_menu(message: types.Message):
    await message.answer('Выберите опцию:', reply_markup=get_ikb())

# Хэндлер на кнопку "Информация" выводит текст
@dp.message_handler(lambda message: message.text == 'Информация')
async def info(message: types.Message):
    await message.answer("Это бот, рассчитывающий дневную норму калорий")

# Хэндлер для кнопки "Формулы расчёта" - отправляет формулу
@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    formula_text = ("Формула Миффлина-Сан Жеора для расчёта нормы калорий:\n"
                    "Для мужчин: 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(г) + 5\n"
                    "Для женщин: 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(г) - 161")
    await call.message.answer(formula_text)
    await call.answer()

# Хэндлер для кнопки "Рассчитать норму калорий" - начинает сбор данных
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

    # Завершаем состояние
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
