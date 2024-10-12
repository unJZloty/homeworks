def introspection_info(obj):
    # Получение типа объекта
    obj_type = type(obj).__name__

    # Получение всех атрибутов объекта (включая методы)
    attributes = dir(obj)

    # Фильтрация методов объекта
    methods = [attr for attr in attributes if callable(getattr(obj, attr))]

    # Фильтрация обычных атрибутов (не методы)
    non_methods = [attr for attr in attributes if not callable(getattr(obj, attr))]

    # Получение модуля, к которому принадлежит объект
    module = getattr(obj, '__module__', 'Модуль не определен')

    # Дополнительные свойства (по типу объекта)
    extra_info = {}
    if hasattr(obj, '__doc__'):
        extra_info['doc'] = obj.__doc__  # Документация объекта (если есть)

    print(f"Тип объекта: {obj_type}")
    print(f"Атрибуты объекта: {', '.join(non_methods)}")
    print(f"Методы объекта: {', '.join(methods)}")
    print(f"Модуль объекта: {module}")

    if extra_info.get('doc'):
        print(f"Документация объекта: {extra_info['doc']}")

# Создание собственного класса
class Car:
    """Класс для представления автомобиля."""

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        """Метод для запуска автомобиля."""
        print(f"{self.brand} {self.model} запущен.")

    def stop(self):
        """Метод для остановки автомобиля."""
        print(f"{self.brand} {self.model} остановлен.")

    def get_info(self):
        """Метод возвращает информацию об автомобиле."""
        return f"{self.year} {self.brand} {self.model}"

# Создание объекта класса Car
my_car = Car("Tesla", "Model S", 2022)

# Интроспекция объекта
introspection_info(my_car)
