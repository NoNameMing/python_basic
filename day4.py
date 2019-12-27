# 日期：2019-08-03
# 内容：循环控制 语句
# chapter 5
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print("\nall of the cars were output.")

# 用 if 检查是否相等 运算符：== 
# 此处说明 Python 区分大小写
car = 'Audi'
if(car.lower() == 'audi'):
    print("\ntrue")
else:
    print("\nfalse")

# 用 != 检查是否不相等
age = 23
if(age == 24):
    print("\nyou are 24 yrs old.")
else:
    print("\nyou are not 24 yrs old.")

# 检查数字是否相等
print(age == 18)

# 大于小于号
print(age < 21)
print(age > 20)

# 代码如诗
flag = True
limitTime = 100000
flagCount = 0
# while(flag):
#     flagCount += 1
#     print("I Love You.")
#     # 我希望是，一万年
#     if (flagCount == limitTime):
#         break

# 检查多个条件
age_0 = 22
age_1 = 18
print(age_0 > 18 and age_1 < 22)
print(age_0 == 22 or age_1 == 18)

# 用 in 判断某个元素是否被包含在列表中
if ('honda' in cars):
    print("\nYes, honda is in the list.")
else:
    print("\nNope, we didn't find honda in the list.")

# 用 not in 判断某个元素是否被包含在列表中
if ('benz' not in cars):
    print("\nYes, benz is not in the list.")
else:
    print("\nNope, benz is in the list.")

# case 5 - 1
car = 'subaru'
print("Is car == 'subaru' ? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi' ? I predict False.")
print(car == 'audi')

# case 5 - 2
# 检查两个字符串相等和不等。
strA = "I am a man."
strB = "I am a woman."
print(strA == strB)
print("\n.lower() method test: if 'I am a man.' == 'i am a man.'")
print(strA.lower() == strA)

# 检查两个数字是否相等
numA = 28
numB = 25
print(numA > numB)
print(numA < numB)
print(numA == numB)
print(numA >= numB)
print(numA <= numB)



