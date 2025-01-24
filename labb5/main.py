from linkedQFile import LinkedQ

class ParentNode:
    '''Klass med värdet på noden och dess förälder/tidigare nod'''
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

def writechain(node:ParentNode):
    '''Skriver ut kedjan som början(startordet) > slutordet i följd'''
    if node.parent is not None:
        writechain(node.parent)
    print(node.word)

def get_buckets(word):
    '''Tar fram vilka buckets ordet tillhör'''
    buckets = []
    for i in range(len(word)):
        word_as_list = list(word)
        word_as_list[i] = '_'
        buckets.append("".join(word_as_list))
    return buckets

def makechildren(parent:ParentNode, q:LinkedQ, buckets,  target, seen):
    '''Söker igenom med breddenförstsökning (lägger till varje barn till noden i kön)'''
    for bucket in get_buckets(parent.word):
        for node in buckets[bucket]:
            if node.word not in seen:
                node.parent = parent
                if node.word == target:
                    writechain(node)
                    exit(0)
                q.enqueue(node)
                seen[node.word] = None
                
    return (q, seen)
            
if __name__ == '__main__':
    start = input("Startord: ")
    target = input("Slutord: ")
    buckets = {}
    with open('word3.txt', 'r', encoding='utf-8') as file:
        for line in file.readlines():
            for word in line.split(' '):
                word = word.strip()
                for bucket in get_buckets(word):
                    if bucket in buckets:
                        buckets[bucket].append(ParentNode(word))
                    else:
                        buckets[bucket] = [ParentNode(word)]
    q = LinkedQ()
    q.enqueue(ParentNode(start))
    seen = {}
    while not q.isEmpty():
        #Breddenförstsökning mha kö
        node = q.dequeue()
        q, seen = makechildren(node, q, buckets, target, seen)
    print("Omöjligt att hitta lösning!")