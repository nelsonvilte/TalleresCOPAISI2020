
#balance=neto // la clase permite administrar una cuenta de una tarjeta de debito
class clsCreditCard3:
    def __init__(self, customer, bank, account, limit):
        self.__customer= customer # self. "__"atributo privado  "_"atributo protegido
        self.__bank=bank
        self.__account=account
        self.__limit =limit        
        self.__balance=0

    def getCustomer(self):
        return self.__customer

    def getBank(self):
        return self.__bank

    def getAccount(self):
        return self.__account

    def getLimit(self):
        return self.__limit

    def getBalance(self):
        return self.__balance

    def setBalance(self, amount):
        self.__balance+= amount

    def charge(self,amount):
        if amount>0:
            if amount+self.getBalance()>self.getLimit():
                return False
            else:
                self.setBalance(amount)
                return True
        else:
            return False


    def makePayment(self,amount): #le resta plata a la cuenta (al balance)
        if amount>0:
            self.setBalance(-amount)