bordje = [" _ "] * 9
x = "|"
#deze input moet om een of andere reden iets gan veranderen in het bord 
x1 = int(input("typ 1-9 om shit te veranderen help \n"))
def retarded_printen(bordje):
	print(bordje[0] + x + bordje[1] + x + bordje[2])
	print(bordje[3] + x + bordje[4] + x + bordje[5])
	print(bordje[6] + x + bordje[7] + x + bordje[8])

def nadenken(xd):
	if xd == 1:
		bordje[0] = "x"
	elif xd == 2:
		bordje[1] = "x"
	elif xd == 3:
		bordje[2] = "x"
	elif xd == 4:
		bordje[3] = "x"
	elif xd == 5:
		bordje[4] = "x"
	elif xd == 6:
		bordje[5] = "x"
	elif xd == 7:
		bordje[6] = "x"
	elif xd == 8:
		bordje[7] = "x"
	elif xd == 9:
		bordje[8] = "x"
	else:
		print('jij retard dat is niet')
	retarded_printen(bordje)
nadenken(x1)
x2 = int(input("typ 1-9 om shit te veranderen help \n"))
nadenken(x2)
x3 = int(input("typ 1-9 om shit te veranderen help \n"))
nadenken(x3)
x4 = int(input("typ 1-9 om shit te veranderen help \n"))
nadenken(x4)
x5 = int(input("typ 1-9 om shit te veranderen help \n"))
nadenken(x5)
x6 = int(input("typ 1-9 om shit te veranderen help \n"))
nadenken(x6)
x7 = int(input("typ 1-9 om shit te veranderen help \n"))
nadenken(x7)
x8 = int(input("typ 1-9 om shit te veranderen help \n"))
nadenken(x8)
x9 = int(input("typ 1-9 om shit te veranderen help \n"))
nadenken(x9)
