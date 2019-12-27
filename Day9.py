# Day 9 Python 函数

# 3 个关于返回的实例
# 实例 1
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# 实例 2
def get_formatted_name2(first_name, middle_name, last_name):
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name2('howard', 'tony', 'stark')
print(musician)

# 实例 3
def get_formatted_name3(first_name, last_name, middle_name=' '):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

car_driver = get_formatted_name3(first_name='sebastian', last_name='vettel')
print(car_driver)

# 返回字典
def build_person(first_name, last_name):
    """返回一个字典，其中包含一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('lewis', 'hanmilton')
print(musician)

# 返回字典函数扩展
def build_person2(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

car_driver =  build_person2('max', 'verstappen', age=20)
print(car_driver)

def get_formatted_name4(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

Flag = True
while Flag:
    print("\nTell me your name: ")
    print("Enter 'q' at any  time to quit.")

    f_name = input("First name: ")

    if f_name == 'q':
        print("\nGood Bye!")
        break

    l_name = input("Last name: ")

    if l_name == 'q':
        print("\nGood Bye!")
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

    Flag = input("\nWish to continue? yes/no")
    if Flag == 'yes':
        Flag = True
    else:
        print("\nGood Bye!")
        Flag = False

# case 8 - 7
def make_album(singer_name, album_name, song_num=''):
    # singer_name = input("\nHello, let's start from the singer's name, please input: ").title()
    # album_name = input("Please enter album's name: ").title()
    album_info = {'singer_name': singer_name, 'album_name': album_name}
    if song_num:
        album_info['song_num'] = song_num 
    return album_info

album_info = make_album('ming', 'pain & grows', '3')
print("\n" + str(album_info))

# case 8 - 8
Flag = 'True'
while Flag:
    print("CAUTION: IF YOU WANT TO EXIT AT ANY TIME, JUST ENTER 'q'. ")
    singer_name = input("\nHello, let's start from the singer's name, please input: ").title()
    album_name = input("Please enter album's name: ").title()

    print(make_album(singer_name, album_name))

    Flag = input("\nWish to continue? yes/no ")
    if Flag == 'yes':
        Flag = True
    else:
        print("\nGood Bye!")
        Flag = False
    
