import random
import numpy as np

def test():

	pop = range(1,257)
	#print(len(pop))

	samp1 = random.choice(pop)
	samp2 = random.choice(pop)
	samp3 = random.choice(pop)
	
	return samp1 == samp2 == samp3

count = 0

for i in range(1, 10000000):
	result = test()
	if i % 100000 == 0:
		print i
	if result == True:
		count += 1
print count