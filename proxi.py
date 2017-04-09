import os

print "Tool For Proxy Makers\nBy @Masterkidravi"
print "\n"
print "MAKE SURE YOU HAVE 'proxies.txt' FILE IN SAME DIRECTORY!"
print "\n"

userpass = raw_input("Do the proxies need :user:pass? (y/n): ")

port = raw_input("Port: ")
global port

new_lines = []
if userpass == "y":

    user = raw_input("User: ")
    passw = raw_input("Pass: ")
    with open("proxies.txt") as f:
        new_lines = [line.strip("\n") + ":" + (port) + ":" + (user) + ":" + (passw) for line in f]
        
    with open("proxies.txt","w") as f:
        f.write("\n".join(new_lines))
        f.close() 
    print "DONE!"


    
        
if userpass == "n":

    with open("proxies.txt") as f:
        new_lines = [line.strip("\n") + ":" + (port) for line in f]
    with open("proxies.txt","w") as f:
        f.write("\n".join(new_lines))
        f.close()
    print "Done!"
