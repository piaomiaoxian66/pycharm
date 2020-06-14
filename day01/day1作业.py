# 给出半径计算圆的周长和面积
# import math
#
# r = input("请输入半径：")
# pi = math.pi
# r = float(r)
# c = 2 * pi * r
# s = r ** 2 * pi
# print("该圆的周长为{}，该圆的面积为{}".format(c, s))

# 给出年份，如果是闰年输出True，否则输出False

def is_leap(year):
    year = int(year)
    if (year % 4 == 0) and (year % 100 != 0):
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


while(True):
    year = input("请输入一个年份:")
    if year == 'exit':
        import sys
        sys.exit(0)
    print("%s是闰年吗? %s" % (year, is_leap(year)))


# # 将薪水以千为单位，输出保留小数后两位
# salary = input("请输入薪水：")
# salary = float(salary)
# salary = salary / 1000
# print(f"My salary is {salary:3.3f}")
#
# # 输出1000个我爱你
#
# ni_11 = "我爱你" * 1000
# print(ni_11)
#
# # “linda”和“我爱你”两个字符串拼接在一起
#
# abc = "linda"
# bcd = "我爱你"
# print(abc + bcd)
