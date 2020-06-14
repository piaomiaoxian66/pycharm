# 与代码沟通input
str=input("我是机器人：请说话：")
print(str+"?")

# 给半径求周长和面积
pai = 3.14
radius = float(input("请输入半径，为你计算周长和面积"))
girth = 2 * pai * radius
area = pai * radius ** 2
print("半径是{}，周长是{}，面积是{}".format(radius, girth, area))

# 判断闰年
y = int(input("请输入年份："))
result = (y % 100 != 0 & y % 4 == 0 or y % 400 == 0)
print(result)

#你是不是我们中的一员?
