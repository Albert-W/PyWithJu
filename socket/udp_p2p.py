import threading
import socket
import sys 

seed = ("127.0.0.1",8888)
peers = {}
peer = () 

def rece(sk):
    while 1:
        # 如果是第一次收到的地址，添加到字典
        # id : addr
        data, addr = sk.recvfrom(1024)
        if addr not in peers.values():
            strs = data.decode().split()
            peers[strs[0]]= addr 
        #print(addr)
        global peer
        peer = addr # 同名之后使用局部变量
        if data == b'exit':
            break
        print(data.decode())
        
        

def send(sk):
    while 1:
        msg_input = input("please input message:")
        if msg_input == "exit":
            break    
        l = msg_input.split() #输入字符串分隔，判断最后一个是否是id
        if l[-1] in peers.keys():
            s = ' '.join(l[:-1])   
            sk.sendto(s.encode(), peers[l[-1]])
        else :
            for p in peers.values():
                sk.sendto(msg_input.encode(),p)
# useage:
# run udp_p2p.py id1 8888 as seed
# run udp_p2p.py id2 8889 as p1
# run udp_p2p.py id3 8890 as p2
# seed: massage id2
# p1: massage id1


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定本机ip和端口号
    port = int(sys.argv[1]) #从命令行获取端口号
    udp_socket.bind(('', port))
    udp_socket.sendto(sys.argv[2].encode(), seed)
    t1 = threading.Thread(target=rece, args=(udp_socket,))
    t2 = threading.Thread(target=send, args=(udp_socket,))
    t1.start()
    t2.start()
 
 
if __name__ == '__main__':
    main()