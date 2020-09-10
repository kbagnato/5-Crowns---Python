import Card
import Deck
import Player
import Round
import Game
import Assembler
import Board

# # test card constructor
# card1 = Card.Card(3, 'S', False)
# print(card1)

# # test array of cards
# hand = []
# hand.append(Card.Card(3, 'S', False))
# hand.append(Card.Card(4, 'S', False))
# hand.append(Card.Card(5, 'S', False))
# print(*hand)

# # test __eq__
# card1Copy = Card.Card(3, 'S', False)
# if (card1 == card1Copy):
# 	print (card1.__str__() + " and " + card1Copy.__str__() + " are equal")
# else:
# 	print (card1.__str__() + " and " + card1Copy.__str__() + " are not equal")
# card2 = Card.Card(4, 'S', False)
# if (card1 == card2):
# 	print (card1.__str__() + " and " + card2.__str__() + " are equal")
# else:
# 	print (card1.__str__() + " and " + card2.__str__() + " are not equal")

# # test __lt__
# if (card1 < card1Copy):
# 	print (card1.__str__() + " < " + card1Copy.__str__())
# else:
# 	print (card1.__str__() + " !< " + card1Copy.__str__())

# if (card1 < card2):
# 	print (card1.__str__() + " < " + card2.__str__())
# else:
# 	print (card1.__str__() + " !< " + card2.__str__())

# if (card1 > card2):
# 	print (card1.__str__() + " > " + card2.__str__())
# else:
# 	print (card1.__str__() + " !> " + card2.__str__())

# # test __gt__ (not yet created)
# card3 = Card.Card(10, 'K', False)
# card4 = Card.Card(10, 'C', False)
# card5 = Card.Card(9, 'K', False)
# if (card3 > card4):
# 	print (card3.__str__() + " > " + card4.__str__())
# else:
# 	print (card3.__str__() + " !> " + card4.__str__())

# if (card3 > card5):
# 	print (card3.__str__() + " > " + card5.__str__())
# else:
# 	print (card3.__str__() + " !> " + card5.__str__())

# # test X J Q K
# print(Card.Card(10, 'T', False))
# print(Card.Card(11, 'T', False))
# print(Card.Card(12, 'T', False))
# print(Card.Card(13, 'T', False))

# # test wildcard
# if (card1.isWildcard()):
# 	print(card1.__str__() + " is wild")
# else:
# 	print(card1.__str__() + " is not wild")
	
# wild = Card.Card(13, 'T', True)
# if (wild.isWildcard()):
# 	print(wild.__str__() + " is wild")
# else:
# 	print(wild.__str__() + " is not wild")

# # test joker
# if (card1.isJoker()):
# 	print(card1.__str__() + " is s joker")
# else:
# 	print(card1.__str__() + " is not joker")
	
# joker = Card.Card(11, '1', False)
# if (joker.isJoker()):
# 	print(joker.__str__() + " is joker")
# else:
# 	print(joker.__str__() + " is not joker")
# notJoker = Card.Card(11, 'S', False)
# if (notJoker.isJoker()):
# 	print(notJoker.__str__() + " is joker")
# else:
# 	print(notJoker.__str__() + " is not joker")

###############################################

# test Deck
# deck = Deck.Deck()
# print(deck)

# # test shuffle
# deck.shuffle()
# print(deck)

# test deal card
# decktoDeal = Deck.Deck()
# print(decktoDeal)

# topCard = decktoDeal.dealCard()
# print("Top card: " + topCard.__str__())
# print(decktoDeal)

###############################################
# test CardDealer
# dealer = CardDealer.CardDealer()
# # print(dealer)

# # test dealCard
# nextCard = dealer.dealCard()

# drawPile = [nextCard, ]
# while (nextCard.getFace() != 0 and nextCard.getSuit() != '0'):
# 	drawPile.insert(0, nextCard)
# 	nextCard = dealer.dealCard()

# print("Draw pile: " + drawPile.__str__())

#######################################
# # test Player
# player = Player.Player()
# # print(player)

# # assign 5 cards to Player
# deck = Deck.Deck()
# for i in range(0, 5):
# 	player.addCard(deck.dealTopCard())
# print(player)

# # test getPointsInHand
# print(player.getPointsInHand())

# # test clearHand
# player.clearHand()
# print(player)

########################################
# test round
# roundNum = 1
# human = Player.Player(0, [])
# # print(hex(id(human)))
# computer = Player.Player(0, [])
# # print(hex(id(computer)))

