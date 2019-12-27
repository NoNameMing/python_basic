# 导入模块
import socket

# 实例初始化
client = socket.socket()

# 访问的服务器 IP 和 PORT
ip_port = ("127.0.0.1", 8889)

# 连接服务器
client.connect(ip_port)
# 此处的 byte 型数据特指 python 3.x 以上

# 定义一个循环，不断发送消息
while True:
    # 接收缓冲区的数据
    data = client.recv(1024)

    # 打印接收的数据
    print(data.decode())

    # 输入发送的消息
    msg_input = input("请输入发送的消息： ")

    # 消息发送
    client.send(msg_input.encode())

    if msg_input == 'exit':
        break

    data = client.recv(1024)
    print(data.decode())