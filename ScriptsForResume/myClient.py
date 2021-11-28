#!/usr/bin/env python3
import socket
import argparse

parser = argparse.ArgumentParser(description="This script creates a client for an echo server")


# Creating group of Arguments

parser.add_argument('-i','--ip', type=str, metavar='[ip address]', default='none', required=True, help='The IP address the Server Connects too.')
parser.add_argument('-p','--port', type=int, metavar='[port]', required=True, help='The pportthe client connects too.')

argsFromCommandLine = parser.parse_args()

# Defining objects

serverAddress = argsFromCommandLine.ip
serverPort = argsFromCommandLine.port
myServerInfo = (serverAddress,serverPort)
dataFromUser =''

# Create socket
myClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the Server
myClientSocket.connect(myServerInfo)

print("Type 'EXIT' at any time to exit client")

# If user types EXIT at any moment, connection will close

while dataFromUser != 'EXIT':
    dataFromUser = input("What Should we send to the Server? :")
    if dataFromUser == '':
        print('\nYou need to enter something to send to the server\n')
        break
    dataToSend = dataFromUser.encode()
    print(f"> Sending '{dataToSend}'to the server")
# sending data
    myClientSocket.send(dataToSend)
# recieve the response and print message
    dataReceived = myClientSocket.recv(1024)
    print('> We Received data from the server:',dataReceived.decode(),'\n')

# close socket with "STOP"

print(f" Closing the connection to {serverAddress}:{serverPort}")
myClientSocket.close()
