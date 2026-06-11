list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for num in list:
    if num % 2 == 0:
        print(num)
        
count=0
for num in list:
    if num % 2 != 0:
        count += 1
print("Total odd numbers:", count)




list=[1,2,4,5,6,7,8,9,10,11]
list.insert(2,3)
list.remove(7)
print(list)


values=[12,45,23,67,45,89,12]
while 12 in values:
    values.remove(12)
print(values)




list1=[1,2,3]
list2=[4,5,6]
list1.extend(list2)
print(list1)



list=[1,2,3,4,5,6]
list[0],list[-1]=list[-1],list[-0]
print(list)



list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19.20]
list2=[num for num in list1 if num % 3 == 0]
print(list2)




list=["apple","orange","graps","pinapple","watermelon","banana"]
list.sort()
print(list)
list.reverse()
print(list)




tuple=(1,2,3,4,5,6,7,8)
for element in tuple:
    print(element)




items=("pen","book","pencile","eraser")
if "book" in items:
    print("'book' exists in the tuple")
    print(items.index("book"))
else:
    print("'book' does not exist in the tuple")

 


 tuple1=(1,2,3,4,5)
 list1 = list(tuple1)
 list1.remove(min(list1))
 tuple2 = tuple(list1)
 print(tuple1)
 print(tuple2)



tuple1=(1,3,5)
tuple2=(2,4,6)
 print(max(tuple1))
 print(max(tuple2))



tuple1 = (1, 2, 3, 2, 4, 1, 5, 3)
x=set.tuple1
tuple2 = tuple(x)
print(tuple1)
print(tuple2)




set={1,2,3,4,5,6,7,8,9,10}
set.pop(1)
set.pop(2)
set.pop(3)
set.pop(4)
set.pop(5)
set.pop(6)
set.pop(7)
set.pop(8)
set.pop(9)
set.pop(10)
print(set)




A={2,4,6,8}
B={1,2,3,4}
print(A.isdisjoint(B))





names={"alice","bob","eve","charlie","david"}
sorted_names=sorted(names)
print(names)








