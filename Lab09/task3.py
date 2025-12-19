class Apple:
    states = ["Відсутнє", "Цвітіння", "Зелене", "Червоне"]

    def __init__(self, index):
        if not isinstance(index, int) or index <= 0:
            raise ValueError("index яблука має бути додатнім цілим числом")
        self._index = index
        self._state = Apple.states[0]

    def grow(self):
        try:
            current_index = Apple.states.index(self._state)
            if current_index < len(Apple.states) - 1:
                self._state = Apple.states[current_index + 1]
        except ValueError:
            pass

    def is_ripe(self):
        return self._state == Apple.states[-1]

    def get_state(self):
        return self._state

    def get_index(self):
        return self._index


class AppleTree:
    def __init__(self, apple_count):
        if not isinstance(apple_count, int) or apple_count < 0:
            raise ValueError("Кількість яблук на дереві має бути невід'ємним цілим числом")
        self.apples = [Apple(i + 1) for i in range(apple_count)]

    def grow_all(self):
        for apple in self.apples:
            apple.grow()

    def all_are_ripe(self):
        if not self.apples:
            return False
        return all(apple.is_ripe() for apple in self.apples)

    def give_away_all(self):
        self.apples = []


class Gardener:
    def __init__(self, name, tree):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Ім'я садівника має бути непорожнім рядком")
        if not isinstance(tree, AppleTree):
            raise TypeError("tree має бути екземпляром AppleTree")
        self.name = name.strip()
        self._tree = tree

    def work(self):
        if self._tree is not None:
            self._tree.grow_all()

    def harvest(self):
        if self._tree is None:
            print("Помилка: дерево не встановлено")
            return
        if self._tree.all_are_ripe():
            print("Урожай зібрано!")
            self._tree.give_away_all()
        else:
            print("Попередження: яблука ще не дозріли!")

    @staticmethod
    def apple_base(apples):
        try:
            apples_list = list(apples)
        except TypeError:
            print("Помилка: apple_base очікує ітерабельну колекцію яблук")
            return

        print("Довідка по яблукам:")
        print(f"Кількість яблук: {len(apples_list)}")
        for apple in apples_list:
            if isinstance(apple, Apple):
                print(f"Яблуко №{apple.get_index()}: {apple.get_state()}")
            else:
                print("Попередження: знайдено невалідний об'єкт замість Apple")


def task03():
    apple1 = Apple(1)
    apple2 = Apple(2)
    apple3 = Apple(3)
    
    apples_list = [apple1, apple2, apple3]
    Gardener.apple_base(apples_list)
    print()

    tree = AppleTree(5)
    gardener = Gardener("Іван", tree)
    
    print("Робота садівника над деревом...")
    gardener.work()  
    gardener.work() 
    print()

    print("Спроба зібрати урожай:")
    gardener.harvest()
    print()

    print("Продовження догляду за деревом...")
    gardener.work()  
    print()

    print("Спроба зібрати урожай знову:")
    gardener.harvest()
    print()

    print("Стан дерева після збору урожаю:")
    print(f"Кількість яблук на дереві: {len(tree.apples)}")
task03()