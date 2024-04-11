#!/usr/bin/python3

# Every object has an identity, a type and a value. An object’s identity never changes once it has been created;
# you may think of it as the object’s address in memory. The ‘is’ operator compares the identity of two objects;
# the id() function returns an integer representing its identity
# Since strings are immutable, Python optimizes resources by making two names that refer to the same string value refer to the same object.
# This holds true for almost all immutable data excluding the tuple, set (not frozenset), long strings and integers outside the range -5 to 256

dee = ("1864-10-23", ["poetry, pretend-fight"])
dum = ("1864-10-23", ["poetry, pretend-fight"])
print(f"dee = {dee}")
print(f"dum = {dum}")
print(f"dee == dum: {dee == dum}") # True
print(f"dee is dum: {dee is dum}") # False
print(f"id(dee) = {id(dee)}, id(dum) = {id(dum)}")
T_doom = dum
print(f"id(T_doom) = {id(dum)}, id(T_doom) = {id(dum)}") # Their ids are the same because they are aliases (different labels for or pointing to the same object)
print(f"T_doom is dum: {T_doom is dum}") # True
skills = T_doom[1]
skills.append("rap")
print(f"dum = {dum}")
print(f"dee == dum: {dee == dum}") # False
