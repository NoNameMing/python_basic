# hello world
message = "hello,line1"
print(message)

message = "world, line2"
print(message)

# 字符串大小写
print("\n字符串大小写区分效果如下：")
name = "no name ming"
print("title方法：" + name.title())
print("upper方法：" + name.upper())
print("lower方法：" + name.lower())

# 字符串拼接
print("\n字符串拼接方法如下：")
firstName = "No"
middleName = "Name"
lastName = "Ming"
fullName = firstName + middleName + lastName
print(fullName)
message = "Hello, " + fullName.title() + "!"

# 打印 制表位
print("\n打印制表位方法效果如下，使用：")
print("\tmessage")

# 打印 制表位 + 换行符
print("\n打印制表位和换行符的方法效果如下：")
print("NewFriends:\n\tMing\n\tWangLiying\n\tXuJinchang")

# 删除字符串末尾的所有空白、左、右空白
print("\n删除字符串末尾的所有空白：")
delBlank = ' 效果 '
print(delBlank.strip())

print("\n删除字符串末尾的左空白：")
delBlank = '效果'
print(delBlank.lstrip())

print("\n删除字符串末尾的右空白：")
delBlank = ' 效果 '
print(delBlank.rstrip())

print("\n**即使是在print中调用 strip() lstrip() rstrip() 方法，相应的字符串也会被改写")