# Syntaxkontroll
from linkedQFile import LinkedQ
class Syntaxfel(Exception):
    '''Byter namn/inheritar från exception, basically för att visa vad som var fel'''
    pass


def readmolecule(q):
    '''Läser in molekyl med syntax: <molekyl> ::= <atom> | <atom><num> (basically antingen en atom eller en atom med antal efter)'''
    readatom(q)
    if not q.isempty():
        readnum(q)
    
def readatom(q):
    '''Läser in en atmom som: <atom>  ::= <LETTER> | <LETTER><letter> (basically antingen en stor bokstav eller en stor följt av en liten)'''
    readuppercase(q)
    if not q.isempty():
        readlowercase(q)

def readuppercase(q):
    '''Kollar efter stora bokstäver, syntax => <LETTER>::= A | B | C | ... | Z'''
    char = q.dequeue()
    if char >= "A" and char <= "Z":
        return
    raise Syntaxfel("Saknad stor bokstav vid radslutet " + char + str(q))


def readlowercase(q):
    '''Kollar efter små bokstäver, syntax => <letter>::= a | b | c | ... | z'''
    char = q.peek()
    if char >= "a" and char <= "z":
        q.dequeue()
def readnum(q):
    '''Kollar efter tal över 2 (som inte börjar på 0) => <num>   ::= 2 | 3 | 4 | ...'''
    nums = []
    while not q.isempty():
        if q.peek().isdigit():
            nums.append(q.dequeue())
        else:
            break
    num = "".join(nums)
    #lagom knasig if-sats
    if num.isdigit() and (int(nums[0]) > 1 or int(nums[0]) == 1 and int(num) > 1):
        return
    if not num.isdigit():
        raise Syntaxfel("Saknad siffra vid radslutet " + str(q))
    raise Syntaxfel("För litet tal vid radslutet " + str(num)[1:] + str(q))

def readmolecule_test(molecule):
    '''Testar om en molekyl är syntaktiskt korrekt'''
    q = LinkedQ()
    try:
        for char in molecule:
            q.enqueue(char)
        readmolecule(q)
    except Syntaxfel as msg:
        return str(msg)
    return "Formeln är syntaktiskt korrekt"

def main():
    '''Kör tills användaren skriver #'''
    while True:
        try:
            user_input = input("Skriv en molekyl: ")
            if user_input == "#":
                break
            q = LinkedQ()
            for char in user_input:
                q.enqueue(char)
            readmolecule(q)
            print("Formeln är syntaktiskt korrekt")
        except Syntaxfel as msg:
            print(msg)
if __name__ == "__main__":
    main()