import socket
# Instance initialization
client = socket.socket()
# visit the server's ip and port
ip_port = ("127.0.0.1",8888)
# connect the server
client.connect(ip_port)


while True:
    # receive the server's msg, get 1024 bytes in every turn.
    data = client.recv(1024)
    # print the data received, byte type file.
    print(data.decode())
    # input message
    msg_input = input("please input message:")

    client.send(msg_input.encode())
    if msg_input == "exit":
        break
    # data = client.recv(1024)
    # print(data.decode())
