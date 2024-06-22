import socket
import os

host = '127.0.0.1'
port = 80
timeout_seconds = 1

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(timeout_seconds)
result = sock.connect_ex((host, int(port)))

if result == 0:
    print("Host: {}, Port: {} - True".format(host, port))
else:
    print("Host: {}, Port: {} - False".format(host, port))
    screen -S port80proxyDT -X stuff "echo while true; do ulimit -n 999999 && proxy --port 80; done\n"

sock.close()
