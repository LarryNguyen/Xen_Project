'''
Created on Jan 20, 2014

@author: dai-network-lab
'''

import pprint
import dpkt, pcap, inspect
import sys
import scapy
from scapy.sendrecv import sniff


class TcpMonitor(object):
    '''
    Tcp Monitoring class
    '''

    def __init__(self, inf, _filter=""):
        '''
        Constructor, need to have an network interface
        '''
        self.inf = inf
        self.filter = _filter
        self.pc = pcap.pcap(name=self.inf)
        if self.filter != "":
            self.pc.setfilter(self.filter)


    def capture(self):
       for ts, pkt in self.pc:
            eth = dpkt.ethernet.Ethernet(pkt)
            print `eth`
            ip = eth.data
            tcp = ip.data


    def capture2(self):
        a=sniff(filter="port 80", count=2)
        a.nsummary()


if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(len(sys.argv))
    if len(sys.argv) != 3:
        print "Usage:"
        print sys.argv[0], " <interface name> <filter>"
        sys.exit(1)


#     pp.pprint(inspect.getmembers(pcap))
    monitor = TcpMonitor(sys.argv[1], sys.argv[2])
    monitor.capture()
    monitor.capture2()


