class Vehicle:
    # Атрибут класса со списком допустимых цветов
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner  # Владелец может изменяться
        self.__model = model  # Модель транспорта
        self.__color = color  # Цвет транспорта
        self.__engine_power = engine_power  # Мощность двигателя

    # Метод возвращает модель транспорта
    def get_model(self):
        return f"Модель: {self.__model}"

    # Метод возвращает мощность двигателя
    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    # Метод возвращает цвет транспорта
    def get_color(self):
        return f"Цвет: {self.__color}"

    # Метод выводит информацию о транспорте
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    # Метод изменяет цвет, если он допустим
    def set_color(self, new_color):
        if new_color.lower() in [color.lower() for color in self.__COLOR_VARIANTS]:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    # Атрибут класса для ограничения количества пассажиров
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)

# Пример использования
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()