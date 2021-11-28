#!/usr/bin/env python3

import socket
import argparse

#binding argparse to a variable
# description used in help Text

parser = argparse.ArgumentParser(description='This script creates a server bound to an IP Address and port.')

#creating arguments using add_arguent

parser.add_argument('-i','--ip', type=str, metavar='[ip address]', default='none', required=True, help='The ipAddress the server is listing to.')

parser.add_argument('-p','--port', type=int, metavar='[port]', required=True, help='The port the server is listening to.')

## validating arguments being passed with parse_args

argsFromCommandLine = parser.parse_args()

# Creating a socket(TCP,IP)

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

myIP = argsFromCommandLine.ip
myPort = argsFromCommandLine.port
myServerInfo = (myIP,myPort)
myTermKey = "EXIT"
killCmd =False

# Bind Socket to IP Address

mySocket.bind(myServerInfo)

# this is telling the server to listen for incommiing connections
mySocket.listen()

# loop for incomming connections

while True:
    print(f"Waiting to connect to {myIP}:{myPort}")
    myConnection, clientAddress = mySocket.accept()
    try:
        print(f"SUCCESSFULL CONNECTION to {clientAddress}")
# Starting Loop to proccess incoming information

        while True:
            incomingData = myConnection.recv(1024)
            print(type(incomingData))
# Decode to Read file
            incomingData = incomingData.decode()
            print(f"Data Recieved:{incomingData}")
            if incomingData == myTermKey:
                myConnection.close()

            elif incomingData:
                incomingData = incomingData.encode()
                print("Sending Data back to the Client")
                myConnection.sendall(incomingData)
            else:
                print(f'End of Client Data {clientAddress}')
                myConnection.close()


#the kill command was recieved if we get this far 

    except:
        print("You Entered the Term Key, Shutting down now.")
