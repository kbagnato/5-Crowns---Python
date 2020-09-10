import copy
#############################################
# Card, represents a playing card
# @author Kevin Bagnato
# @since 3/11/2020
#############################################

class Card:
	# initializer 
	def __init__(self, inFace, inSuit, inWild = False):
		"""
		Parameters
		----------
		inFace : int
			the face value of the card
		inSuit : char
			the suit of the card
		inWild : boolean, optional
			the wildcard status
		"""

		self.__face = copy.deepcopy(inFace)
		self.__suit = copy.deepcopy(inSuit)
		self.__wild = copy.deepcopy(inWild)
		
	#################################
	############ getters ############
	#################################
	""" return face """
	def getFace(self):
		return self.__face

	""" return suit """
	def getSuit(self):
		return self.__suit.__str__()
	
	""" return if card is joker """
	def isJoker(self):
		return (self.__face == 11 and (self.__suit == '1' or self.__suit == '2' or self.__suit == '3'))

	""" return if card is wildcard """
	def isWildcard(self):
		# if self.__wild:
		# 	print(self.__str__() + " is wild")
		return self.__wild

	""" return point value of card """
	def getValue(self):
		if (self.isJoker()):
			return 50
		
		if (self.__wild):
			return 20

		if (self.__face == "X"):
			return 10
		if (self.__face == "J"):
			return  11
		if (self.__face == "Q"):
			return  12
		if (self.__face == "K"):
			return 13

		return int(self.__face)

	################################
	########### mutators ###########
	################################
	""" update wildcard status to given face 
	@param inWildFace the current wildcard """
	def updateWildcard(self, inWildFace):
		if (int(self.__face) == inWildFace):
			self.__wild = True
		else:
			self.__wild = False

	""" return card as a string e.g. 3H or 5D* if round==3"""
	def __str__(self):
		result = ""

		face = self.__face
		if (face == 10):
			face = 'X'
		if (face == 11):
			face = 'J'
		if (face == 12):
			face = 'Q'
		if (face == 13):
			face = 'K'

		result += face.__str__() + self.__suit.__str__()
		# don't because it won't save properly
		# if (self.__wild):
			# result += "*"

		return result

	### override comparison operators ###
	# https://stackoverflow.com/questions/1227121/compare-object-instances-for-equality-by-their-attributes
	# """ override equals ( == ) """
	# def __eq__(self, other):
	# 	if not isinstance (other, Card):
	# 		return False
		
	# 	return self.__face == other.__face and self.__suit == other.__suit

	# """ override less than ( < ) """
	# def __lt__(self, other):
	# 	# order by suit
	# 	if (self.__suit < other.__suit):
	# 		return True
	# 	if (self.__suit > other.__suit):
	# 		return False
		
	# 	# then order by suit
	# 	return self.__face < other.__face
	# 	# # order by face
	# 	# if (self.__face < other.__face):
	# 	# 	return True
	# 	# if (self.__face > other.__face):
	# 	# 	return False
		
	# 	# # then order by suit
	# 	# return self.__suit < other.__suit
