import random

class Blackjack:
    def __init__(self, aitype = 'standard'):
        self.AItype = aitype
        self.PlayerWin = 0
        self.AIWin = 0
        self.Tied = 0
        self.round = 1
        self.cards = []
        self.valueCards = {}
        types = ['Clover', 'Spade', 'Heart', 'Diamond']
        numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.strscore = {0:'Burst', 22:'Blackjack'}
        for i in range(1,22):
            self.strscore[i] = str(i)

        for type in types:
            for j in range(len(numbers)):
                card = numbers[j] + '-' + type
                self.cards.append(card)
                if j < 9:
                    self.valueCards[card] = j + 1
                else:
                    self.valueCards[card] = 10

    def getround(self):
        return self.round - 1

    def gameresult(self):
        return [self.PlayerWin, self.AIWin, self.Tied]

    def iterate(self):
        random.shuffle(self.cards)
        self.lstAIHand = [self.cards[0]]
        self.lstPlayerHand = [self.cards[1], self.cards[2]]
        self.scoreAI = self.calculateScore(self.lstAIHand)
        self.scorePlayer = self.calculateScore(self.lstPlayerHand)
        self.idxCard = 3

        print("-------------------------------------------------")
        print("Round : " + str(self.round))
        self.showCurrentCards()
        if self.scorePlayer == 22:
            print("Player`s Hand is  Blackjack!")
        else:
            self.actionPlayer()
        if self.scorePlayer != 0:
            self.actionAI()
        self.checkWinning()
        print("Round : " + str(self.round) + " End")
        print("-------------------------------------------------")
        self.round = self.round + 1

    def showCurrentCards(self):
        print("AI's Hand : " + str(self.lstAIHand))
        print("AI Current Score : " + self.strscore[self.scoreAI])
        print("Player's Hand : " + str(self.lstPlayerHand))
        print("Player Current Score : " + self.strscore[self.scorePlayer])

    def calculateScore(self, Cards):
        Values = []
        for card in Cards:
            Values.append(self.valueCards[card])
        num_A = Values.count(1)
        score = sum(Values)
        if score > 21:
            return 0  # Burst
        elif score == 11 and num_A == 1 and len(Cards) == 2:
            return 22  # Blackjack
        else:
            if num_A == 0:
                return score
            else:
                scores = [score]
                for i in range(num_A):
                    scores.append(score+10)
                scores.sort(reverse=True)
                for s in scores:
                    if s <= 21:
                        return s

    def checkWinning(self):
        print("AI Current Score : " + self.strscore[self.scoreAI])
        print("Player Current Score : " + self.strscore[self.scorePlayer])
        if self.scorePlayer > self.scoreAI:
            print("Player Win!")
            self.PlayerWin = self.PlayerWin + 1
        elif self.scorePlayer == self.scoreAI:
            print("Tied")
            self.Tied = self.Tied + 1
        else:
            print("AI Win!")
            self.AIWin = self.AIWin + 1

    def actionPlayer(self):
        stop = False
        while not stop:
            print("(H)it or (P)ass ??? Type!")
            action = input()
            if action == 'H' or action == 'h':
                print("Player get card : " + self.cards[self.idxCard])
                self.lstPlayerHand.append(self.cards[self.idxCard])
                self.scorePlayer = self.calculateScore(self.lstPlayerHand)
                self.idxCard = self.idxCard + 1
                if self.scorePlayer == 21:
                    print("Player get 21!")
                    stop = True
                elif self.scorePlayer == 0:
                    print("Player Burst!")
                    stop = True
                else:
                    print("Player's Hand : " + str(self.lstPlayerHand))
                    print("Player Current Score : " + str(self.scorePlayer))
            else:
                stop = True

    def actionAI(self):
        stop = False
        while not stop:
            if self.scoreAI < self.scorePlayer:
                print("AI Hit")
                print("AI get card : " + self.cards[self.idxCard])
                self.lstAIHand.append(self.cards[self.idxCard])
                self.scoreAI = self.calculateScore(self.lstAIHand)
                self.idxCard = self.idxCard + 1
                if self.scoreAI == 0:
                    print("AI Burst!")
                    stop = True
                else:
                    print("AI's Hand : " + str(self.lstAIHand))
                    print("AI Current Score : " + str(self.scoreAI))
            else:
                print("AI pass")
                stop = True

if __name__ == "__main__":
    b = Blackjack()
    stop = False
    while stop != True:
        b.iterate()
        print("play more game? press (Y), or (y)")
        a = input()
        if a == 'Y' or a == 'y':
            continue
        stop = True
    result = b.gameresult()
    print("Total ", b.getround(), "round, ")
    print("Player win ", result[0], "times")
    print("AI win ", result[1], "times")
    if result[0] > result[1]:
        print("Finally, Player win!")
    elif result[0] == result[1]:
        print("Finally, Tied!")
    else:
        print("Finally, AI win!")