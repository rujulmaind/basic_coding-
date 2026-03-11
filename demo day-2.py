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
# for i in range(1,11):
#     print(i*2)
# printing table from 2 to 10 in horizontal way
# for i in range(2,11):
#     for j in range(1,11):
#         print(i*j,end="\t")
#     print()
# print table from 2 to 20 
# for i in range(1,11):
#     for j in range(2,11):
#         print(i*j,end="\t")
#     print()
# print("-------------------------------------------------------------------------------")
# print("-------------------------------------------------------------------------------")
# for i in range(1,11):
#     for j in range(11,21):
#         print(i*j,end="\t")
#     print()

#check if valaue is positive or negative or zero
# num=int(input("Enter a number: "))
# if num>0:
#     print("Positive number")
# if num<0:
#     print("Negative number")
# if num==0:
#     print("Zero")

#write a program to accpet the days and check the working day or weekend
# day=input("Enter the day: ")
# if day=="Saturday" or day=="Sunday" or day=="saturday" or day=="sunday" or day=="SATURDAY" or day=="SUNDAY":
#     print("It's a weekend!")
# if day!="Saturday" and day!="Sunday" and day!="saturday" and day!="sunday" and day!="SATURDAY" and day!="SUNDAY":
#     print("It's a working day.")

#wite a program to accept 3 paper marks and calculate total, oercentage and if percentage is greate than equal to 60 then he/she is elligible for placement
# marks1=int(input("Enter marks of paper 1: "))
# marks2=int(input("Enter marks of paper 2: "))
# marks3=int(input("Enter marks of paper 3: "))
# total=marks1+marks2+marks3
# percentage=(total/300)*100
# print("Total marks: ",total)
# print("Percentage: ",percentage)
# if percentage>=60:
#     print("Congratulations! You are eligible for placement.")
# if percentage<60:
#     print("Sorry! You are not eligible for placement.")

#write a program to accept 5 different value in 5 different variable and check maximum value and print by using simple if statement
# num1=int(input("Enter number 1: ")) 
# num2=int(input("Enter number 2: "))
# num3=int(input("Enter number 3: "))
# num4=int(input("Enter number 4: "))
# num5=int(input("Enter number 5: "))
# if num1>num2 and num1>num3 and num1>num4 and num1>num5:
#     print("Maximum number is: ",num1)
# if num2>num1 and num2>num3 and num2>num4 and num2>num5:
#     print("Maximum number is: ",num2)
# if num3>num1 and num3>num2 and num3>num4 and num3>num5:
#     print("Maximum number is: ",num3)
# if num4>num1 and num4>num2 and num4>num3 and num4>num5:
#     print("Maximum number is: ",num4)   
# if num5>num1 and num5>num2 and num5>num3 and num5>num4:
#     print("Maximum number is: ",num5)
