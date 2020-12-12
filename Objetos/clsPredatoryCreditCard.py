import clsCreditCard as superc
import math

class clsPredatoryCreditCard(superc.clsCreditCard3):

    def __init__(self, customer, bank, account, limit, apr):
        superc.clsCreditCard3.__init__(self, customer, bank, account, limit)#invocacion al constructor de la superclase
        self.setApr(apr) 

    def setApr(self, apr):
        self.__apr=apr

    def getApr(self):
        return self.__apr

    def charge(self,amount):
        success=superc.clsCreditCard3.charge(self, amount)

        if not success:
            self.setBalance(-abs(amount))

        return success

    def processMonth(self):
        if self.getBalance()>0:
            monthlyFactor = pow(1+ self.getApr(), 1/12.0)

            anterior = self.getBalance()
            self.setBalance(anterior*monthlyFactor)
            self.setBalance(-anterior)