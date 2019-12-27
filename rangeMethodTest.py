# 列表生成方式 1
numbers = []
numbers = list(range(1, 19, 2))
print("\n方式1：" + str(numbers))

# 列表生成方式 2
listName = []

for val in range(1, 23, 2):
	listName.append(val)

print("\n方式2：" + str(listName))

# 列表生成方式 3
oddNumber = [val for val in range(1, 25, 2)]
print("\n方式3: " + str(oddNumber))