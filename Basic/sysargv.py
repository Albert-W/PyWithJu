# import this 
import sys 
import argparse 
def args():
    print("the system argv is:")
    print(sys.argv) 
    print(len(sys.argv))
    for arg in sys.argv:
        print(arg)

def parseargs():
    parser = argparse.ArgumentParser(description='type in the ip and host.')
    parser.add_argument('-i','--ip', metavar='', dest='myip', help="type you ip address",
                            )
    parser.add_argument('-p','--port' , default=10001,
                            )
    args = parser.parse_args()
    print(args)
    print(args.ip)
    print(args.port)


        

if __name__ == '__main__':
    parseargs()
