#Imports the socket module
import time
import socket

#Assigns variable s and specifies what socket we're setting up
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM )

#Host and port variables for binding to the socket later
host = '127.0.0.1'
port = 6977

#Binds the host and port to the socket, double parentheses for awkward formatting.
s.bind((host, port))
print("For devs: bound ", host, port, "to socket")

#Listens on the socket, 5 represents amount of failed connections allowed
s.listen(1)
print("Listening...")

#Testing stuff ignore these
sname = s.getsockname() #Gets socket information
print("Socket name: ", sname) #Prints socket information

#Incoming connection gets accepted
conn, addr = s.accept()

#Displays who connected
print("Current connections: ", addr)

#The loop that sends our message :)
while True:
    time.sleep(2)
    data = "Woah, testing! :)"
    conn.send(str.encode(data))