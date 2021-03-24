#LISTS
list2=[1,2,3,4,["apple","orange"] ,[True,False]]
print (list2)
print (list2[1])
print (list2[2])
print(list2[3])
print (list2[4])
print (list2[5])
print(list2[3:6])
#checking if item exists in list
fruits = ["apple","banana","cherry"]
if "apple" in fruits:
  print("yes apple is in fruits")
#changing list items
fruits = ["apple","banana","cherry","orange","kiwi","mango"]
fruits[1]="blackcurrent" #changing second item
print (fruits)
fruits[1:3] = ["watermelon"] #change 2nd and 3rd value by replacing it with one value
print (fruits)
fruits.insert(2,"passion") #insert() method inserts an item at the specified index
print (fruits)
#add listitems
fruits = ["apple","banana","cherry"]
fruits.append("orange")
print (fruits)
#loop through a list
#print all items in the list ,one by one
fruits = ["apple", "banana","cherry"]
for x in fruits:
  print(x)
#use the range( )and len( )functions to create a suitable iterable
for i in range(len(fruits)):
  print(fruits[i])