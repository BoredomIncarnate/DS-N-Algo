from Node import Node

class LinkedList():
    def __init__(self, head: Node = None):
        self._head = head

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, head: Node):
        if isinstance(head, Node):
            self._head = head
        else:
            raise TypeError(f"head must be type Node")

    def traverse(self):
        while self._head != None:
            print(self._head.value)
            self._head = self._head.next

ll: LinkedList = LinkedList(Node("a"))
ll.head.next = Node("b")
ll.head.next.next = Node("c")
ll.traverse()
        