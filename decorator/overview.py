def func():
    def inside_func():
        return "inside_func() was called"

    return inside_func


inside_func = func()

print(inside_func())


def func_as_param(var_func):
    var_func()


def example_decorator(func_need_decorator):
    def inside_func_decorator():
        print("After the function")
        func_need_decorator()
        print("Before the function")

    return inside_func_decorator


@example_decorator
def hello():
    print("Hello world")


hello()
# funtion_with_decorator = example_decorator(hello)

# funtion_with_decorator()
