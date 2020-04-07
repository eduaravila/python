class First():
    # this is a class attribute predefined
    type = "Human"

    def __init__(self, name):
        super().__init__()
        self.name = name

    def say_name(self):
        print(self.name)


me = First("Eduardo")
me.say_name()

# ? get the type of the variable
print(type(me))
print(me.type)


# when you pass the word "pass" you tell the compiler that is fine
class Useless():
    pass
