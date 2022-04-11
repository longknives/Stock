import main
import time
import sys
import psutil

def setVar(ending):
    
    command1=input(str)
    commands = ["end", "start","startconsole", "startr-cpu", "graph-one", "graph-two", "graph-all"]
    for x in range(3):
     if command1 == commands[0]:
        time.sleep(5)
        quit()
        
    if(command1 == commands[1]):
        ending == True
    
    if (command1 == commands[2]):
         sys.stdout = open('ENTERDIRECTORY, 'w')
   
    if (command1 == commands[3]):
        print('RAM memory % used:', psutil.virtual_memory()[2])
        print('The CPU usage is: ', psutil.cpu_percent(4))

    
        
    

