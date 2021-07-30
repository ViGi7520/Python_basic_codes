import random

times = 0
score = 0
perdice = 0

while score < 100:                  # score or times can be interchaged
    dice = random.randrange(1, 6)
    score = dice + perdice
    perdice = score
    times +=1

    print( times, "attempts done. your score:", score)
print ('Total Attempt=', times)