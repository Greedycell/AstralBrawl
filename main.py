import json
import socket
import time
import os
import platform
from threading import Thread
from Protocol.MessageFactory import *
from Logic.Device import Device
from Core.Crypto import Crypto

config = json.load(open("config.json", "r"))
server_address = ("0.0.0.0", config["Port"])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

class ClientSocket(Thread):
    def __init__(self, client, address):
        super().__init__(daemon=True)
        self.client = client
        self.address = address
        self.device = Device(client)

    def recvall(self, size):
        data = b""
        while len(data) < size:
            chunk = self.client.recv(size - len(data))
            if not chunk:
                raise EOFError
            data += chunk
        return data

    def run(self):
        print("[*] >> A connection has appeared!", self.address)
        crypter = Crypto()
        last_packet = time.time()
        while True:
            header = self.client.recv(7)
            if len(header) > 0:
                if not header:
                    break
                last_packet = time.time()
                packetid = int.from_bytes(header[:2], "big")
                length   = int.from_bytes(header[2:5], "big")
                version  = int.from_bytes(header[5:], "big")
                payload = self.recvall(length)
                pdata = crypter.decrypt(packetid, payload)
                if packetid in MessageFactory:
                    msg = MessageFactory[packetid](payload, self.client)
                    msg.decode()
                    msg.process(crypter)
                else:
                    print("[*] >> Unhandled packet:", packetid)
            if time.time() - last_packet > 10:
                print(f"[*] >> IP: {self.address} disconnected!")
                self.client.close()
                break

class StartServer:
    def run(self):
        sock.bind(server_address)
        # listen for connections
        sock.listen()
        print("[SERVER] >> Listening on 0.0.0.0:{}".format(config['Port']))

        while True:
            client, addr = sock.accept()
            ClientSocket(client, addr).start()

if __name__ == "__main__":
    # Platform stuff
    if os.name == "nt":  # Windows
        os.system("title AstralBrawl V11")
    else:  # Linux/MacOS
        print("\033]0;AstralBrawl V11\007", end="")
    os.system("cls" if platform.system() == "Windows" else "clear")

    print("""
    _        _             _ ____                     _ 
   / \   ___| |_ _ __ __ _| | __ ) _ __ __ ___      _| |
  / _ \ / __| __| '__/ _` | |  _ \| '__/ _` \ \ /\ / / |
 / ___ \\__  \ |_| | | (_| | | |_) | | | (_| |\ V  V /| |
/_/   \_\___/\__|_|  \__,_|_|____/|_|  \__,_| \_/\_/ |_|
    """)
    print('Server created by @Greedycell on Github!')
    print(' ')

    StartServer().run()