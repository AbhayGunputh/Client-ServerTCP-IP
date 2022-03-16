import socket
import sys

IP = socket.gethostbyname(socket.gethostname())
PORT = 12345
ADDR = (IP, PORT)
FORMAT= "utf-8"

print("[Starting] server is starting")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)
s.listen(5)
print("[Listening] server is listening")

while True:
    clientsocket, address = s.accept()
    print("Connection established with {}".format(address))

    file = open("Downloads/download.jpeg",'wb')    
    msg = clientsocket.recv(1024)
    
    while msg:
        file.write(msg)
        msg = clientsocket.recv(1024)
    
    arr = list(msg)
    arr = list(map(int, arr))
    arr.reverse()
    ansParity = []

    r = 0
    while((len(arr) + 1) > pow(2,r)):
        r = r+1

    for j in range(1, r+1):
        sum = 0
        for i in range(1, len(arr)+1):
            x = format(i, "b")
            if(j <= len(x) and x[0-j] == '1'):
                sum += arr[i-1]

        if(sum%2 == 0): ansParity.append(0)                #EVEN PARITY USED
        else: ansParity.append(1)

    ansParity.reverse()
    print(ansParity)
    tempString = ''.join(str(x) for x in ansParity)
    num = len(tempString)
   
    if(num == 0):
        print("NO ERROR IN CHECKSUM")
        print("File received successfully")
        clientsocket.send(bytes("NO ERROR", FORMAT))
    else:
        print("ERROR at INDEX => " + str(num))
        clientsocket.send(bytes("ERROR at INDEX => " + str(num), FORMAT))
    file.close()
    clientsocket.close()
    #print(f"[Disconnected] {addr} disconnected")
