import random


class Coin:
    SIDES = ("heads", "tails")

    def __init__(self, side="heads"):
        if side not in self.SIDES:
            raise ValueError("Можливі значення: heads або tails")
        self.__sideup = side

    def toss(self):
        self.__sideup = random.choice(self.SIDES)
        return self.__sideup

    def get_sideup(self):
        return self.__sideup


def task02(tosses=10):
    coin = Coin()
    results = [coin.toss() for _ in range(tosses)]
    print(f"{tosses} підкидань: {', '.join(results)}")


task02()

