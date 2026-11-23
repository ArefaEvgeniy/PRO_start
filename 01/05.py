def func_1(a):
    def func_2(b):
        print(a + b)

    return func_2


a = func_1(10)

a(5)
