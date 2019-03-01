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
tn.write("no router isis 1\n")
tn.write("commit\n")

tn.write("router ospf 2\n")
tn.write("router-id 1.1.1.8\n")
tn.write("segment-routing mpls\n")
tn.write("segment-routing forwarding mpls\n")
tn.write("segment-routing sr-prefer\n")
tn.write("address-family ipv4 unicast\n")
tn.write("redis static\n")
tn.write("area 0\n")
tn.write("mpls traffic-eng\n")
tn.write("interface Loopback0\n")
tn.write("prefix-sid absolute 16008\n")
tn.write("interface GigabitEthernet0/0/0/0\n")
tn.write("network point-to-point\n")
tn.write("fast-reroute per-prefix\n")
tn.write("fast-reroute per-prefix ti-lfa enable\n")
tn.write("interface GigabitEthernet0/0/0/1\n")
tn.write("network point-to-point\n")
tn.write("fast-reroute per-prefix\n")
tn.write("fast-reroute per-prefix ti-lfa enable\n")
tn.write("interface GigabitEthernet0/0/0/2\n")
tn.write("network point-to-point\n")
tn.write("fast-reroute per-prefix\n")
tn.write("fast-reroute per-prefix ti-lfa enable\n")
tn.write("interface GigabitEthernet0/0/0/3\n")
tn.write("network point-to-point\n")
tn.write("fast-reroute per-prefix\n")
tn.write("fast-reroute per-prefix ti-lfa enable\n")
tn.write("mpls traffic-eng router-id Loopback0\n")
tn.write("commit\n")

tn.write("end\n")
tn.write("show run | in router ospf \n")
tn.write("exit\n")

print tn.read_all()