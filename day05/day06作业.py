# 1、创建一个空列表，命名为names，往里面添加 soph、Rain、Jack、linda、tom和Black元素。
names = ['soph', 'Rain', 'Jack', 'linda', 'tom', 'Black']
# 2、往(1)中的names列表里Black前面插入一个Blue。
names.insert(5, 'Blue')  # before 插入第五索引前面
# print(names)
# 3、把names列表中soph的名字改成中文。  # 修改
names[0] = '苏菲'
# print(names)
# 4、往names列表中Rain后面插入一个子列表["oldboy","oldgirl"]。
names.insert(2, ["oldboy", "oldgirl"])
# print(names)
# 5、返回names列表中tom的索引值（下标）。
# print(names.index("tom"))
# 6、创建新列表[1,2,3,4,2,5,6,2]，合并到names列表中。
list3 = [1, 2, 3, 4, 2, 5, 6, 2]
# 把整个list3追加到最后面，相当于列表中的子列表
names.append(list3)
# print(names)
# extend通过append循环列表加入到前面的列表中
names.extend(list3)
# print(names)
# 7、取出names列表中索引4-7的元素。
# print(names[4:8])
# 8、取出names列表中索引2-10的元素，步长为2。
# print(names[2:11:2])
# 9、取出names列表中最后3个元素。
# print(names[-3:])
# 10、循环names列表，打印每个元素的索引值和元素。
# for index in names:
#     print(index)
# 11、循环names列表，打印每个元素的索引值和元素，当索引值为偶数时，把对应的元素改成-1。
# for i, index in enumerate(names):
#     if i % 2 == 0:
#         index = -1
#         print(i, index)
#     else:
#         print(i, index)
# 12、names列表里有3个2，请返回第二个2的索引值，不要人肉，要动态找。
# print(names)
# print(names.index(2))
# names.remove(2)
# print(names)
# print(names.index(2)+1)

# 13、现有商品列表如下：
# • 　　products = [[“iphone",6888],["MacPro",14800],["⼩⽶6",2499],
#                 ["Coffee",31],["Book",60],["Nike",699]]， • 需打印出带索引和不带索引格式：
# products = [["iphone",6888],["MacPro",14800],["⼩⽶6",2499],["Coffee",31],["Book",60],["Nike",699]]
# # for i in products:
# #     print(i)
# for i,indext in enumerate(products):
#     print(i,indext)

# 1. 想出⾄少5个你渴望去旅游的地⽅。
list1 = ['shanghai', 'suzhou', 'hangzhou', 'nanjing', 'tianjin']
# 2. 将这些地⽅存储在⼀个列表中，并确保其中的元素不是按字⺟顺序排列的。
# 3. 按原始排列顺序打印该列表。不要考虑输出是否整洁的问题，只管打印原始Python列表。
# list1.sort()
# print(list1)
# 4. 使⽤sorted()按字⺟顺序打印这个列表，同时不要修改它。
# print(sorted(list1))
# print(list1)
# 5. 再次打印该列表，核实排列顺序未变。
# print(list1)
# 6. 使⽤sorted()按与字⺟顺序相反的顺序打印这个列表， 同时不要修改它。********
# print(sorted(list1, reverse=True))
# print(list1)
# 7. 再次打印该列表，核实排列顺序未变。
# print(list1)
# 8. 使⽤reverse()修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
# print(list1)
# list1.reverse()
# print(list1)
# 9. ⽤reverse()再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序。
# list1.reverse()
# print(list1)
# 10. 使⽤sort()修改该列表，使其元素按字⺟顺序排列。打印该列表，核实排列顺序确实变了。
# print(sorted(list1))
# print(list1)

"""
• 3.列表倒数a=[123,4567,12,3456] 输出 a = [321, 7654, 21, 
6543]
"""
# • 1.元组元素求和b=(1,2,3,4,5,6,7,8,9)
# b = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# a=sum(b)
# print(a)

# • 2.输出元组内7的倍数及个位为7的数
b = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)
for i in b:
    if i % 7 == 0 or i % 10 == 7:
        print(i)

# • 3.列表倒数a=[123,4567,12,3456] 输出 a = [321, 7654, 21,
# 6543]
a = [123, 4567, 12, 3456]
b = []
for i in a:
    num = str(i)
    s = num[::-1]
    n = int(s)
    b.append(n)
print(b)