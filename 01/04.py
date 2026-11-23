def func(a, b, c, d):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print(f"d: {d}")


dict = {"a": 100, "b": 200, "c": 300, "d": 400}
func(**dict)

print(func)
ff = func

del func
ff(**dict)
