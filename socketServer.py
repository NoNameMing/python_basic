# 导入模块
import socket

# 创建实例
sk = socket.socket()

# 定义绑定的 IP 和 PORT
ip_port = ("127.0.0.1", 8888)

# 绑定和监听
sk.bind(ip_port)

# 最大连接数
sk.listen(5)

# 提示信息
print("正在进行等待接收数据")

# 接收数据
conn, address = sk.accept()

# 定义信息
msg = "Hello, Client"

# python3 以上，网络数据的接收发送都是 byte 类型
# 如果发送数据是 str 型的需要进行编码

# 返回信息
conn.send(msg.encode())

# 创建实例

# 主动关闭连接
conn.close()



