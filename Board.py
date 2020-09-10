import Game
import Card
import Assembler
import copy
import random

# # https://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html

# from tkinter import Tk, Label, E, Button, SUNKEN,  Frame, Text, DISABLED, END, Toplevel, Entry, StringVar
from tkinter import *

class Board:
	################################
	####### class attrributes ######
	################################
	BTN_WIDTH = 15
	CARD_WIDTH = 9
	CARD_HEIGHT = 5
	PLAYER_CARD_AREA_WIDTH = CARD_WIDTH * 5
	CONSOLE_HEIGHT = 10
	BUTTON_PADDING = 10
	
	# current game
	__game = None

	# help is toggleable
	__helpEnabled = False

	def __init__(self, master):
		self.master = master
		master.title("5 Crowns by Kevin Bagnato")
		# master.configure(background="plum1")

		""" computer area """
		# computer frame
		self.computerFrame = Frame(self.master)
		self.computerFrame.config(background="tan2", padx=self.BUTTON_PADDING, pady=self.BUTTON_PADDING)
		self.computerFrame.grid()
		
		# computer score label
		self.computerScoreLabel = Label(self.computerFrame, text="Computer Score: TBD")
		self.computerScoreLabel.configure(background="chocolate1", relief=SUNKEN, width = self.PLAYER_CARD_AREA_WIDTH)
		self.computerScoreLabel.grid()

		# computer hand frame
		self.computerHandFrame = Frame(self.computerFrame)
		self.computerHandFrame.grid()

		""" human area """
		# human frame
		self.humanFrame = Frame(self.master)
		self.humanFrame.configure(background="pale green", relief=SUNKEN, padx=self.BUTTON_PADDING, pady=self.BUTTON_PADDING)
		self.humanFrame.grid()
		
		# human score label
		self.humanScoreLabel = Label(self.humanFrame, text = "Human Score: TBD")
		self.humanScoreLabel.configure(background="SeaGreen3", width = self.PLAYER_CARD_AREA_WIDTH, relief=SUNKEN)
		self.humanScoreLabel.grid()

		# human hand frame
		self.humanHandFrame = Frame(self.humanFrame)
		self.humanHandFrame.grid()

		# human hand buttons
		# humanHandBtn will be populated by the player's cards
		self.humanHandBtn = []
		for i in range(Game.Game.MAX_ROUND + 2):
			# make space for new element
			self.humanHandBtn.append(None)
			self.humanHandBtn[i] = Button(self.humanHandFrame, text="empty card")
			self.humanHandBtn[i].configure(width=self.CARD_WIDTH, height=self.CARD_HEIGHT)
			# place then hide the card buttons
			self.humanHandBtn[i].grid(row=0, column=i)
			self.humanHandBtn[i].grid_remove()

		""" draw pile area """
		self.drawPileFrame = Frame(self.master)
		self.drawPileFrame.configure(background="light sky blue", padx=self.BUTTON_PADDING, pady=self.BUTTON_PADDING)
		self.drawPileFrame.grid(row=0, column = 1)

		# draw pile header
		self.drawPileHeader = Label(self.drawPileFrame, text="Draw Pile")
		self.drawPileHeader.configure(background="deep sky blue", width=self.CARD_WIDTH, relief=SUNKEN)
		self.drawPileHeader.grid()
		
		# draw pile body
		self.drawPileBody = Frame(self.drawPileFrame)
		self.drawPileBody.grid()

		""" discard pile area """
		self.discardPileFrame = Frame(self.master)
		self.discardPileFrame.configure(background="light goldenrod", padx=self.BUTTON_PADDING, pady=self.BUTTON_PADDING)
		self.discardPileFrame.grid(row=1, column = 1)

		# discard pile header
		self.discardPileHeader = Label(self.discardPileFrame, text="Discard Pile")
		self.discardPileHeader.configure(background="gold", width=self.CARD_WIDTH, relief=SUNKEN)
		self.discardPileHeader.grid()
		
		# draw pile body
		self.discardPileBody = Frame(self.discardPileFrame)
		self.discardPileBody.grid()

		""" round stats area """
		# round stats area
		self.roundInfoFrame = Frame(self.master)
		self.roundInfoFrame.configure(background="pink2", padx = 5, pady = 5)
		self.roundInfoFrame.grid(row=2)

		# round number
		self.roundNumberLabel = Label(self.roundInfoFrame, text = "Round: TBD")
		self.roundNumberLabel.configure(background="pink2")
		self.roundNumberLabel.grid(row=0, column=0)

		# empty cell
		self.emptyCell = Label(self.roundInfoFrame, text="\t")
		self.emptyCell.configure(background="pink2")
		self.emptyCell.grid(row=0, column=1)

		# next player
		self.nextPlayerLabel = Label(self.roundInfoFrame, text="Next Player: TBD")
		self.nextPlayerLabel.configure(background="pink2")
		self.nextPlayerLabel.grid(row=0, column=3)

		""" input buttons """
		# buttons area
		self.buttonsFrame = Frame(self.master)
		self.buttonsFrame.configure(background="wheat3", padx = 5, pady = 5)
		self.buttonsFrame.grid(row = 3)
		
		# new game button
		self.btnNewGame = Button(self.buttonsFrame, text="New Game", command=self.newGame)
		self.btnNewGame.grid(row = 0, column = 0)
		
		# save button
		self.btnNewGame = Button(self.buttonsFrame, text="Save", command=self.createSavePopup)
		self.btnNewGame.grid(row = 0, column = 1)
		
		# load button
		self.btnNewGame = Button(self.buttonsFrame, text="Load", command=self.createLoadPopup)
		self.btnNewGame.grid(row = 0, column = 2)

		# quit button
		self.close_button = Button(self.buttonsFrame, text="Quit", command=master.quit)
		self.close_button.grid(row = 0, column = 3)
		
		# move button
		self.btnMove = Button(self.buttonsFrame, text="Move", command=self.move)
		self.btnMove.grid(row=1, column = 0)

		# go out button 
		self.btnGoOut = Button(self.buttonsFrame, text="Go Out", command=self.userGoOut)
		self.btnGoOut.grid(row = 1, column=1)

		# next round button
		self.btnNextRound = Button(self.buttonsFrame, text="Next Round", command=self.nextRound)
		self.btnNextRound.grid(row=1, column = 2)

		# help button
		self.btnHelp = Button(self.buttonsFrame, text="Help", command=self.help)
		self.btnHelp.grid(row=1, column=3)
		
		""" console (scrollable text box) """
		self.__console = Text(self.master, width=self.PLAYER_CARD_AREA_WIDTH + 5, height=self.CONSOLE_HEIGHT, state=DISABLED)
		self.__console.grid(row = 4, columnspan=2)
		self.consoleLog("Welcome to 5 Crowns by Kevin Bagnato")

		# add padding to all elements on grid
		for child in self.master.winfo_children():
			child.grid_configure(padx=5, pady=5)

	""" print a message to console """
	def consoleLog(self, string):
		# console must be able to be modified
		self.__console.config(state="normal")

		# add message to end of console
		self.__console.insert("end", string + "\n")

		# scroll to bottom
		self.__console.see("end")
		
		# user cannot modify the console
		self.__console.config(state="disabled")

	""" create a new instance of Game and call the coin toss """
	def newGame(self):
		self.consoleLog("Starting new game...")
		self.__game = Game.Game()
		self.btnMove["state"] = NORMAL
		self.btnNextRound["state"] = DISABLED
		self.updateBoard()
		self.coinToss()

	""" create a popup offering heads or tails """
	def coinToss(self):
		# create new window
		self.coinTossPopup = Toplevel()
		self.coinTossPopup.title("Coin Toss")

		# instructional text
		enterText = Label(self.coinTossPopup, text="Call heads or tails ")
		enterText.grid(row = 0, padx=15, pady=10)

		# heads button
		headsBtn = Button(self.coinTossPopup, text="Heads", command = lambda :self.callToss("heads"))
		headsBtn.grid(row=1, column=0, padx=15, pady=10)
		
		# tails button
		tailsBtn = Button(self.coinTossPopup, text="Tails", command = lambda :self.callToss("tails"))
		tailsBtn.grid(row=1, column=1, padx=15, pady=10)
		
	""" set the next player based on the given call """
	def callToss(self, call):
		# create random toss
		random.seed()
		toss = random.choice(["heads", "tails"])

		# check if user called it right and update the first player
		if toss == "heads" and call.find("heads") != -1:
			self.consoleLog("You called the toss!")
			self.__game.getRound().setHumanNext(True)
		else:
			self.consoleLog("You didn't predict the toss correctly.")
			self.__game.getRound().setHumanNext(False)
		
		# update board and clear popup
		self.updateBoard()
		self.coinTossPopup.destroy()

	""" add human's cards to frame as buttons """
	def move(self):
		# can only move if game has started
		if self.__game is None:
			self.consoleLog("Game has not started yet")
			return
		
		else:
			# check which player is next
			if self.__game.getRound().getHumanNext() == True:
				# human's turn
				if (self.__game.getWaitingForHumanDiscard() == False):
					# human needs to draw a card
					self.consoleLog("Click a pile to draw from")
				else:
					# human needs to discard a card
					self.consoleLog("Click a card to discard")
			else:
				# computer's turn - make move, store computer's best assembly, and print rational
				bestAss = self.__game.moveComputer(self.__game.getPlayerOut())
				self.consoleLog(self.__game.getRound().getComputer().getLastMoveDesc())
				self.updateBoard()

				# TODO if playerOut == True then new round
				if self.__game.getPlayerOut() == True:
					self.consoleLog("The computer's best assembly: " + bestAss.__str__())
					self.nextRound()

				# check if computer went out iff the human has not already
				if self.__game.getPlayerOut() == False:
					if len(bestAss.getRemainingCards()) == 0:
						# computer has go out
						self.consoleLog("The computer went out! " + bestAss.__str__())
						
						# enable flag for last round
						self.__game.setPlayerOut(True)

						self.consoleLog("You can make one more move.")
						self.btnMove["state"] = DISABLED
						self.updateBoard()
	
				# beginning of human's turn - offer help
				if (self.__helpEnabled):
					self.consoleLog(self.__game.helpHumanDraw(self.__game.getPlayerOut()))

	""" have the user draw the given card if the time is right """
	def userClickedPile(self, card):
		if self.__game.getRound().getHumanNext() == True and self.__game.getWaitingForHumanDiscard() == False:
			self.consoleLog("You picked up a " + card.__str__())
			# the game API requires an integer (0 for draw, 1 for discard)
			if card == self.__game.getRound().getDrawPile()[0]:
				self.__game.humanDraw(0)
			else:
				self.__game.humanDraw(1)
			self.updateBoard()

			# user next discards - offer help
			if (self.__helpEnabled):
				self.consoleLog(self.__game.helpHumanDiscard())

		else:
			self.consoleLog("hey now isn't the time")

	""" have the user discard the selected card if the time is right """
	def userClickedCard(self, card):
		if self.__game.getRound().getHumanNext() == True and self.__game.getWaitingForHumanDiscard() == True:
			self.consoleLog("You dropped a " + card.__str__())
			
			# the game API requires an integer (index of card in hand)
			for i in range(len(self.__game.getRound().getHuman().getHand())):
				if card == self.__game.getRound().getHuman().getHand()[i]:
					self.__game.humanDiscard(i)
					break
			self.updateBoard()


			# check if computer has already gone out
			if self.__game.getPlayerOut() == True:
				# human go out because they need to make their best move
				# end round
				self.consoleLog("the computer already went out\nnext round pls")
				self.btnNextRound["state"] = NORMAL
				# self.btnMove["state"] = DISABLED
				self.updateBoard()
			else:
				self.__game.setWaitingForHumanGoOut(True)

				# offer advice when the user can go out
				if self.__game.getPlayerOut() is not True and self.__game.humanCanGoOut() == True:
					self.consoleLog("You should go out now!")

				self.consoleLog("Now the computer needs to go.")
		else:
			# the user should not be discarding now
			self.consoleLog("hey now isn't the time")

	""" have the user go out if possible (tell game API to go out) """
	def userGoOut(self):
		# make sure game has started
		if self.__game is None:
			self.consoleLog("Can't go out if the game hasn't started.")
			return
		
		# make sure the other player has not already gone out
		if self.__game.getPlayerOut() is True:
			self.consoleLog("Can't go out if the other player already has.")
			return

		# player can only go out after discarding
		if self.__game.getWaitingForHumanGoOut() == False:
			self.consoleLog("Can't go out before you make your moves.")
			return

		# see if user can go out
		bestAssembly = self.__game.humanGoOut()
		if len(bestAssembly.getRemainingCards()) == 0:
			self.consoleLog("You went out!")
			self.updateBoard()
			
			# tell game a player has one out
			self.__game.setPlayerOut(True)
		else:
			# player cannot go out, take no action
			self.consoleLog("You can't go out now.")
		
		# print the player's best assembly
		self.consoleLog("Your best assembly: " + bestAssembly.__str__())

	""" create popup to get a filepath to save from """
	def createSavePopup(self):
		if self.__game is not None:
			# create new window
			self.savePopup = Toplevel()
			self.savePopup.title("Save Game")

			# instructional text
			enterText = Label(self.savePopup, text="Enter a full pathname: ")
			enterText.grid(row = 0, column=0)

			# user text entry
			filenameVar = StringVar()
			filenameEntry = Entry(self.savePopup, width=40, textvariable=filenameVar)
			filenameEntry.grid(row=0, column=1)

			# load button
			button = Button(self.savePopup, text="Save", command = lambda :self.save(filenameVar.get()))
			button.grid(column=1)#, sticky=E)

			# add padding to all
			# TODO This doesn't do the button
			# for child in self.loadPopup.winfo_children():
			# 	child.configure(padx=10, pady=10)
		else:
			self.consoleLog("Start a game before saving.")

	""" save the current game to the given file """
	def save(self, filename):
		print("saving " + filename)
		self.__game.save(filename)

	""" create popup to get a filepath to load from """
	def createLoadPopup(self):
		# create new window
		self.loadPopup = Toplevel()
		self.loadPopup.title("Load Game")

		# instructional text
		enterText = Label(self.loadPopup, text="Enter a full pathname: ")
		enterText.grid(row = 0, column=0)

		# user text entry
		filenameVar = StringVar()
		filenameEntry = Entry(self.loadPopup, width=40, textvariable=filenameVar)
		filenameEntry.grid(row=0, column=1)

		# load button
		button = Button(self.loadPopup, text="Load", command = lambda :self.load(filenameVar.get()))
		button.grid(column=1)#, sticky=E)

		# add padding to all
		# TODO This doesn't do the button
		# TODO this causes some Exceptions
		# for child in self.loadPopup.winfo_children():
		# 	child.configure(padx=10, pady=10)

	""" load game stats from a given file """
	def load(self, filename):
		# close popup
		self.loadPopup.destroy()
		self.consoleLog("Loading " + filename + "...")
		
		# create game if user has not yet started
		if self.__game is None:
			self.__game = Game.Game()
		
		# load game from file
		self.__game.load(filename)

		# set flags
		self.__game.setWaitingForHumanDiscard(False)
		self.__game.setWaitingForHumanGoOut(False)
		self.__game.setPlayerOut(False)

		self.btnMove["state"] = NORMAL

		self.updateBoard()

	""" begin the next round """
	def nextRound(self):
		if self.__game is not None:
			# print player's best assemblies
			humanBestAssembly = Assembler.Assembler.getBestAssembly(Assembler.Assembler(self.__game.getRound().getHuman().getHand()), Assembler.Assembler())
			self.consoleLog("Human: " + humanBestAssembly.__str__())
			computerBestAssembly = Assembler.Assembler.getBestAssembly(Assembler.Assembler(self.__game.getRound().getComputer().getHand()), Assembler.Assembler())
			self.consoleLog("Computer: " + computerBestAssembly.__str__())
						
			# remove assemblies from human's hand and add remaining cards score to running score 
			self.__game.getRound().getHuman().setHand(humanBestAssembly.getRemainingCards())
			self.__game.getRound().getHuman().addToScore(self.__game.getRound().getHuman().getPointsInHand())
			self.consoleLog("You earned " + self.__game.getRound().getHuman().getPointsInHand().__str__() + " points.")
			# do the same for computer
			self.__game.getRound().getComputer().setHand(computerBestAssembly.getRemainingCards())
			self.__game.getRound().getComputer().addToScore(self.__game.getRound().getComputer().getPointsInHand())
			self.consoleLog("The computer earned " + self.__game.getRound().getComputer().getPointsInHand().__str__() + " points.")
			self.updateBoard()
			# check if game should continue
			if self.__game.getRound().getRoundNumber() < self.__game.MAX_ROUND:
				# next round should be loaded
				self.consoleLog("Loading next round...")

				# player to go out begins next round
				humanStartsNextRound = self.__game.getRound().getHumanNext()
				self.__game.nextRound(humanStartsNextRound)
				self.btnMove["state"] = NORMAL
				self.btnNextRound["state"] = DISABLED
				self.updateBoard()
			else:
				# end of game - no more rounds
				self.consoleLog("That was the last round.")
				humanScore = self.__game.getRound().getHuman().getScore()
				computerScore = self.__game.getRound().getComputer().getScore()

				# print game winner
				if humanScore < computerScore:
					self.consoleLog("Congrats, you won the game!")
				elif computerScore < humanScore:
					self.consoleLog("The computer won. Better luck next time.")
				else:
					self.consoleLog("Amazing, it's a tie!")

				self.consoleLog("Please start or load a game.")
		else:
			self.consoleLog("Start a game before starting the next round.")

	""" call for help """
	def help(self):
		# toggle help mode
		if (self.__helpEnabled):
			self.consoleLog("Help disabled.")
			self.__helpEnabled = False
			self.btnHelp.configure(relief=RAISED)
		else:
			self.consoleLog("Help enabled.")
			self.__helpEnabled = True
			self.btnHelp.configure(relief=SUNKEN)

			# offer help when turned on
			if self.__game is None:
				self.consoleLog("Start a game to get help.")
			else:
				if self.__game.getRound().getHumanNext() == True:
					# human is up
					if self.__game.getWaitingForHumanDiscard() == False:
						# human needs to draw card
						self.consoleLog('lastmove: ' + self.__game.getPlayerOut().__str__())
						self.consoleLog(self.__game.helpHumanDraw(self.__game.getPlayerOut()))
					else:
						self.consoleLog(self.__game.helpHumanDiscard())
				else:
					self.consoleLog("The computer needs to go.")

	""" print the given card to the console
	used for testing """
	def printCard(self, card):
		self.consoleLog(card.__str__())

	""" update the board to match the model """
	def updateBoard(self):
		if self.__game is not None:
			# set round number
			self.roundNumberLabel.config(text="Round: " + self.__game.getRound().getRoundNumber().__str__())

			# set next player
			if self.__game.getRound().getHumanNext():
				self.nextPlayerLabel.config(text="Next Player: Human")
			else:
				self.nextPlayerLabel.config(text="Next Player: Computer")

			# update draw pile
			if len(self.__game.getRound().getDrawPile()) != 0:
				self.updatePile(self.drawPileBody, self.__game.getRound().getDrawPile()[0])
			else:
				self.updatePile(self.drawPileBody, Card.Card(0, '0'))

			# update discard pile
			if len(self.__game.getRound().getDiscardPile()) != 0:
				self.updatePile(self.discardPileBody, self.__game.getRound().getDiscardPile()[0])
			else:
				self.updatePile(self.discardPileBody, Card.Card(0, '0'))
			
			# update player's score
			self.humanScoreLabel.config(text="Human Score: " + self.__game.getRound().getHuman().getScore().__str__())
			self.computerScoreLabel.config(text="Computer Score: " + self.__game.getRound().getComputer().getScore().__str__())

			# update computer's hand
			self.updateComputerHand(self.__game.getRound().getComputer().getHand())

			# update human's hand
			for i in range(Game.Game.MAX_ROUND + 2):
				if i < len(self.__game.getRound().getHuman().getHand()):
					self.updateHumanCard(i, self.__game.getRound().getHuman().getHand()[i])
					self.humanHandBtn[i].grid()
				else:
					self.humanHandBtn[i].grid_remove()

	""" update the given pile to the given card
	clear the previous button, if any """
	def updatePile(self, pileBody, card):
		# remove buttons from body
		for child in pileBody.winfo_children():
			child.destroy()

		self.drawPileBtn = Button(pileBody, text=card.__str__(), command = lambda :self.userClickedPile(card))
		self.drawPileBtn.configure(width=self.CARD_WIDTH, height=self.CARD_HEIGHT)
		self.drawPileBtn.grid()

	""" update the human's card buttons """
	def updateHumanCard(self, idx, card):
		self.humanHandBtn[idx].config(text=card.__str__(), command = lambda : self.userClickedCard(card))

	""" update the given player's frame with buttons representing the given hand """
	def updateComputerHand(self, hand):
		# remove previous buttons
		for child in self.computerHandFrame.winfo_children():
			child.destroy()
		
		# create button for each card in hand
		for i in range(Game.Game.MAX_ROUND + 2):
			if i < len(hand):
				b = Button(self.computerHandFrame, text=hand[i].__str__())
				# b["state"] = DISABLED
				b.configure(fg="black", width = self.CARD_WIDTH, height = self.CARD_HEIGHT)
				b.grid(row=0, column=i)
			else:
				self.humanHandBtn[i].configure(text="N/A", command = lambda : self.consoleLog("N/A"))

# create self and start main loop
root = Tk()
board = Board(root)
root.mainloop()