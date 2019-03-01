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
tn.write("router isis 1\n")
tn.write("address-family ipv4 unicast\n")
tn.write("microloop avoidance segment-routing\n")
tn.write("commit\n")
tn.write("end\n")
tn.write("show run router isis | in microloop\n")
tn.write("exit\n")

print tn.read_all()

