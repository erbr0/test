class Node:
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next        

class Stack:

    def __init__(self):
        self.top = None

    def push (self, data):
        tmp = Node(data)
        tmp.next = self.top #för att peka vidare på de under i traven
        self.top = tmp

    def pop(self):
        if(self.isEmpty()):
            return None
        else:
            tmp = self.top.data #en kopia av strängen beda hamnar i tmp
            self.top = self.top.next
            return tmp

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False


print(__name__)


s = Stack()
s.push('Ada')
s.push('Beda')

data1 = s.pop()
print(data1)
data2 = s.pop()
print(data2)
data3 = s.pop()
print(data3)
print(s.isEmpty())