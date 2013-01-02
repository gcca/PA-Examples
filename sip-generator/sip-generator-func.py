#!/usr/bin/env python

import os
import socket
import sys
import time

if len(sys.argv) != 5:
        print "SIP Request Generator - Function Test"
        print "Usage: sip-generator-func.py <server address> <port> <number of iterations> <seconds between requests>"
        sys.exit(0)

server = (sys.argv[1])
port = int(sys.argv[2])
iteration = int(sys.argv[3])
wait = int(sys.argv[4])
loop = iteration

def sip-generator

for i in range(iteration):
        # Create a Socket
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the Server
        connect=s.connect((sys.argv[1],port))
        # Send the SIP register request
        s.send('REGISTER sip:' + (sys.argv[1]) + ' sip/2.0' + '\r\n')
        print "Generating SIP Register commands to " + server + " Port", port
        time.sleep(wait)
s.close
sys.exit(1)
