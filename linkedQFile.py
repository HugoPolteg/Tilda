class Node:
    '''Klassen nod, en nod i en enkelt länkad lista'''
    def __init__ (self, value, next=None):
        self.value = value
        self.next = next


class LinkedQ:
    '''Enkelt länkad lista, bra för att implementera dynamisk minnesallokering och om man endast vill ha åt första eller sista elementet'''
    def __init__ (self):
        '''Har referens till första och sista elementet i listan'''
        self.first = None
        self.last= None

    def enqueue(self, value):
        '''Lägger till en nod längst bak i listan/kön'''
        node = Node(value, self.last)
        self.last = node
        
        if self.first is None:
            self.first = node
    def dequeue(self):
        '''Tar ut första elementet ur listan/kön och returnerar det (returnerar falskt om det inte finns)'''
        if self.size() == 0:
            return False
        
        value = self.first.value
        if self.size() == 1:
            self.first = None
            self.last = None
            return value
        
        itr = self.last
        
        while itr:
            #Kollar om nästa element är slutet av kön, isf sätter den det aktuella elementet som först och tar bort referensen till den efter
            #Funkar iom automatisk garbage collection, ex knas i c++
            if itr.next.next is None:
                self.first = itr
                itr.next = None
                break
            itr = itr.next
        
        return value
    
    def isEmpty(self):
        '''Kollar om kön är tom, eg borde det räcka med att kolla en men vrf inte'''
        return self.first is None and self.last is None
    def size(self):
        '''returnerar size genom att iterera o räkna elementen'''
        count = 0 
        itr = self.last
        while itr:
            itr = itr.next
            count += 1 
        return count
    
    def __str__(self):
        '''returnerar listan som en sträng med pilar för förtydligande av sekvens'''
        itr = self.last
        qstring = ''
        while itr:
            qstring += str(itr.value) + '>'
            itr = itr.next
        
        return qstring
    


