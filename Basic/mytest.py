# import this 
import sys 
def fn():
    print(__name__)

if __name__ == '__main__':
    print(len(sys.argv))
    for arg in sys.argv:
        print(arg)
