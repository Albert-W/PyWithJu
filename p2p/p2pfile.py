import socket
import sys 
import threading

# send file to destination.
# parameters(filename, ip, port)
def sendf(ip = '127.0.0.1'):
    while 1:
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        msg_input = input("please input filename:")
        # 1.txt 9002
        l = msg_input.split()
        filename = l[0]
        host = int(l[1])
        sk.connect((ip, host))
        with open(filename,'rb') as f:
            for i in f:
                sk.send(i)
                data = sk.recv(1024)    
                if data != b'success':
                    break
        sk.send('finished'.encode())
        print("send file finished")
        

# receive file from others. 
def recef(port, ip = '127.0.0.1'):
    while 1:
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.bind((ip,port))    
        sk.listen()
        conn, addr = sk.accept()
        with conn:
            with open('file','ab') as f:
                data = conn.recv(1024)
                if data == b'finished':
                    return 
                f.write(data)
                # 发送接收完成标志
                conn.send('success'.encode()) 
            print("receive file finished")          
 
def main():
    # creat socket
    # tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定本机ip和端口号
    port = int(sys.argv[1]) #从命令行获取端口号
    # tcp_socket.bind(('', port))

    t1 = threading.Thread(target=recef, args=(port,))
    t2 = threading.Thread(target=sendf, args=())
    t1.start()
    t2.start()

# usage:
# python p2pfile.py 9001
# python p2pfile.py 9002
# 1.txt 9002
# 1.txt 9001 
 
if __name__ == '__main__':
    main()