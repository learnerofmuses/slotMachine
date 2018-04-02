import random

def lottery_draw():
	index = []

        for i in range(7):
                num = random.randint(0,9)
                index.append(num)
        return index

#IPO
#Input          #Processing             #Ouput
#n/a            randomly creates        returns the list
#               list between 0 - 9
#

