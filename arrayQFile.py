from array import array

class ArrayQ:
    '''Klass för kön implementerat via array (dynamisk men kan endast inehålla en datatyp)'''
    def __init__(self):
        '''Skapar en tom array av typen int'''
        self.arr = array('i')

    def enqueue(self, insertion):
        '''Lägger in ett element sist i kön'''
        self.arr.append(insertion)

    def dequeue(self):
        '''Tar ut det första elementet(index 0) ur kön och returnerar elementet'''
        return self.arr.pop(0)
    
    def isempty(self):
        '''Returnerar en bool (True om den är tom, falsk annars)'''
        return len(self.arr) == 0
    def size(self):
        '''Returnerar storleken (len) av kön'''
        return len(self.arr)

    def __str__ (self):
        '''Returnerar kön som en sträng'''
        return str(self.arr)
    
if __name__ == '__main__':
    q = ArrayQ()
    q.enqueue(1)
    q.enqueue(2)
    x = q.dequeue()
    y = q.dequeue()
    if (x == 1 and y == 2):
        print("OK")
    else:
        print("FAILED")