import os

print "Tool For Proxy Makers\nBy @Masterkidravi"
print "\n"
print "MAKE SURE YOU HAVE 'proxies.txt' FILE IN SAME DIRECTORY!"
print "\n"

port = (raw_input("Port:"))
user = (raw_input("User: "))
passw = (raw_input("Pass: "))

new_lines = []

with open("proxies.txt") as f:
       new_lines = [line.strip("\n") + ":" + (port) + ":" + (user) + ":" + (passw) for line in f]
with open("proxies.txt","w") as f:
       f.write("\n".join(new_lines))



