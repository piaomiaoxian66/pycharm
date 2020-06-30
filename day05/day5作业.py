# # 转换大写
# str1="abcd"
# print(str.upper(str1))
#
# # 计算位置
# print(str1.find('cd'))
#
# # 用逗号分割
# str2="a,b,c,d"
# print(str2.split(','))

# # 改错 "{name}喜欢{fruit}".format(name="李雷")
# str1="李雷"
# str2="fruit"
# print("{}喜欢{}".format(str1,str2))

# # 替换字符串
# str10086='python 蟒蛇'
# print(str10086.replace('python','java'))
#
#
# # 将字符串通过某个字符连在一起
# seq = ("y", "u", "z", "i", "m", "o", "u")
# print('_'.join(seq))
# print('_'.join(seq).split('_'))
#
# 将字符串按某个字符分隔开输出
# str3="我说:我今天很高兴！"   # 想得到今天很高兴！
# print(str3.split("我")[2])
# print(str3.split(":"))
# str4 = "编号 标题 测试数据 测试结果"
# print(str4.split(" "))

"""
给定⼀个 haystack 字符串和⼀个 needle 字符串，在 haystack
字符串中找出 needle 字符串出现的第⼀个位置 (从0开始)。如
果不存在，则返回 -1。
输⼊:haystack = "hello", needle = "ll"输出:2
输⼊:haystack = "aaaaa", needle = "bba"输出:-1
"""
# haystack = "hello"
# needle = "ll"
# print(haystack.find(needle))
# haystack = "aaaaa"
# needle = "bba"
# print((haystack.find(needle)))

# 把'hello'的第⼀个字符'h'，改为⼤写的'H'
# qwer='hello'
# print(qwer.replace('h','H'))

# # 将Python替换成python
# string = "Python is good"
# print(string.replace("Python","python"))

# # 获取字符串中.html前面的部分，用尽可能多的方法
# string = "python修炼第一期.html"
# print(string[:-5])   # 直接取
# print(string.split(".")[0])   # 切片
# print(string.replace(".html",""))   # 替换
# print(string.rstrip(".html"))  # 去除右边字符串
# string = "python修炼第一期"
# print(string)

# 如何获取字符串的长度  使用len（str）即可获得

# str0="this is a book"
# # 将book换成apple
# print(str0.replace("book","apple"))
# # 判断该字符串是否以this开头
# print(str0.startswith('this'))
# # 判断该字符串是否以apple结尾
# print(str0.endswith("apple"))
# # 将大写转换成小写
# print(str0.lower())
# # 将小写转换成大写
# print(str0.upper())
# # 删除末尾的回车符
# str1="this is a book\n"
# print(str1.rstrip("\n"))


# x="abc"
# y="def"
# z=["d","e","f"]
# # 求出x.join(y)和x.join(z)
# print(x.join(y))
# print(x.join(z))

# a="hehheh "
# # 去除收尾空格
# print(a.rstrip(" "))
# print(a.split(" ")[0])

# s="linda tom linda meshial linda"
# # 统计字符串中n和m出现的次数
# print(s.count("n"))
# print(s.count("m"))