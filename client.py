#Imports socket module
import socket

#Asks the user for a host and declares port variable
host = '127.0.0.1'
port = 6977

#Creates a new socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Accepts incoming connections
s.connect((host, port))

#While loop
while True:

  #Recieves data in a buffer size max of 1024
  data = s.recv(9999999).decode()

  #prints the data to the terminal
  print(data)

#closes the connection after data stops
s.close()