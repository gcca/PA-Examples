#!/usr/bin/env python

import base64
import getpass
import os
import socket
import sys
import traceback
import random
import paramiko
import interactive

if len(sys.argv) != 6:
        print "Usage: http-client-ssh.py <server address> <port> <number of iterations> <username> <password>"
        sys.exit(0)

server = (sys.argv[1])
port = int(sys.argv[2])
iteration = int(sys.argv[3])
username = (sys.argv[4])
password = (sys.argv[5])
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
        print host + url + ' User Agent: ' + agent + ' - Response: ' + result

# Connect and use paramiko Client to negotiate SSH2 across the connection
try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#    client.set_missing_host_key_policy(paramiko.WarningPolicy)
    print 'Connecting...'
    client.connect(server, port, username, password)
    chan = client.invoke_shell()
    print repr(client.get_transport())
    print 'Establishing SSH connection...'
    print
    interactive.interactive_shell(chan)
    chan.close()
    client.close()

except Exception, e:
    print '*** Caught exception: %s: %s' % (e.__class__, e)
    traceback.print_exc()
    try:
        client.close()
    except:
        pass
    sys.exit(1)
