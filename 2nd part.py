import random

Ndays = 8
daysoff = range(1,25)
concurrent_tol = 3

while True:
    cntr = 0
    sample = random.sample(daysoff, Ndays)
    sample.sort()
    for i in range(1,Ndays-1):
        if abs(sample[i]-sample[i-1]) == 1:
            cntr +=1
        if abs(sample[i]-sample[i+1]) == 1:
            cntr +=1

    if cntr<concurrent_tol:
        print ("Found a good set of off-days :")
        print (sample)
        break
    else:
        print ("Didn't find a good set, trying again")
        print (sample)