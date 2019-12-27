import socket

# ipv4 udp
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ip port 设置
ip_port = ("127.0.0.1", 8888)

# 绑定端口
sk.bind(ip_port)

while True:
    data = sk.recv(1024)
    print(data.decode())