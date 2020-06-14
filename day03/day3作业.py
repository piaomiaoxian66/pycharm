# 1、如果输⼊“1，2，3，4”，显示正⽉，⼆⽉，三⽉，四⽉…  数字与汉字⽉份转换
str_month = input("输入数字，即可转化成为汉字月份")
if str_month == '1':
    print("一月")
elif str_month == '2':
    print("二月")
elif str_month == '3':
    print("三月")
elif str_month == '4':
    print("四月")
elif str_month == '5':
    print("五月")
elif str_month == '6':
    print("六月")
elif str_month == '7':
    print("七月")
elif str_month == '8':
    print("八月")
elif str_month == '9':
    print("九月")
elif str_month == '10':
    print("十月")
elif str_month == '11':
    print("十一月")
else:
    print("十二月")


# 2、对商品猜价格：设定⼀个神秘价格。你从控制台输⼊信息价格，让⽤户猜，只提示，猜⼤了，猜⼩了，猜对。
str_price = input("猜出商品的价格")
if str_price < '125':
    print("猜小了")
elif str_price > '125':
    print("猜大了")
else:
    print("猜对了")

# 3、简单描述变量从创建，引⽤到销毁的过程。
# 当变量被赋值的时候，此时就是一个变量创建的过程。
# 创建的时候他计一，每被引用一次，计数就上涨一。
# 被新引用之后，之前变量的赋值就被销毁，变量又被重新赋值

# 4、去除重复元素
# 想出⼏种思路，⽤⼀种实现
list1 = [1, 2, 5, 6, 7, 4, 8, 2, 7, 9, 4, 6, 3]
print(list(set(list1)))
