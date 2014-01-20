#!/usr/bin/env python

import Socket


if __name__ == "__main__":

    server = 'localhost'
    port = 50007
    sock = Socket.create_client(server,port)

    data = "Windows"
    Socket.send_data(sock,data)
    while True: 
        result = Socket.receive_data(sock)
        print result
    
    Socket.close(sock)
