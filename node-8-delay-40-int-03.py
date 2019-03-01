import getpass
import sys
import telnetlib

HOST = "198.18.1.48"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("conf t\n")
tn.write("mpls traffic\n")
tn.write("int g0/0/0/3\n")
tn.write("admin-weight 40\n")
tn.write("commit\n")
tn.write("end\n")
tn.write("show run mpls traffic\n")
tn.write("show cdp nei\n")
tn.write("exit\n")

print tn.read_all()