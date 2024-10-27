from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import InputFile
import asyncio
from crud_functions import dbTableIsEmpty, initiate_db_products, get_all_products
from crud_functions import initiate_db_users, add_user, is_included

api = "7676999659:AAE1MtIJ9edxCEz7qyNSdBqV0-yUDDFhgq0"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

initiate_db_products()
get_all_products()
initiate_db_users()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age_reg = State()

class UserState(StatesGroup):
    growth = State()
    weight = State()
    age_calc = State()

def get_main_menu():
    button_reg = KeyboardButton('Регистрация')
    button_info = KeyboardButton('Информация')
    button_calc = KeyboardButton('Рассчитать')
    button_buy = KeyboardButton('Купить')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button_reg, button_info)
    keyboard.add(button_calc, button_buy)
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

@dp.message_handler(text="Регистрация")
async def sign_up(message: types.Message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text
    if is_included(username):
        await message.answer("Пользователь существует, введите другое имя:")
    else:
        await state.update_data(username=username)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age_reg.set()

@dp.message_handler(state=RegistrationState.age_reg)
async def set_age(message: types.Message, state: FSMContext):
    age = message.text
    if age.isdigit():
        await state.update_data(age=int(age))

        user_data = await state.get_data()
        add_user(user_data['username'], user_data['email'], user_data['age'])

        await message.answer("Регистрация завершена!")
        await state.finish()
    else:
        await message.answer("Пожалуйста, введите корректный возраст.")

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.\nНажми "Рассчитать", чтобы начать.', reply_markup=get_main_menu())

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
    await UserState.age_calc.set()

@dp.message_handler(state=UserState.age_calc)
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
    calories = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f"Ваша норма калорий: {calories:.2f} ккал в день.")

    await state.finish()


@dp.message_handler(lambda message: message.text == 'Купить')
async def get_buying_list(message: types.Message):
    products = get_all_products()

    if not products:
        await message.answer("Продукты не найдены.")
        return

    for i in get_all_products():
        photo = InputFile(f"{i[4]}")
        await message.answer_photo(
            photo=photo,
            caption=f'{i[1]} '
                f'| Описание: {i[2]} '
                f'| Цена: {i[3]}'
        )

    await message.answer('Выберите продукт для покупки:', reply_markup=get_buying_menu())

@dp.callback_query_handler(lambda call: call.data == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
