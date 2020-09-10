import Player

class Computer(Player.Player):
	pass

	################################
	########## constructor #########
	################################
	def __init__(self, inScore, inHand):
		Player.Player.__init__(self, inScore, inHand)
		self.__lastMoveDesc = ""

	################################
	########### accessors ##########
	################################
	def getLastMoveDesc(self):
		return self.__lastMoveDesc

	################################
	########### mutators ###########
	################################
	""" draw card with logic """
	def drawCard(self, drawPile, discardPile, playerOut):
		choice, reason = super(Computer, self).helpDraw(drawPile, discardPile, playerOut)

		if choice == 0:
			self.__lastMoveDesc = "Computer is drawing from the draw pile because " + reason + " It's a " + drawPile[0].__str__() + ". "
			super(Computer, self).drawCard(drawPile)
		else:
			self.__lastMoveDesc = "Computer is drawing " + discardPile[0].__str__() + " from the discard pile becase " + reason
			super(Computer, self).drawCard(discardPile)

	""" discard card with logic """
	def discardCard(self, discardPile):
		choice, reason = super(Computer, self).helpDiscard()

		# self.__lastMoveDesc += "Computer is discarding " + super(Computer, self).__hand[choice].__str__() + " because " + reason
		self.__lastMoveDesc += "\nComputer is discarding " + self.getHand()[choice].__str__() + " because " + reason
		super(Computer, self).discardCard(discardPile, choice)