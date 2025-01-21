class Node:
    '''Trädnod, pekare till elementet nedåt till höger och vänster'''
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Bintree:
    def __init__(self):
        self.root = None

    def put(self,new_value):
        # Sorterar in newvalue i trädet
        self.root = putta(self.root,new_value)

    def __contains__(self,value):
        # True om value finns i trädet, False annars
        return finns(self.root,value)

    def write(self):
        # Skriver ut trädet i inorder
        skriv(self.root)
        print("\n")
def finns(root:Node, new_value):
    '''Kollar om värdet finns i trädet'''
    itr = root
    while True:
        if new_value == itr.value:
            return True
        elif new_value > itr.value:
            if itr.right is not None:
                itr = itr.right
            else:
                return False
        elif new_value < itr.value:
            if itr.left is not None:
                itr = itr.left
            else:
                return False

def putta(root:Node, value):
    '''Lägger in ett värde i trädet utifrån om det är större/mindre än varje nod -> höger respektive vänster'''
    if root is None:
        root = Node(value)
        return root
    itr = root
    while True:
        if value == itr.value:
            print("Värdet finns redan i trädet")
            return ""
        if value > itr.value:
            if itr.right is not None:
                itr = itr.right
            else:
                itr.right = Node(value)
                return root
        elif value < itr.value:
            if itr.left is not None:
                itr = itr.left
            else:
                itr.left = Node(value)
                return root
    
def skriv(root:Node):
    '''Inorder traversal som skriver ut värdena (alfabetiskt/min->max)'''
    values = []
    itr = root
    while values or itr:
        #Går till värdet längst ned till vänster o lägger till dem längs vägen till listan/stacken
        while itr:
            values.append(itr)
            itr = itr.left
        #printar senaste (FIFO) värdet
        itr = values.pop()
        print(itr.value)
        #Går till höger o kör igen
        itr = itr.right

if __name__ == '__main__':
    svenska_ord = ["Sol","Bok","Vän","Ljus","Vatten","Blomma","Träd","Snö","Stjärna","Vind"]
    svenska_ord_träd = Bintree()
    for ord in svenska_ord:
        svenska_ord_träd.put(ord)

    svenska_ord_träd.write()