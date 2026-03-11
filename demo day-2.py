mylist=["apple","banana","cherry","orange","kiwi","melon","mango","grapes","pineapple","strawberry"]
#how print whole list and its type and how to access individual items and slicing of list
# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:2])
# print(mylist[:])
# print(mylist[::-1])

#adding new items to the list
# mylist.append("watermelon")
# mylist.append("papaya")
# print(mylist)

#inserting an item at a specific position
# mylist.insert(2,"blueberry")
# print(mylist)

#removing an item from the list
# mylist.remove("kiwi")
# print(mylist)

#copying a list
# newlist=mylist.copy()
# print(mylist)
# print(newlist)

#example of multidimensional list
# mylist=[[1,2],[4,5],[7,8]]
# print("Example of multidimnsional list:")
# print(mylist)
# #print(mylist[row][column])
# print(mylist[0][0])
# print(mylist[1][1])
# print(mylist[2][0]) 
# print(mylist[2][1])
# print(mylist[0][1])
# print(mylist[1][0])

#deleting an item or whole list using del keyword
# del mylist
# del mylist[1]
# print(mylist)

#clear the list
# mylist.clear()
# print(mylist)

#construct a list using list() constructor
# mylist=list(("apple","banana","cherry"))
# print(mylist)

#reverse the list
# mylist.reverse()  
# print(mylist)

# #reverse the list in descending order
# mylist.reverse(-1)
# print(mylist)

#to return the address of the variable
# math=10
# phy=50
# print(id(math))
# print(id(phy))

#alising a list
# mylist=[1,2,3]
# newlist=mylist
# print(mylist)
# print(newlist)

#membership operator in and not in
# name = "mango"
# print("Z" in name)
# print("Z" not in name)

#looping through a list
for i in mylist:
    print(i)