import socket
import threading
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from message import Message
import sys


bit_size = 2048
keys = RSA.generate(bit_size)

exported_Key = keys.publickey().export_key().decode('utf-8')


try:
    PORT = int(sys.argv[2])
    HOST = sys.argv[1]
except:
    print(F'Usage: python {sys.argv[0]} <IP> <PORT>')


SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

SERVER.bind((HOST,PORT))


# Generar Claus

def New_Client(Socket):
    # Send Public key
    message_to_send = Message(exported_Key)
    serial_message = message_to_send.serialize()
    Socket.send(serial_message)
    decipher_rsa = PKCS1_OAEP.new(keys)

    
    # Main loop for the client
    while True:
        msg_len = Socket.recv(128).decode('utf-8')
        if msg_len:
            msg_len = int(msg_len)
            msg = Socket.recv(msg_len)
            # Convert bytes into dictionary object
            print('\n--------Missate Xifrat---------\n')
            print(msg)

            dec_data = decipher_rsa.decrypt(msg)
            print('\n--------Missate Desxifrat---------\n')
            print(str(dec_data).replace("b'","").replace("'",''))


def main(server):
    server.listen()
    print(F'[STATUS] Server started on {HOST}:{PORT}')
    while True:
        client_socket, address = server.accept()
        print(F'[INFO] New Connection from {address}')
        newTrhead = threading.Thread(target = New_Client, args=(client_socket,))
        newTrhead.start()
        

if __name__ == '__main__':
    main(SERVER)