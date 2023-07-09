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
    
    def offer_contract(self, su, type, investment):
        FundingRound(su, self, type, investment)

    def funding_rounds(self):
        funding_rounds = []
        for fr in FundingRound.all:
            if fr.venture_capitalist == self:
                funding_rounds.append(fr)
        return funding_rounds
    
    def portfolio(self):
        portfolio_list = []
        for fr in FundingRound.all:
            if fr.venture_capitalist == self and fr.startup not in portfolio_list:
                portfolio_list.append(fr.startup)
        return portfolio_list
    
    def biggest_investment(self):
        largest_investment = 0
        largest_fr = FundingRound
        for fr in FundingRound.all:
            if fr.venture_capitalist == self and fr.investment > largest_investment:
                largest_investment = fr.investment
                largest_fr = fr
        return largest_fr

    def invested(self, domain):
        total_invested = 0
        for fr in FundingRound.all:
            if fr.startup.domain == domain and fr.venture_capitalist == self:
                total_invested += fr.investment
        return total_invested    
