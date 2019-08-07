import threading
import socket
import sys 
import json 
import util.p2pfile as pf
import util.p2pUdp as pu 

class Node:
    seed = ("127.0.0.1",8891)
    peers = {}
    myid = ""
    udp_socket = {}

    def rece(self):
        while 1:
            data, addr = pu.recembase(self.udp_socket)
            action = json.loads(data)
            # print(action["type"],addr)
            self.dispatch(action, addr)
    def dispatch(self, action,addr):
        if action['type'] == 'newpeer':
            print("A new peer is coming")
            self.peers[action['data']]= addr
            # print(addr)
            pu.sendJS(self.udp_socket, addr,{
            "type":'peers',
            "data":self.peers
            })         

        if action['type'] == 'peers':
            print("Received a bunch of peers")
            self.peers.update(action['data'])
            # introduce youself. 
            pu.broadcastJS(self.udp_socket, {
                "type":"introduce",
                "data": self.myid
            },self.peers) 

        if action['type'] == 'introduce':
            print("Get a new friend.")
            self.peers[action['data']]= addr   

        if action['type'] == 'input':
            print(action['data'])  

    def startpeer(self):
        pu.sendJS(self.udp_socket,self.seed,{
            "type":"newpeer",
            "data":self.myid
        })

    def send(self):
        while 1: 
            msg_input = input("$:")
            if msg_input == "exit":
                break    
            if msg_input == "friends":
                print(self.peers) 
                continue      
            l = msg_input.split()
            if l[-1] in self.peers.keys():
                toA = self.peers[l[-1]]
                s = ' '.join(l[:-1]) 
                if msg_input.startswith('#f'):
                    pf.sendfbase(l[1], toA)
                else:
                    pu.sendJS(self.udp_socket, toA,{
                        "type":"input",
                        "data":s
                    })      
            else :
                pu.broadcastJS(self.udp_socket, {
                    "type":"input",
                    "data":msg_input
                },self.peers)
                continue 
def main():
    port = int(sys.argv[1]) #从命令行获取端口号
    fromA = ("127.0.0.1",port)
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((fromA[0],fromA[1]))
    peer = Node()
    peer.myid = sys.argv[2]
    peer.udp_socket = udp_socket
    # print(fromA, peer.myid)
    peer.startpeer()
    t1 = threading.Thread(target=peer.rece, args=())
    t2 = threading.Thread(target=peer.send, args=())
    output = "output"
    t3 = threading.Thread(target=pf.recef,args=(output,fromA))
    t1.start()
    t2.start()
    t3.start()

if __name__ == '__main__':
    main()           

# usage:
# python main.py 8891 id1
# python main.py 8892 id2
# python main.py 8893 id3
