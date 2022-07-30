from random import shuffle
suite = 'H D S C'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
# deck = [(s,r) for s in suite for r in ranks]
# print(deck)

class deck():
    def __init__(self):
        print("Creating a new deck of cards")
        self.allcards=[(s,r) for s in suite for r in ranks]

    def shuffle(self):
        print("shuffling the cards")
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26], self.allcards[26:])


class hand():
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards ".format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()


class player():
    def __init__(self, name, hand):
        self.name=name
        self.hands = hand

    def play_card(self):
        drawn_card = self.hands.remove_card()
        print("{} has placed: {}".format(self.name,drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hands.cards) < 3:
            return self.hands.cards
        else:
            for x in range(3):
                war_cards.append(self.hands.remove_card())
            return war_cards

    def still_has_cards(self):
        return len(self.hands.cards) !=0

print("let's begin the war")

d=deck()
d.shuffle()
half1, half2 = d.split_in_half()
h = hand(half1)
comp = player("computer",h)
name = input("what is your name?")
user = player(name, hand(half2))

total_rounds = 0
war_count = 0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds +=1
    print("Time for a new round!")
    print("here are the current standings")
    print(user.name + "has the count: "+ str(len(user.hands.cards)))
    print(comp.name + "has the count: "+ str(len(comp.hands.cards)))
    print("play a card!")
    print("\n")
    table_cards =[]
    c_card = comp.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        war_count += 1

        print("war!")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if ranks.index(c_card[1]) < ranks.index(p_card[1]):
            user.hands.add(table_cards)
        else:
            comp.hands.add(table_cards)

    else:
        if ranks.index(c_card[1]) < ranks.index(p_card[1]):
            user.hands.add(table_cards)
        else:
            comp.hands.add(table_cards)

print("Game over, number of rounds :" + str(total_rounds))
print(" a war happened "+str(war_count)+" times")
print("does the computer still have cards ?")
print(str(comp.still_has_cards()))
print("does the user still has cards ?")
print(str(user.still_has_cards()))
