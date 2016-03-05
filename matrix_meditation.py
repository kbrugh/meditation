import os, random, time
 
def lucid(meditation):
    beginTime = time.time() #set beginning time
    while((time.time()- beginTime)<timemax): # check time difference
        time.sleep(delay)
        print os.urandom(256), meditation, os.urandom(random.randint(0, 256))

      
 
if __name__ == '__main__':
    meditation = raw_input("Enter meditation: ")
    Hz = float(raw_input("Enter brainwave frequency, in Hz: "))
    timer = int(raw_input("Enter time, in minutes: "))
    delay = 1 / Hz
    timemax = timer * 60
    lucid(meditation)
