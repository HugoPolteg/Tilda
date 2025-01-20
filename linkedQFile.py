class Node:
    def __init__ (self, value, next=None):
        self.value = value
        self.next = next


class LinkedQ:
    def __init__ (self, first=None, last=None):
        self.first = first
        self.last= last

    def enqueue(self, value):
        
        node = Node(value, self.last)
        self.last = node
        
        if self.first == None: 
            self.first = node
        

    def Queue(self):
        self.first = None
        self.last = None
    
    def dequeue(self):
        if self.size() == 0:
            return False
        
        value = self.first.value
        if self.size() == 1:
            self.Queue()
            return value
        
        iter = self.last
        
        while iter: 
            if iter.next.next == None:
         
                self.first = iter
                iter.next = None
                break
            iter = iter.next
        
        return value
    
    def isEmpty(self):
        if self.first == None and self.last == None:
            return True
        else:
            return False
        
    def size(self):
        count = 0 
        iter = self.last
        while iter:
            iter = iter.next
            count += 1 
        return count
    
    def __str__(self):
        iter = self.last
        qstring = ''
        while iter:
            qstring += str(iter.value) + '>'
            iter = iter.next
        
        return qstring
    


