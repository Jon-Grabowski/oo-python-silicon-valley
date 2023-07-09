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
