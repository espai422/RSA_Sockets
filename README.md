# RSA_Sockets
Basic comunication between two sockets with RSA encryptation for the messages

## Dependences

There is only one python library
```
pip install pycryptodome
```

if you have installed **pycrypto**, you should uninstall it.
```
pip uninstall pycrypto
```

## Set-Up

you will nes to start the server and the client with two positional arguments both must have the same arguments. This arguments are the IP addr and the port. The IP must be the IP addr of the server computer. The port can be any free port. Here you have an example.

```bash
python Server.py 192.168.1.75 5050

python Client.py 192.168.1.75 5050
```



