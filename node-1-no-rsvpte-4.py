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
tn.write("no int tunnel-te4\n")
tn.write("no explicit-path name 1-2-4\n")
tn.write("commit\n")
tn.write("end\n")
tn.write("show ip interface brief\n")
tn.write("exit\n")

print tn.read_all()