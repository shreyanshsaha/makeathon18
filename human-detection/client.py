host = "192.168.43.94"
port = 1605
from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect((host, port))
print("Connected with server!")
data = ""
if (data != "exit"):
   s.send(data)
s.close()
