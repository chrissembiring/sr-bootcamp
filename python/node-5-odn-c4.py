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
tn.write("on-demand color 4\n")
tn.write("dynamic\n")
tn.write("pce\n")
tn.write("metric type te\n")
tn.write("commit\n")
tn.write("end\n")
tn.write("show run segment-routing | in on-demand \n")
tn.write("exit\n")

print tn.read_all()