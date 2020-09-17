#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def is_even_len(string):
	return len(string) % 2 == 0


def get_num_char(string, char):
	nombreChar = 0
	for c in string:
		nombreChar += 1 if c == char else 0
	return nombreChar


def get_first_part_of_name(name):
	first_part = name.split("-")[0]
	capitalized = first_part[0].upper() + first_part[1:].lower()
	return "Bonjour, " + capitalized


def get_random_sentence(animals, adjectives, fruits):
	animal_choisi = animals[random.randrange(len(animals))]
	adj_choisi = adjectives[random.randrange(len(adjectives))]
	fruit_choisi = fruits[random.randrange(len(fruits))]
	return "Aujourd’hui, j’ai vu un %s s’emparer d’un panier %s plein de %s." % (animal_choisi, adj_choisi, fruit_choisi)


if __name__ == "__main__":
	spam = "Bonjour!"
	parity = "pair" if is_even_len(spam) else "impair"
	print(f"Le nombre de caractère dans la chaine '{spam}' est {parity}.")

	eggs = "Hello, world!"
	print(f"Le nombre d'occurrence de l dans '{eggs}' est : {get_num_char(eggs, 'l')}.")

	parrot = "jean-marc"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon", "dragon", "homme")
	adjectives = ("rouge", "officiel", "lourd", "bleu", "multicolore", "brisé")
	fruits = ("pommes", "kiwis", "bananes", "bleuets")
	print(get_random_sentence(animals, adjectives, fruits))
