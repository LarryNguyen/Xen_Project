#!/usr/bin/env python
#echo server program

import sys, time

import XenAPI
import VirtNet
import Socket

if __name__ == "__main__":

    #url = "http://163.180.116.91"
    url = "http://163.180.117.227"
    username = "root"
    #password = "DaiZen123"
    password = "!icns@322"

    port = 50007
    sock = Socket.create_server(port)
    request = Socket.receive_data(sock)
    while len(request) > 0:

    # First acquire a valid session by logging in:    
#    session = XenAPI.Session(url)
#    session.xenapi.login_with_password(username, password)

#    eths = VirtNet.get_eths(session, "Window")

#    i = 0
#    while i < len(eths):
#        print eths[i]
#        VirtNet.tcpdump(eths[i])
#        i += 1

        data = VirtNet.tcpdump('en0')
        print data
        print '======================\n'
        if(len(data) > 0):
            Socket.send_data(sock,'IDLE')
    Socket.close(sock)

