import subprocess
import os
import time


def hibernate():
    #subprocess.call(['shutdown','/h'])
    pass

def shutdown():
    #subprocess.call(['shutdown','/s'])
    pass

def restart():
    #restarts the local machine suddenly/immediately 
    subprocess.call(['shutdown','/r','-t','0'])
    

def main_task():
    #provide the file name path here , no need to create at first time . we just need to give the path with file name 
    file = r"C:\Users\girishsj\startup_counter.txt"
    subprocess.call(['whoami'])
    subprocess.call(['hostname'])

    if(os.path.isfile(file)==False):
        count = int(input("How many times would you like to run the program ? : "))
        #defines the counter value to run the script that times 
        with open(file,'a+') as f:
            f.write(str(count)+'\n')
        restart()
    else:
        with open(file,'r') as f:
            lines = f.readlines()
        
        with open(file,'a+') as f:
            value = int(lines[-1].strip('\n'))
            if(value>0):
                f.write(str(value-1)+'\n')
                time.sleep(1)
                restart()
                
            else:
                print("Program is done its turn")
                os._exit(1)

    #restart()
        
        

if __name__ == "__main__":
    main_task()
