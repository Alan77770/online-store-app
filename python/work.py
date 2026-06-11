list=[1,2,3,4,5,6,7,8,9,10]
list.append(11)
list.insert(12,13)
list.remove(11)
print(list)

marks=[45,67,89,34,67,90,45]
marks.count(67)
print(marks.count(67))
marks.index(90)
print(marks.index(90))
marks.sort()
print(marks)
marks.reverse()
print(marks)



list=[ "ram","john","david","lolan","edwin"]
list.reverse()
print(list)


list1=[10,20,30,40,50]
list2=[60,70,80]
list1.extend(list2)
list1.pop(7)
list1.clear()
print(list1)



list=[1,2,3,4,5,6,7,8]
print(max(list))
print(min(list))
x=list.copy
print(list)



list=[1,2,2,3,3,4,4,5]
list.remove(2)
list.remove(3)
list.remove(4)
print(list)



tuple=(6,5,4,3,2,1)
print(tuple.index(6))
print(tuple.index(5))
print(len(tuple))


data=(10,20,30,40,20,50)
print(data.count(20))
print(data.index(40))



tuple1=(1,2,3)
list1=list(tuple1)
list1.append(4)
tuple2=tuple(list1)
print(tuple2)




tuple1=(1,2,3)
tuple2=(4,5,6)
tuple3=(tuple1+tuple2)
print(tuple3)
if 3 in tuple1:
   print(True)
else:
   print(False)



set={1,2,3,4,5,6,7}
set.remove(5)
print(set)



set={1,3,5,3,1,0}
print(set)


x={10,20,30}
y={30,40,50}
x.update(y)
x.discard(40)
print(x)



a={1,2}
b={1,2,3,4}
print(a.issubset(b))
