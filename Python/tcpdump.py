#!/usr/bin/env python

import subprocess

def tcpdump(vif):
	p = subprocess.Popen(('sudo', 'tcpdump -i ' + vif,'-l'), stdout=subprocess.PIPE)
	try:
		for row in p.stdout:
			print row.rstrip()
	except KeyboardInterrupt:
		p.terminate()