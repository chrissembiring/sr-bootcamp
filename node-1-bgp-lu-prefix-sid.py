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
tn.write("router bgp 65000\n")
tn.write("ibgp policy out enforce-modification\n")
tn.write("address-family ipv4 unicast\n")
tn.write("allocate-label all\n")
tn.write("neighbor 1.1.1.4\n")
tn.write("remote-as 65000\n")
tn.write("update-source Lo0\n")
tn.write("address-family ipv4 labeled-unicast\n")
tn.write("route-reflector-client\n")
tn.write("next-hop-self\n")
tn.write("neighbor 1.1.1.5\n")
tn.write("remote-as 65000\n")
tn.write("update-source Lo0\n")
tn.write("address-family ipv4 labeled-unicast\n")
tn.write("route-reflector-client\n")
tn.write("next-hop-self\n")
tn.write("commit\n")
tn.write("end\n")
tn.write("show bgp ipv4 label sum\n")
tn.write("exit\n")

print tn.read_all()
