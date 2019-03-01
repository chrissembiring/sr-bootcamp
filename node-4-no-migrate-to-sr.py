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
tn.write("router isis 1\n")
tn.write("interface lo0\n")
tn.write("address-family ipv4 unicast\n")
tn.write("no prefix-sid absolute 16004\n")
tn.write("no prefix-sid strict-spf absolute 17004\n")
tn.write("interface lo44\n")
tn.write("address-family ipv4 unicast\n")
tn.write("no prefix-sid absolute 16499\n")
tn.write("exit\n")
tn.write("exit\n")
tn.write("address-family ipv4 unicast\n")
tn.write("no segment-routing mpls\n")
tn.write("commit\n")
tn.write("end\n")
tn.write("show run router isis | in prefix-sid\n")
tn.write("exit\n")

print tn.read_all()

