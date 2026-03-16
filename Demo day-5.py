# def msg(): # called function
#     print("Hello World")
#     n1 = int(input("Enter the value of n1: "))
#     n2 = int(input("Enter the value of n2: "))
#     sum = n1 + n2
#     sub = n1 - n2
#     mul = n1 * n2
#     div = n1 / n2
#     return sum, sub, mul, div
# result = msg()
# print(result)


# positional arguments
# keyword arguments
# default arguments
# variable length arguments/ variable no. of arguments

# 1. positional arguments
# def personalInfo(fname, lname):
#     print("First name: ", fname)
#     print("Last name: ", lname)

# fname="Rujul"
# lname="Maind"
# personalInfo(fname, lname)


# 2. Default argument
# def cityName(city="Nagpur"):
#      print("City: ", city)


# cityName("New York")
# cityName("Mumbai")
# cityName()

#3. variable length arguments
# def studentsName(*names):
#     print("Students name: ", names)

# studentsName("Rujul", "Rakshit", "Ayush", "Shivaji")

mylist=[1,2,3,4,5]
def searchElement(target):
    for i in range(len(mylist)):
        if target==mylist[i]:
             print("Element found at index: ", i)
             break
searchElement(3)