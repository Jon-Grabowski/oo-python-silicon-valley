from .funding_round import FundingRound

class Startup:
   all = []
   founder_lock = True
   domain_lock = True
   
   def __init__(self, name, founder, domain):
      self.name = name
      self.founder = founder
      self.domain = domain
      self.all.append(self)

   def __repr__(self):
      return f"<{self.name}>"

   def get_found(self):
      return self._founder     
   def set_found(self, founder):
      if self.founder_lock:
         self._founder = founder.capitalize()
         self.founder_lock = False
      else:
         print("Founder can not be changed after company started.")  
   founder = property(get_found, set_found)

   def get_dom(self):
      return self._domain     
   def set_dom(self, domain):
      if self.domain_lock:
         self._domain = domain
         self.domain_lock = False
      else:
         print("Domain can not be changed after company started.")  
   domain = property(get_dom, set_dom)

   def pivot(self, new_name, new_dom):
      self.domain_lock = True
      self.domain = new_dom
      self.name = new_name

   def find_by_founder(founder):
      for startup in Startup.all:
         if startup.founder == founder.capitalize():
            return startup
         
   def domains():
      return [startup.domain for startup in Startup.all]

   def sign_contract(self, vc, type, investment):
      FundingRound(self, vc, type, investment)

   def num_funding_rounds(self):
      num_rounds = 0
      for fr in FundingRound.all:
         if fr.startup == self:
            num_rounds += 1
      return num_rounds
   
   def total_funds(self):
      total_funds = 0
      for fr in FundingRound.all:
         if fr.startup == self:
            total_funds += fr.investment
      return total_funds
   
   def investors(self):
      vc_list = []
      for fr in FundingRound.all:
         if fr.startup == self and fr.venture_capitalist not in vc_list:
            vc_list.append(fr.venture_capitalist)
      return vc_list
   
   def big_investors(self):
      big_vc_list = []
      for fr in FundingRound.all:
         if fr.startup == self and fr.venture_capitalist not in big_vc_list and fr.venture_capitalist.total_worth >= 1000000000:
            big_vc_list.append(fr.venture_capitalist)
      return big_vc_list
   
   