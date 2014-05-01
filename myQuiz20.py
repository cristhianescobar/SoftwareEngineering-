#!/usr/bin/env python3

a = [2,3,4]

print((a+a)[10:-10:-2])

a = [0,1,2]
print(a+a)
print((a+a)[-8:10:1])


class A:
	def __init__(self):
		self.i = 2

	def f(self):
		print(self.i)

class B(A):
	def __init__(self) :
		pass

	def g(self) :
		self.i = 3
		# print("B instance called g()")

	def f(self, num):
		print ("Class B: ")
		print (self.i)


x = A()
x.f()

x =  B()
# x.f()

x.g()
x.f(2)
