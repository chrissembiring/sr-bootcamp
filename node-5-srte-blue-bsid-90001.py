import getpass
import sys
import telnetlib

HOST = "198.18.1.45"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("conf t\n")
tn.write("segment-routing\n")
tn.write("traffic-eng\n")
tn.write("segment-list 5-6-8-1-4\n")
tn.write("index 10 mpls label 16006\n")
tn.write("index 20 mpls label 16008\n")
tn.write("index 30 mpls label 16001\n")
tn.write("index 40 mpls label 90001\n")
tn.write("policy node-14\n")
tn.write("color 14 end-point ipv4 1.1.1.4\n")
tn.write("candidate-paths\n")
tn.write("preference 100\n")
tn.write("explicit segment-list 5-6-8-1-4\n")
tn.write("commit\n")
tn.write("end\n")
tn.write("show run segment-routing | in policy \n")
tn.write("exit\n")

print tn.read_all()