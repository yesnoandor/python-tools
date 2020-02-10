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
@Name: client.py
@Author: wenyu xu
@Mail: wenyu__xu@163.com

@Description:

'''

import socket


if __name__ == '__main__':
    '''
    ip_port = ('127.0.0.1', 9999)
    sk = socket.socket()
    sk.connect(ip_port)

    #while True:
        #data = sk.recv(1024)
        #print('receive:', data)
    inp = input('please input:')
    sk.sendall(inp)
        ##data = sk.recv(1024)
        ##print('receive:', data)

    #    if inp == 'exit':
    #        break

    sk.close()
    '''

    client = socket.socket()  # 默认是AF_INET、SOCK_STREAM
    client.connect(("localhost", 9999))
    while True:
        s = input(">>")
        print(s)
        print(s.encode("utf-8"))
        client.send(s.encode("utf-8"))
        data = client.recv(1024)
        print(data)
        print(data.decode("utf-8"))
    client.close()
    pass

