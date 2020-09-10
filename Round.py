import Deck
import Player
import Card
import Computer

import copy

class Round:
	# current round number
	# __roundNum = None

	# # players
	# __human = None
	# __computer = None

	# # next player flag
	# __humanNext = True

	# # draw and discard piles
	# __drawPile = []
	# __discardPile = []

	################################
	########## constrctor ##########
	################################
	""" initalize the round and set up all cards """ 
	def __init__(self, inRoundNum, inHumanNext, inHuman, inComputer):
		# get values from arguments
		self.__roundNum = int(inRoundNum)
		self.__human = copy.deepcopy(inHuman)
		self.__computer = copy.deepcopy(inComputer)
		self.__humanNext = inHumanNext
		
		# only deal if the player's have no cards
		if len(inHuman.getHand()) == 0:
			# deal cards to players
			deck = Deck.Deck()
			deck.updateWildcards(self.__roundNum  + 2)
			for i in range(self.__roundNum + 2):
				self.__computer.addCard(deck.dealTopCard())
				self.__human.addCard(deck.dealTopCard())

			# move remaining cards to draw pile
			self.__drawPile = []
			topCard = deck.dealTopCard()
			while (len(deck.getCards()) > 0):
				self.__drawPile.insert(0, topCard)
				topCard = deck.dealTopCard()

			# move top card to discard pile
			self.__discardPile = []
			self.__discardPile.append(self.__drawPile[0])
			del self.__drawPile[0]


	################################
	########### accessors ##########
	################################
	""" return round number """
	def getRoundNumber(self):
		return self.__roundNum
	
	""" return human player """
	def getHuman(self):
		return self.__human

	""" return computer player """
	def getComputer(self):
		return self.__computer

	""" return draw pile """
	def getDrawPile(self):
		return self.__drawPile

	""" return discard pile """
	def getDiscardPile(self):
		return self.__discardPile

	""" return human player next """
	def getHumanNext(self):
		return self.__humanNext

	""" return Round as string """
	def __str__(self):
		# add round number
		result = "Round: " + str(self.__roundNum) + "\n\n"
		
		# add players
		result += "Computer:\n" + self.__computer.__str__() + "\n\n"
		result += "Human :\n" + self.__human.__str__() + "\n\n"

		# add card piles
		result += "Draw Pile: "
		for card in self.__drawPile:
			result += card.__str__() + " "
		result += "\n\n"
	
		result += "Discard Pile: "
		for card in self.__discardPile:
			result += card.__str__() + " "
		result += "\n\n"

		# add next player
		result += "Next Player: "
		if self.__humanNext is True:
			result += "Human"
		else:
			result += "Computer"

		return result

	################################
	########### mutators ###########
	################################	
	""" set the draw pile """
	def setDrawPile(self, inDrawPile):
		self.__drawPile = inDrawPile
		
	""" set the discard pile """
	def setDiscardPile(self, inDiscardPile):
		self.__discardPile = inDiscardPile

	""" set human next flag """
	def setHumanNext(self, inHumanNext):
		self.__humanNext = inHumanNext

	""" step the computer through its turn """
	def moveComputer(self, playerOut):
		# draw card
		self.__computer.drawCard(self.__drawPile, self.__discardPile, playerOut)
		
		# arrange cards
		self.__computer.assemble()

		# discard card
		self.__computer.discardCard(self.__discardPile)

		# update next player flag
		self.__humanNext = True

		# return the computer's best assembly
		return self.__computer.goOut()

	""" move a card from the given pile to the human's hand """
	def humanDrawCard(self, choice):
		if (choice == 0):
			self.__human.drawCard(self.__drawPile)
		else:
			self.__human.drawCard(self.__discardPile)

	""" move the given card to the discard pile """
	def humanDiscardCard(self, choice):
		self.__human.discardCard(self.__discardPile, choice)

		# update next player flag
		self.__humanNext = False

	""" return if the human goes out """
	def humanGoOut(self):
		return self.__human.goOut()

	""" start the next round """
	def nextRound(self):
		# increment round number
		self.__roundNum += 1

		# clear player's cards
		self.__human.clearHand()
		self.__computer.clearHand()

		# deal cards


	""" create a Round from a file 
	@help https://docs.python.org/3/tutorial/inputoutput.html """
	def fileToRound(self, filename):
		newRound = None

		# open file for reading
		with open(filename, 'r') as f:
			content = f.read()
			newRound = self.stringToRound(content)
			
			# file is automatically closed using "with"

		return newRound

	""" return a game from the given string """
	def stringToRound(self, string):
		# data to grab
		roundNum = 0
		computerScore = 0
		computerHand = []
		humanScore = 0
		humanHand = []
		drawPile = []
		discardPile = []
		humanNext = True

		# look through each line of the string
		lines = string.split("\n")
		for i in range(len(lines)):
			line = lines[i]

			# search for round number
			if line.find("Round: ") != -1:
				# get substring from after "Round: "
				roundNum = line[line.find("Round: ") + 7:]
			
			# search for computer
			if line.find("Computer:") != -1:
				for j in range(i, len(lines)):
					line = lines[j]
					# search for computer score
					if line.find("Score: ") != -1:
						computerScore = line[line.find("Score: ") + 7:]
					# search for computer hand
					if line.find("Hand: ") != -1:
						computerHand = self.stringToHand(line[line.find("Hand: ") + 6: ])
						break

			# search for human
			if line.find("Human:") != -1:
				for j in range(i, len(lines)):
					line = lines[j]
					# search for human score
					if line.find("Score: ") != -1:
						humanScore = line[line.find("Score: ") + 7:]
					# search for human hand
					if line.find("Hand: ") != -1:
						humanHand = self.stringToHand(line[line.find("Hand: ") + 6: ])
						break

			# search for draw pile
			if line.find("Draw Pile: ") != -1:
				drawPile = self.stringToHand(line[line.find("Draw Pile: ") + 11: ])

			# search for draw pile
			if line.find("Discard Pile: ") != -1:
				discardPile = self.stringToHand(line[line.find("Discard Pile: ") + 14: ])

			# search for next player
			if line.find("Next Player: ") != -1:
				if (line.find("Human") != -1):
					humanNext = True
				else:
					humanNext = False

		# print("Round number: " + roundNum)
		# print("Computer Score: " + computerScore.__str__())
		# string = ""
		# for card in computerHand:
		# 	string += card.__str__() + " "
		# print("Computer Hand: " + string)
		# print("Human Score: " + humanScore.__str__())
		# string = ""
		# for card in humanHand:
		# 	string += card.__str__() + " "
		# print("Human Hand: " + string)
		# string = ""
		# for card in drawPile:
		# 	string += card.__str__() + " "
		# print("Draw Pile: " + string)
		# string = ""
		# for card in discardPile:
		# 	string += card.__str__() + " "
		# print("Discard Pile: " + string)
		# print("Human Next: " + humanNext.__str__())

		# update wildcards in all hands
		for card in humanHand:
			card.updateWildcard(int(roundNum) + 2)
		for card in computerHand:
			card.updateWildcard(int(roundNum) + 2)
		for card in drawPile:
			card.updateWildcard(int(roundNum) + 2)
		for card in discardPile:
			card.updateWildcard(int(roundNum) + 2)

		human = Player.Player(humanScore, humanHand)
		computer = Computer.Computer(computerScore, computerHand)
		round = Round(roundNum, humanNext, human, computer)
		round.setDrawPile(drawPile)
		round.setDiscardPile(discardPile)
		return round

	""" return a hand of cards from the given string """
	def stringToHand(self, string):
		# trim whitespace
		string = string.strip()
		hand = []
		# go through every third index
		for i in range(0, len(string), 3):
			# build card from string
			face = string[i]
			if (face == "X"):
				face = 10
			if (face == "J"):
				face = 11
			if (face == "Q"):
				face = 12
			if (face == "K"):
				face = 13
			suit = string[i + 1]
			hand.append(Card.Card(int(face), suit, False))

		return hand