
import sys
import socket

fqdnvalue = input("Enter the web address you are looking to resolve : ")

try:
    host = str(fqdnvalue).replace("https://", "").replace("http://", "").replace("www.", "")

except socket.gaierror:
    print("ERROR\n Make sure you entered a correct website")
    sys.exit(2)

ip = socket.gethostbyname(host)
print(ip)