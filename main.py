#import random
bordje = [" _ "] * 9
x = "|"
#deze input moet om een of andere reden iets gan veranderen in het bord 
def retarded_printen(bordje):
	print(bordje[0] + x + bordje[1] + x + bordje[2])
	print(bordje[3] + x + bordje[4] + x + bordje[5])
	print(bordje[6] + x + bordje[7] + x + bordje[8])
#deze var geeft aan of je hebt gewonnen
win = 0
while True:
	#input van x ding
	kruis = input('kies 1 - 9\n')
	kruis = int(kruis)
	#kijk hier is het makkeijker voor de retard om in te vullen
	kruis -= 1
	#het invullen van de x
	bordje[kruis] = "x"
	#pritnen van het bordje
	retarded_printen(bordje)
	#het checken of er 3 op een rij is, dit kon efficiënter
	if bordje[0] == "x" and bordje[1] == "x" and bordje[2] == "x":
		win = 1
	elif bordje[0] == "x" and bordje[3] == "x" and bordje[6] == "x":
		win = 1
	elif bordje[2] == "x" and bordje[5] == "x" and bordje[8] == "x":
		win = 1
	elif bordje[6] == "x" and bordje[7] == "x" and bordje[8] == "x":
		win = 1
	elif bordje[0] == "x" and bordje[4] == "x" and bordje[8] == "x":
		win = 1
	elif bordje[2] == "x" and bordje[4] == "x" and bordje[6] == "x":
		win = 1
	if win == 1:
		print('you won!')
		break
