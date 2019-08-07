import threading
import socket
import sys 
import json 

seed = ("127.0.0.1",8881)

# { 
#   id1 = ["127.0.0.1",8888],
#   id2 = addr2,
# } 
# peers = {'seed':seed}
# tuple is unable to transport through json.
peers = {}

# ("127.0.0.1",8889)
peer = () 

myid = ""

# parse the received data, take action base on their type. 
def rece(sk):
    while 1:
        data, addr = sk.recvfrom(1024)
        action = json.loads(data) 
        # action = {
        #     type:'newpeer',
        #     data:'id'
        # }
        
        dispatch(sk,action, addr)

        
def dispatch(sk,action, addr):
    
    # when seed peer receives message from now peer. 
    # action = {
    #     type:'newpeer',
    #     data:'id'
    # }
    # 1, add new peer to seed's dict.
    # 2, send dict to new peer.
    # To do: new peer send 'hello' to every peers in dict.
    if action['type'] == 'newpeer':
        peers[action['data']]= addr
        sendms(sk,{
            "type":'peers',
            "data":peers
        },addr)
    # when receive dict peers.     
    if action['type'] == 'peers':
        global myid
        peers.update(action['data'])
        # introduce youself. 
        broadcast(sk,{
            "type":"introduce",
            "data": myid
        })   

    if action['type'] == 'introduce':
        peers[action['data']]= addr   

    if action['type'] == 'input':
        print(action['data'])    

def sendms(sk,message,addr):
    # print("sending:{} to {}".format(message,addr))
    sk.sendto(json.dumps(message).encode(),(addr[0],addr[1]))

def broadcast(sk, message):
    print("broadcasting:{}".format(message))
    for p in peers.values():
        sendms(sk,message,(p[0],p[1]))   


def startpeer(sk,id):
    sendms(sk,{
        "type":"newpeer",
        "data":id
    },seed)

def send(sk):
    while 1:
        msg_input = input("please input message:")
        if msg_input == "exit":
            break    
        if msg_input == "friends":
            print(peers) 
            continue    
        # chat with single peer. 
        # "good morning id2"
        l = msg_input.split() #输入字符串分隔，判断最后一个是否是id
        if l[-1] in peers.keys():
            host = peers[l[-1]][0]
            port = peers[l[-1]][1]
            s = ' '.join(l[:-1]) 

            sendms(sk,{
                "type":"input",
                "data":s
            }, peers[l[-1]])
        # "#f 1.txt id2"
        


        # broadcast with every peer.    
        else :
            broadcast(sk,{
                "type":"input",
                "data":msg_input
            })
            continue

# useage:
# python p2pNet.py 8881 id1
# python p2pNet.py 8882 id2
# python p2pNet.py 8883 id3
# friends # return peers
# hello # send hello to all peers. 
# good morning id2 # send good morning to id2


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定本机ip和端口号
    port = int(sys.argv[1]) #从命令行获取端口号
    global myid
    myid = sys.argv[2]
    udp_socket.bind(('', port))

    startpeer(udp_socket, myid)
    t1 = threading.Thread(target=rece, args=(udp_socket,))
    t2 = threading.Thread(target=send, args=(udp_socket,))
    t1.start()
    t2.start()
 
 
if __name__ == '__main__':
    main()