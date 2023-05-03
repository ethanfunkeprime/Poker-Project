from PyQt5.QtWidgets import *
from view import *
import random

master_deck = [["ace", "clubs", "assets/Clubs 1.png", 14],
               ["deuce", "clubs", "assets/Clubs 2.png", 2],
               ["three", "clubs", "assets/Clubs 3.png", 3],
               ["four", "clubs", "assets/Clubs 4.png", 4],
               ["five", "clubs", "assets/Clubs 5.png", 5],
               ["six", "clubs", "assets/Clubs 6.png", 6],
               ["seven", "clubs", "assets/Clubs 7.png", 7],
               ["eight", "clubs", "assets/Clubs 8.png", 8],
               ["nine", "clubs", "assets/Clubs 9.png", 9],
               ["ten", "clubs", "assets/Clubs 10.png", 10],
               ["jack", "clubs", "assets/Clubs 11.png", 11],
               ["queen", "clubs", "assets/Clubs 12.png", 12],
               ["king", "clubs", "assets/Clubs 13.png", 13],
               ["ace", "diamonds", "assets/Diamond 1.png", 14],
               ["deuce", "diamonds", "assets/Diamond 2.png", 2],
               ["three", "diamonds", "assets/Diamond 3.png", 3],
               ["four", "diamonds", "assets/Diamond 4.png", 4],
               ["five", "diamonds", "assets/Diamond 5.png", 5],
               ["six", "diamonds", "assets/Diamond 6.png", 6],
               ["seven", "diamonds", "assets/Diamond 7.png", 7],
               ["eight", "diamonds", "assets/Diamond 8.png", 8],
               ["nine", "diamonds", "assets/Diamond 9.png", 9],
               ["ten", "diamonds", "assets/Diamond 10.png", 10],
               ["jack", "diamonds", "assets/Diamond 11.png", 11],
               ["queen", "diamonds", "assets/Diamond 12.png", 12],
               ["king", "diamonds", "assets/Diamond 13.png", 13],
               ["ace", "hearts", "assets/Hearts 1.png", 14],
               ["deuce", "hearts", "assets/Hearts 2.png", 2],
               ["three", "hearts", "assets/Hearts 3.png", 3],
               ["four", "hearts", "assets/Hearts 4.png", 4],
               ["five", "hearts", "assets/Hearts 5.png", 5],
               ["six", "hearts", "assets/Hearts 6.png", 6],
               ["seven", "hearts", "assets/Hearts 7.png", 7],
               ["eight", "hearts", "assets/Hearts 8.png", 8],
               ["nine", "hearts", "assets/Hearts 9.png", 9],
               ["ten", "hearts", "assets/Hearts 10.png", 10],
               ["jack", "hearts", "assets/Hearts 11.png", 11],
               ["queen", "hearts", "assets/Hearts 12.png", 12],
               ["king", "hearts", "assets/Hearts 13.png", 13],
               ["ace", "spades", "assets/Spades 1.png", 14],
               ["deuce", "spades", "assets/Spades 2.png", 2],
               ["three", "spades", "assets/Spades 3.png", 3],
               ["four", "spades", "assets/Spades 4.png", 4],
               ["five", "spades", "assets/Spades 5.png", 5],
               ["six", "spades", "assets/Spades 6.png", 6],
               ["seven", "spades", "assets/Spades 7.png", 7],
               ["eight", "spades", "assets/Spades 8.png", 8],
               ["nine", "spades", "assets/Spades 9.png", 9],
               ["ten", "spades", "assets/Spades 10.png", 10],
               ["jack", "spades", "assets/Spades 11.png", 11],
               ["queen", "spades", "assets/Spades 12.png", 12],
               ["king", "spades", "assets/Spades 13.png", 13]]

class Controller(QMainWindow, Ui_poker_window):
    player_hand = []
    computer_hand = []
    working_deck = master_deck[:]
    random.shuffle(working_deck)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.deal_button.clicked.connect(lambda: self.deal())
        self.show_button.clicked.connect(lambda: self.show())
        self.clear_button.clicked.connect(lambda: self.reset())

# This function deals cards to both the player and the computer and changes the cards in the player's display accordingly.
    def deal(self):
        if len(self.working_deck) >= 10:
            for i in range(5):
                self.computer_hand.append(self.working_deck.pop())
                self.player_hand.append(self.working_deck.pop())

        self.player_hand_card1.setPixmap(QtGui.QPixmap(self.player_hand[0][2]))
        self.player_hand_card2.setPixmap(QtGui.QPixmap(self.player_hand[1][2]))
        self.player_hand_card3.setPixmap(QtGui.QPixmap(self.player_hand[2][2]))
        self.player_hand_card4.setPixmap(QtGui.QPixmap(self.player_hand[3][2]))
        self.player_hand_card5.setPixmap(QtGui.QPixmap(self.player_hand[4][2]))

    def reset(self):
        self.player_hand = []
        self.computer_hand = []
        self.working_deck = master_deck[:]
        random.shuffle(self.working_deck)

        self.computer_hand_card1.setPixmap(QtGui.QPixmap("assets/Back Red 1.png"))
        self.computer_hand_card2.setPixmap(QtGui.QPixmap("assets/Back Red 1.png"))
        self.computer_hand_card3.setPixmap(QtGui.QPixmap("assets/Back Red 1.png"))
        self.computer_hand_card4.setPixmap(QtGui.QPixmap("assets/Back Red 1.png"))
        self.computer_hand_card5.setPixmap(QtGui.QPixmap("assets/Back Red 1.png"))

        self.player_hand_card1.setPixmap(QtGui.QPixmap("assets/Back Red 1.png"))
        self.player_hand_card2.setPixmap(QtGui.QPixmap("assets/Back Red 1.png"))
        self.player_hand_card3.setPixmap(QtGui.QPixmap("assets/Back Red 1.png"))
        self.player_hand_card4.setPixmap(QtGui.QPixmap("assets/Back Red 1.png"))
        self.player_hand_card5.setPixmap(QtGui.QPixmap("assets/Back Red 1.png"))