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
tn.write("segment-list 4-up\n")
tn.write("index 10 address ipv4 10.1.5.1\n")
tn.write("index 20 address ipv4 10.1.2.2\n")
tn.write("index 30 mpls label 16004\n")
tn.write("exit\n")
tn.write("segment-list 4-down\n")
tn.write("index 10 address ipv4 10.5.6.6\n")
tn.write("index 20 address ipv4 10.6.7.7\n")
tn.write("index 30 address ipv4 10.4.7.4\n")
tn.write("exit\n")
tn.write("policy node-4\n")
tn.write("color 4 end-point ipv4 1.1.1.4\n")
tn.write("candidate-paths\n")
tn.write("preference 100\n")
tn.write("explicit segment-list 4-up weight 1\n")
tn.write("explicit segment-list 4-down weight 2\n")
tn.write("commit\n")
tn.write("end\n")
tn.write("show run segment-routing | in policy \n")
tn.write("exit\n")

print tn.read_all()