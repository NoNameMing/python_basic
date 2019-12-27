import socket

sk = socket.socket()

ip_port = ('127.0.0.1', 9999)

sk.bind(ip_port)

sk.listen(5)

while True:
    # 等待客户端连接
    conn, address = sk.accept()
    # 一直使用当前连接进行数据发送
    # 直到结束标志的出现
    # 打开文件等待数据写入
    while True:
        with open("file", "ab") as f:
            # 接收数据
            data = conn.recv(1024)
            if data == b'quit':
                break
            # 写入文件
            f.write(data)
        # 接收完成标志
        conn.send('success'.encode())
    # 打印提示信息
    print('文件接收完成！')
# 关闭连接
sk.close()

