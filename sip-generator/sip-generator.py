#!/usr/bin/env python

import os
import socket
import sys
import random
import time

if len(sys.argv) != 5:
        print "SIP Request Generator"
	print "Usage: sip-generator.py <server address> <port> <number of iterations> <time between requests>"
        sys.exit(0)

server = (sys.argv[1])
port = int(sys.argv[2])
iteration = int(sys.argv[3])
wait = int(sys.argv[4])
loop = iteration

for i in range(iteration):
        host = random.choice([x.strip() for x in open('hosts.cfg')])
        # Create a Socket
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the Server
        connect=s.connect((sys.argv[1],port))
        # Send the SIP register request
        s.send('REGISTER sip:' + host + ' sip/2.0' + '\r\n')
        result=s.recv(24)
        print host + ' - Response: ' + result
        s.close
	time.sleep(wait)
sys.exit(1)
