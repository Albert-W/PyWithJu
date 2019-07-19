import socket
sk = socket.socket()
ip_port = ("127.0.0.1",9999)
sk.connect(ip_port)
# open file
with open("socket_server.py",'rb') as f:
    # split file to lines
    for i in f:
        # upload file
        sk.send(i)
        # 等待接收完成
        data = sk.recv(1024)
        if data != b'success':
            break
# give finish signal
sk.send('finished'.encode())