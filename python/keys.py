d={1:'abc',2:'deep'}
d1={2:'aaa', 3:'ccc'}
print(d.keys())
print(d1.keys())
print(d.values())
print(d1.values())
print(d.items())
print(d1.items())

d1=d.copy()
print(d)

d1.clear()
print(d1)


print(d.get(1))


d.pop(2)
print(d)


d.popitem()
print(d)



d.update(d1)
print(d)