import getpass
import sys
import telnetlib

HOST = "198.18.1.44"
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
tn.write("segment-list 4-5\n")
tn.write("index 10 address ipv4 10.4.7.7\n")
tn.write("index 20 mpls label 16005\n")
tn.write("policy node-15\n")
tn.write("color 15 end-point ipv4 1.1.1.5\n")
tn.write("candidate-paths\n")
tn.write("preference 100\n")
tn.write("explicit segment-list 4-5\n")
tn.write("commit\n")
tn.write("end\n")
tn.write("show run segment-routing | in policy \n")
tn.write("exit\n")

print tn.read_all()