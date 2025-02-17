class DictHash():
    '''implementation av hash-tabell via dict'''
    def __init__(self):
        self.hash_table = {}
    def store(self, nyckel, data):
        '''lagrar data som value i hash_table, med nyckel som key.'''
        self.hash_table[nyckel] = data
        
    def search(self, nyckel):
        '''slår upp nyckel i hash_table.'''
        return self.hash_table[nyckel]
    def __getitem__(self, nyckel):
        return self.search(nyckel)
    def __contains__(self, nyckel):
        return nyckel in self.hash_table
    def __str__(self):
        return str(self.hash_table)

class HashNode:
    """Noder till klassen Hashtable """

    def __init__(self, key = "", data = None):
        """key är nyckeln som anvands vid hashningen
            data är det objekt som ska hashas in"""
        self.key = key
        self.data = data



class Hashtable:
    '''Hemmagjord hashtable med modulushashning och linear probing'''
    def __init__(self, size):
      """size: hashtabellens storlek"""
      self.size = size
      #tabell med tuples som (key, value)
      self.table = [None]*size

    def store(self, key, data):
        """key är nyckeln
            data är objektet som ska lagras
            Stoppar in "data" med nyckeln "key" i tabellen."""
        h = self.hashfunction(key)
        #Kollsionshantering via linear probing
        while self.table[h] is not None:
            if self.table[h][0] == key:
                self.table[h] = (key, data)
                return
            #linear probing
            if h == self.size-1:
                h = 0
            else:
                h+=1
        self.table[h] = (key, data)




    def search(self, key):
        """key är nyckeln
            Hamtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
            Om "key" inte finns ska det bli KeyError """
        
        h = self.hashfunction(key)
        while self.table[h] is not None:
            if self.table[h][0] == key:
                return self.table[h][1]
            #linear probing
            if h == self.size-1:
                h = 0
            else:
                h+=1
        raise KeyError

    def hashfunction(self, key):
        """key är nyckeln
            Beräknar hashfunktionen för key"""
        key = str(key)
        key_value = 0
        for char in key:
            #Multiplicerar för att undvika kollision
            key_value += key_value*33 + ord(char)
        hash_value = key_value % self.size
        return hash_value

if __name__ == '__main__':
    dicthash = DictHash()
    with open('kdrama.csv', 'r') as file:
        value = 0
        key = ""
        for line in file.readlines():
            for word in line.split(','):
                if any(i.isdigit() for i in word) and '.' in word:
                    value = float(word.strip())
                    dicthash.store(key,value)
                else:
                    key = word
            