# round = Round.Round(roundNum, True, human, computer)

# # print(round)

# # test load
# #round.fileToRound("C:\\Users\\kdawg\\Desktop\\Ramapo\\OPL\\5_Crowns_python\\serial\\case1.txt")

# # test save
# # round.save("C:\\Users\\kdawg\\Desktop\\Ramapo\\OPL\\5_Crowns_python\\serial\\test.txt")

# # test Game
# game = Game.Game()
# # print(game)

# # test load
# # game.load()

# # test play
# game.startGame()

# # test moveComputer
# print("Moving computer...")
# game.moveComputer()
# print(game.__str__())

# # test humanDrawCard
# print("Human is drawing card...")
# game.humanDrawCard(1)
# print(game)

# # test humanDiscardCard
# print("Human is discarding card...")
# game.humanDiscardCard(2)
# print(game)


# test Assembler sort by hand
# hand = []
# hand.append(Card.Card(5, 'D', False))
# hand.append(Card.Card(5, 'T', False))
# hand.append(Card.Card(11, '3', False))
# hand.append(Card.Card(11, '1', False))
# hand.append(Card.Card(3, 'S', False))
# hand.append(Card.Card(5, 'S', False))
# hand.append(Card.Card(11, 'S', False))
# hand.append(Card.Card(4, 'S', False))
# print("original hand: ")
# print(*hand)
# print()

# assembler = Assembler.Assembler()

# test sort by face
# sorted = assembler.sortHandByFace(hand)
# print("sorted by face: ")
# print(*sorted)
# print()

# # test sort by suit
# print("sorted by suit: ")
# sorted = assembler.sortHandBySuit(hand)
# print(*sorted)
# print()

# test isBook
# hand = []
# hand.append(Card.Card(11, 'S', False))
# hand.append(Card.Card(4, 'D', False))
# hand.append(Card.Card(4, 'S', False))
# print(*hand)
# print(assembler.isBook(hand))
# print() 

# hand = []
# hand.append(Card.Card(4, 'S', False))
# hand.append(Card.Card(4, 'D', False))
# hand.append(Card.Card(4, 'S', False))
# print(*hand)
# print(assembler.isBook(hand))
# print()


# hand.append(Card.Card(11, '1', False))
# print(*hand)
# print(assembler.isBook(hand))
# print()

# test isRun
assembler = Assembler.Assembler()

# hand = []
# hand.append(Card.Card(4, 'S', False))
# hand.append(Card.Card(4, 'D', False))
# hand.append(Card.Card(4, 'S', False))
# print(*hand)
# print(assembler.isRun(hand))
# print()

# hand.append(Card.Card(11, '1', False))
# print(*hand)
# print(assembler.isRun(hand))
# print()

# hand.append(Card.Card(11, 'D', True))
# print(*hand)
# print(assembler.isRun(hand))
# print()

# hand = []
# hand.append(Card.Card(3, 'S'))
# hand.append(Card.Card(4, 'S'))
# hand.append(Card.Card(4, 'S'))
# print(*hand)
# print(assembler.isRun(hand).__str__() + "\n")

# del hand[2]
# hand.append(Card.Card(5, 'S'))
# print(*hand)
# print(assembler.isRun(hand).__str__() + "\n")

# hand = []
# hand.append(Card.Card(4, 'S', True))
# hand.append(Card.Card(4, 'D'))
# hand.append(Card.Card(5, 'S'))
# print(*hand)
# print(assembler.isRun(hand))
# print()

# """ test getAllBooks """
# hand = []
# hand.append(Card.Card(4, 'D'))
# hand.append(Card.Card(7, 'D'))
# hand.append(Card.Card(4, 'T'))
# hand.append(Card.Card(4, 'H'))
# hand.append(Card.Card(4, 'D'))
# hand.append(Card.Card(3, 'D'))
# hand.append(Card.Card(6, 'D'))
# hand.append(Card.Card(3, 'T'))
# hand.append(Card.Card(3, 'S'))
# print(*hand)

# allAssemblies = assembler.getAllBooks(hand)
# for assembly in allAssemblies:
# 	print(*assembly)
# 	# for card in assembly:
# 	# 	print(card.__str__() + " ", end="")
# 	# print()


