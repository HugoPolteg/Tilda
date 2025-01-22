class Node:
    '''Trädnod, pekare till elementet nedåt till höger och vänster'''
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Bintree:
    '''Enkelt binärt träd'''
    def __init__(self):
        '''Har endast referens till rot/initialnod'''
        self.root = None

    def put(self,new_value):
        '''Lägger in ett värde i trädet genom extern funktion putta (copypastad från canvas)'''
        # Sorterar in newvalue i trädet
        self.root = putta(self.root,new_value)

    def __contains__(self,value):
        '''Kollar om ett värde finns i trädet genom extern funktion finns (copypastad från canvas)'''
        # True om value finns i trädet, False annars
        return finns(self.root,value)

    def write(self):
        '''Skriver ut alla värden i trädet genom extern funktion skriv (copypastad från canvas)'''
        # Skriver ut trädet i inorder
        skriv(self.root)
        print("\n")
def finns(root:Node, new_value):
    '''Kollar om värdet finns i trädet'''
    itr = root
    while itr:
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
    if root is not None:
        skriv(root.left)
        print(root.value)
        skriv(root.right)

if __name__ == '__main__':
    #Testar med några ord
    svenska_ord = ["Sol","Bok","Vän","Ljus","Vatten","Blomma","Träd","Snö","Stjärna","Vind"]
    svenska_ord_träd = Bintree()
    for ord in svenska_ord:
        svenska_ord_träd.put(ord)

    svenska_ord_träd.write()