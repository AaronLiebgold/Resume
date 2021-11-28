#!/usr/bin/env python3

import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host,port))
s.listen(1)
print(host)
print("Waiting For Incoming Connections.....")
conn, addr = s.accept()
print( addr, "Has Successfully Connected to the Server..")


fileName = input("Please enter the filename you would like to send :")
file = open(fileName,'rb')
file_data = file.read(1024)
conn.send(file_data)
print("Data has been transferd successfuly!")
