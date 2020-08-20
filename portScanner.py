import socket
import argparse
import threading

class PortScanner:
    def __init__(self, targetIp:str, portBegin:int, portEnd:int):
        self.targerIp = targetIp
        self.portBegin, self.portEnd = portBegin, portEnd

    def scan(self, ip:str, port:int):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            print(f'port {port} is open.')
        except: pass
    
    def scanThread(self):
        for _ in range(self.portBegin, self.portEnd):
            t = threading.Thread(target=self.scan, args=(self.targerIp, _))
            
            t.daemon = True
            t.start()
            t.join()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-ip', dest='ip', type=str, required=True, help='target ip address')
    
    parser.add_argument('-from', dest='_from', type=int, required=False, help='starting port')
    parser.add_argument('-to', dest='_to', type=int, required=False, help='ending port')
    
    args = parser.parse_args()

    if args._from is None:
        args._from = 1
    if args._to is None:
        args._to = 65535 
    
    scanner = PortScanner(args.ip, args._from, args._to)
    scanner.scanThread()