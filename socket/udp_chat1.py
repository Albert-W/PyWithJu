import threading
import socket



def rece(sk):
    while 1:
        data, addr = sk.recvfrom(1024)
        if data == b'exit':
            break
        print(data.decode())

def send(sk):
    while 1:
        msg_input = input("please input message:")
        if msg_input == "exit":
            break
        #绑定了对方的ip和端口
        sk.sendto(msg_input.encode(), ('',9081))


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定本机ip和端口号
    udp_socket.bind(('', 9080))
    t1 = threading.Thread(target=rece, args=(udp_socket,))
    t2 = threading.Thread(target=send, args=(udp_socket,))
    t1.start()
    t2.start()
 
 
if __name__ == '__main__':
    main()