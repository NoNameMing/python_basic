# 导入 socketserver 包
import socketserver

# 定义一个类
class MyServer(socketserver.BaseRequestHandler):
    # 首先执行 setup
    def setup(self):
        pass

    # 然后执行 handle
    def handle(self):
        conn = self.request
        msg = "Hello, outside."
        conn.send(msg.encode())
        while True:
            data = conn.recv(1024)
            print(data.decode())
            if data == 'exit':
                break
            conn.send(data)
        # pass

    # 最后执行 finish
    def finish(self):
        pass
    
if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(("127.0.0.1", 8889), MyServer)
    server.serve_forever()
