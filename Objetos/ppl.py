import clsCreditCard as superc
import clsPredatoryCreditCard as subc

if __name__=='__main__':
    obj1 = superc.clsCreditCard3('JC', 'California Savings', '0001 001', 2500)
    obj2 = superc.clsCreditCard3('CC', 'California Federal', '0001 066', 3500)

    print (obj1.getCustomer()  + " " + obj1.getBank())
    print (obj2.getCustomer()  + " " + obj2.getBank())
       
     obj3 = subc.clsPredatoryCreditCard('XX', 'Macro Bank', '0002 059', 4000, 0.0825)
    obj3.charge(500)
    obj3.processMonth()
    print(obj3.getCustomer()  + " " + obj3.getBank() + " " + str(obj3.getBalance()))