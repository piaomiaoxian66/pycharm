# print(3 and 4)   #3是true返回4
# print(3 or 4)   #3是true返回3
# number=1
# print()

# a=-5
# print(id(a))
# b=-5
# print(id(b))

from sys import getrefcount
a = [1, 2, 3]
print(getrefcount(a))
b=a
print(getrefcount(a))
c = [a, a]
print(getrefcount(a))
del c,b
print(getrefcount(a))
del a
print("a被销毁了")