import socket
import select


def parseData(data):
  print("Data: ", data)

BUFFER = 2048
clientList=dict({})
host = ''
port = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientList[server]={'ip':'', 'port':12345}
server.bind((host, port))
server.listen(5)
print("Server is listening for connections!")
while clientList:
  readable,_,_ = select.select(clientList,[],[],0)
  for sock in readable:
    if sock is server:
      conn, addr = server.accept()
      clientList[conn] = {'ip':addr[0], 'port':addr[1]}
      print("New Connection: ", clientList[conn])
    else:
      data = sock.recv(BUFFER)
      if not data:
        print("Connection closed by: ", sock.getpeername())
        del clientList[sock]
      else:
        parseData(data.decode('ascii'))
