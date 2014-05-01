#!/usr/bin/env python3

# ----------
# RegExps.py
# ----------

import re

sentence = "Looking for an 'A' \n somewhere here"
# print (sentence)

# Start of a string Regular Expresion
a = re.split("^Looking",sentence)
assert(len(a) == 2)
a = re.split("^None", sentence)
assert(len(a) == 1)

# End of the string 
sentence = "One big party\nFor me only"
a = re.compile("y$", re.M)
r = a.split(sentence)
print (r)


sentence = "1No1"
a = re.split("\d", sentence)
assert(len(a) == 3)
print (a)

print ("Done")