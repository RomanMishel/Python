import time

def from_one_to_hundred():
    counter = 0
        
    while counter <= 100:
        print(counter)
        time.sleep(1)
        counter +=1

from_one_to_hundred()