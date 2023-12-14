
# "Creating a Beep Alarm Program in Python"


import winsound
import time

def beeep_alarm():
    for  repates in range (5):
        winsound.Beep(3000,500)
        winsound.Beep(4000,300)
        

#timeduration is user input

timeduration= int(input("SET TIMER: "))

hours , min , seconds =0,0,0

for i in range(timeduration):
    print('\n' * 10)    
    seconds +=1

    if seconds == 60:
        min += 1
        seconds=0

    if min == 60:
        hours += 1
        min=0

    print(str(hours)  + ':' + str(min) + ':' + str(seconds))
    time.sleep(1)
print('TIME IS  OVER AND BEEP SOUND')

if __name__=='__main__':
    beeep_alarm()





