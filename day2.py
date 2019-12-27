# 日期：2019年8月1日
# 日程：学习 Python Day 2
# 内容：字符串收尾、数字部分（浮点和整数）

# 使用字符串时避免语法错误，以下这种情况不能用单引号
message = "One of Python's strengths is its diverse community."
print(message)

# 字符串打印练习 p22 case 2 - 3 至 2 - 7

# case2 - 3
name = "NoName Ming"
print("Hello" + name +", would you like to learn some Python today?")

# case 2 - 4
# 打印小写
print(name.lower())

# 打印大写
print(name.upper())

# 打印首字母大写
print(name.title())

# case 2 - 5 
saying = 'I said, "try everything"'
print(saying)

# case 2 - 6
famous_person = "ChenHongyu"
message = "Hello"
message2 = ", would you like to learn some Python today?"
print(message + famous_person + message2)

# case 2 - 7
delBlank = " NmN "
print(delBlank)
print(delBlank.lstrip())
print(delBlank.rstrip())
print("\t\n" + delBlank.strip())

# 2.4 数字

# 次方运算 3 的 4 次方
p = 3 ** 4
print(p)

# 和 string 一起打印时需要把 int 转化为 string 类型
age = 23
message = "Happy" + str(age) + "rd Birthday!"

print(message)

# case 2 - 7
print(5 + 3)
print(5 - 3)
print(5 * 3)
print(5 / 3)

# case 2 - 8
message = "Best Number of mine is "
num = 6
print(message + str(num))

# Chapter 3 列表

# 自行车列表
bicycles = ['terk', 'cannoandale', 'redline', 'specialized']
# 打印所有数据
print(bicycles)

# 3.1 索引 

# 打印第三个数据，下标从 0 开始
print(bicycles[2].title())

# 访问列表最后一个元素
print(bicycles[-1])

# 访问列表倒数第二个元素，之后的以此类推
print(bicycles[-2])

message = "My Best bicycle is a " + bicycles[0].title() + "."
print(message)

# case 3 - 1
friends = ["YinHaoming", "ShenYunlong", "LeiShang", "ZhengYi", "LinYuchao"]
print(friends)

# case 3 - 2
print(friends[3])

# case 3 - 1
message = "I used to be the best friend of " + friends[0] + "."

# 3.2 修改列表元素

# 修改某索引处的列表值
motorbicycles = ['honda', 'yamaha', 'suzuki']
motorbicycles[0] = 'hondaBestGP2Engine' 

# 在列表最后一位添加一个元素
motorbicycles.append('ducati')
print(motorbicycles)

# 有了 append 方法之后的 创建表的方式
listTest = [] 
listTest.append('h2')
listTest.append('y2')
listTest.append('s2')

# 在索引处插入元素，索引处后方元素向后移动
motorbicycles.insert(1, 'ducati')
print(motorbicycles)

# 删除元素 del 方法，特性：删除后不再使用
del motorbicycles[0]
print(motorbicycles)

# 删除元素 pop 方法，默认删除最后一个，但是可以通过指定下标删除特定元素。特性：删除后还可以使用
poped_motor = motorbicycles.pop()
print(motorbicycles)
print("poped element: " + poped_motor)
print("the first element to be deleted: " + motorbicycles.pop(0))

# 根据值删除元素，但是删除的是它第一次出现的位置的那个元素；也就是说，默认只删除一次。
motorbicycles.remove('suzuki')

# case 3 - 4
toBeInvented = []
toBeInvented.append('Father & Mother')
toBeInvented.append('YinHaoming')
toBeInvented.append('TonyStark')

# case 3 - 5
message = ["Dear ", ", I'd love to invite you to my party"]
for guest in toBeInvented:
	print(message[0] + guest + message[1])

# case 3 - 6
toBeInvented.insert(0, 'GrandFather & GrandMother')
toBeInvented.insert(2, 'NoNameMing')
toBeInvented.append('Petter Parker')

for guest in toBeInvented:
	print(message[0] + guest + message[1])

# case 3 - 7
while (len(toBeInvented) != 2):
	poped_guest = toBeInvented.pop()
	print("Sorry, " + "my dear friend " + poped_guest + ", I can't invite you anymore")
	pass

message.insert(1, ", though something wrong happend")
message.append(" still.")
for guest in toBeInvented:
	print(message[0] + guest + message[1] + message[2] + message[3])

# 3.3 组织列表
cars = ["bmw", "audi", "toyota", "subaru"]

# 按首字母从低到高排列
cars.sort()
print(cars)

# 倒置数组（按字母顺序）
cars.sort(reverse = True)
print(cars)

# 临时倒置数组的方法 sorted()
cars = ["bmw", "audi", "toyota", "subaru"]
print("Here is the original list: ")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars))

print("\nHere is the original list again: ")
print(cars)

# 倒置数组（相反于最开始的顺序）
cars.reverse()
print(cars)

# 数组长度
print(len(cars))


# case 3 - 8
palcesWantToGo = []
palcesWantToGo.insert(0, 'MoutainHua')
palcesWantToGo.append('HangZhou')
palcesWantToGo.append('ChongQing')
palcesWantToGo.append('HongKong')
palcesWantToGo.append('Tokyo')

print("\nthe original sequence of the places I want to go: ")
print(palcesWantToGo)
print("\nsorted sequence of the places I want to go, but I didn't change the arr sequence.")
print(sorted(palcesWantToGo))
print("\nchecking if the sequence is changed: ")
print(palcesWantToGo)

palcesWantToGo.reverse()
print("\nreversing the arr with the reverse method: ")
print(palcesWantToGo)

palcesWantToGo.reverse()
print("\nrecover the arr: ")
print(palcesWantToGo)

palcesWantToGo.sort()
print("\n按字母排序：")
print(palcesWantToGo)

palcesWantToGo.sort(reverse = True)
print("\n按字母倒置排序：")
print(palcesWantToGo)

# chapter 4 列表操作
# chapter 4 - 1

magicians = ["alice", "david", "carolina"]

# 循环打印列表元素
for magician in magicians:
	print(magician)








