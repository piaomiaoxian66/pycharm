"""  1
what_he_does = ' plays '
his_instrument = ' guitar '
his_name = 'Robert Johnson'
artist_intro = his_name + what_he_does +his_instrument

print(artist_intro)   #输出结果 Robert Johnson plays  guitar
"""
"""  2
num = 1
string = '1'
num2 = int(string)
print(num + num2)
"""

"""  3
words = 'words' *3
print(words)
"""

"""  4
word = 'a loooooong word'
num = 12
string = 'bang!'
total = string * (len(word) - num)  #等价于字符串'bang！'*4
print(total)
"""

"""  5
name = 'My name is Mike'

print(name[0])
print(name[-4])
print(name[11:14])
print(name[11:15])
print(name[5:])
print(name[:5])
"""

"""  6
word = 'friends'
find_the_evil_in_your_friends = word[0]+word[2:4]+word[-3:-1]
print(find_the_evil_in_your_friends)
print(word[2:4])
print(word[-3:-1])
"""

"""  7
url = 'http://ww1.site.cn/14d2e8ejw1exjogbxdxhj20ci0kuwex.jpg'
file_name = url[-10:]
print(file_name)
"""

"""  8
phone_number = '1303-998-9241'
hiding_number = phone_number.replace(phone_number[:9],'*'*9)
print(hiding_number)
"""

"""  9
search = '168'
num_a = '1386-168-0006'
num_b = '1681-222-0006'

print(search + ' is at ' + str(num_a.find(search)) + ' to ' + str(num_a.find(search) + len(search)) + ' of num_a ')
print(search + ' is at ' + str(num_b.find(search)) + ' to ' + str(num_b.find(search) + len(search)) + ' of num_b ')
"""






























