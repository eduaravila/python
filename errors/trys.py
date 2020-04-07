

def infinite_add():
    while True:
        try:
            number = input("Set a number plss:")
            result = number + 2
        except SyntaxError as sintax_error:
            print(f"Some sintax error, {sintax_error}")
        except TypeError as type_error:
            print(f"Some type error, {type_error}")
        else:
            print("The try code goes good")
            break
        finally:
            print("this code is runned even if there is an error")


# infinite_add()

try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except:
    print("Cant't multiply strings")

try:
    x = 5
    y = 0

    z = x/y
except ZeroDivisionError as error:
    print("ZeroDivisionError: division by zero")

finally:
    print("All done")
