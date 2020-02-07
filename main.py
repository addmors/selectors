import miniupnpc
import socket
import selectors
from open_upnp import open_upnp
import sys


port_no = 5001
selector = selectors.DefaultSelector()

def close(_socket):
    print('Client disconnect')
    _socket.close()
    selector.unregister(_socket)
def server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server_socket.bind((miniupnpc.UPnP().lanaddr, port_no))
    server_socket.listen()
    selector.register(fileobj=server_socket,events=selectors.EVENT_READ, data=accept_connection)

def accept_connection(server_socket):
    client_socket ,addr = server_socket.accept()
    print('Connection from: ', addr)
    selector.register(fileobj=client_socket,events=selectors.EVENT_READ, data=send_message)


def send_message(client_socket):
    try:
        requset = client_socket.recv(4096)
        if requset ==b'':
            close(client_socket)
        else:
            print(requset.decode())
            response = 'Hello world'.encode("utf-8")
            client_socket.send(response)
    except:
        close(client_socket)
def event_lop():
    while True:
        events = selector.select()

        for key,_ in events:
            callback = key.data
            callback(key.fileobj)




if __name__ == '__main__':
    open_upnp(5001)
    server()
    event_lop()