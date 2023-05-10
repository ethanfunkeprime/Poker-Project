from PyQt5.QtWidgets import *
from view import *
import random
from score import score

"""
Card images for this project taken from opengameart.org
License that came with cards:
------------------------------------------------------------------------------------------
Card Pack by Andrew Tidey

    License (Creative Commons Zero, CC0)
    http://creativecommons.org/publicdomain/zero/1.0/
    You may use these assets in personal and commercial projects.

    Credit to me via name (Andrew Tidey) or link to website (andrewtidey.blogspot.co.uk) is
    appreciated but not necessary :)
-----------------------------------------------------------------------------------------
Thank you, Andrew!
"""

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

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

    def __init__(self, *args, **kwargs) -> None:
        """
        Sets up display window and connects buttons to functions.
        :param args:
        :param kwargs:
        """

        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.deal_button.clicked.connect(lambda: self.deal())
        self.show_button.clicked.connect(lambda: self.swap())
        self.clear_button.clicked.connect(lambda: self.reset())
        self.winner_label.setText("Deal cards to begin.")
        self.show_button.setHidden(True)
        self.card_swap1.setHidden(True)
        self.card_swap2.setHidden(True)
        self.card_swap3.setHidden(True)
        self.card_swap4.setHidden(True)
        self.card_swap5.setHidden(True)
        self.clear_button.setHidden(True)

    def deal(self) -> None:
        """
        Deals five cards to computer and five cards to player and shows the cards in the player's display.
        """

        if len(self.working_deck) >= 10:
            for i in range(5):
                self.computer_hand.append(self.working_deck.pop())
                self.player_hand.append(self.working_deck.pop())

        self.player_hand_card1.setPixmap(QtGui.QPixmap(self.player_hand[0][2]))
        self.player_hand_card2.setPixmap(QtGui.QPixmap(self.player_hand[1][2]))
        self.player_hand_card3.setPixmap(QtGui.QPixmap(self.player_hand[2][2]))
        self.player_hand_card4.setPixmap(QtGui.QPixmap(self.player_hand[3][2]))
        self.player_hand_card5.setPixmap(QtGui.QPixmap(self.player_hand[4][2]))

        self.winner_label.setText("Select up to three cards to replace, then press show.")
        self.clear_button.setHidden(False)
        self.show_button.setHidden(False)
        self.card_swap1.setHidden(False)
        self.card_swap2.setHidden(False)
        self.card_swap3.setHidden(False)
        self.card_swap4.setHidden(False)
        self.card_swap5.setHidden(False)
        self.deal_button.setHidden(True)

    def swap(self) -> None:
        """
        Replaces the player's cards they wish to discard and finds the game's winner.
        """

        num_checked = 0
        if self.card_swap1.isChecked():
            num_checked += 1
        if self.card_swap2.isChecked():
            num_checked += 1
        if self.card_swap3.isChecked():
            num_checked += 1
        if self.card_swap4.isChecked():
            num_checked += 1
        if self.card_swap5.isChecked():
            num_checked += 1

        if num_checked > 3:
            self.winner_label.setText("Please select only up to three cards.")
        else:
            if len(self.working_deck) >= 5:
                if self.card_swap1.isChecked():
                    self.player_hand[0] = self.working_deck.pop()
                if self.card_swap2.isChecked():
                    self.player_hand[1] = self.working_deck.pop()
                if self.card_swap3.isChecked():
                    self.player_hand[2] = self.working_deck.pop()
                if self.card_swap4.isChecked():
                    self.player_hand[3] = self.working_deck.pop()
                if self.card_swap5.isChecked():
                    self.player_hand[4] = self.working_deck.pop()

            self.player_hand_card1.setPixmap(QtGui.QPixmap(self.player_hand[0][2]))
            self.player_hand_card2.setPixmap(QtGui.QPixmap(self.player_hand[1][2]))
            self.player_hand_card3.setPixmap(QtGui.QPixmap(self.player_hand[2][2]))
            self.player_hand_card4.setPixmap(QtGui.QPixmap(self.player_hand[3][2]))
            self.player_hand_card5.setPixmap(QtGui.QPixmap(self.player_hand[4][2]))

            self.computer_hand_card1.setPixmap(QtGui.QPixmap(self.computer_hand[0][2]))
            self.computer_hand_card2.setPixmap(QtGui.QPixmap(self.computer_hand[1][2]))
            self.computer_hand_card3.setPixmap(QtGui.QPixmap(self.computer_hand[2][2]))
            self.computer_hand_card4.setPixmap(QtGui.QPixmap(self.computer_hand[3][2]))
            self.computer_hand_card5.setPixmap(QtGui.QPixmap(self.computer_hand[4][2]))

            computer_handname, computer_score = score(self.computer_hand)
            player_handname, player_score = score(self.player_hand)

            if player_score > computer_score:
                self.winner_label.setText(f"You win! You had: {player_handname}.")
            elif player_score == computer_score:
                self.tie_function(self.player_hand, self.computer_hand, player_handname, computer_handname)
            else:
                self.winner_label.setText(f"You lose! The computer had: {computer_handname}.")

            self.show_button.setHidden(True)
            self.card_swap1.setHidden(True)
            self.card_swap2.setHidden(True)
            self.card_swap3.setHidden(True)
            self.card_swap4.setHidden(True)
            self.card_swap5.setHidden(True)

    def reset(self) -> None:
        """
        Returns everything to how it was when the program started.
        """

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

        self.winner_label.setText("Deal cards to begin.")
        self.show_button.setHidden(True)
        self.card_swap1.setHidden(True)
        self.card_swap2.setHidden(True)
        self.card_swap3.setHidden(True)
        self.card_swap4.setHidden(True)
        self.card_swap5.setHidden(True)
        self.clear_button.setHidden(True)
        self.deal_button.setHidden(False)
        self.card_swap1.setChecked(False)
        self.card_swap2.setChecked(False)
        self.card_swap3.setChecked(False)
        self.card_swap4.setChecked(False)
        self.card_swap5.setChecked(False)

    def tie_function(self, player_hand: list, computer_hand: list, player_handname: str, computer_handname: str) -> None:
        """
        Determines who wins in a draw between the player and the computer by comparing all the cards in their hands.
        :param player_hand: List of cards in the player's hand.
        :param computer_hand: List of cards in the computer's hand.
        :param player_handname: Name of the type of hand the player has.
        :param computer_handname: Name of the type of hand the computer has.
        """

        player_hand_nums = []
        player_hand_suits = []
        player_hand_vals = []
        player_sorted_hand = []

        for card in player_hand:
            player_hand_nums.append(card[0])
            player_hand_suits.append(card[1])
            player_hand_vals.append(card[3])

        for i in range(len(player_hand_vals)):
            player_sorted_hand.append(min(player_hand_vals))
            player_hand_vals.remove(min(player_hand_vals))

        computer_hand_nums = []
        computer_hand_suits = []
        computer_hand_vals = []
        computer_sorted_hand = []

        for card in computer_hand:
            computer_hand_nums.append(card[0])
            computer_hand_suits.append(card[1])
            computer_hand_vals.append(card[3])

        for i in range(len(computer_hand_vals)):
            computer_sorted_hand.append(min(computer_hand_vals))
            computer_hand_vals.remove(min(computer_hand_vals))

        i = 4
        while i >= 0:
            if player_sorted_hand[i] > computer_sorted_hand[i]:
                self.winner_label.setText(f"You win! You had: {player_handname}.")
                break
            elif player_sorted_hand[i] < computer_sorted_hand[i]:
                self.winner_label.setText(f"You lose! The computer had: {computer_handname}.")
                break
            else:
                i -= 1

        if self.winner_label.text() == 'Select up to three cards to replace, then press show.' \
                or self.winner_label.text() == 'Please select only up to three cards.':
            self.winner_label.setText(f"You draw! Both you and the computer had: {computer_handname}.")
