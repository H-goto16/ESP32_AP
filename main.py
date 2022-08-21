import socket
import network
import ssl
import re

ESSID = "ESP32"
PASSWORD = "ESPWROOM32"
IP = "192.168.5.1"

def wifi(essid, pwd, ip, mask, gw, dns):
    ap = network.WLAN(network.AP_IF)
    ap.config(essid = essid, authmode = 3, password = pwd)
    ap.ifconfig((ip,mask,gw,dns))
    print("(ip,netmask,gw,dns)=" + str(ap.ifconfig()))
    ap.active(True)
    return ap

wifi(ESSID, PASSWORD, IP, '255.255.255.0', IP, '8.8.8.8')

def web_page():
    html = """
   """
    return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    request = str(conn.recv(1024)).lower()
    print("request : "+  request)
    m = re.search(r'test=(\w+)', request)
    if m != None :
        word = m.group(0)
        print(word[5:])
    conn.close()

