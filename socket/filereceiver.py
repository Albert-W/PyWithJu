import socket
sk = socket.socket()
ip_port = ("127.0.0.1",9999)
sk.bind(ip_port)
sk.listen(5)
while True:
    # wait for connection from client
    conn, address = sk.accept()
    # 一直使用当前链接
    while True:
        # open file and append binary data.
        with open("file",'ab') as f:
            data = conn.recv(1024)
            if data == b'finished':
                break
            f.write(data)
            # 发送接收完成标志
            conn.send('success'.encode())    
    print("file upload is finished")        
sk.close()

