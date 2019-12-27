# Python Day 12 
# 创建 和 使用 类
class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性和 name 和 age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")
    
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")
    
my_dog = Dog('willie', 6)

# 1.访问属性例子 my_dog.name

print("\nMy dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# 2.调用方法
my_dog.sit()
my_dog.roll_over()

# 3.创建多个实例
ming_dog = Dog('ming', 7)
your_dog = Dog('ziyanziyu', 12)

print("\nMy dog's name is " + ming_dog.name.title() + ".")
print("My dog is " + str(ming_dog.age) + " years old.")
ming_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()

# case 9 - 1
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("\nThe restaurant's name is " + self.restaurant_name.title() + ".")
        print("The restaurant's cuisine_type is " + self.cuisine_type.title() + ".")
    
    def open_restaurant(self):
        print("The restaurant " + self.restaurant_name.title() + " is now opened.")
    
# case 9 - 2
a_restaurant = Restaurant('A', 'big')
b_restaurant = Restaurant('B', 'mid')
c_restaurant = Restaurant('C', 'small')

a_restaurant.describe_restaurant()
b_restaurant.describe_restaurant()
c_restaurant.describe_restaurant()

# case 9 - 3
class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("\nThe user's first name is " + self.first_name.title()
            + ", the user's second name is " + self.last_name.title() + ".")

    def greet_user(self):
        print("Hello, " + self.first_name.title() + " " + self.last_name.title() + ".")

a_user = User("tony", "stark")
b_user = User("steve", "rogers")

a_user.describe_user()
a_user.greet_user()

b_user.describe_user()
b_user.greet_user()
    
# 9.2 使用类和实例
class Car():

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

my_new_car = Car('audi', 'a4', 2016)
print("\n" + my_new_car.get_descriptive_name())





    