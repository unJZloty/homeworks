import threading
import time

tot_en = 100
lock = threading.Lock()

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        global tot_en
        days = 0

        print(f"{self.name}, на нас напали!")

        while True:
            with lock:
                if tot_en <= 0:
                    break

                days += 1
                min_en = min(self.power, tot_en)
                tot_en -= min_en

            print(f"{self.name} сражается {days} день(дня)..., осталось {tot_en} воинов.")

            time.sleep(1)

        print(f"{self.name} одержал победу спустя {days} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")
