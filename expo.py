import time 

sec = 0 
print "Place the bomb here?\n\n>yes\n>no"
command = raw_input('>')

if command == "yes":
    while sec != 3:
        print ">>>>>>", sec
        time.sleep(0.8)
        sec += 1
    print "time is up"
    



