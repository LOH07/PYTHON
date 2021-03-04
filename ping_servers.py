import os
import time

servers = ['0.0.0.1','127.0.0.1']

pings = [0,0]

while True:
    print('\nPress "Ctrl" + "C" to stop this program\n')
    
    for i in range(0,len(servers)):
        print(f'Sending pings to server {servers[i]} ...\n')
        
        os.system(f'ping -c 1 {servers[i]} > ping.txt')
    
        with open('ping.txt','r') as f:
            txt = f.read()
        
        if ' 0% ' in txt:
            print(f'Ping successful to server {servers[i]}\n')
        else:
            pings[i] += 1
            print(f'Ping not succesful to server {servers[i]}')
            print(f'missed pings to server {servers[i]} is {pings[i]}\n')
            if pings[i] == 3:
                print('Sending email message ...')
                pings[i] = 0
            else:
                pass
    print('Waiting 10 seconds ...')
    
    time.sleep(10)
    
    os.system('clear')
