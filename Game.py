import Player
import Round
import Computer
import Assembler

import random

class Game:
	MAX_ROUND = 11

	################################
	########## constructor #########
	################################
	def __init__(self):
		# players live in game to keep running score between rounds
		self.__human = Player.Player(0, [])
		self.__computer = Computer.Computer(0, [])

		# create round 1
		self.__round = Round.Round(1, True, self.__human, self.__computer)
		
		# gamestate flags
		# true after the user has picked up a card and before the user discards
		self.__waitingForHumanDiscard = False

		# true after the user has put down a card and before the computer moves
		self.__waitingForHumanGoOut = False
		
		# true when a player has successfully gone out
		self.__playerOut = False
		
	################################
	########### accessors ##########
	################################
	""" return the game as a string """
	def __str__(self):
		return self.__round.__str__()

	""" return the current round """
	def getRound(self):
		return self.__round

	""" return the waiting for human discard flag """
	def getWaitingForHumanDiscard(self):
		return self.__waitingForHumanDiscard

	def setWaitingForHumanDiscard(self, flag):
		self.__waitingForHumanDiscard = flag

	""" return the waiting for human to go out flag """
	def getWaitingForHumanGoOut(self):
		return self.__waitingForHumanGoOut

	""" set the waiting for human to go out flag """
	def setWaitingForHumanGoOut(self, flag):
		self.__waitingForHumanGoOut = flag

	""" return the player is currently out flag """
	def getPlayerOut(self):
		return self.__playerOut

	""" set the  player is currently out flag """
	def setPlayerOut(self, flag):
		self.__playerOut = flag
	
	################################
	########### mutators ###########
	################################	
	""" get a file from the user and load the given file """
	def load(self, filename):
		# filename = input("Enter a full pathname (including filename): ")
		newRound = self.__round.fileToRound(filename)
		self.__round = newRound
		self.__human = self.__round.getHuman()
		self.__computer = self.__round.getComputer()

		# print("Loaded new round.")
		# print(self)

	""" save the game to a given location """
	def save(self, filename):
		f = open(filename, 'w')
		f.write(self.__str__())
		f.close()

	""" get the call from the user
	no longer used, can be called from start.py for testing
	def coinToss(self):
		# user input
		call = input("Heads / Tails: ").lower()
		# random flip
		toss = random.randint(0, 1)
		print("Toss: ", end="")
		if toss == 0:
			print("Heads")
		else:
			print("Tails")
		# return correct call
		return toss == 0 and call.find("head") != -1
	"""
	""" begin the game
	no longer used, can be called from start.py for testing
	def startGame(self):
		self.__round.setHumanNext(self.coinToss())
		print(self)

		# begin main loop
		self.play()
	"""
	""" loop through rounds until the end of the game 
	no longer used, can be called from start.py for testing
	def play(self):
		# make one move at a time until a one player goes out
		while (not self.__playerOut):
			if self.__round.getHumanNext() == True:
				if (not self.__waitingForHumanDiscard):
					# ask user what pile to draw from
					choice = input("Draw or Discard Pile (0 / 1): ")
					self.humanDrawCard(int(choice))
					self.__waitingForHumanDiscard = True
				else:
					# ask user which card to discard
					choice = input("Which card (0 - " + (len(self.__round.getHuman().getHand()) - 1).__str__() + "): ")
					self.humanDiscardCard(int(choice))

					# ask user to go out
					choice = input("Go Out? (Yes / No): ")
					if choice.lower().find("yes") != -1:
						self.__playerOut = self.humanGoOut()
						
					# turn off flag for human's turn
					self.__waitingForHumanDiscard = False
			else:
				# computer plays entire turn
				self.__playerOut = self.moveComputer()
				
				# print computer's reasoning
				print(self.__round.getComputer().getLastMoveDesc())

			# print round info between moves
			print(self.__str__())

		print("Someone has gone out!")
		# store shallow copy of winner
		if self.__round.getHumanNext():
			winner = self.__round.getComputer()
		else:
			winner = self.__round.getHuman()
	
		# print winning assembly
		winnerAssemblies = Assembler.Assembler.getBestAssembly(Assembler.Assembler(winner.getHand()), Assembler.Assembler()).getAssemblies()
		print("Round winner's assemblies: ", end="")
		for ass in winnerAssemblies:
			print(*ass)

		# one player has gone out
		if (self.__round.getHumanNext):
			print("damn you lost the round. make one more move")
		else:
			print("aight son! the computer is making one more move")
		
		# make last move
		if self.__round.getHumanNext() == True:
			# ask user what pile to draw from
			choice = input("Draw or Discard Pile (0 / 1): ")
			self.humanDrawCard(int(choice))
			# ask user which card to discard
			choice = input("Which card (0 - " + len(self.__round.getHuman().getHand()).__str__() + "): ")
			self.humanDiscardCard(int(choice))
		else:
			# computer plays entire turn
			self.moveComputer()
			# print computer's reasoning
			print(self.__round.getComputer().getLastMoveDesc())

		# print round after last move
		print(self)

		# print loser's assemblies
		if (self.__round.getHumanNext() == True):
			loserAssemblies = Assembler.Assembler.getBestAssembly(Assembler.Assembler(self.__round.getComputer().getHand()), Assembler.Assembler()).getAssemblies()
			print("Loser's assemblies: ", end="")
			for ass in loserAssemblies:
				print(*ass)
		else:
			loserAssemblies = Assembler.Assembler.getBestAssembly(Assembler.Assembler(self.__round.getHuman().getHand()), Assembler.Assembler()).getAssemblies()
			print("Loser's assemblies: ", end="")
			for ass in loserAssemblies:
				print(*ass)
	"""

	################################
	###### API for Controller ######
	################################
	""" have human draw from given pile
	choice == 0 means drawPile
	choice == 1 means discardPile """
	def humanDraw(self, choice):
		# human draw
		self.humanDrawCard(int(choice))
		# set flag to now discard
		self.__waitingForHumanDiscard = True
	
	""" have human discard a given card
	choice == the index in hand """
	def humanDiscard(self, choice):
		# human discard given card
		self.humanDiscardCard(int(choice))
		# turn off flag for discarding
		self.__waitingForHumanDiscard = False 
		
		# set flag to allow go out
		self.__waitingForHumanGoOut = True

	""" step the computer through its turn """
	def moveComputer(self, playerOut):
		# human can't move during computer's turn
		self.__waitingForHumanGoOut = False

		# move computer, store if it went out
		bestAssembly = self.__round.moveComputer(playerOut)
		
		# human waits to draw after computer moves
		self.__waitingForHumanDiscard = False
		return bestAssembly

	""" return a helpful message for the user drawing a card """
	def helpHumanDraw(self, lastMove):
		draw = self.__round.getDrawPile()
		discard = self.__round.getDiscardPile()

		choice, reason = self.__round.getHuman().helpDraw(draw, discard, lastMove)

		if choice == 0:
			return "You should draw from the draw pile because " + reason
		else:
			return "You should draw from the discard pile because " + reason

	def helpHumanDiscard(self):
		choice, reason = self.__round.getHuman().helpDiscard()
		return "You should drop the " + self.__round.getHuman().getHand()[choice].__str__() + " because " + reason

	""" step the human through drawing a card """
	def humanDrawCard(self, choice):
		self.__round.humanDrawCard(choice)

	""" step the human through discarding a card """
	def humanDiscardCard(self, choice):
		self.__round.humanDiscardCard(choice)

	""" return if the human went out """
	def humanGoOut(self):
		return self.__round.humanGoOut()

	""" return if the human can go out """
	def humanCanGoOut(self):
		bestAss = Assembler.Assembler.getBestAssembly(Assembler.Assembler(self.getRound().getHuman().getHand()), Assembler.Assembler())
		
		if len(bestAss.getRemainingCards()) == 0:
			print("HUMAN SHOULD GO OUT: " + bestAss.__str__()) 
			return True
		else:
			return False

	""" load the next round """
	def nextRound(self, humanBeginsRound):
		if (self.__round.getRoundNumber() <= self.MAX_ROUND):
			nextRoundNum = self.__round.getRoundNumber() + 1

			# clear player's hands
			self.__human.clearHand()
			self.__computer.clearHand()

			# create new round object
			del self.__round
			self.__round = Round.Round(nextRoundNum, humanBeginsRound, self.__human, self.__computer)

			# disable all flags
			self.__waitingForHumanDiscard = False
			self.__waitingForHumanGoOut = False
			self.__playerOut = False
			return True
		else:
			return False