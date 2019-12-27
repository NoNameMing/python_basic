# Day5 
# 内容：chapter5 --- if 语句

# 5 - 3 if语句
# 判定方式 --- if-else 结构
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Go for your voting!")
else:
    print("Sorry, you are too young to vote.")
    print("Pleae register to vote as soon as you turn 18!")

# 判定方式 --- if-elif-else 结构
age = 12
if age < 4:
    print("\nYour admission cost is $0.")
elif age < 18:
    print("\nYour admission cost is $5.")
else:
    print("\nYour admission cost is $10.")

# 判定方式 --- 多个 elif 结构
age = 68
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 3

print("\nYour admission cost is $" + str(price) + ".")

# 判定方式 --- 省略 else 代码块
age = 64

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 3

print("\nYour admission cost is $" + str(price) + ".")

# 以上判定方式只能判定只有一个条件满足的情况。

# 以下方式可检查作者关心的所有条件：
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("\nAdding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

alien_color = 'red'

# case 5 - 3
if alien_color == 'green':
    print("5PTS! KILLING GREEN ALIENS!")
else:
    print("You didn't get any points.")

# case 5 - 5
if alien_color == 'green':
    print("5PTS! KILLING GREEN ALIENS!")
elif alien_color == 'red':
    print("10PTS! KILLING YELLOW ALIENS!")
else:
    print("15PTS! KILLING RED ALIENS")

# case 5 - 6
age = 23
if age < 2:
    print("He/She is a baby.")
elif age < 4:
    print("He/She is learning walking.")
elif age < 13:
    print("He/She is a child.")
elif age < 20:
    print("He/She is a teenager.")
elif age < 65:
    print("He/She is an adult.")
else:
    print("He/She is old.")

# case 5 - 7
favorite_fruits = ['peach', 'watermelon', 'banana']
if 'peach' in favorite_fruits:
    print("\npeach found in your list.")
if 'apple' in favorite_fruits:
    print("\napple found in your list.")
if 'life' in favorite_fruits:
    print("\nlife continues.")
if 'watermelon' in favorite_fruits:
    print("\nwatermelon found in your list.")
if 'banana' in favorite_fruits:
    print("\nbanana found in your list.")
print("\nlist-search completed.")

# 5 - 4 使用 if 语句处理列表
# 简单循环
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print("\nAdding " + requested_topping + ".")

print("\nFinished making your pizza!")

# 处理特殊元素
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("\nSorry, we are out of green peppers right now.")
    else:
        print("\nAdding " + requested_topping + ".")

print("\nFinished making your pizza!")

# 处理列表是否为空的
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("\nAre you sure you want a plain pizza?")

# 使用多个列表
avaliable_toppings = ['mushrooms', 'olives', 'green peppers',
                     'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in avaliable_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")

# case 5 - 8 && 5 - 9
users = ['admiNUser', 'user2', 'user3', 'user4','user5']

for user in users:
    if user == 'admiNUser':
        print("\nHello admin, would you like to see a status report?")
    elif user == '':
        print("\nThe user does not have a name.")
    else:
        print("\nWe've found ueser " + user + ".")

# case 5 - 10
current_users = ['Abbie', 'Baby', 'Cindy', 'Delta', 'Ela', 'John']
new_users = ['Abbie', 'Baby', 'Cry', 'Derrick', 'Elisa', 'JOHN']
temp = []

# 笨办法，用一个新数组存储 current_users 中转化后的字符串
for current_user in current_users:
    temp.append(current_user.lower()) 

for new_user in new_users:
    if new_user.lower() in temp:
        print("Sorry, the user " + new_user + " is already in the list")
    else:
        current_users.append(new_user)
        print("the new user has been put in the list.")
print("the current_users are: " + str(current_users))

# case 5 - 11
numList = []
number = 1

while number != 10:
    numList.append(number)
    number += 1

for number in numList:
    if number == 1:
        print("\n" + str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")
    