""" test getAllRuns """
# hand = []
# hand.append(Card.Card(4, 'D'))
# hand.append(Card.Card(5, 'D'))
# hand.append(Card.Card(6, 'D'))
# hand.append(Card.Card(9, 'T'))
# hand.append(Card.Card(10, 'T'))
# hand.append(Card.Card(11, 'T'))
# hand.append(Card.Card(12, 'T'))
# print(*hand)
# runs = assembler.getAllRuns(hand)
# for run in runs:
# 	print(*run)


""" test getAllAssemblies """
# hand = []
# hand.append(Card.Card(4, 'H'))
# hand.append(Card.Card(4, 'T'))
# hand.append(Card.Card(4, 'D'))
# hand.append(Card.Card(7, 'D'))
# hand.append(Card.Card(3, 'S'))
# hand.append(Card.Card(6, 'D'))
# hand.append(Card.Card(5, 'D'))


# hand.append(Card.Card(4, 'D'))
# hand.append(Card.Card(11, 'T'))
# hand.append(Card.Card(4, 'D'))
# hand.append(Card.Card(12, 'T'))
# hand.append(Card.Card(3, 'D'))
# hand.append(Card.Card(3, 'T'))
# # hand.append(Card.Card(5, 'D'))
# # hand.append(Card.Card(9, 'T'))
# # hand.append(Card.Card(6, 'D'))
# # hand.append(Card.Card(5, 'T'))
# # hand.append(Card.Card(10, 'T'))
# print(*hand)
# sorted = assembler.sortHandBySuit(hand)
# print (*sorted)

# runs = assembler.getAllRuns(hand)
# print("runs:")
# for ass in runs:
# 	print(*ass)

# asses = assembler.getAllAssemblies(hand)
# for ass in asses:
# 	print(*ass)


# print(assembler.__str__())
# tempAssembly = Assembler.Assembler(hand)
# print("trying to solve: " + tempAssembly.__str__())
# print()

# allAssemblies = assembler.getAllAssemblies(hand)

# print("all assemblies:")
# for ass in allAssemblies:
# 	print(*ass)
# 	for idk in ass:
# 		print(*idk)
# allAssemblies = assembler.getAllBooks(hand)
# for ass in allAssemblies:
# 	print(*ass)

# # """ test getBestAssembly """
# print(assembler.getBestAssembly(Assembler.Assembler(hand), Assembler.Assembler()).__str__())

# """ test getBestHand """
# print(*assembler.getBestHand(hand))

# game = Game.Game()
# game.startGame()

# # TODO this don't work
# hand = []
# hand.append(Card.Card(5, "T"))
# hand.append(Card.Card(7, "T"))
# hand.append(Card.Card(8, "T"))
# hand.append(Card.Card(4, "C", True))

# print(Assembler.Assembler.isRun(hand))

# game = Game.Game()
# game.load("C:\\Users\\kdawg\\Desktop\\Ramapo\\OPL\\5_Crowns_python\\serial\\case1.txt")
# game.play()

# hand = []
# hand.append(Card.Card(3, "T", True))
# hand.append(Card.Card(6, "H"))
# hand.append(Card.Card(12, "S"))
# hand.append(Card.Card(11, "3"))
# print(*Assembler.Assembler.getBestHand(hand))

# c = Controller.Controller()
# c.run()

# test assembler
# hand = []
# hand.append(Card.Card(3, 'D', True))
# hand.append(Card.Card(9, 'D'))
# hand.append(Card.Card(5, 'H'))
# hand.append(Card.Card(7, 'T'))
# print("hand = ", end="")
# print(*hand)

# print(Assembler.Assembler.getBestAssembly(Assembler.Assembler(hand), Assembler.Assembler()))

# hand = []
# hand.append(Card.Card(5, 'T'))
# hand.append(Card.Card(4, 'S', True))
# hand.append(Card.Card(7, 'T'))
# hand.append(Card.Card(8, 'T'))

# print(Assembler.Assembler.getBestAssembly(Assembler.Assembler(hand), Assembler.Assembler()).__str__())

# print ("Hand: ", end="")
# print(*hand)
# print(Assembler.Assembler.isRun(hand).__str__())

# draw = []
# draw.append(Card.Card(3, 'H', True))
# discard = []
# discard.append(Card.Card(6, 'D', True))

# p1 = Player.Player(0, hand)

# print("player: " + p1.__str__())
# print("draw: ", end="")
# print(*draw)
# print("discard: ", end="")
# print(*discard)

# choice, reason = p1.helpDraw(draw, discard)
# print("choice: " + choice.__str__())
# print("reason: " + reason)

# round = Round.Round(1, True, p1, Player.Player())
