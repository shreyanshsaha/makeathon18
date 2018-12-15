import socket
import sys
import select
import subprocess
import argparse
import time
import re, uuid 



parser = argparse.ArgumentParser(description='Display WLAN signal strength.')
parser.add_argument(dest='interface', nargs='?', default='wlan0',
                    help='wlan interface (default: wlan0)')
args = parser.parse_args()

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('192.168.43.95',12345))
time.sleep(0.1)
client.send("\n".encode('ascii'))
socket_list=[sys.stdin,client]

while True:
    # ready,_,_=select.select(socket_list,[],[],0)
    # for socket in ready:
        # if socket is client:
        #     data=client.recv(1024)
        #     print(data.decode('ascii'))
        #     if not data :
        #         sys.exit()
    macAd=':'.join(re.findall('..', '%012x' % uuid.getnode()))    
    cmd = subprocess.Popen('iwconfig %s' % args.interface, shell=True,
                    stdout=subprocess.PIPE)
    b=-1                
    for line in cmd.stdout:
        if 'Link Quality' in line:
            a= line.lstrip(' ')[-10:-7]
            a=abs(int(a))
            if(a<50):
                b='0'
            if(a>50 and a<57):
                b='1'
            if(a>60):
                b='2'
            client.send(str(b).encode('ascii'))
            client.send(macAd.encode('ascii'))


        elif 'Not-Associated' in line:
            b='No signal'
            client.send(str(b).encode('ascii'))

    # msg=sys.stdin.readline()
    # client.send(str(msg).encode('ascii')) 
    
