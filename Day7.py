# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program."

# # Day7 用户输入 和 while 循环
# message = input("Tell me something, and I will repeat it to you: ")
# print(message)

# name = input("\nPlease input your name: ")
# print("Hello, " + name + "!")

# # 为了清晰，把字符串写入两行
# prompt = "\nIf you tell me who you are, we can personalize the messages you see."
# prompt += "\nWhat is your  first name? "

# name = input(prompt)
# print("Helllo, " + name + "!")

# # 数值务必转换为 int 才行
# age = input("\nHow old are you? ")
# age = int(age)
# print(age >= 18)

# height = input("\nHow tall are you, in inches?")
# height = int(height)

# if height >= 36:
#     print("You are good.")
# else:
#     print("You need to be taller!")

# # 求模运算符
# number = input("\nEnter a number, and I'll tell you if it's even or odd: ")
# number = int(number)

# if number % 2 == 0:
#     print("The number " + str(number) + " is even.")
# else:
#     print("The number " + str(number) + " is odd.")

# # case 7 - 1
# message = "\nWhat kind of car do you want to rent? "
# message += "Let me see if I can find you a Subaru "
# car = input(message)
# print("So, I will find you a " + car)

# # case 7 - 2
# num = input("\nMay I ask you the number of you guys? ")
# num = int(num)
# if num > 8:
#     print("Sorry, No adaptable desk.")
# else:
#     print("Okay, I will arrange immediately.")

# # case 7 - 3
# number = input("\ntell me the number, I will tell you if it is the times of 10.")
# number = int(number)
# if number % 10 == 0:
#     print("the number % 10 == 0")
# else:
#     print("the number % 10 == " + str(number % 10))

# print("")
# current_number = 1
# while current_number < 5:
#     print(str(current_number) + "is the current number.")
#     current_number += 1

# # while 通过 判定输入 来结束循环
# message = ""
# while message != "quit":
#     message = input(prompt)
#     if message != "quit":
#         print(message)

# # while 使用 标志 结束循环
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# # while 使用 break 结束循环
# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else:
#         print("You want to go to " + city.title() + "!")

# while 中使用 continue
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue

#     print(current_number)

# # case 7 - 4
# message = ""
# incredients = []
# while message != "quit":
#     message = input("please input your incredients, input 'quit' to end.")
#     if message != "quit":
#         incredients.append(message)
#     else:
#         print("all the incredients you have chosen are: " + str(incredients))
#         continue

# # case 7 - 5
# message = ""
# price = 0
# while message != "sold out":
#     age = input("May I know your age? ")
#     age = int(age)
#     if age < 3:
#         print("You are free to get in, sweet heart.")
#     elif age < 12:
#         price = 10
#         print("You need to pay $" + str(price) + ", kido.")
#     else:
#         price = 15
#         print("You need to pay $" + str(price) + " for the ticket.")
    
# # 7 - 6
# active = ""
# price = 0
# while active != "quit":
#     age = input("May I know your age? ")
#     age = int(age)
#     if active != "quit":
#         if age < 3:
#             print("You are free to get in, sweet heart.")
#         elif age < 12:
#             price = 10
#             print("You need to pay $" + str(price) + ", kido.")
#         else:
#             price = 15
#             print("You need to pay $" + str(price) + " for the ticket.")
#     else:
#         break
#     active = input("Do you want to quit? Input 'quit' to quit, input any key to continue.")

# case 7 - 7 没意思

# 7.3 使用 while 循环来处理列表和字典
# 首先，创建一个待验证的用户列表
# 和一个用于存储已验证用户的用户的空列表
# unconfirmed_users = ['lance', 'brain', 'vans']
# confirmed_users = []

# # 验证每个用户，直到没有未验证用户为止
# # 将每个验证过的列表都移动到已验证用户列表中
# while unconfirmed_users:
#     # pop 方法验证
#     current_user = unconfirmed_users.pop()

#     print("Veryfying user: " + current_user.title())
#     confirmed_users.append(current_user)

#     # 显示所有已验证的用户，直到没有未验证用户为止

# print("\nThe following users have been confirmed: ")
# for user in confirmed_users:
#     print(user.title())

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)

#  使用用户输入来填充字典
# responses = {}

# # 设置一个标志，指出调查是否继续
# polling_activce = True

# while polling_activce:
#     # 提示输入被调查者的名字和回答
#     name = input("\nWhat is your name? ")
#     response = input("\nWhich mountain would you like to climb someday? ")
    
#     # 将答卷存储在字典中
#     responses[name] = response

#     # 看看是否还有人要参与调查
#     repeat = input("Would you like to another person to respond? (yes/no) ")
#     if repeat == 'no':
#         polling_activce = False

# # 调查结束，显示结果
# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(name + ", would you like to climb " + response + ".")

# case 7 - 8
sandwich_orders = ['bacon', 'bagel toast', 'baked bean']
finished_sandwiches = []
# for sandwich in sandwich_orders:
#     print("making " + sandwich.title() + " for special you!")
#     finished_sandwiches.append(sandwich)

# print("\nAll the finishes sandwiches: ")
# for sandwich in finished_sandwiches:
#     print(sandwich.title())

# # case 7 - 9

# # 先得有熏肉才能删除
# times = 0
# while times < 3:
#     sandwich_orders.append("pastrami")
#     times += 1

# # 删除熏肉
# while "pastrami" in sandwich_orders:
#     sandwich_orders.remove("pastrami")

# print("pastrami is sold out!")
# print("food left: " + str(sandwich_orders))

# case 7 - 10

# 建立字典
responses = {}

# 设定标记
polling_activce = True

# 循环处理
while polling_activce:
    name = input("\nWhat is your name?")
    response = input("\nWhat's your ideal place to take a vacation?")
    
    # 存储结果
    responses[name] = response

    # 判定是否要继续
    key = input("\nIf you wish to continue?(yes/no)")

    if key == 'no':
        polling_activce = False
    else:
        continue

for name, result in responses.items():
    print(name.title() + " wants to go to " + result.title() + " to take a vacation.")

