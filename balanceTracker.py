from datetime import datetime

class Transaction:
    _account = None
    _quantity = None
    _tDate = None
    _prev = None
    _next = None
    
    def __init__(self, account, quantity, tDate = datetime.now()):
        self._account = account
        self._quantity = quantity
        self._tDate = tDate
        
    def addTran(self, account, quantity, tDate = datetime.now()):
        newTran = Transaction(account, quantity, tDate)
        newTran._prev = self
        #print(f'newTran: {newTran}')
        self._next = newTran
        #print(f'self._next: {self._next}')
        return newTran
    
    def len(self):
        firstTran = self.first()
        if firstTran == None:
            return 0
        else:
            count = 1
            while True:
                if firstTran._next == None:
                    break
                else:
                    count += 1
                    firstTran = firstTran._next
            return count
    
    def first(self):
        thisTran = self
        while True:
            if thisTran._prev == None:
                if thisTran._next == None:
                    return thisTran
                else:
                    return thisTran._next
                break
            else:
                thisTran = thisTran._prev
    
    def printTran(self):
        thisTran = self.first()
        while True:
            if thisTran == None:
                break
            else:
                print(f'Transaction account, quantity, timestamp: {thisTran._account}, {thisTran._quantity}, {thisTran._tDate}')
                thisTran = thisTran._next
        

tranList = Transaction(None, None)
#print(f'tranList, .account, .quantity, .tDate, .prev, .next: {tranList}, {tranList._account}, {tranList._quantity}, {tranList._tDate}, {tranList._prev}, {tranList._next}')
tranList = tranList.addTran('widgetA', 5)
#print(f'tranList, .account, .quantity, .tDate, .prev, .next: {tranList}, {tranList._account}, {tranList._quantity}, {tranList._tDate}, {tranList._prev}, {tranList._next}')
tranList = tranList.addTran('widgetA', 10)
#print(f'tranList, .account, .quantity, .tDate, .prev, .next: {tranList}, {tranList._account}, {tranList._quantity}, {tranList._tDate}, {tranList._prev}, {tranList._next}')

tranList.printTran()
