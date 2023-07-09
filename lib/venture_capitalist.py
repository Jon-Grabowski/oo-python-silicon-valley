from .funding_round import FundingRound

class VentureCapitalist:
    all = []
    tres_commas_club = []

    def __init__(self, name, total_worth):
        self.name = name.capitalize()
        self.total_worth = total_worth
        VentureCapitalist.all.append(self)
        if self.total_worth >= 1000000000:
            VentureCapitalist.tres_commas_club.append(self)

    def __repr__(self):
        return f"<Name: {self.name} | Net Worth: {self.total_worth}>"
