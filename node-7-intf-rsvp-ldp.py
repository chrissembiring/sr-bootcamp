import getpass
import sys
import telnetlib

HOST = "198.18.1.47"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("conf t\n")
tn.write("rsvp\n")
tn.write("int g0/0/0/0\n")
tn.write("int g0/0/0/1\n")
tn.write("int g0/0/0/2\n")
tn.write("int g0/0/0/3\n")
tn.write("int g0/0/0/4\n")
tn.write("mpls traffic\n")
tn.write("int g0/0/0/0\n")
tn.write("int g0/0/0/1\n")
tn.write("int g0/0/0/2\n")
tn.write("int g0/0/0/3\n")
tn.write("mpls ldp\n")
tn.write("router-id 1.1.1.7\n")
tn.write("address-family ipv4\n")
tn.write("label local \n")
tn.write("no allocate \n")
tn.write("commit\n")
tn.write("end\n")
tn.write("show run rsvp\n")
tn.write("exit\n")
print tn.read_all()