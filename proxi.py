import os
import subprocess
import time
print "Tool For Proxy Makers\nBy @Masterkidravi"
print "\n"
print "MAKE SURE YOU HAVE 'proxies.txt' FILE IN SAME DIRECTORY!"
print "\n"

userpass = raw_input("Do the proxies need :user:pass? (y/n): ")

port = raw_input("Port: ")

file = "proxies.txt"
new_lines = []
if userpass == "y":

    user = raw_input("User: ")
    passw = raw_input("Pass: ")
    with open(file) as f:
        new_lines = [line.strip("\n") + ":" + (port) + ":" + (user) + ":" + (passw) for line in f]
        
    with open(file,"w") as f:
        f.write("\n".join(new_lines))
        f.close() 
        time.sleep(3)
    
        subprocess.call(['open', '-a', 'TextEdit', file])
    print "DONE!"
    
        
if userpass == "n":

    with open(file) as f:
        new_lines = [line.strip("\n") + ":" + (port) for line in f]
    with open(file,"w") as f:
        f.write("\n".join(new_lines))
        f.close()
        subprocess.call(['open', '-a', 'TextEdit', file])
        
    print "Done!"
