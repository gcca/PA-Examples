#!/usr/bin/env python

import os
import socket
import sys
#import random
import time

if len(sys.argv) != 5:
        print "SIP Request Generator - No Random Hosts"
	print "Usage: sip-generator-no-random-hosts.py <server address> <port> <number of iterations> <seconds between requests>"
        sys.exit(0)

server = (sys.argv[1])
port = int(sys.argv[2])
iteration = int(sys.argv[3])
wait = int(sys.argv[4])
loop = iteration

for i in range(iteration):
        # Create a Socket
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the Server
        connect=s.connect((sys.argv[1],port))
        # Send the SIP register request
        s.send('REGISTER sip:' + (sys.argv[1]) + ' sip/2.0' + '\r\n')
#        print server + ' - Port ' + port + ' - Iterations ' + iteration + ' - Wait Time: ' + wait + ' seconds' 
        s.close
	time.sleep(wait)
sys.exit(1)
