# Day10 Python 传递列表

# 传递列表
def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
    
usernames = ['hannah', 'try', 'margot']
greet_users(usernames)

# 在函数中修改列表

# 首先创建一个列表，其中包含一些要打印的设计
unprinted_desings = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 模拟打印设计，直到没有未打印的设计为止
# 打印每个设计后，都将其移到列表 completed_models 中

while unprinted_desings:
    current_design = unprinted_desings.pop()

    # 模拟根据设计制作 3D 打印模型的过程
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# 显示打印好的所有模型：
print("\nThe following models have been printed: ")
for completed_models in completed_models:
    print(completed_models)

# 整理过的实例
def print_models(unprinted_desings, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表 completed_models 中
    """
    while unprinted_desings:
        current_design = unprinted_desings.pop()

        # 模拟根据设计制作 3D 打印模型的过程
        print("Printing model with a auto method: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的模型"""
    print("\nThe following models have been printed with the auto method: ")
    for completed_model in completed_models:
        print(completed_model)
    
unprinted_designs = ['macbook pro keyboard', 'ipad keyboard', 'wireless case']
completed_models = []

# 调用以上两个函数
# print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# 8.4.2 保留副本
print_models(unprinted_designs[:], completed_models)

print("\n保留副本的方式不会改变原有的列表，原有的 unprinted_designs 列表如下：")
print(unprinted_designs)

# case 8 - 9
print("")
def show_magicians(magicians_names):
    for magician_name in magicians_names:
        print("We have found the magician: " + magician_name)

magicians_names = ['David Copperfield', 'Derron Brown']
show_magicians(magicians_names)

# case 8 - 10
print("")

def make_great(magicians_names):
    for i in range(len(magicians_names)):
        current_name = "the Great " + magicians_names[i]
        magicians_names[i] = current_name

# make_great(magicians_names)
# show_magicians(magicians_names)

# case 8 - 11
print("")
new_names = []

def make_great_with_return(magicians_names, new_names):
    for i in range(len(magicians_names)):
        current_name = "the Great " + magicians_names[i]
        magicians_names[i] = current_name

        # 加入的新方法
        new_names.append(current_name)
    return new_names

make_great_with_return(magicians_names[:], new_names)

print("\nThe old list was: ")
show_magicians(magicians_names)

print("\nThe new list is: ")
show_magicians(new_names)

# 8.5 传递任意数量的实参

# 可以接受任意数量的实参
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

