class Obi(object):
   def __init__(self):
      self._obi = 1
   
   @property
   def obi(self):
      return self._obi

   @obi.setter
   def obi(self, value):
      self._obi = value

obi2 =  Obi()
print(obi2.obi)
obi2.obi = 2
print(obi2.obi)
