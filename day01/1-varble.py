print("hello word!")
print("hello word!")


"""
命名规则：
1、变量名只能包含字⺟、数字和下划线。变量名可以⽤字⺟或下划线打头，但不能以数字打头。
2、变量名不能包含空格，但可使⽤下划线来分割其中的单词。
3、不要将Python关键字和函数名⽤作变量名。(help()——keywords)
4、变量名应既简短⼜具有描述性。
5、慎⽤⼩写字⺟l和⼤写字⺟O，因为可能被看错。

Python 中的变量不需要声明。每个变量在使⽤前都必须赋值，变量赋值以后该变量才会被创建。
• 在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
• 等号（=）⽤来给变量赋值。a=1
• 等号（=）运算符左边是⼀个变量名,等号（=）运算符右边是存储在变量中的值。
"""

#
# a3_ = 10
# bc_top = 20
# l1O0 = 11
#
# int1 = 10
# float2 = 12.8
# bool3 = True
# string4 = '我是最帅的'
# list1 = [1, 5.3, 'abc', [6, 8]]
# tuple2 = (1, 2, 'abc')
# dict3 = {'name': 'yuzimou', 'age': 21}
# set4 = {1, 2, 'abc'}
#
# print(type(int1))
# print(type(float2))
# print(type(bool3))
# print(type(string4))
# print(type(list1))
# print(type(tuple2))
# print(type(dict3))
# print(type(set4))


# 数据类型的本质是什么
# 长度，空间的大小

# import sys
#
# print(sys.getsizeof(int1))
# print(sys.getsizeof(float2))
# print(sys.getsizeof(bool3))
# print(sys.getsizeof(string4))
# print(sys.getsizeof(list1))
# print(sys.getsizeof(tuple2))
# print(sys.getsizeof(dict3))
# print(sys.getsizeof(set4))


"""
基本⽤法
• print("⽂件1:", file_name, "⽂件2:", new_name)
• %⽤法
• print("⽂件1的名字是%s,⽂件2的名字是%s，有%d个" %(file_name,new_name,num))
• format⽤法
• print("⽂件1的名字是{},有{:.0f}个,⽂件2的名字是{}".format(file_name,num,new_name))
• 最新⽤法f，python3.6以上⽀持
• print(f'My salary is {salary:10.3f}’)
• print(f"⽂件1的名字是{file_name}，有{num}个,⽂件2的名字是{new_name}")
"""


str3 = "淡黄的长裙，蓬松的头发"
str4 = "裤子"
salary = 99999.99
# print("我今天的搭配是",str3,"我明天穿",str4)
# print("我今天的搭配是%s，我明天穿%s。"%(str3,str4))
# print("我今天的搭配是{}，我明天穿{}。".format(str3,str4))
# print(f"我今天穿的{str3},明天穿{str4}")

# 10总长，3小数点后3位 f:float
print(f"My salary is {salary:10.3f}")
"""
1、整数的输出      ⼗进制：%d,
2、浮点数输出      %f ——保留⼩数点后⾯六位有效数字，%.3f，保留3位⼩数位
3、字符串输出      %s
                 %10s——右对⻬，占位符10位
                 %-10s——左对⻬，占位符10位
                 %.2s——截取2位字符串
                 %10.2s——10位占位符，截取两位字符串
"""