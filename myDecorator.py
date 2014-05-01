#!/usr/bin/env python3


# c must be callable
def Decorator(c):
	x = c()
	return lambda : x


class A(object):
	def __init__(self):
		print("A.A()", end = " ")

# Both A's are different objects
# That live in a different place in memmory
print(A() is A()) #False


A = Decorator(A)
# calls the cunstructor once, keeping reference to the same obj
print(A() is A())

A = Decorator(A)
print(A() is A())