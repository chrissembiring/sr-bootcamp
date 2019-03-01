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
tn.write("int tunnel-te4215\n")
tn.write("ipv4 unn lo0\n")
tn.write("autoroute announce\n")
tn.write("dest 1.1.1.5\n")
tn.write("path-option 4 explicit name 4-2-1-5\n")
tn.write("exit\n")
tn.write("explicit-path name 4-2-1-5\n")
tn.write("index 10 next-address strict ipv4 unicast 10.2.4.2\n")
tn.write("index 20 next-address strict ipv4 unicast 10.1.2.1\n")
tn.write("index 30 next-address loose ipv4 unicast 1.1.1.5\n")
tn.write("commit\n")
tn.write("end\n")
tn.write("show ip interface brief\n")
tn.write("exit\n")

print tn.read_all()