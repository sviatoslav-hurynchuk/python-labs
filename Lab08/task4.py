class Dog:
    mammal = "ссавець"
    nature = "дружній"
    breed = "невідома порода"

    def __init__(self, name, age):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Ім'я має бути непустим рядком")
        self.name = name.strip()

        if not isinstance(age, (int, float)) or age < 0 or age > 30:
            raise ValueError("Вік має бути додатнім числом не більше 30")
        self.age = int(age)

    def describe(self):
        if self.age == 1:
            age_word = "рік"
        elif 2 <= self.age <= 4:
            age_word = "роки"
        else:
            age_word = "років"
        return f"{self.name}, {self.age} {age_word}, {self.breed}"

    def speak(self):
        return f"{self.name} каже: Гав!"

    def info(self):
        return {
            "name": self.name,
            "age": self.age,
            "mammal": self.mammal,
            "nature": self.nature,
            "breed": self.breed,
        }


class Beagle(Dog):
    nature = "цікавий та товариський"
    breed = "бігль"

    def track(self):
        return f"{self.name} відстежує запах."


class GermanShepherd(Dog):
    nature = "відданий та уважний"
    breed = "німецька вівчарка"

    def guard(self):
        return f"{self.name} охороняє територію."


class Husky(Dog):
    nature = "активний і товариський"
    breed = "хаскі"

    def pull_sled(self):
        return f"{self.name} тягне уявні сани."


class Pets:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_pet(self, pet):
        self.animals.append(pet)

    def show_pets(self):
        lines = [f"Домашні тварини власника {self.name}:"]
        for index, pet in enumerate(self.animals, start=1):
            info = pet.info()
            age = info['age']
            if age == 1:
                age_word = "рік"
            elif 2 <= age <= 4:
                age_word = "роки"
            else:
                age_word = "років"
            lines.append(
                f"{index}. {info['name']} ({info['breed']}), {age} {age_word}, характер: {info['nature']}"
            )
        return "\n".join(lines)


def task04():
    pets = Pets("Святослав")
    dogs = [
        Beagle("Лаки", 3),
        GermanShepherd("Бруно", 5),
        Husky("Сніжок", 2),
    ]
    for dog in dogs:
        pets.add_pet(dog)
        print(f"{dog.describe()}")
        print(f"{dog.speak()}")
    print(pets.show_pets())


task04()

