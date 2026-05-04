import time 

wait = 1
max_retreis = 5
attempts = 0

while attempts < max_retreis:
    print("Attempt is "+ str(attempts + 1) + " , " + "wait time is"+ str(wait))
    time.sleep(wait)
    attempts += 1
    wait *= 2

