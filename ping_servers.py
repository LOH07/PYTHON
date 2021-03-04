import os
import time

# This is the list of servers to be pinged
servers = ['0.0.0.1','127.0.0.1']

# each of the items in the 'pings' list corresponds to one of the servers
# so the len(pings) should be equal to the len(servers)
pings = [0,0]

# this is the MAIN LOOP that will run until someone presses 'Ctrl'+'C'
while True:
    print('\nPress "Ctrl" + "C" to stop this program\n')
    
    # this is the loop that will run every X seconds (see 'time.sleep()' below)
    for i in range(0,len(servers)):
        print(f'Sending pings to server {servers[i]} ...\n')
        
        # this command SENDS THE PING(S) and WRITES THE OUTPUT to the 'ping.txt' file
        os.system(f'ping -c 1 {servers[i]} > ping.txt')
        
        # this command OPENS the 'ping.txt' file and READS it
        with open('ping.txt','r') as f:
            txt = f.read()
        
        # the following statements check if the pings were successful or not
        # by searching in the 'ping.txt' file
        if ' 0% ' in txt:
            print(f'Ping successful to server {servers[i]}\n')
        else:
            pings[i] += 1
            print(f'Ping not succesful to server {servers[i]}')
            print(f'missed pings to server {servers[i]} is {pings[i]}\n')
            
            # if one of the servers couldn't be pinged for 3 times
            # an email message can be sent (the code needed for that can be added)
            if pings[i] == 3:
                print('Sending email message ...')
                pings[i] = 0
            else:
                pass
    
    print('Waiting 10 seconds ...')
    
    # this command creates a break of 10 seconds between the FOR LOOPS
    # so the 'servers' are pinged every 10 seconds and THIS CAN BE ADJUSTED as needed
    time.sleep(10)
    
    # this command CLEARS the terminal (the screen)
    os.system('clear')
