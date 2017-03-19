'''
"Oral Exam Randomizer"

Notes:
-I have not done the math, but I cannot establish for certain that this method produces
or could produce the same number of permutations. 

-It's not really random, at least not given that the "random" module is not random 
enough for security purposes, but given the situation, it's good enough.

- This program is not "scalable" and does not take into account a situation in which
there is an odd number of students. However, as a "soluzione da due soldi", I can live content
with that which I have created. A future release or update could rectify this.

-This may not work for Python 3.x, but oh well, it did what I wanted.

'''


import random

#Student names
classList = ['Alyssa','Bishal', 'Courtney', 'Desmond', 'Pablo', 'Pedro', 'Brandon', 'Veronica', 'Adrianna', 'Tommy', 'Jackson', 'Jack', 'Luca', 'Maddison', 'Henry','Madeleine', 'Anthony','Lissette','Emma', 'Nikita']

#generate pairs


#This shuffles the above list of students. Is it truly n-factorial, where n is len(list)?
random.shuffle(classList)

#Now we divide the shuffled list into two halves. This is a bit of a cheat.
group1 = classList[:10]
group2 = classList[10:]

#We pair one half with another, and we add a random integer from 1 to 3 inclusive (scenario number)
for student1, student2 in zip(group1,group2):
	print student1 + ' and ' + student2 + " , Situation: " + str(random.randint(1,3))


