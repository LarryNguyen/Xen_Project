'''
Created on Jan 20, 2014

@author: dai-network-lab
'''


import pprint
from scapy.sendrecv import sniff
import sys, time, sched


class TcpMonitor(object):
    '''
    Tcp Monitoring class
    '''

    def __init__(self, iface, filter="",timeout=5):
        '''
        Constructor, need to have an network interface
        '''
        self.iface = iface
        self.filter = filter
        self.packets = None
        self.s = None
        self.timeout = timeout

    def sniffPackets(self):
        self.packets = sniff(iface=self.iface, filter=self.filter, timeout=self.timeout)


    def intervalAction(self, packets):
        print len(packets), "packets with filter (", self.filter, ") get captured"
        '''
            do something here
        '''

        # recapture the packets again
        self.capture()


    def capture(self):
        self.s = sched.scheduler(time.time, self.sniffPackets())
        self.s.enter(5, 1, self.intervalAction(self.packets), ())
        self.s.run()

if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=2)
    if len(sys.argv) != 3:
        print "Usage:"
        print sys.argv[0], " <interface name> <filter>"
        sys.exit(1)

#     pp.pprint(inspect.getmembers(pcap))
    monitor = TcpMonitor(sys.argv[1], sys.argv[2])
    monitor.capture()


