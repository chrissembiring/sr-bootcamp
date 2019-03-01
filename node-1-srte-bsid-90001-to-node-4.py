import getpass
import sys
import telnetlib

HOST = "198.18.1.41"
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
tn.write("segment-list 1-7-3-2-4\n")
tn.write("index 10 mpls label 16007\n")
tn.write("index 20 mpls label 16002\n")
tn.write("index 30 mpls label 16004\n")
tn.write("policy node-4\n")
tn.write("binding-sid mpls 90001\n")
tn.write("color 4 end-point ipv4 1.1.1.4\n")
tn.write("candidate-paths\n")
tn.write("preference 100\n")
tn.write("explicit segment-list 1-7-3-2-4\n")
tn.write("commit\n")
tn.write("end\n")
tn.write("show run segment-routing | in policy \n")
tn.write("exit\n")

print tn.read_all()