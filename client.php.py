import time
import socket
from threading import Thread
class client_socket():
    def __init__(self):
        self.port_no = 5001
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('192.168.1.67', self.port_no))
        self.shutdown = False

    def get_message(self):
        while not self.shutdown:
            try:
                requset = self.client_socket.recv(4096)
                if requset==b'':
                    print('Server disconnect')
                    self.client_socket.close()
                    break
                print(requset.decode("utf-8"))
            except:
                self.shutdown = True
                print(self.shutdown)
                self.client_socket.close()
                break
    def close(self):
        self.client_socket.close()
    def send_message(self):
        while not self.shutdown:
            try:
                message = input()
                if message != "":
                    self.client_socket.send(message.encode("utf-8"))
                time.sleep(0.2)
            except:
                self.shutdown = True
                self.client_socket.send("left chat ".encode("utf-8"))

if __name__ == "__main__":
    client = client_socket()
    rT = Thread(target=client.get_message)
    rT.start()
    client.send_message()
    client.close()
    rT.join()

