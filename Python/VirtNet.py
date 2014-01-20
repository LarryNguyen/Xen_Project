#!/usr/bin/env python


import sys, time

import XenAPI
import subprocess as sub

def get_eths(session, username):

    # Find a non-template VM object
    vms = session.xenapi.VM.get_all()
    print "Server has %d VM objects (this includes templates):" % (len(vms))
    eths = []
    for vm in vms:
        record = session.xenapi.VM.get_record(vm)
        if not(record["is_a_template"]) and not(record["is_control_domain"]):
            name = record["name_label"]
            if username in name:
                print "Found VM uuid", record["uuid"], "called: ", name

                record = session.xenapi.VM.get_record(vm)            
                # Make sure the VM has powered down
                print "  VM '%s' is in power state '%s'" % (name, record["power_state"])
                
                #Checking network
                domid = session.xenapi.VM.get_domid(vm)
                vifs = session.xenapi.VM.get_VIFs(vm)
                for vif in vifs:
                    device = session.xenapi.VIF.get_device(vif)
                    eth = "eth%s.%s" % (domid, device)
                    eths.append(eth)

    return eths


# Need to run in root mode
def tcpdump(vif):
    command = 'sudo tcpdump -i %s -l' % (vif)
    print command
    p = sub.Popen(('sudo', 'tcpdump', '-i', vif, '-l'), stdout=sub.PIPE)

    output = []
    start = time.time()
    
    while time.time() < start + 5:
        s = p.stdout.readline()
        #do domething with s
        output.append(s)

    return output

