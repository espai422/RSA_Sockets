import socket
import sys
import pickle
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Socket Settings
try:
    PORT = int(sys.argv[2])
    SERVER = sys.argv[1]
except:
    print(F'Usage: python {sys.argv[0]} <IP> <PORT>')

# Connect to the server
Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Client.connect((SERVER,PORT))

# Recive Sebastia Key
msg_len = Client.recv(128).decode('utf-8')
if msg_len:
    msg_len = int(msg_len)
    msg_bytes = Client.recv(msg_len)
    
    # Convert bytes into dictionary object
    Public_Key = pickle.loads(msg_bytes)
    print(Public_Key)

    # Import public Key
    KEY = RSA.import_key(Public_Key.encode('utf-8'))
    cipher_rsa = PKCS1_OAEP.new(KEY)

while True:
    RawMessage = input('=> ')

    message = cipher_rsa.encrypt(RawMessage.encode('utf-8'))
    msg_len = len(message)
    send_len = str(msg_len).encode('utf-8')
    send_len += b' ' * (128 - len(send_len))

    print(message)
    Client.send(send_len)
    Client.send(message)
