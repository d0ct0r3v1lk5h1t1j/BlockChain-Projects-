import random

#   reward of validatng a block ----
REWARD = 100

#   function to run Proof of stake consensus algorithm ----
def Consensus(valid_identities):

#   Total stake is the sum of coins of all the nodes who wish to compete for block creation ----
    totalstakes = 0

#   The algorithm randomly selects a node to validator, 
#   where is probability of a node getting selected is proportional to their stake in the system ----
    for x in valid_identities:
        totalstakes += x.stakes

#   Running a random function in the consensus process ----
    randomstake = random.randint(1,totalstakes)
    print(randomstake)

#   finding the segment where the random number generated lies in ----
    temptotal = 0
    for x in valid_identities:
        if randomstake > temptotal and randomstake <= temptotal + x.stakes:
            x.stakes += REWARD
            for y in valid_identities:
                print(y.name)
                print(y.stakes)
            print(x.name)
            return x.name
        else:
            temptotal += x.stakes

     