import socket # needed for socket

UDP_IP = "127.0.0.1"
UDP_PORT = 7331

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

print('RC Tank Controller')

while True:
    msg = input("Enter a command: ")
    sock.sendto(msg.encode(), (UDP_IP, UDP_PORT))