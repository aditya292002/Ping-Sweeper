import os
 
IP = input("[+] Enter the Host IP Address:\t")


# Getting ping-sweep range 
start_sweep = int(input("Start ping sweep on : \t"))
end_sweep = int(input("End ping sweep at : \t"))

dot = IP.rfind(".")
IP = IP[0:dot + 1]

print("[+] Starting Ping Sweeper on " + IP + str(start_sweep))

# Checking for valid sweep range
if(start_sweep <= 0):
   start_sweep = 1

if(end_sweep > 255):
   end_sweep = 255

noOfAliveHosts = 0


# Running Ping-Sweep
for i in range(start_sweep, end_sweep + 1):
    host = IP + str(i)
    response = os.system("ping -c 1 -w 1 " + host + " >/dev/null")
 
    if response == 0:
        print(host + " is up")
        noOfAliveHosts+=1
    else:
        print(host + " is down")

print("No. of Alive Hosts : ", noOfAliveHosts)
