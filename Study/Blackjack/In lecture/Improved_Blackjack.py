import random

def copy(List):
    new_List = []
    for i in List:
        new_List.append(i)
    return new_List

class Card:
    def __init__(self, name):
        self.name = name
        self.value = 0
        
class Blackjack:
    def __init__(self,numObserved):
        self.numObserved = numObserved
        self.cards = []
        self.idxCard = 0
        
        types = ['Clover', 'Spade', 'Heart', 'Diamond']
        numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        
        # Making card set
        for type in types:
            for j in range(len(numbers)):
                card = Card(numbers[j] + '-' + type)
                card.value = j+1
                self.cards.append(card)
                
    def iterate(self):
        
        random.shuffle(self.cards)
        self.lstAIHand = []
        self.lstPlayerHand = []
        self.scoreAI = 0
        self.scorePlayer = 0
        self.round = 0
        self.idxCard = 0
        self.actionLastPlayer = 'Hit'
        self.actionLastAI = 'Hit'
        self.Take_or_pass=0
        
        stop = False
        while stop == False:
            self.showCurrentObservedCards()
            self.actionPlayer()
            self.actionAI()
            stop = self.checkWinning()
        
    def action(self, observed_card, Player_Hand, AI_Hand, past_action):
        if self.find_winning(observed_card, Player_Hand, AI_Hand, past_action)!=False:
            return self.find_winning(observed_card, Player_Hand, AI_Hand, past_action)
        obsv = copy(observed_card)
        PH = copy(Player_Hand)
        AH = copy(AI_Hand)
        b=1
        a=0
        if past_action == 'Player_take' or past_action == 'Player_pass':
            if past_action == 'Player_take':
                a = self.action(obsv, PH, AH, 'AI_pass')
            else:
                a = self.action(obsv, PH, AH, 'Double_pass')
            AH.append(obsv.remove(obsv[0]))
            b = self.action(obsv, PH, AH, 'AI_take')
        elif past_action ==  'AI_take' or past_action == 'AI_pass':
            if past_action == 'AI_take':
                a = self.action(obsv, PH, AH, 'Player_pass')
            else:
                a = self.action(obsv, PH, AH, 'Double_pass')
            PH.append(obsv.remove(obsv[0]))
            b = self.action(obsv, PH, AH, 'Player_take')
            
        self.Take_or_pass=0
        if a < b:
            self.Take_or_pass='t'
        else:
            self.Take_or_pass='p'
            
        return a+b
    
    def find_winning(self, observed_card, Player_Hand, AI_Hand, past_action):
        
        if past_action == 'Double_pass' or len(observed_card) == 0:
            if self.sumvalue(Player_Hand) < self.sumvalue(AI_Hand):
                return 1
            else:
                return 0
        if self.sumvalue(Player_Hand) > 21:
            return 1
        elif self.sumvalue(Player_Hand) == 21:
            return 0
        elif self.sumvalue(AI_Hand) > 21:
            return 0
        elif self.sumvalue(AI_Hand) == 21:
            return 1
        else:
            return False
        
    def sumvalue(self, cards):
        sum = 0
        for i in cards:
            sum = sum + i.value
        return sum
        
    def showCurrentObservedCards(self):
        print ("-------------------------------------------------")
        self.observedCards = self.cards[self.idxCard:min(len(self.cards),self.idxCard+self.numObserved)]
        print ("Round : "+str(self.round))
        observed_list=[]
        for i in self.observedCards:
            observed_list.append(i.name)
        print(observed_list)
        print("AI Current Score : "+str(self.scoreAI))
        AI_list=[]
        for i in self.lstAIHand:
            AI_list.append(i.name)
        print("AI's Hand : "+str(AI_list))
        print("Player Current Score : " + str(self.scorePlayer))
        Player_list=[]
        for i in self.lstPlayerHand:
            Player_list.append(i.name)
        print("Player's Hand : " + str(Player_list))
        self.round = self.round + 1
        
    def checkWinning(self):
        print("AI Current Score : "+str(self.scoreAI))
        print("Player Current Score : " + str(self.scorePlayer))
        if self.scorePlayer > 21:
            print ("Player Lose!")
            return True
        if self.scoreAI > 21:
            print("AI Lose!")
            return True
        if self.scorePlayer == 21:
            print("Player Win!")
            return True
        if self.scoreAI == 21:
            print("AI Win!")
            return True
        if self.actionLastAI == 'Pass' and self.actionLastPlayer == 'Pass':
            if self.scorePlayer > self.scoreAI:
                print ("Player Win!")
                return True
            elif self.scoreAI > self.scorePlayer:
                print ("AI Win!")
                return True
            else:
                print ("Tie, Both Wins!")
                return True
        return False

    def actionPlayer(self):
        print("Player Cards to Play : " + self.observedCards[0].name)
        print("(H)it or (P)ass ??? Type!")
        action = input()
        if action == 'H' or action == 'h':
            self.idxCard = self.idxCard + 1
            self.lstPlayerHand.append(self.observedCards[0])
            self.scorePlayer = self.scorePlayer + self.observedCards[0].value
            self.observedCards.remove(self.observedCards[0])
            self.actionLastPlayer = 'Hit'
        else:
            self.actionLastPlayer = 'Pass'

    def actionAI(self):
        if not self.checkWinning():
            self.action(self.observedCards, self.lstPlayerHand, self.lstAIHand, self.actionLastPlayer)
            print("AI Cards to Play : "+self.observedCards[0].name)
            if self.Take_or_pass == 't':
                self.actionLastAI = 'Hit'
            else:
                if self.actionLastPlayer == 'Hit':
                    self.actionLastAI = 'Pass'
                else:
                    if self.scoreAI < self.scorePlayer:
                        print("INSIDE AI : AI cannot pass because Player will win if AI pass")
                        self.actionLastAI = 'Hit'
                    else:
                        self.actionLastAI = 'Pass'
            print("AI "+self.actionLastAI)
            if self.actionLastAI == 'Hit':
                self.idxCard = self.idxCard + 1
                self.lstAIHand.append(self.observedCards[0])
                self.scoreAI = self.scoreAI + self.observedCards[0].value
                self.observedCards.remove(self.observedCards[0])
        else:
            self.stop = True

if __name__ == "__main__":

    Game = Blackjack(5)
    stop = 'Y'
    while stop=='Y' or stop=='y':
        Game.iterate()
        print("If you wanna more game? type Y or y")
        stop = input()