from array import array
from  arrayQFile import ArrayQ
from linkedQFile import LinkedQ
import sys
'''
import unittest

class TestQueue(unittest.TestCase):

    def test_isEmpty(self):
        #isEmpty ska returnera True för tom kö, False annars
        q = LinkedQ()
        self.assertTrue(q.isEmpty(), "isEmpty på tom kö")
        q.enqueue(17)
        self.assertFalse(q.isEmpty(), "isEmpty på icke-tom kö")

    def test_order(self):
        #Kontrollerar att kö-ordningen blir rätt
        q = LinkedQ()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
'''
if __name__ == "__main__":
    #unittest.main()
    

    #Konverterar knäkt, dam, kung och ess till deras numeriska värden (måste ju vara int)
    conversion_table = {'Kn':11, 'D': 12, 'K':13, 'E':14}

    #indata = sys.stdin.readline()
    indata = input()
    user_inputs = indata.split(' ')
    user_input_arr = array('i')
    q = LinkedQ()
    #Lägger in allt i kön
    for user_input in user_inputs:
        user_input = user_input.strip()
        if user_input in conversion_table.keys():
            q.enqueue(conversion_table[user_input])
        if user_input.isnumeric():
            q.enqueue(int(user_input))

    bord = []
    count = 0 
    #Fixar trollkarlsalgoritmen aka varannan på bordet, varannan längst bak i högen tills allt är på bordet
    while q.size() != 0:
        if count % 2 == 0:
            first = q.dequeue()
            q.enqueue(first)
        else:
            first = q.dequeue()
            bord.append(first)
        count += 1
    #Printar ut det bra formaterat
    bord_str = ""
    for kort in bord:
        converted = False
        for key, value in conversion_table.items():
            if kort == value:
                bord_str+=str(key) + " "
                converted = True
        if not converted:
            bord_str+=str(kort) + " "
    print(bord_str)