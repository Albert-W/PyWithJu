# multi threat server
import socketserver

# define a class
class MyServer(socketserver.BaseRequestHandler):
    # 如果handle方法出现报错，则会进行跳过。
    # setup finish无论如何一定会执行。
    def setup(self):
        pass

    def handle(self):
        # 定义连接变量
        conn = self.request
        msg = "hello world."
        conn.send(msg.encode())
        while True:
            data = conn.recv(1024)
            print(data.decode())
            if data == b'exit':
                break
            conn.send(data)

        conn.close()
    def finish(self):
        pass    

if __name__ =="__main__":
    # 创建多线程实例
    ip_port = ("127.0.0.1",8888)
    server = socketserver.ThreadingTCPServer(ip_port,MyServer)
    # 开启异步多线程，等待连接
    server.serve_forever()
