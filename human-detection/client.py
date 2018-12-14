from socket import *
def connectToServer():
    host = "172.16.40.139"
    port = 12345
    
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((host, port))
    return s
    print("Connected with server!")

def sendData(data,s):
    if (data != "exit"):
        s.send(data.encode('ascii'))
    
def closeServer(s):
    s.send("Disconnected".encode('ascii'))
    s.close()