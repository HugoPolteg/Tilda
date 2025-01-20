from array import array


class ArrayQ:
    def __init__(self, arr=None):
        

        if arr is None:
            arr = array('i')  

        if isinstance(arr, list):
            arr = array('i',arr)

        if not isinstance(arr, array):
            raise TypeError("Input must be an array, list or empty")
        
        self.arr = arr
    def queue(self):
        self.arr.clear()
        return self.arr
    
    def enqueue(self, insertion):
        self.insertion = insertion
        self.arr.append(self.insertion)
        return self.arr
    
    def dequeue(self):
        first = self.arr.pop(0)
        return first
    
    def isempty(self, empty):
        self.empty = empty

        if len(self.arr) == 0:
            empty = True

        else:
            empty = False
    def size(self):
        return len(self.arr)

    def __str__ (self):
        return str(self.arr) 