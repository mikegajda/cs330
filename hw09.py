import random
import numpy as np

# A human-resources manager called Imelda has the budget to interview 
# 20 applicants for a single job, one per day. After each interview, s
# he has to decide instantly whether to give the offer to today’s applicant 
# or continue interviewing. She evaluates each applicant as they come, 
# giving them a score. This score only depends on the applicant, not on whom she has seen before. 
# All scores will be distinct. Imelda wants to maximize the probability of getting the 
# applicant with the best score (including the ones she has not seen yet). She decides 
# on the following strategy: invite the applicants in random order. Interview the first 
# k and let them go. After this, choose the first applicant whose score is better than any 
# one previously seen (if none of them has such a score, choose the last one). Let T(k) be 
# the event that the applicant with highest score is chosen.

# (a) (10pts) Show that Pr(T(10)) ≥ 1/4.

# (b) (10pts) Show that Pr(T(9)) > Pr(T(10)).

def test():

	pop = range(1,20)
	#print(len(pop))

	samp1 = random.choice(pop)
	samp2 = random.choice(pop)
	samp3 = random.choice(pop)
	
	return samp1 == samp2 == samp3

count = 0


#test one million times
for i in range(1, 10000000):
	result = test()

	#print every one hundred thousand trials
	if i % 100000 == 0:
		print i
	if result == True:
		count += 1
#print the result		
print count