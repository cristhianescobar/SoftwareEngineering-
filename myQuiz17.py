from copy import copy, deepcopy

class A:
	def __init__(self):
		self.a = [2, [3], 4]

x = A()
y = copy(x)

print(x.a is y.a)
print(x.a == y.a)

z = deepcopy(x)

# False since its a referance comparison?
print(x.a is z.a)
# The second element is an array, so I am guessing the 
# thing that is store in A()[1] is a reference? NOOOOO
# False since the way deep copy works is recursovely copies all the items in the array
print (x.a is z.a)


# since x and y are both pointing to A()
# they both share the same data. To prove
# this let's ater the data on x and see if it still equals x

y.a[0] = "Changed using y"

print(str(x.a[0]))
print(str(x.a[0]) == "Changed using y")
print(x.a)
print(x.a[0] == y.a[0])

# So what we learned from this quiz is that when using copy
# we are essantially just making a copy of the reference of the actual obj
# therefore if we were to compare x and y they are essentially equals
# print(x is y) is false because the reference itself  are both in different places in memory
