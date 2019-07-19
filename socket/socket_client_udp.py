import socket
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_port = ("127.0.0.1", 8888)
while True:
    msg_input = input("please input message:")
    if msg_input == "exit":
        break
    sk.sendto(msg_input.encode(),ip_port)
    data, addr = sk.recvfrom(1024)
    print(data.decode())

sk.close()