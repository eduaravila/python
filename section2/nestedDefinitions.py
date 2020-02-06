# LEGB
# LOCAL
# ENCLOSING FUNCTION
# GLOBAL
# PYTHON BUILD IN

# ? global x
x = 10


def private():
    # ? local
    x = 50

    def enclosedThing():
        # ? enclosing function variable
        return x
    enclosedThing()


def modifieGlobal():
    global x  # * takes the global variable memory space & modify the orginal variable

    x = "New value"
