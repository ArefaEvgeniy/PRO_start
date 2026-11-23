import copy


a = [1, 2, [5, 66, 7], 3]

b = a.copy()
b.append(22)
c = a[:]
c.pop()
d = copy.copy(a)
d.extend([4, 5, 6])
f = copy.deepcopy(a)
d[2].append(99)


print(a)
print(b)
print(c)
print(d)
print(f)
