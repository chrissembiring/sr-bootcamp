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
tn.write("pcc\n")
tn.write("no pce address ipv4 1.1.1.201\n")
tn.write("commit\n")
tn.write("end\n")
tn.write("show segment traffic pcc ipv4 peer \n")
tn.write("exit\n")

print tn.read_all()