from fastapi import FastAPI

# Создаем приложение FastAPI
app = FastAPI()

# Маршрут к главной странице
@app.get("/")
async def Get_Main_Page() -> dict:
    return {"message": "Главная страница"}

# Маршрут к странице администратора
@app.get("/user/admin")
async def Get_Admin_Page() -> dict:
    return {"message": "Вы вошли как администратор"}

# Маршрут к страницам пользователей с параметром user_id
@app.get("/user/user_id")
async def Get_User_ID(user_id: int = 123) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# Маршрут к страницам пользователей с данными в адресной строке
@app.get("/user")
async def Get_User_Info(username: str = 'Andrey', age: int = 50) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
