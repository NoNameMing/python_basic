# Python 学习 Day6
# 内容 Chapter 6 字典

# 6.1 一个简单的字典
# 键值对用一对花括号表示
alien_0 = {'color': 'green', 'points': 5}

# 访问字典中的值
print(alien_0['color'])
print(alien_0['points'])

# 同上
new_points = alien_0['points']
print("\nYou just earned " + str(new_points) + " points!")

# 添加键值对值
alien_0['x_position'] = 0
alien_0['y_position'] = 25

# 打印键值对，类似打印数组所有内容
print(alien_0)

# 空字典创建，使用花括号
alien_0 = {}

alien_0['color'] = 'green'
alien_0['ponits'] = 5

print("\nthe new dictionary:")
print(alien_0)

# 修改字典中的值
alien_0 = {'color': 'green'}
print("\nThe alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + '.')

# 向右移动外星人
# 据外星人当前速度决定他们能移动多远

# 初始化
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("\nOriginal x-position: " + str(alien_0['x_position']))

# 判定条件
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人速度一定很快
    x_increment = 3
    
# 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

# 修改外星人的速度
alien_0['speed'] = 'fast'
print("\nFast speed activated, current speed is " 
    + alien_0['speed'] + ".")

# 再走一次
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人速度一定很快
    x_increment = 3
    
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

# 删除键值对
alien_0['points'] = 100
print("\nthe current dictionary is: " + str(alien_0))

del alien_0['points']
print("\nAfter deleting the key 'points', the dictionary is: "
     + str(alien_0))

# 由类似对象组成的字典
favorite_languages = {
    'jea': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'ming': 'c++',
    'jie': 'python',
    }

print("\nMing's favorite language is " +
    favorite_languages['ming'].title() +
    ".")

# case 6 - 1
An_old_friend = {'first_name': 'Yi', 'last_name': 'Zheng', 
                'age': '18', 'city': 'NanJing'}

print("\nthe info of my old friend is " + str(An_old_friend))

# case 6 - 2
Attitudes_To_Life = {'Parents': 'Love', 'PeopleLoveMe': 'Respect',
                    'Enemies': 'defend', 'MySelf': 'Deciplined'}
print("\nMy Attitude to my parents: " + Attitudes_To_Life['Parents'])
print("My Attitude to myself: " + Attitudes_To_Life['MySelf'])

# case 6 - 3
# 与题意不同，我做的是一个搜索键值对
Searching_Key = {'p': 'Python', 'c': 'C/C++', 'j': 'Java', 
                'r': 'Ruby'}

print("\nSimple show for my Search_Key: " + str(Searching_Key))

# 6.3 遍历字典
# 遍历键值对 items()
for keys, values in Searching_Key.items():
    print("\nKey: " + keys)
    print("Value: " + values)

# 遍历字典中的所有键 keys()
# print("\nAll keys in Searching_Key: ")
# for name in Searching_Key.keys():
#     print(name.title()) 
#     if name.values() in favorite_languages.values():
#         print("the key " + name + "finds the person who love it and the pserson is " 
#         + name.values().key())

# 遍历字典中的所有键 keys() 方法
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +
        ", I see your favorite language is " +
        favorite_languages[name].title() + "!")

# 用 keys() 确定某个人是否接受了调查
if 'Ming' not in favorite_languages.keys():
    print("\nMing, please take our poll!")
    print("Ming: Fuck You.")

flag = 0
for name in sorted(favorite_languages.keys()):
    if flag == 0:
        print("\n" + name.title() + ", fuck you.")
        flag = 1
        continue
    print(name.title() + ", fuck you.")

# 遍历字典中的所有值 values() 方法
print("\nthe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# 集合，类似列表。但不考虑元素是否重复
print("\nThe following language have been mentioned(no repeating): ")
for language in set(favorite_languages.values()):
    print(language.title())

# case 6 - 4
dictionary = {'Flask': 'a lightweight WSGI web application framework', 
            'PyPI': 'a repository of software for the Python programming language.',
            'pip': 'the package installer for Python',
            'Fabric': 'a high level Python (2.7, 3.4+) library designed to execute shell commands remotely over SSH',
            'Django': 'a high-level Python Web framework'
            }

# 控制格式变量
flag = 0
for key in dictionary.keys():

    if flag == 0:
        print("\n" + key + ": " + dictionary[key])
        flag = 1
        continue
    print(key + ": " + dictionary[key])

# case 6 - 5
rivers = {'nile': 'egypt', 'changjiang river': 'china',
        'amazon': 'brazil', 'nile': 'kennya'}

for river, country in rivers.items():
    print("The " + river.title() + "runs through " + country.title() + ".")

print("\nall the rivers:")
for river in set(rivers.keys()):
    print(river)

print("\nall the countries:")
for country in set(rivers.values()):
    print(country)

# case 6 - 6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people_invited = ['jen', 'sarah']

print("")
for name in favorite_languages.keys():
    if name in people_invited:
        print("Dear, " + name + ". Thank you for coming.")
    else:
        print("Dear, " + name + ". I would like to invite you to my investigation.")
    
# 6.4 嵌套
# 6.4.1 字典列表，列表中存字典
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

print("")
for alien in aliens:
    print(alien)

# 自动生成 aliens
# 空列表
print("")
aliens = []

# 创建30个相同外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# 显示前五个外星人
for alien in aliens:
    print(alien)
print("...")

# 显示创建了多少个外星人
print("Total number of aliens: " + str(len(aliens)))

# 生成方式升级
aliens = []

# 先生成
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'low'}
    aliens.append(new_alien)

# 再修改
for alien in aliens[0: 3]:
    if alien['color'] == 'green':
        alien['color'] == 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# 显示前五个外星人
for alien in aliens[0: 5]:
    print(alien)
print("...")

# 6.4.2 在字典中存储列表
# 例子1：
    # 存储所有披萨信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

    # 概述所点的披萨
print("You ordered a " + pizza['crust'] + "-crust pizza" +
        "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

# 例子2：
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
    }

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
            print("\t" + language.title())

# 6.4.3 字典中存储字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last' : 'curie',
        'location': 'paris',
        }
    }

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

# case 6 - 7
