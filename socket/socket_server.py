import socket
import random
# 创建实例
sk = socket.socket()
ip_port = ("127.0.0.1",8888)
# 绑定监听
sk.bind(ip_port)
# 最大连接数,最多5个请求等待
sk.listen(5)
# continually waitting; 
while True:
    print("The server is waitting ...")
    # conn是链接对象
    conn, address = sk.accept()

    # 定义信息
    msg = "hello,  A connect is established."
    # 返回信息
    # python3.x以上，网络数据发送接受都是byte类型。
    # 如果发送的数据是str型，则需要进行编码。
    conn.send(msg.encode())
    # 不断接收客户观发来的消息
    while True:
        # receive data from client
        data = conn.recv(1024)
        print(data.decode())
        # receive the command of exit
        if data == b'exit':
            break
        # handle the data
        msg_input = input("please input message:")

        conn.send(msg_input.encode())
        # conn.send(data)  
        # conn.send(str(random.randint(1,1000)).encode())  
        if msg_input == "exit":
            break
    # 主动关闭连接
    conn.close()