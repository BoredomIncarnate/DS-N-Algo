class Node():
    def __init__(self, value=None, next=None):
        self._value: any = value
        self._next: Node = next

    def getvalue(self):
        return self._value

    def setvalue(self, newValue):
        self._value = newValue

    def getnext(self):
        return self._next

    def setnext(self, newNext):
        self._next = newNext

    value = property(getvalue, setvalue)
    next = property(getnext, setnext)
  
