class Node():
    def __init__(self, value=None, next=None):
        self._value = value
        self._next = next

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

head = Node("a")
next = Node("b")
head.next = next
print(head.value)
print(head.next.value)   
