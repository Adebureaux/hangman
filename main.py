import sys
import os
import random
import string

with open("dico.txt", 'r') as dico:
	for dico_size, line in enumerate(dico):
		pass
pick = random.randint(0,dico_size)

i = -1
word = ""
with open("dico.txt", 'r') as dico:
	while i < pick:
		word = dico.readline()
		i += 1
word = word.rstrip()

current = ""
len = len(word)
i = 0
while i < len:
	current += "_"
	i += 1
current = list(current)

last = 20
while last > 0:
	print("Il vous reste", last, "coup(s) a jouer")
	print(' '.join(current))
	print("Tapez une lettre")
	user_input = "/"
	while user_input and user_input[0].isalpha() == False:
		user_input = sys.stdin.readline()
	if not user_input:
		user_input = "/"
	ret = 0
	pos = 0
	while ret != -1:
		ret = word.find(user_input[0].upper(), pos)
		if ret != -1:
			current[ret] = user_input[0].upper()
			pos += ret + 1
	if ''.join(current) == word:
		last = -1
	print()
	last -= 1
if last == -2:
	print(word)
	print("Bravo vous avez gagné !")
else:
	print("Vous avez perdu :(")
