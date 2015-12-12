import random
WORDS1 = ["Automated","Table-Based", "Dynamic","Generalized", "LL", "Relaxed", "GLR", "AGLR", "BRNGLR", "RINGLR","information system"]
WORDS2 = ["transformation","language support", "abstract parsing", "support parsing", "reengineering"]
WORDS3 = ["of", "in", "with"]  
WORDS4 = ["dynamic SQL queries","integrated development environment", "String-Embedded Languages", "Regular Approximations ", "information system reengineering"]
print("Welcome to YC title generator")
maxln = min([len(WORDS1),len(WORDS2),len(WORDS4)])
number = int(input("Please enter how powerful is your work (< " + str(maxln) +"): "))
while number > maxln:
	number = int(input("Please enter how powerful is your work (<" + str(maxln) +"): "))
name = ""
for i in range(0, number):
	position1 = random.randrange(len(WORDS1))
	position2 = random.randrange(len(WORDS2))
	position3 = random.randrange(len(WORDS3))
	position4 = random.randrange(len(WORDS4))
	name += WORDS1[position1] + " " + WORDS2[position2]+ " "+WORDS3[position3] + " "+ WORDS4[position4]
	if i != (number - 1):
		name += " and "
	del WORDS1[position1]
	del WORDS2[position2]
	del WORDS4[position4]
print("Greate title for your work: ", name)
