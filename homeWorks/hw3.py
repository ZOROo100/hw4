class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def moneyx(self, add_ballance):
        add_ballance = int(input("How much money:"))
        self.balance += add_ballance

    def _kill(self):
        self.balance -= self.balance
        if self.balance ==0:
            print('Sorry, you do not have enough')

    def __jackpot(self):
        return self.balance * 10

    def show_bank(self, our_player):
        return self.balance + our_player.balance

    


