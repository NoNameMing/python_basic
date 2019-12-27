# Python Day 11

from Day10 import show_completed_models
from Day10 import show_completed_models as scm

# chapter 8.5.1 结合使用 位置实参 和 任意数量实参
def make_pizza(size, *toppings):
    """概述要制作的 pizza """
    print("\nMaking a " + str(size) + 
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# chapter 8.5.2 使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的的一切"""
    profile = {}
    profile['first_name'] = first
    profile['second_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('ming', 'noname', 
                            location = '中国',
                            field = '山西',
                            hobby = '代码')

print(user_profile)

# case 8 - 12
def make_sandwich(*toppings):
    print("\nThe toppings you have added: ")
    for topping in toppings:
        print("- " + topping)

make_sandwich('辣椒', '洋葱')
make_sandwich('培根', '番茄', '虾')
make_sandwich('芝士', '胡萝卜', '洋葱')

# case 8 - 13
# line 24

# case 8 - 14
def store_cars(manufacture, model, **car_info):
    car_store_info = {}
    car_store_info['car_manufacture'] = manufacture
    car_store_info['car_model'] = model
    for key, value in car_info.items():
        car_store_info[key] = value
    return car_store_info

car_info = store_cars('audi', 'A6L', 
                        len = '5050')
print("\n" + str(car_info))

# 8.6 导入了函数，在代码头部
test = ['NoName', 'ming']

# 方式一 - 调用模块
import Day10
# 格式 module_name.function_name()
print("\n方式一")
Day10.greet_users(test)

# 方式二 - 直接调用包中函数
from Day10 import show_completed_models
# 调用单个函数时不需要写 包名 ，直接写就好
print("\n方式二")
hello = []
show_completed_models(hello)

# 方式三 - 给函数指定别名
from Day10 import show_completed_models as scm
print("\n方式三")
# 改变导入函数名，与函数二相同
scm(hello)

# 方式四 - 给模块指定别名
import Day10 as dt
print("\n方式四")
dt.greet_users(test)

# 方式五 - 导入模块中所有函数
from Day10 import *
magician = ['Ming']
print("\n方式五")
show_magicians(magician)

