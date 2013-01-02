#!/usr/bin/env python

import os
import socket
import sys
#import random
import time

if len(sys.argv) != 5:
        print "FTP PASV Generator"
	print "Usage: ftp-pasv.py <server address> <port> <number of iterations> <seconds between requests>"
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
        # Send the FTP PASV Commands
        s.send('USER anonymous\r\n')
	s.send('PASS anonymous@microsoft.com\r\n')
	s.send('SYST\r\n')
	s.send('FEAT\r\n')
	s.send('PWD\r\n')
	s.send('PASV\r\n')
	s.send('227 Entering Passive Mode (10,10,1,10,22,80\r\n')
        print "Generating FTP PASV Commands to " + server + " Port", port
	time.sleep(wait)
s.close
sys.exit(1)
