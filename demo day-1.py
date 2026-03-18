# print(2+1)
# print("2"+"1")
# val1=input("Enter first number: ")
# val2=input("Enter second number: ")
# print(val1+val2)


# print(int(3.14))
# print(int(True))
# print(int(4.17))


#print(float(3))
#print(float(False))
#print(float(True))
#print(float(4.22))
#print(str(4))

#print(complex(2))
#print(complex(12.5))
#print(complex(True))
#print(complex(False))
#print(complex("5"))
#print(complex("5.6"))
#print(complex(5,-3))
#print(complex(True,False))

#print(bool(0)) # False
#print(bool(15)) # True
#print(bool(3.14)) # True
#print(bool(0.0)) # False
#print(bool(1+2j)) #True
#print(bool(0+0j)) # False
#print(bool(-1)) # True
#print(bool(False)) # False
#print(bool(True)) # True

#write a program to calculate the simple interest
#principal = 100000
#rate = 10
#time = 1        
#simple_interest = (principal * rate * time) / 100
#print("Simple Interest:", simple_interest)

#write a program to acccept a centigrate temperature and convert it to fahrenheit
#centigrade = float(input("Enter temperature in Centigrade: "))  
#fahrenheit = (centigrade * 9/5) + 32
#print("Temperature in Fahrenheit:", fahrenheit)

#write a orogram to swap two numbers using a temporary variable
#a = 5
#b = 10
#print("Before swapping: a =", a, "b =", b)
#temp = a  # temporary variable
#a = b
#b = temp
#print("After swapping: a =", a, "b =", b)

#write a program to swap two numbers without using a temporary variable
#x = 100   
#y = 200
#print("Before swapping: x =", x, "y =", y)
#x = x + y  # x now holds the sum of x and y
#y = x - y  # y now holds the original value of x
#x = x - y  # x now holds the original value of y
#print("After swapping: x =", x, "y =", y)

#write a proogram to convert height to inch and inch to cm
#h=10
#inch = h*12
#cm = inch*2.14
#print("Height in inches:", inch)
#print("Height in centimeters:", cm) 

#reverse a three digit no.
#num = 123 #num=123
#a= num%10 #a=3
#num = num//10 #num=12
#b= num%10   #b=2
#num = num//10 #num=1
#c= num%10 #c=1
#reverse = (a*100) + (b*10) + c
#print("Reverse of the number is:", reverse)

#reverse a seven digit no.
num = 1234567
a= num%10 #a=7
num = num//10 #num=123456
b= num%10   #b=6
num = num//10 #num=12345
c= num%10 #c=5
num = num//10 #num=1234
d= num%10 #d=4
num = num//10 #num=123
e= num%10 #e=3
num = num//10 #num=12
f= num%10 #f=2
num = num//10 #num=1
g= num%10 #g=1
reverse = (a*1000000) + (b*100000) + (c*10000) + (d*1000) + (e*100) + (f*10) + g
print("Reverse of the number is:", reverse)