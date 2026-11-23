def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result

    return wrapper


@decorator  # func_1 = decorator(func_1)
def func_1(a, b):
    return (a + b) ** 2


@decorator
def func_2():
    print("Hello World")


print(func_1(10, 20))
print("-----------")
func_2()
