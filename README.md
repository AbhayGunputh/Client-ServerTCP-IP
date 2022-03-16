# Client Server TCP/IP Using PYTHON
Basically the program is to transfer photo from the server to client. The client is able to see all the available photos on the server and they can choose which photo to download. Once the client has choose the image to download, the downloaded image will be saved in the folder Downloads.

The program uses Hamming code for parity check. The program uses even parity.

## Programs
- Server.py
- Client.py


> To run the program, the user will have to open 2 terminal at the same time.
> In the first terminal, the user MUST run "server.py" first
> In the second terminal, the user will run "client.py"
> With this process the client will be able to connect with the server.

## To run server.py
In the first terminal type:
```sh
python3 server.py
```
## To run client.py
In the second terminal type:
```sh
python3 client.py
```
Once the user has select the image to download, the user can check the folder Downloads to see the image.

## Installation
Using the Installation script to install the program in a computer.
```sh
chmod u+x install
./install
```

