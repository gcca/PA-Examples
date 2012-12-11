#!/usr/bin/python
import socket
import sys
import random

if len(sys.argv) != 4:
	print "Usage: http-client.py <server address> <port> <number of iterations>"
	sys.exit(0)

port = int(sys.argv[2])
iteration = int(sys.argv[3])
loop = iteration

for i in range(iteration): 
	url = random.choice([x.strip() for x in open('urls.cfg')])
	host = random.choice([x.strip() for x in open('hosts.cfg')])
	agent = random.choice([x.strip() for x in open('agents.cfg')])
	# Create a Socket
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Connect to the Server
	connect=s.connect((sys.argv[1],port))
	# Send the HEAD request
	s.send('GET ' + url + ' HTTP/1.1' + '\r\n')
	s.send('Accept-Language: en-US' + '\r\n')
	s.send('User-Agent= ' + agent + '\r\n')
	s.send('Accept-Encoding: ' + '\r\n')
	s.send('Host: ' + host + '\r\n')
	s.send('Connection: Keep-Alive' + '\r\n')
	s.send('\r\n')
	result=s.recv(512)
	s.close()
	print host + url + ' User Agent: ' + agent + ' - Response: ' + result
#	s.close()