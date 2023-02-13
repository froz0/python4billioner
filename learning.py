# #Python Syntax
# print("hello world") #this an python syntax

# #Python Indentation
# if 5 < 6:
#   print("five is less than six!")

# if 5 > 2:
# print("Five is greater than two!") #this an error

# if 6 > 4:
#       print('six is greater than four')#this is an correct

# if 5 < 9:
#   print("five is less than nine")
#      print("five is less than nine") #this is an error

# if 5 < 9:
#   print("five is less than nine")
#   print("five is less than nine") # this is  correct

# 03/02/23

# Variable Names

# myvar = "froz"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John"
# print(myvar, _my_var) #this is a variable names

# QowlE = "manga"
# al_bashiiri = "novel"
# _fr0_z = "anime"
# SALIH = 'GOT'
# dost = [SALIH, QowlE, al_bashiiri, _fr0_z]
# print(dost) #this is a variable names

#  2qowle = 'froz'
# qow-le = 'albashiiri'
# qow le = "salih" #this is an error

# 2elma = "water"
# ekme-k = "yamurta"
# tat li = "sigaret" #this is an error

# Many Values to Multiple Variables
# Y = x = W = "Kedi"
# print(Y)
# print(x)
# print(W) # this is a Many Values to Multiple Variables

# froz = ["qowle", "albashiiri", "salih"]
# x, h, f = froz
# print(x, h, f) #Unpack a Collection

# yahya = ["solo leveling", "manga", "bleach"]
# yahya = x, y, z
# print(x, y, z) # this is error

# m3 = ['sara', 3, 'mia khalifa']
# d3, s3, c8 = m3
# print(s3) #this is froz's project.

# y = ["ali", "mohammed", "said"]
# h4, f8, s2 = y
# print(s2)

# 06/02/23
# Output Variables

#The Python print() function is often used to output
# x = "Python is awesome"
# print(x)

# #In the print() function, you output multiple variables, separated by a comma:
# x = "qowle"
# y = "sen"
# z = "amk"
# print(x, y, z)#this is a output variables

# #You can also use the + operator to output multiple variables:
# x = "qowle "
# y = "sen "
# z = "amk "
# print(x + y + z)#Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".

# x = 130
# froz = 70
# print(x + froz) #For numbers, the + character works as a mathematical operator:

# # In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
# # x = 130
# # froz = qowle
# # print(x + froz) #this is a error

# #The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
# x = 130
# froz = "albashiiri"
# print(x, froz)

# 07/02/23

# Global Variables

# x = "awesome"

# def myfunc():
#   print("Python is " + x)
# myfunc()
# # Global variables can be used by everyone, both inside of functions and outside.
# #exable 2

# Y = "waaye"

# def saad7():
#   print("maskaxdayda faaroq " + Y)

# saad7()

#Create a variable inside a function, with the same name as the global variable

# d = "agalar"

# def saad7():
#   d = "orenci"
#   print("shaqo waa " + d)

# saad7()

# print(d)

# def maaji3():
#   global B
#   B = "codes"

# maaji3()
# print(B)

# #The global Keyword

# #Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

# # To create a global variable inside a function, you can use the global keyword.

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)

# def syntax9():
#   global M
#   M = 7 + 3

# syntax9()
# print(M)

#Also, use the global keyword if you want to change a global variable inside a function.

# x = "casiir"

# def myfunc():
#   global x
#   x = "caano"

# myfunc()

# x = "casiir"
# x = "four"
# print(x)

# print("hilib " + x) #To change the value of a global variable inside a function, refer to the variable by using the global keyword:

# 09/02/23
#Python Data Types

#Built-in Data Types
#In programming, data type is an important concept. Variables can store data of different types, and different types can do different things.

#Python has the following data types built-in by default, in these categories:

# x = 5
# print(x)
# print(type(x))

# # Text Type:	str
# A = "froz"
# print(A)
# print(type(A))

# # Numeric Types:	int, float, complex
# #integer
# B = 5
# print(B)
# print(type(B))

# # float
# C = 5.3
# print(C)
# print(type(C))

# #complex
# D = 5j
# print(D)
# print(type(D))

# # Sequence Types:	list, tuple, range
# #list
# E = ["albashiiri", "froz", "qowle"]
# print(E)
# print(type(E))

# #tuple
# F = ("albashiiri", "froz", "qowle")
# print(F)
# print(type(F))

# #range
# H = range(5)
# print(H)
# print(type(H))

# # Mapping Type:	dict

# I = {"name": "John", "age": 36}
# print(I)
# print(type(I))

# # Set Types:	set, frozenset
# #set
# J = {"albashiiri", "froz", "qowle"}
# print(J)
# print(type(J))

# #frozenset
# K = frozenset({"albashiiri", "froz", "qowle"})
# print(K)
# print(type(K))

# # Boolean Type:	bool
# #bool
# L = True
# print(L)
# print(type(L))

# # Binary Types:	bytes, bytearray, memoryview
# #bytes
# L = b"Hello qowle"
# print(L)
# print(type(L))

# #bytearray
# M = bytearray(7)
# print(M)
# print(type(M))

# #memoryview
# N = memoryview(bytes(5))
# print(M)
# print(type(N))

# # None Type:	NoneType
# O = None
# print(O)
# print(type(O))

#cotinue 10/02/23
#Setting the Specific Data Type

# If you want to specify the data type, you can use the following constructor functions:
"""
#str:
a = str("qowle")
print(a)

#int:
b = int(666)
print(666)

#flout:
c = float(6.5)
print(c)

#complex
d = complex(3j)
print(d)

#list
e = list(("merhaba", "dunya"))
print(e)

# tuple
f = tuple(("benim", "adim", "froz"))
print(f)

#range
g = range(100)
print(g)

#dict
h = dict(name="froz", age=22)
print(h)

#set
i = set(("elma", "prtokal", "limon"))
print(i)

#frozenset
j = frozenset(("elma", "prtokal", "limon"))
print(j)

#bool
k = bool(98)
print(k)

#bytes
l = bytes(8)
print(i)

#bytearray
m = bytearray(4)
print(m)

# memoryview
n = memoryview(bytes(23))
print(n)

# 13/02/2023
#Python numbers

#integer
o = 35656222554887711
print(o)

#Float
p  = 9.7639
print(p)
"""
# Float can also be scientific numbers with an "e" to indicate the power of 10.
# e qiimaheeda waa 10 yacni, 5e1 = 5 * 10 waanna 50. mar walba e waxa ka dambeeya tirada ey tahay baa zero u xisaabin. tusaale 1e4 waa (1*10000 = 10000)
#float power
p2 = 5e8 #500000000
print(p2)

#complex
q = 234.5j
print(q)

#Type Conversion
#convert from int to float:

r = float(10)
print(r)

# convert float to complex

s = complex(29.44)
print(s)

# Random Number

# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

#Import the random module, and display a random number between 1 and 9:

import random

print(random.randrange(5, 18944))














