#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
                   _ooOoo_
                  o8888888o
                  88" . "88
                  (| -_- |)
                  O\  =  /O
               ____/`---'\____
             .'  \\|     |//  `.
            /  \\|||  :  |||//  \
           /  _||||| -:- |||||-  \
           |   | \\\  -  /// |   |
           | \_|  ''\---/''  |   |
           \  .-\__  `-`  ___/-. /
         ___`. .'  /--.--\  `. . __
      ."" '<  `.___\_<|>_/___.'  >'"".
     | | :  `- \`.;`\ _ /`;.`/ - ` : | |
     \  \ `-.   \_ __\ /__ _/   .-` /  /
======`-.____`-.___\_____/___.-`____.-'======
                   `=---=' 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
         佛祖保佑       永无BUG 



@Date: 2020/2/9
@Name: server.py
@Author: wenyu xu
@Mail: wenyu__xu@163.com

@Description:

'''


import sys
import logging
import threading
from socketserver import ThreadingTCPServer, TCPServer, BaseRequestHandler


class EchoHandler(BaseRequestHandler):
    def setup(self):
        super().setup()
        self.event = threading.Event()      # 初始化工作

    def finish(self):
        super().finish()
        self.event.set() # 清理工作

    def handle(self):
        super().handle()

        try:
            while not self.event.is_set():
                data = self.request.recv(1024).decode()
                print(data)
                msg = '{}{}'.format(self.client_address, data).encode()
                print(msg)
                self.request.send(msg)
        except Exception as e:
            print(e)

        finally:
            print('=== end ====')


class ChatServerHanlder(BaseRequestHandler):
    clients = {}

    def setup(self):
        super().setup()
        self.event = threading.Event()
        self.clients[self.request] = self.client_address

    def finish(self):
        super().finish()
        self.clients.pop(self.request)
        self.event.set()
        print(self.clients)

    def handle(self):
        super().handle()
        while not self.event.is_set():
            data = self.request.recv(1024)
            print(data)
            if data.strip() == b'quit' or data == b'':
                break

            print(data.decode())
            msg = ' your msg is {} '.format(data.decode()).encode()
            print(msg)
            for s in self.clients:
                s.send(msg)


def EchoServer():
    server = ThreadingTCPServer(('127.0.0.1', 9999), EchoHandler)

    server_thread = threading.Thread(target=server.serve_forever, name='EchoServer', daemon=True)
    server_thread.start()

    try:
        while True:
            cmd = input('>>')
            if cmd.strip() == 'quit':
                server.shutdown()
                break
            print(threading.enumerate())
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        pass
    finally:
        print('exit')
        sys.exit(0)

    pass


def ChatServer():
    FOMAT = '%(asctime)s %(thread)s %(threadName)s %(message)s'
    logging.basicConfig(level=logging.INFO, format=FOMAT)

    laddr = ('127.0.0.1', 9988)
    server = ThreadingTCPServer(laddr, ChatServerHanlder)
    print(server.socket)
    threading.Thread(target=server.serve_forever, name='server').start()

    try:
        while True:
            cmd = input(">>>>")
            if cmd == 'quit':
                server.shutdown()
                break
            print(threading.enumerate())
    except Exception as e:
        print(e)

    except KeyboardInterrupt:
        pass
    finally:
        print('exit')
        sys.exit(0)


if __name__ == "__main__":
    # EchoServer()
    ChatServer()

'''
import threading
from socketserver import ThreadingTCPServer, BaseRequestHandler
import sys
import logging

FOMAT = '%(asctime)s %(thread)s %(threadName)s %(message)s'
logging.basicConfig(level=logging.INFO, format=FOMAT)




laddr = ('127.0.0.1', 9999)
server = ThreadingTCPServer(laddr, ChatServerHanlder)
print(server.socket)
threading.Thread(target=server.serve_forever, name='server').start()

try:
    while True:
        cmd = input(">>>>")
        if cmd == 'quit':
            server.shutdown()
            break
        print(threading.enumerate())
except Exception as e:
    print(e)

except KeyboardInterrupt:
    pass
finally:
    print('exit')
    sys.exit(0)
'''

'''
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        #conn.sendall('我是多线程')

        Flag = True
        while Flag:
            data = conn.recv(1024)
            print(str(data, 'utf-8'))
            if data == 'exit':
                Flag = False
            #else:
            #    conn.sendall('请重新输入.')

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), MyServer)     # 生成一个多线程的server
    server.serve_forever()
    pass
'''

'''
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data = self.request.recv(1024)
            if not self.data:
                print("%s客户端连接已断开"%self.client_address)
                break
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(("localhost",6969),MyServer)  # 开启一个线程
    server.serve_forever()
'''






