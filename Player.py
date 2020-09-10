import Assembler

import copy

class Player:
	#################################
	########## contructor ##########
	#################################
	def __init__(self, inScore, inHand):
		self.__score = int(inScore)
		self.__hand = copy.deepcopy(inHand)

	#################################
	########### accessors ###########
	#################################
	""" return the player's hand """
	def getHand(self):
		return self.__hand

	""" return the player's score """
	def getScore(self):
		return self.__score

	""" return the sum value of the player's hand """
	def getPointsInHand(self):
		# count the total points in hand
		sum = 0
		for card in self.__hand:
			sum += card.getValue()
		return int(sum)

	""" return object type, score, and hand as a string """
	def __str__(self):
		# add score
		result = "\tScore: " + self.__score.__str__() + "\n"

		# add hand
		result += "\tHand: "
		for card in self.__hand:
			result += card.__str__() + " "
		
		return result

	#################################
	########### mutators ############
	#################################
	""" add a given card to the player's hand """
	def addCard(self, inCard):
		newCard = copy.deepcopy(inCard)
		self.__hand.append(newCard)

	def addToScore(self, score):
		self.__score += int(score)

	""" remove all cards from the player's hand """
	def clearHand(self):
		self.__hand.clear()

	""" set the hand to the given hand """
	def setHand(self, newHand):
		self.clearHand()
		for card in newHand:
			self.__hand.append(card)

	""" move the top card from drawPile to Player' hand """
	def drawCard(self, drawPile):
		self.addCard(drawPile[0])
		del drawPile[0]

	""" order the cards in the best assembly """
	def assemble(self):
		self.__hand = Assembler.Assembler.getBestHand(self.__hand)

	""" move the given card to the pile """
	def discardCard(self, discardPile, cardIdx):
		discardPile.insert(0, self.__hand[cardIdx])
		del self.__hand[cardIdx]

	""" return if the player goes out """
	def goOut(self):
		bestAss = Assembler.Assembler.getBestAssembly(Assembler.Assembler(self.__hand), Assembler.Assembler())
		if len(bestAss.getRemainingCards()) == 0:
			# player can assemble all cards - remove hand
			self.clearHand()
		
		# return the best attempt at assembling
		return bestAss
	
	#################################
	########### utililty ############
	#################################
	""" suggest a pile to draw from 
	end reason with a perion e/g/ "You should draw from the __ because {reason}
	draw pile is 0
	discard pile is 1
	error is -1 (both piles empty) """
	def helpDraw(self, drawPile, discardPile, lastMove):
		# can't draw from an empty pile
		if len(drawPile) == 0 and len(discardPile) == 0:
			reason = "both piles are empty."
			return -1, reason
		if len(drawPile) == 0:
			reason = "the draw pile is empty"
			return 1, reason
		if len(discardPile) == 0:
			reason = "the discard pile is empty."
			return 0, reason

		# player can only see the top of the discard pile
		discard = discardPile[0]

		# draw jokers
		if (discard.isJoker()):
			reason = "it is a Joker." 
			return 1, reason
		# draw wildcards
		if (discard.isWildcard()):
			reason = "it is a wildcard." 
			return 1, reason

		# check to see if discard pile can be used in an assembly
		"""
		count remaining cards of best assembly of current hand
		add discard pile to copy of hand
		count remaining cards of best assembly of copy of hand
		if counts are equal
			it is used in an assembly
		"""
		bestOfCurrentHand = Assembler.Assembler.getBestAssembly(Assembler.Assembler(self.__hand), Assembler.Assembler())
		
		# create temp hand with discard added to it
		handWithDiscard = copy.deepcopy(self.__hand)
		handWithDiscard.append(discard)
		# print("handWithDiscard: ", end="")
		# print(*handWithDiscard)
		
		bestOfHandWithDiscard = Assembler.Assembler.getBestAssembly(Assembler.Assembler(handWithDiscard), Assembler.Assembler())
		# print("best of hand with discard: " + bestOfHandWithDiscard.__str__())

		# see if more cards are assembled with card from discard pile
		if len(bestOfHandWithDiscard.getRemainingCards()) <= len(bestOfCurrentHand.getRemainingCards()):
			# print("bestOfCurentHand: " + bestOfCurrentHand.__str__())
			# print("bestOfHandWithDiscard: " + bestOfHandWithDiscard.__str__())
			
			# suggest discard pile
			return 1, "it can be used in an assembly."

		# check potential assemblies if it is not the last move
		# TODO this never seems to be true
		if lastMove is not True:
			# print("last move is not true")
			# see if the discard card can potentially be used with any remaining cards
			for card in bestOfCurrentHand.getRemainingCards():
				# see if book can be made
				if discard.getFace() == card.getFace():
					return 1, "you can potentially make a book with " + card.__str__()
				
				# see if run can be made
				if (discard.getSuit() == card.getSuit() and 
					(discard.getFace() - 2 >= card.getFace() and discard.getFace() + 2 <= card.getFace())):
					return 1, "you can potentially use in a run with " + card.__str__()

		# suggest draw pile because the discard pile cannot be used
		return 0, "the discard pile can not be used."

	""" suggest which card to drop  """
	def helpDiscard(self):
		# see if one car can be dropped and all others assembled
		for cardDroppedIdx in range(len(self.__hand)):
			shortHand = copy.deepcopy(self.__hand)
			del shortHand[cardDroppedIdx]

			# check if all other cards can be assembled
			if len(Assembler.Assembler.getBestAssembly(Assembler.Assembler(shortHand), Assembler.Assembler()).getRemainingCards()) == 0:
				reason = "all other cards can be assembled."
				return cardDroppedIdx, reason
		

		# look through remaining cards of current assembly - see if any are 'useful'
		bestOfCurentHand = Assembler.Assembler.getBestAssembly(Assembler.Assembler(copy.deepcopy(self.__hand)), Assembler.Assembler())

		# print("best of current hand: " + bestOfCurentHand.__str__())

		# loop through all remaining cards but the last
		for i in range(len(bestOfCurentHand.getRemainingCards())):
			
			# print("looking at " + bestOfCurentHand.getRemainingCards()[i].__str__())
			face = bestOfCurentHand.getRemainingCards()[i].getFace()
			suit = bestOfCurentHand.getRemainingCards()[i].getSuit()

			# loop though all cards
			useful = False

			# wilds/jokers always useful
			if bestOfCurentHand.getRemainingCards()[i].isJoker() or bestOfCurentHand.getRemainingCards()[i].isWildcard():
				useful = True

			# compare this card to all the others
			for j in range(len(bestOfCurentHand.getRemainingCards())):
				
				# print('comparing to: ' + bestOfCurentHand.getRemainingCards()[j].__str__())

				# check for potential book
				if bestOfCurentHand.getRemainingCards()[j].getFace() == face:
					useful = True

				# check for potential run
				if (bestOfCurentHand.getRemainingCards()[j].getSuit() == suit and
					(bestOfCurentHand.getRemainingCards()[j].getFace() > face - 2 or bestOfCurentHand.getRemainingCards()[j].getFace() < face + 2)):
					useful = True

			# suggest first card that is not useful
			if not useful:
				# i is mapped to the cards remaining after assembly - we need to find the same card index in the entire hand
				for search in range(len(self.__hand)):
					if bestOfCurentHand.getRemainingCards()[i].getSuit() == self.__hand[search].getSuit() and bestOfCurentHand.getRemainingCards()[i].getFace() == self.__hand[search].getFace():
						return search, "it is not close to an assembly."

		# all cards are useful - drop the highest value
		handCopy = copy.deepcopy(self.__hand)
		highestIdx = 0
		highestVal = handCopy[highestIdx].getValue()
		for i in range(len(handCopy)):
			if (not handCopy[i].isJoker() and not handCopy[i].isWildcard()) and handCopy[i].getValue() > highestVal:
				highestIdx = i
				highestVal = handCopy[i].getValue()
		return highestIdx, "it has the highest value of unused cards"	