# 作者：NoNamingMing
# 主题：Python 学习 Day3
# 内容：第四章 列表知识

# chapter 4 列表操作
# chapter 4 - 1
magicians = ["alice", "david", "carolina"]

# 循环打印列表元素
for magician in magicians:
	print(magician)

# 在 for 循环结束时打印一条信息
print("Thank you, everyone!")

# case 4 - 1
pizzas = ["focaccia", "margherita", "romana"]
for pizza in pizzas:
    print("\nI have not eaten " + pizza + ".")
print("\nFor, only one time, I ate pizzahut with ZhengYi. After that, i didnt eat anyone anymore.")

# case 4 - 2
# felidae 猫科动物
felidaes = ["lions", "tigers", "felis silverstris"]
for felidae in felidaes:
    print("\n" + felidae + "belongs to felidaes.")
print("\nI am talking about felidaes.")

# range() 函数

# 例子：生成 1 - 8 的数字
for value in range(1, 9):
    print("\n" + str(value))

# 用 range() 函数 生成列表
numbers = list(range(1, 10))
print("\n" + str(numbers))

# 用 range() 函数 指定步长 接下来的最后一个参数 2
even_numbers = list(range(2, 11, 2))
print("\n" + str(even_numbers))

# 用 range() 函数 创建数组 方法一
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print("\n" + str(squares))

# 用 range() 函数 创建数组 方法二
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print("\n" + str(squares))

# 最小值、最大值 求和
print(min(squares))
print(max(squares))
print(sum(squares))

squaresTest = [value ** 2 for value in range(1, 11)]
print("\n" + str(squaresTest))

# case 4 - 3
for val in range(1, 21):
    print("\n" + str(val))

# case 4 - 4
print("meaningless")

# case 4 - 5
listLongs = [val for val in range(1, 1000001)]
print(max(listLongs))
print(min(listLongs))
print(sum(listLongs))

# print 4 - 6
oddNumber = [val for val in range(1, 21, 2)]
print("\nfor print is meaningless, simple is better: " + str(oddNumber))

# case 4 - 7
# out = [val % 3 == 0 for val in range(3, 31)]
out = []
for val in range(3, 31):
    if val % 3 == 0:
        out.append(val)
print("\n" + str(out))

# case 4 - 8
out = [val ** 3 for val in range(1, 11)]
print("\n" + str(out))

# case 4 - 9
# 方法已经用过

# 4.4 列表切片
players = ["Sebastian Vettel", "Charles Leclerc", "Lando Norris", "Carlos Sainz"]

# 切片索引位置理解
print(players[0: 2])

# 未指定第一个索引时，自动从头开始
print(players[: 3])

# 不指定第二个索引，从第一个索引直接结束
print(players[1: ])

# 打印最后三名车手信息
print(players[-3: ])

# 遍历切片列表
for racer in players[: 3]:
    print(racer)

# 复制列表
my_foods = ["vegetables", "water", "chicken", "shrimp"]
copy_foods = my_foods[:]

print("\nmy food list is: " + str(my_foods))
print("\ncopy food list is: " + str(copy_foods))

my_foods.append("purewater")
copy_foods.append("beef")

print("\nmy food list now is: " + str(my_foods))
print("\ncopy food list now is: " + str(copy_foods))

# case 4 - 10
print("\nthe first three items in lists are: " + str(my_foods[0: 3]))
print("\nthe middle three items in lists are: " + str(my_foods[1: 4]))
print("\nthe first three items in lists are: " + str(my_foods[-3: ]))

# case 4 - 11
friend_pizzas = pizzas[:]
pizzas.append("pizzahut")
friend_pizzas.append("fruitpizza")

print("my list of pizza is: " + str(pizzas))
print("friend list of pizza is: " + str(friend_pizzas))

# 4 - 12
# for 用烂了，没意思。

# 4 - 5 元组 元素不可修改
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# 虽然不可修改，但是可以重新赋值
print("original dimensions: " + str(dimensions))
dimensions = (300, 400)
print("dimensions after modified: " + str(dimensions))

# case 4 - 13
foodSupplies = ("apples", "tomatoes", "onions", "watermelons", "carrots")
for foodSupply in foodSupplies:
    print("\n" + foodSupply)

# 会被 Python 拒绝的语句：
# foodSupplies[0] = "ap"

foodSuppliesModified = foodSupplies[:]
foodSuppliesModified = ("apples", "tomatoes", "onions", "melons", "chesseburger")
print(foodSuppliesModified)

