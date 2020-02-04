import socket
from open_upnp import open_upnp
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
client_socket.connect(('91.77.244.112',5001))

while True:
    message = input().encode("utf-8")
    client_socket.sendto(message, ('192.168.1.67',5001))


