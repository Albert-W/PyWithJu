import socket
import sys 
import threading

# send file to destination.
# parameters(filename, ip, port)
# def sendf(output, ip, port):

# the basic function of send file.
def sendfbase(filename, toA):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          
    sk.connect((toA[0], toA[1]))
    with open(filename,'rb') as f:
        for i in f:
            sk.send(i)
            data = sk.recv(1024)    
            if data != b'success':
                break
    sk.send('finished'.encode())
    print("send file finished")
    
# send file to a peer in customized manner. 
def sendf(ip):
    while 1:        
        msg_input = input("please input filename:")
        # 1.txt 9002
        l = msg_input.split()
        filename = l[0]
        port = int(l[1])
        sendfbase(filename,ip,port)
        

# receive file from others. 
# parameters(filename, ip, port)
def recef(filename, fromA):
    while 1:
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.bind((fromA[0], fromA[1]))    
        # the maximum number of connections. 
        sk.listen(5)
        conn, addr = sk.accept()  
        # send data using this connection util finished.   
        with conn:
            while True:
            # byte, append to file. 
                with open(filename,'ab') as f:
                    data = conn.recv(1024)
                    if data == b'finished':
                        break 
                    f.write(data)
                    # 发送接收完成标志
                    conn.send('success'.encode()) 
            print("receive file finished")           
 
def main():

    ip = '127.0.0.1'
    myPort = int(sys.argv[1]) #从命令行获取端口号
    output = "output" # the name of output file. 
    t1 = threading.Thread(target=recef, args=(output,ip,myPort))
    t1.start()

    t2 = threading.Thread(target=sendf, args=(ip,))
    t2.start()

# usage:
# python p2pfile.py 9001
# python p2pfile.py 9002
# 1.txt 9002
# 1.txt 9001 
 
if __name__ == '__main__':
    main()