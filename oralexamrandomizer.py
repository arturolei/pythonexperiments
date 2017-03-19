import random

classList = ['Alyssa','Bishal', 'Courtney', 'Desmond', 'Pablo', 'Pedro', 'Brandon', 'Veronica', 'Adrianna', 'Tommy', 'Jackson', 'Jack', 'Luca', 'Maddison', 'Henry','Madeleine', 'Anthony','Lissette','Emma', 'Nikita']

#generate pairs

random.shuffle(classList)

group1 = classList[:10]
group2 = classList[10:]


for student1, student2 in zip(group1,group2):
	print student1 + ' and ' + student2 + " , Situation: " + str(random.randint(1,3))



'''
for item in pairArray:
	print item 
'''
