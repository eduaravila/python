class Animal():

    def __init__(self, name):
        super().__init__()
        self.name = name

    def talk():
        raise Exception("this, method should be inhered for a child class ")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def talk(self):
        print(f"{self.name}, says guau!")


poki = Dog("Poki")
poki.talk()
