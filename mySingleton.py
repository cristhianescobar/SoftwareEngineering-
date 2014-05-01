#!/usr/bin/env python

# ------------
# Singleton.py
# ------------

print("Singleton.py")

class A (object) :
    def f (self) :
        return "A.f()"

y = A()
print (y.f())

A = A()
print(A.f())

# b = A()
# print(b.f()

def BDecorator(callable1):
	x = callable1()
	return lambda : x

@BDecorator	
class B1 (object) :
    def f (self) :
        return "B1.f()"




only = B1()
print(only.f())
assert(only is B1())

