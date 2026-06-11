set={1,2,3}
set.add(4)
print(set)



set={4,5,6}
set.clear()
print(set)


set={4,5,6}
set.discard(5)
print(set)



set={10,11,12}
s=set.copy()
print(s)


set={3,5,7}
set.remove(3)
print(set)



set1={1,2}
set2={3,4}
print(set1.difference(set2))




set1={1,2,3}
set2={4,5,6}
print(set1.union(set2))




set1={1,2,3}
set2={3,2,1}
print(set1.intersection(set2))



set1={1,3}
set2={2,4}
print(set1.isdisjoint(set2))

