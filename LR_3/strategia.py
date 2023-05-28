from abc import ABC, abstractmethod
import random


class Strategy(ABC):
    @abstractmethod
    def choose(self):
        pass


class RockStrategy(Strategy):
    def choose(self):
        return "камень"


class ScissorsStrategy(Strategy):
    def choose(self):
        return "ножницы"


class PaperStrategy(Strategy):
    def choose(self):
        return "бумага"


class Player:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def choose(self):
        return self._strategy.choose()


class Game:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2

    def play(self):
        choice1 = self.player1.choose()
        choice2 = self.player2.choose()

        if choice1 == choice2:
            print("Ничья")
        elif (choice1 == "камень" and choice2 == "ножницы") or \
             (choice1 == "ножницы" and choice2 == "бумага") or \
             (choice1 == "бумага" and choice2 == "камень"):
            print("Игрок 1 выиграл")
        else:
            print("Игрок 2 выиграл")



n = 1
while n == 1:
    print("Игрок 1: Выберите - камень, ножницы, бумага, случайный. Делайте выбор с умом, от этого зависит ваша жизнь")
    player1 = input()
    while player1 not in ("камень", "ножницы", "бумага","случайный"):
        print("Выберите то, что вы видете в строке выше, ЭТО ПРОСТО, не тупите")
        player1 = input()
    if player1 == "случайный":
        player1 = Player(random.choice([RockStrategy(), ScissorsStrategy(), PaperStrategy()]))
    if player1 == "камень":
        player1 = Player(RockStrategy())
    if player1 == "ножницы":
        player1 = Player(ScissorsStrategy())
    if player1 == "бумага":
        player1 = Player(PaperStrategy())
    
    print("Игрок 2: Выберите - камень, ножницы, бумага, случайный. Делайте выбор с умом, от этого зависит ваша жизнь")
    player2 = input()
    while player2 not in ("камень", "ножницы", "бумага","случайный"):
        print("Выберите то, что вы видете в строке выше, ЭТО ПРОСТО, не тупите")
        player2 = input()
    if player2 == "случайный":
        player2 = Player(random.choice([RockStrategy(), ScissorsStrategy(), PaperStrategy()]))
    if player2 == "камень":
        player2 = Player(RockStrategy())
    if player2 == "ножницы":
        player2 = Player(ScissorsStrategy())
    if player2 == "бумага":
        player2 = Player(PaperStrategy())
    game = Game(player1, player2)
    game.play()
    print("Для повтора введите 1")
    n=int(input())