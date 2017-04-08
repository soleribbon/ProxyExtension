import os

print "Tool For Proxy Makers\nBy @Masterkidravi"
print "\n"
print "MAKE SURE YOU HAVE 'proxies.txt' FILE IN SAME DIRECTORY!"
print "\n"

userpass = raw_input("Do the proxies need :user:pass? (y/n): ")



new_lines = []
if userpass == "y":
    port = (raw_input("Port:"))
    user = (raw_input("User: "))
    passw = (raw_input("Pass: "))
    with open("proxies.txt") as f:
        new_lines = [line.strip("\n") + ":" + (port) + ":" + (user) + ":" + (passw) for line in f]
    with open("proxies.txt","w") as f:
        f.write("\n".join(new_lines))
    print "Done!"   
if userpass == "n":
    port = (raw_input("Port:"))
    with open("proxies.txt") as f:
        new_lines = [line.strip("\n") + ":" + (port) for line in f]
    with open("proxies.txt","w") as f:
        f.write("\n".join(new_lines))
    print "Done!"
