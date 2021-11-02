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
current = list(current)

last = 10
while last > 0:
	print("Il vous reste", last, "coup(s) a jouer")
	print(current)
	print("Tapez une lettre")
	user_input = "/"
	while user_input and user_input[0].isalpha() == False:
		user_input = sys.stdin.readline()
	if user_input:
		char = user_input[0]
	else:
		char = "/"
	pos = word.find(char)
	while pos != -1:
		current[pos] = char
		pos = word.find(char)
	last -= 1
