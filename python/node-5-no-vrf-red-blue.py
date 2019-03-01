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
tn.write("no vrf red\n")
tn.write("no vrf blue\n")
tn.write("no int lo5\n")
tn.write("no int lo15\n")
tn.write("no int lo50\n")
tn.write("no int lo55\n")
tn.write("no int lo155\n")
tn.write("no int lo150\n")
tn.write("router bgp 65000\n")
tn.write("neighbor-group RR-services-group\n")
tn.write("address-family vpnv4 unicast\n")
tn.write("no route-policy SET_COLOR_IN in\n")
tn.write("no vrf red\n")
tn.write("no vrf blue\n")
tn.write("no extcommunity-set opaque 4\n")
tn.write("no extcommunity-set opaque 14\n")
tn.write("no extcommunity-set opaque 40\n")
tn.write("no extcommunity-set opaque 44\n")
tn.write("no extcommunity-set opaque 140\n")
tn.write("no extcommunity-set opaque 144\n")
tn.write("no route-policy SET_COLOR_IN\n")
tn.write("commit\n")
tn.write("end\n")
tn.write("show vrf all\n")
tn.write("exit\n")

print tn.read_all()

