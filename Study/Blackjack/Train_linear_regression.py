import csv
import random

class Blackjack:
    def __init__(self, aitype = 'standard', discountFactor = 0.99):
        self.AItype = aitype
        self.round = 1
        self.cards = []
        self.valueCards = {}
        self.Hitrecord = []
        self.Passrecord = []
        self.discountFactor = discountFactor
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
        return self.Hitrecord, self.Passrecord

    def iterate(self):
        random.shuffle(self.cards)
        self.lstAIHand = [self.cards[0]]
        self.lstPlayerHand = [self.cards[1], self.cards[2]]
        self.scoreAI = self.calculateScore(self.lstAIHand)
        self.scorePlayer = self.calculateScore(self.lstPlayerHand)
        self.idxCard = 3
        self.PlayerHaveAce = 0
        self.tempHitRecord = []
        self.tempPassRecord = []

        if self.scorePlayer != 22:
            self.actionPlayer()
        if self.scorePlayer != 0:
            self.actionAI()
        self.checkWinning()
        self.round = self.round + 1

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

    def sumPlayerScore(self):
        score = 0
        for card in self.lstPlayerHand:
            score += self.valueCards[card]
        return score

    def checkWinning(self):
        if self.scorePlayer > self.scoreAI:
            result = 1
        elif self.scorePlayer == self.scoreAI:
            result = 0
        else:
            result = -1
        result2 = result
        for i in range(len(self.tempHitRecord)):
            self.Hitrecord.append(self.tempHitRecord[-1]+[result])
            result = result * self.discountFactor
        result = result2
        for j in range(len(self.tempPassRecord)):
            self.Passrecord.append(self.tempPassRecord[-1]+[result])
            result = result * self.discountFactor

    def actionPlayer(self):
        stop = False
        while not stop:
            if self.scorePlayer < 12:
                if self.valueCards[self.cards[self.idxCard]] == 1:
                    self.PlayerHaveAce = 1
                self.lstPlayerHand.append(self.cards[self.idxCard])
                self.scorePlayer = self.calculateScore(self.lstPlayerHand)
                self.idxCard = self.idxCard + 1
                if self.scorePlayer == 21:   # get maximum score
                    stop = True
            else:
                action = random.randint(0, 1)  # 0 = pass, 1 = Hit
                if action == 1:
                    if self.valueCards[self.cards[self.idxCard]] == 1:
                        self.PlayerHaveAce = 1
                    self.tempHitRecord.append([self.sumPlayerScore(), self.scoreAI, self.scorePlayer])
                    self.lstPlayerHand.append(self.cards[self.idxCard])
                    self.scorePlayer = self.calculateScore(self.lstPlayerHand)
                    self.idxCard = self.idxCard + 1
                    if self.scorePlayer == 21:   # get maximum score
                        stop = True
                    elif self.scorePlayer == 0:   # Burst
                        stop = True
                else:
                    self.tempPassRecord.append([self.sumPlayerScore(), self.scoreAI, self.scorePlayer])
                    stop = True

    def actionAI(self): # Hit When AI`s Score < Player`s Score
        stop = False
        while not stop:
            if self.scoreAI < self.scorePlayer:
                self.lstAIHand.append(self.cards[self.idxCard])
                self.scoreAI = self.calculateScore(self.lstAIHand)
                self.idxCard = self.idxCard + 1
                if self.scoreAI == 0:
                    stop = True
            else:
                stop = True

if __name__ == "__main__":
    b = Blackjack()
    num = 2000
    for i in range(num):
        b.iterate()
    resultH, resultP = b.gameresult()
    file = open('test5.csv', 'w', newline="")
    data = csv.writer(file)
    data.writerow(['내 점수','AI 점수','ACE 보유','결과'])
    data.writerows(resultH)
    file.close()
    file = open('test6.csv', 'w', newline="")
    data = csv.writer(file)
    data.writerow(['내 점수', 'AI 점수', 'ACE 보유', '결과'])
    data.writerows(resultP)
    file.close()