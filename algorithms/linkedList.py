
class LinkedList():


    class _Next():
        item = None
        next = None
        
    first = _Next()

    def __init__(self):
        super().__init__()

    def isEmpty(self):
        return self.first.item== None

    def pop(self):
        self.first = self.first.next

    def push(self, value):
        newFirst = self._Next()
        newFirst.item = value
        newFirst.next = self.first
        self.first = newFirst


linked = LinkedList()
linked.push(1)
linked.push(2)
print(linked.first.item)
linked.pop()
print(linked.first.item)
linked.pop()
print(linked.first.item)
print(linked.isEmpty())
