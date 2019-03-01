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
tn.write("int g0/0/0/0\n")
tn.write("no shut\n")
tn.write("commit\n")
tn.write("end\n")
tn.write("show ip interface brief\n")
tn.write("exit\n")

print tn.read_all()