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

tn.write("no route-policy SID($SID)\n")

tn.write("router bgp 65000\n")
tn.write("no ibgp policy out enforce-modification\n")

tn.write("address-family ipv4 unicast\n")
tn.write("no network 1.1.1.4/32 route-policy SID(4)\n")
tn.write("no allocate-label all\n")

tn.write("no neighbor 1.1.1.1\n")

tn.write("commit\n")
tn.write("end\n")
tn.write("show bgp ipv4 label sum\n")
tn.write("exit\n")

print tn.read_all()