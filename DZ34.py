import threading
from time import sleep


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            self.enemies -= self.power
            day = int((self.enemies / 100) + 1)
            print(f"{self.name} сражается {day} день(дня)..., осталось {self.enemies} воинов.")
            sleep(1)  # Задержка в 1 секунду
        if self.enemies == 0:
            print(f"{self.name} одержал победу спустя {day} дней(дня)!")


if __name__ == "__main__":
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)
    first_knight.start()
    second_knight.start()

    # Ожидаем завершения потоков
    first_knight.join()
    second_knight.join()

    print("Все битвы закончились!")
