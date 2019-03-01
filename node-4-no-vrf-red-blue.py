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
tn.write("router bgp 65000\n")
tn.write("no vrf red\n")
tn.write("no vrf blue\n")
tn.write("no int lo4\n")
tn.write("no int lo14\n")
tn.write("no int lo40\n")
tn.write("no int lo44\n")
tn.write("no int lo144\n")
tn.write("no int lo140\n")
tn.write("no vrf red\n")
tn.write("no vrf blue\n")
tn.write("commit\n")
tn.write("end\n")
tn.write("show vrf all\n")
tn.write("exit\n")

print tn.read_all()
