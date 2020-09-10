import Card
import copy

class Assembler:
	""" constructor """
	def __init__(self , inRemainingCards = [], inAssemblies = []):
		self.__assemblies = copy.deepcopy(inAssemblies)
		self.__remainingCards = copy.deepcopy(inRemainingCards)

	################################
	########### accessors ##########
	################################
	""" return the assembly's remaining cards """
	def getRemainingCards(self):
		return self.__remainingCards

	""" return the assembly's assemblies """
	def getAssemblies(self):
		return self.__assemblies

	""" return true if there are no cards in the assembly """
	def isEmpty(self):
		return len(self.__assemblies) == 0 and len(self.__remainingCards) == 0

	""" return the score of the remaining cards """
	def getScore(self):
		score = 0
		for card in self.__remainingCards:
			score += card.getValue()
		return score

	""" return the assembly as a string """
	def __str__(self):
		# add assemblies
		result = "Assemblies: "
		for ass in self.__assemblies:
			result += "["
			for card in ass:
				result += card.__str__() + " "
			result += "]; "
		
		# add remaining cards
		result += "Remaining cards: "
		for card in self.__remainingCards:
			result += card.__str__() + " "
		result += "; "
		result += "Score: " + self.getScore().__str__()
		return result

	################################
	########### mutators ###########
	################################
	""" move a given set of cards from the remaining cards to the list of assemblies """
	def removeAssembly(self, assembly):
		# add assembly to list
		self.__assemblies.append(assembly)

		# remove assembly from hand
		# look at each card in assembly
		for card in assembly:
			# look at each card in hand
			for i in range(len(self.__remainingCards)):
				if (self.__remainingCards[i].getFace() == card.getFace() and 
						self.__remainingCards[i].getSuit() == card.getSuit()):
					del self.__remainingCards[i]
					break

	################################
	########### utility ############
	################################
	""" return the hand in order of best assemblies then remaining cards """
	@staticmethod
	def getBestHand(inHand):
		# get best assembly from a copy of the given hand
		bestAssembly = Assembler.getBestAssembly(Assembler(copy.deepcopy(inHand)), Assembler())

		# hand to return
		result = []

		# add all cards from assemblies in order
		for ass in bestAssembly.getAssemblies():
			for card in ass:
				result.append(card)

		# add all remaining cards
		for card in bestAssembly.getRemainingCards():
			result.append(card)

		return result

	""" return the best possible assembly  """
	@staticmethod
	def getBestAssembly(inAssembly, cheapestChild):
		# print("self: " + inAssembly.__str__())
		
		# list of all possible assemblies that can be made from remaining cards
		allAssemblies = Assembler.getAllAssemblies(inAssembly.getRemainingCards())

		# return self if no children can be made
		if len(allAssemblies) == 0 or len(inAssembly.getRemainingCards()) == 0:
			# print("returning self")
			return inAssembly
		else:
			# create children nodes
			children = []

			# populate children with one assembly removed per child
			for assembly in allAssemblies:
				child = copy.deepcopy(inAssembly)
				child.removeAssembly(assembly)
				children.append(child)

			# find the cheapest child 
			for child in children:
				# print("\tchild: " + child.__str__())
				if (cheapestChild.isEmpty() or
						child.getBestAssembly(child, cheapestChild).getScore() < cheapestChild.getScore()):
					cheapestChild = child.getBestAssembly(child, cheapestChild)

		return cheapestChild

	@staticmethod
	def getAllAssemblies(inHand):
		# total list of assemblies
		allAssemblies = []

		# all runs and books
		books = Assembler.getAllBooks(inHand)
		runs = Assembler.getAllRuns(inHand)

		# print("books: ")
		for book in books:
			# print("\t", end="")
			# print(*book)
			allAssemblies.append(book)	

		# print("runs: ")
		for run in runs:
			# print("\t", end="")
			# print(*run)
			allAssemblies.append(run)

		# TODO remove duplicates
		result = []
		for ass in allAssemblies:
			if ass not in result:
				result.append(ass)
		return result
		
	""" return all possible books """
	@staticmethod
	def getAllBooks(inHand):
		allBooks = []

		# make an assembly starting with each card
		for startIdx in range(len(inHand)):
			hand = copy.deepcopy(inHand)
			possibleBook = []

			# start possible assembly with each card
			startCard = copy.deepcopy(hand[startIdx])
			possibleBook.append(startCard)
			del hand[startIdx]

			# books must have same face
			faceToMatch = possibleBook[0].getFace()

			# see if following cards can be used for book
			handFaceSort = Assembler.sortHandByFace(hand)
			for cmpIdx in range(len(handFaceSort)):
				if (handFaceSort[cmpIdx].isJoker() or 
						handFaceSort[cmpIdx].isWildcard() or 
						faceToMatch == handFaceSort[cmpIdx].getFace()):
					# add card to list
					possibleBook.append(handFaceSort[cmpIdx])

					# add valid book to return value
					if Assembler.isBook(possibleBook):
						allBooks.append(possibleBook)
						
						# avoid shallow copies
						possibleBook = copy.deepcopy(possibleBook)
			
		result = []
		for book in allBooks:
			if book not in result:
				result.append(book)
		
		return allBooks

	
		# # remove duplicates
		# TODO This still doesn't work 
		# b = list()
		# for sublist in allBooks:
		# 	if sublist not in b:
		# 		b.append(sublist)
		# return b

	
		# for search in range(len(allBooks) - 1):
		# 	for i in range(search + 1, len(allBooks)):
		# 		if i >= len(allBooks):
		# 			break
		# 		print("i=" + i.__str__() + " ", end="")
		# 		print(*allBooks[i])

		# 		lhs = Assembler.sortHandByFace(allBooks[search])
		# 		rhs = Assembler.sortHandByFace(allBooks[i])

		# 		print("lhs: ", end="")
		# 		print(*lhs)
		# 		print("rhs: ", end="")
		# 		print(*rhs)

		# 		if Assembler.sameHand(lhs, rhs).__str__():
		# 			print("deleteing " + i.__str__())
		# 			del allBooks[i]
		# 			i -= 1
			
		# return allBooks

	""" return all possible runs """
	@staticmethod
	def getAllRuns(inHand):
		# print("looking at hand: ", end="")
		# print(*inHand)

		# total list of runs
		allRuns = []

		handSuitSorted = Assembler.sortHandBySuit(inHand)
		# print("hand sorted: ", end="")
		# print(*handSuitSorted)

		# try to make a run from each card
		for startIdx in range(len(handSuitSorted)):
			# make copy of hand with one card in possibleRun
			handShort = copy.deepcopy(handSuitSorted)
			startCard = copy.deepcopy(handShort[startIdx])
			del handShort[startIdx]
			
			# print("handShort: ", end="")
			# print(*handShort)

			# cards with matching suit, following faces (to be validated)
			possibleRun = []
			possibleRun.append(startCard)

			# store face and suit
			face = int(startCard.getFace())
			suit = startCard.getSuit()

			# print("starting with: " + startCard.__str__())

			# see if following cards can be used for runs
			for cmpIdx in range(len(handShort)):
				# print("face = " + face + " type: ", end="")
				# print(type(face))
				
				# check for possible run
				if (handShort[cmpIdx].isJoker() or
						handShort[cmpIdx].isWildcard() or
						(suit == handShort[cmpIdx].getSuit() and
						face + 1 == handShort[cmpIdx].getFace())):
					# add cards with matching suit in face range to possible run
					possibleRun.append(handShort[cmpIdx])

					# looking for next face now
					face += 1

					# add valid books to return value
					if Assembler.isRun(possibleRun):
						allRuns.append(possibleRun)

						# create copy of self
						possibleRun = copy.deepcopy(possibleRun)
		
		return allRuns

	""" return if the given hand is a valid book """
	@staticmethod
	def isBook(hand):
		# books must be 3 cards or longer
		if (len(hand) < 3):
			return False

		result = True
		
		# set face to match
		face = hand[0].getFace()

		# check if all cards have the same face
		for i in range(len(hand)):
			if (hand[i].getFace() != face):
				# jokers and wilds continue book
				if (hand[i].isJoker() or hand[i].isWildcard()):
					continue
				else:
					result = False
					break
		return result

	""" return if the given hand is a valid run """
	@staticmethod
	def isRun(inHand):
		# run must be 3 or more cards long
		if len(inHand) < 3:
			return False

		# sort by suit, face
		# count/remove all jokers/wilcards
		# if run is about to break, try to use joker/wildcard if it's not possible		
		
		hand = Assembler.sortHandBySuit(copy.deepcopy(inHand))
		
		# count and remove all jokers/wildcards
		totalWilds = 0
		i = 0
		while i < len(hand):
			# if current card is joker
			if hand[i].isJoker() or hand[i].isWildcard():
				totalWilds += 1
				del hand[i]
				i -= 1
			i += 1

		# print("hand after removal: ", end="")
		# print(*hand)
			
		# all joker/wild is cool
		if len(inHand) <= 1:
			return True
		
		# cards must have matching suit
		suitToMatch = hand[0].getSuit()

		# track current face to determine if next card follows
		currentFace = hand[0].getFace()

		# look at each card in hand
		for i in range(len(hand)):
			# check if card is valid
			if not (hand[i].getSuit() == suitToMatch and hand[i].getFace() + 1 != currentFace):
				# check if wildcard can be used in place
				if totalWilds > 0:
					# print("using a wild")
					totalWilds -= 1
					# print("stepping back to check the same card")
					i -= 1
				else:
					return False

			# look for next face
			currentFace += 1
		
		# no cards failed
		return True

	""" sort given hand by face then suit """
	@staticmethod
	def sortHandByFace(inHand):
		hand = copy.deepcopy(inHand)

		# bobble sort by face
		for i in range(len(hand) - 1):
			for j in range(len(hand) - i - 1):
				# swaps cards if current card is greater than next card or current Card is joker
				if hand[j].getFace() > hand[j + 1].getFace() or hand[j].isJoker():
					# https://stackoverflow.com/questions/14836228/is-there-a-standardized-method-to-swap-two-variables-in-python[]
					hand[j], hand[j + 1] = hand[j + 1], hand[j]

		# sort jokers
		hand = Assembler.sortJokers(hand)
		return hand
	
	""" sort given hand by suit then face """
	@staticmethod
	def sortHandBySuit(inHand):
		hand = copy.deepcopy(inHand)

		# TODO this does not put jokers at the end

		# bobble sort by suit
		for i in range(len(hand) - 1):
			for j in range(len(hand) - i - 1):
				# swap Cards if
				# current Card is Joker
				# OR current Card suit is greater than next Card suit
				# OR suits are same and current Card face is greater than next Card face
				if hand[j].isJoker():
					hand[j], hand[j + 1] = hand[j + 1], hand[j]
				elif hand[j].getSuit() > hand[j + 1].getSuit():
					hand[j], hand[j + 1] = hand[j + 1], hand[j]
				elif (hand[j].getSuit() == hand[j + 1].getSuit()) and (hand[j].getFace() > hand[j + 1].getFace()):
					hand[j], hand[j + 1] = hand[j + 1], hand[j]
					# https://stackoverflow.com/questions/14836228/is-there-a-standardized-method-to-swap-two-variables-in-python[]
		
		# sort jokers
		hand = Assembler.sortJokers(hand)
		return hand
	
	""" move jokers to the end of the hand """
	@staticmethod
	def sortJokers(inHand):
		hand = copy.deepcopy(inHand)

		# print("sorting jokers for hand")
		# print(*hand)

		# bubble sort jokers by suit
		for i in range(len(hand) - 1):
			for j in range(len(hand) - i - 1):
				# if both cards are jokers then sort by suit
				if hand[j].isJoker() and hand[j + 1].isJoker() and hand[j].getSuit() > hand[j + 1].getSuit():
					print("swapping " + hand[j].__str__() + " and " + hand[j+1].__str__())
					# swap cards
					hand[j], hand[j + 1] = hand[j + 1], hand[j]

		return hand

	""" return if the given hands have matching cards """
	@staticmethod
	def sameHand(leftHand, rightHand):
		# hands must have same length
		if len(leftHand) != len(rightHand):
			return False

		# compare hands one card at a time
		for i in range(len(leftHand)):
			# check if cards do not match
			if leftHand[i] != leftHand[i]:
				return False

		# all cards matched
		return True