import logging

# Настройка логирования
logging.basicConfig(
    filename='runner_tests.log',
    level=logging.INFO,
    filemode='w',
    format='%(asctime)s / %(levelname)s: / %(message)s',  # Формат логов
    datefmt='%Y-%m-%d %H:%M:%S',
    encoding='utf-8'
)

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

# first = Runner('Вося', 10)
# second = Runner('Илья', 5)
# third = Runner('Арсен', 10)
# t = Tournament(101, first, second)
# print(t.start())

class RunnerTest:

    def test_walk(self):
        try:
            # Создаем объект с отрицательной скоростью
            r1 = Runner('Вася', -5)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f'Неверная скорость для Runner: {e}', exc_info=True)

    def test_run(self):
        try:
            # Создаем объект с некорректным типом для имени
            r2 = Runner(2, 10)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f'Неверный тип данных для объекта Runner: {e}', exc_info=True)


if __name__ == '__main__':
    test = RunnerTest()
    test.test_walk()
    test.test_run()
