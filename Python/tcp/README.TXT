INSTALL SCAPY 2.X IN XENSERVER DOM0

1- FIRST ENABLE CENTOS REPO http://cristiansan.wordpress.com/2012/05/23/xenserver-trick-linux-repository/
2- UPDATE PYTHON TO 2.6 https://wiki.openstack.org/wiki/XenServer/PostInstall#Install_Python_2.6_in_Dom0
3- INSTALL SCAPY http://www.secdev.org/projects/scapy/doc/installation.html#fedora
4- SNIFF BY THESE COMMANDS
$ scapy
$ sniff(iface="eth0", prn=lambda x: x.show())
