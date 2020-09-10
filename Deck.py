#############################################
# Deck, represents a full set of cards (108)
# @author Kevin Bagnato
# @since 3/11/2020
#############################################

import Card
import random
import copy

class Deck:
	#################################
	########### constants ###########
	#################################
	# valid suits
	__SUITS = ('S', 'C', 'D', 'H', 'T')
	
	# lowest valid face 
	__MIN_FACE = 3

	# greatest valid face
	__MAX_FACE = 13

	#################################
	######## class variables ########
	#################################
	# cards in the deck
	# __cardVector = []

	""" create a card of each face and suit and add it to the deck """
	def __init__(self):
		# seed random number generator
		random.seed()
		
		self.__cardVector = []

		for i in range(0, 2):
			# add all ordinary cards to the deck
			for suit in self.__SUITS:
				for face in range(self.__MIN_FACE, self.__MAX_FACE + 1):
					# add card to list, none are wild
					self.__cardVector.append(Card.Card(face, suit, False))

			# add jokers
			for joker in range (1, 4):
				self.__cardVector.append(Card.Card(11, joker, False))

		# shuffle the deck
		random.shuffle(self.__cardVector)
		

	###################################
	############ accessors ############
	###################################
	""" return if the deck has no cards """
	def isEmpty(self):
		return len(self.__cardVector) == 0

	def getCards(self):
		return self.__cardVector

	##################################
	############ mutators ############
	##################################
	""" update all the card's wildcard status """
	def updateWildcards(self, inWildFace):
		for i in range(len(self.__cardVector)):
			self.__cardVector[i].updateWildcard(inWildFace)

		# for card in self.__cardVector:
		# 	card.updateWildcard(inWildFace)

	""" remove the top card from the deck and return it """
	def dealTopCard(self):
		# return empty card if deck is empty
		if (len(self.__cardVector) == 0):
			print("HEY there's no cards in this deck I can't deal")
			return Card.Card(0, '0', False)
		else:
			# get and remove first card
			# topCard = copy.deepcopy(self.__cardVector[0])
			topCard = self.__cardVector[0]
			del self.__cardVector[0]

			# return top card
			return topCard

	""" return the list of cards """
	def __str__(self):
		result = ""

		for card in self.__cardVector:
			result += card.__str__() + " "

		return result