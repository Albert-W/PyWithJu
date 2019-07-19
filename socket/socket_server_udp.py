import socket
# Instance initialization, IPV4, UDP
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server's ip and port
ip_port = ("127.0.0.1", 8888)
sk.bind(ip_port)
while True:
    # data = sk.recv(1024)
    # print(data.decode)
    data, addr = sk.recvfrom(1024)
    print(data.decode())
    msg_input = input("please input message:")
    if msg_input == "exit":
        break
    sk.sendto(msg_input.encode(),addr)