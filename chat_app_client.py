import socket

print("client side calisti\n")
host = "127.0.0.1"
port = 5000
format="utf-8"
byte_size=1024
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))
print("client olusturuldu")

while True:
    message = client.recv(byte_size).decode(format)
    if not message:
        print("Bağlanti kapandi.")
        break
    if message.lower() == "quit":
        client.send("Çikiş yapildi".encode(format))
        client.close()
        break
    else:
        print(f"Server: {message}")
        reply = input("Enter your message: ")
        client.send(reply.encode(format))

client.close()  









