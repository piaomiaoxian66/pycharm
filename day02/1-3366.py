# list1 = [1, 2, 3]
# print(id(list1))
# list1.append(4)
# print(id(list1))
# list2 = ['a', 1]
# print(id(list2))
# list3 = list1 + list2
# print(id(list3))
# print(list3 * 2)


# 可变
# list1 = [1, 2, 3]
# print(id(list1))
# list2 = [1, 2, 3]
# print(id(list2))
# list3 = list1 + list2
# print(list1 == list2)  # True
# print(list1 == [1, 3, 2])  # False
# print([1, 2] in [1, 2, 3])  # False
# print([1, 2] in [[1, 2], 3])  # True
# print(1 in [1, 2, 3])  # True


# print(list1 is list2)  # False
# print(list1 is not list3)  # True

# 字符串中的and 返回是后面值，or 返回的是前面值
# print(list1 and list3)  # [1,2,3,4] list3    当第一个值是true的时候返回l3
# print(list1 or list3)  # [1,2,3] list1       当第一个值是true的时候返回l1
# print([] or list3)  # [1,2,3,4] list3        当第一个值是flase的时候返回l3
# print(not (list1 or list3))  # Flase

# 1 and 1 true
# 1 and 0 flase
# 0 and 1 flase
# 0 and 0 flase

# 元组tuple 不可变，相对不变东西，不希望变化东西
# my_info =('name','sex','age')
# print(my_info[1])
#
#
# tuple1=(1,2,'a')
# tuple2=('3','汉字',(6,0),90)
# tuple3=tuple2+tuple1      #两个tuple可相加
# print(tuple3)
# 不能与其他类型运算
# print(tuple2+'a')
# print(tuple2+[2,5,10])
# print(tuple2+10)
# print(tuple1*3)         #可与数字相乘
# print('a' in tuple1)       #成员 可判断
# print((6,0) in tuple2)      # tuple中的元素可以使⽤成员运算
# print(tuple1 in (1, 2, 'a', 90))
# ⽐较两个tuple包含关系不正确，⽆法⽐较
# print(tuple1 not in (1, 2, 'a', 90))
# print(tuple1 == tuple3)   # 只能比较相等

#   key:value键值对   字典类型:无序的，key是唯一的，通过key来找到value
# dict1 = {'name': 'yuzimou', 'age': 21, 'sex': 'male'}
# print(dict1['name'])
# print(dict1['age'])
# print(dict1)
# dict2={}
# print(dict2)
#
# set1={1,23,'abc'}
# set2=set()
# print(set1)
# print(set2)
















