import socket
print("server side calisti\n")
host = "127.0.0.1"
port = 5000
byte_size=10240
format="utf-8"

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()
client_socket, client_address = server.accept()
print("server dinlemede ")      
print(f"Bağlanan: {client_address}")
client_socket.send("Server bağlantisi gerçekleşti".encode(format))    #bağlanan tarafa baglanti mesaji gönderdik
                                      

while True:
    message=client_socket.recv(byte_size).decode(format)                #belirtilen size da mesaj kabulu
    if message.lower()=="quit":
        client_socket.send("cikis yapildi".encode(format))
        client_socket.close()                                           #client quit gönderirse cikis yapar
        server.close()
        break
    else:
        print(f"client:{message}\n")                             
        message=input("enter your message\n")
        client_socket.send(message.encode(format))

client_socket.close()
server.close()    



