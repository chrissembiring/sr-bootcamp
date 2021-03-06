import getpass
import sys
import telnetlib

HOST = "198.18.1.47"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("conf t\n")
tn.write("no rsvp\n")
tn.write("mpls ldp\n")
tn.write("address-family ipv4\n")
tn.write("label\n")
tn.write("local\n")
tn.write("allocate for no_ldp\n")
tn.write("commit\n")
tn.write("end\n")
tn.write("show run router isis | in \"segment-routing|prefix-sid\"\n")
tn.write("exit\n")

print tn.read_all()

