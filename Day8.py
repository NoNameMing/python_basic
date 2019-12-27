# Day 8 Python 函数
# Chapter 8

# 定义函数
def greet_user():
    print("显示简单的问候语")

# 调用函数
greet_user()

# 不能重复定义函数，此处需要改名
def greet_user2(username):
    print("hello, " + username.title() + "!")

# 直接写参数进行调用
greet_user2("Ming")

# 调用变量
username = "ming"
greet_user2(username)

# case 8 - 1
def display_message():
    print(" I am learning function in this chapter.")

# case 8 - 2
def favorite_book(title):
    print("One of my favorite book is " + title.title() + ".")
title = "Empire of Qin"
favorite_book(title)

# 位置实参
# 括号内的参数是实参
def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# 实际的参数是 'harry' & 'hamster'
describe_pet('hamster', 'harry')

# 关键字实参
describe_pet(pet_name = "harry", animal_type = "hamster")

# 默认值
def describe_pet_with_default_value(pet_name, animal_type = 'dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet_with_default_value(pet_name = 'willie')

# 默认值也可以修改
describe_pet_with_default_value(pet_name = 'william', animal_type = 'tiger')

# case 8 - 3
def make_shirt(size, parameter):
    print("the size of the shirt is " + size + ", and the parameter on it is " + parameter + ".")

make_shirt(parameter = "FKY", size = "M")

# case 8 - 4
def make_shirt_with_default_value(size, parameter = 'I love python'):
    print("the size of the shirt is " + size + ", and the parameter on it is " + parameter + ".")

make_shirt_with_default_value(size = 'L')
make_shirt_with_default_value(size = 'M')
make_shirt_with_default_value(size = 'M', parameter = 'I need python')

# case 8 - 5
def describe_city(city, country = 'china'):
    print("\n" + city.title() + " is in " + country.title() + ".")

describe_city(city = 'hangzhou')
describe_city(city = 'beijing')
describe_city(city = 'paris', country = 'france')






