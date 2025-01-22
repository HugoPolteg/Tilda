from bintreeFile import Bintree

def makeTree():
    '''Gör ett träd genom att ta input(från kattis?)'''
    tree = Bintree()
    data = input().strip()
    while data != "#":
        tree.put(data)
        data = input().strip()
    return tree

def searches(tree):
    '''Hittar värden i trädet genom in(__contains__) funktionen'''
    findme = input().strip()
    while findme != "#":
        if findme in tree:
            print(findme, "found")
        else:
            print(findme, "not found")
        findme = input().strip()

def main():
    '''Testar om trädet funkar'''
    #tree = makeTree()
    #searches(tree)
    svenska = Bintree()
    with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()                # Ett trebokstavsord per rad
            if ordet in svenska:
                print(ordet, end = " ") 
            else:
                svenska.put(ordet)             # in i sökträdet
    print("\n")
    engelska = Bintree()
    with open('engelska.txt', 'r', encoding='utf-8') as engelska_fil:
        for line in engelska_fil:
            for word in line.split(' '):
                word = word.strip()
                if word in engelska:
                    pass
                else:
                    if word in svenska:
                        print(word, end = " ")
                    else:
                        engelska.put(word)
if __name__ == '__main__':
    main()