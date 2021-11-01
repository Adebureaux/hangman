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

print(word)

current = ""
len = len(word)
i = 0
while i < len:
	current += "_"
	i += 1

last = 10
while last > 0:
	print("Il vous reste", last, "coup(s) a jouer")
	print(current)
	user_input = "/"
	while user_input and user_input[0].isalpha() == False:
		user_input = sys.stdin.readline()
	user_input = list(user_input)
	current = list(current)
	pos = word.find(user_input[0])
	if pos != -1:
		current[pos] = user_input[0]
	print(pos);
	last -= 1
