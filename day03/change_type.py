# 字符串转化成整数   int()
# a = '10'
# b = 10
# c = int(a) + b
# print(c)

# 整数转换成字符串   str()

# a = '10'
# b = 10
# c = a + str(b)
# print(c)

# 把字符串编程小数前面加   float

# a = '10.8'
# b = 10.3
# c = float(a) + b
# print(c)

# 把小数 （强转）成int类型 ,失去小数部分
# c = 3.1415
# print(int(c))
# d = 9.99
# print(int(d))
# print(int(c + d))

"""
tuple(s) 将序列 s 转换为⼀个元组
list(s) 将序列 s 转换为⼀个列表
set(s) 转换为可变集合
dict(d) 创建⼀个字典。d 必须是⼀个 (key, value)元组序列。
eval(str) ⽤来计算在字符串中的有效Python表达式,并返回⼀个对象。 eval(“3*5”)
chr(x) 将⼀个整数转换为⼀个字符 chr(97)  数字转换成字母
repr(x) 将对象 x 转换为表达式字符串
"""""

str1 = "yuzimou是中国人是中国人"
# print(tuple(str1))
# print(list(str1))
# print(set(str1))  # set无序的，没有重复    去重
# print(str(set(str1)))
# tuple1=('name','age')
# tuple2=('于子谋',21)
# print(dict(tuple1))
# 无法强转，按要求定义可以
# dict1={tuple1,tuple2}
# print(dict1)


# print(chr(65))
# print(chr(97))
# str2 = '3*5'
# 期望返回是15不是3*5，而是计算后的值
# print(eval(str2))

b = {"name": "yuzimou", "age": 21}
# print(type(b))
# print(b['name'])
str_b = repr(b)
print(str_b[0])


my_list1=[1,2,3,3,4,5,5]
print(set(my_list1)) # 列表list转成set 变成不重复的。
print(list(set(my_list1))) # 转换成列表    换成一个不重复的列表
print(set(b)) # 字典类型dict转成set只有key值
print(set(b.values)) # 字典类型dict转成set只有key值
print(list(b.values())) # 字典转成列表，key,value可以单转
print(list(b.keys())) # 字典转成列表，key,value可以单转