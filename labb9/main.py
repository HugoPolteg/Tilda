# Syntaxkontroll
from linkedQFile import LinkedQ
import sys
ATOMS = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Fl', 'Lv']
class Syntaxfel(Exception):
    '''Byter namn/inheritar från exception, basically för att visa vad som var fel'''
    pass

def readformula(input:str):
    '''Tar formatet <formel>::= <mol> \n och fixar det till en lista genom split -> iterera'''
    for mol in input.split('\n'):
        q = LinkedQ()
        for char in mol:
            q.enqueue(char)
        readmol(q)
def readformula_test(input:str):
    q = LinkedQ()
    for char in input:
        q.enqueue(char)
    try:
        readmol(q)
    except Syntaxfel as e:
        return str(e)
    return "Formeln är syntaktiskt korrekt"
def readmol(q:LinkedQ, parentheses = False):
    '''Läser in molekyl med syntax: <mol> ::= <group> | <group><mol>
 (basically antingen en grupp eller en grupp med en molekyl efter)'''
    readgroup(q)
    if q.peek() == ")" and parentheses:
        return
    if not q.isempty():
        readmol(q, parentheses)
def checkgroupstart(char):
    return (char >= "A" and char <= "Z" or char == "(" or char >= "a" and char <= "z")
def readgroup(q:LinkedQ):
    '''Läser in grupp med syntax: <group> ::= <atom> |<atom><num> | (<mol>) <num>
 (basically antingen en atom eller en atom med antal efter eller en molekyl inom parantes med nummer efter)'''
    group_start = q.peek()
    if not checkgroupstart(group_start):
        raise Syntaxfel("Felaktig gruppstart vid radslutet " + str(q))
    if group_start == "(":
        q.dequeue()
        readmol(q, True)
        if q.peek() != ")":
            raise Syntaxfel("Saknad högerparentes vid radslutet " + str(q))
        q.dequeue()
        readnum(q)
    else:
        readatom(q)
        if not q.isempty():
            if q.peek().isdigit():
                readnum(q)

def readatom(q:LinkedQ):
    '''Läser in en atmom som: <atom>  ::= <LETTER> | <LETTER><letter> (basically antingen en stor bokstav eller en stor följt av en liten)'''
    char = readuppercase(q)
    if not q.peek():
        if char not in ATOMS:
            q.dequeue()
            raise Syntaxfel("Okänd atom vid radslutet " + str(q))
    elif char + q.peek() not in ATOMS:
        if char not in ATOMS:
            q.dequeue()
            raise Syntaxfel("Okänd atom vid radslutet " + str(q))
    else:
        q.dequeue()

        
    

def readuppercase(q:LinkedQ):
    '''Kollar efter stora bokstäver, syntax => <LETTER>::= A | B | C | ... | Z'''
    char = q.dequeue()
    if char >= "A" and char <= "Z":
        return char
    raise Syntaxfel("Saknad stor bokstav vid radslutet " + char + str(q))


def readlowercase(q:LinkedQ):
    '''Kollar efter små bokstäver, syntax => <letter>::= a | b | c | ... | z'''
    char = q.peek()
    if char >= "a" and char <= "":
        q.dequeue()
def readnum(q:LinkedQ):
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

def main():
    '''Kör tills användaren skriver #'''
    for line in sys.stdin:
        try:
            line = line.strip()
            if line == "#":
                break
            readformula(line)
            print("Formeln är syntaktiskt korrekt")
        except Syntaxfel as msg:
            print(msg)
if __name__ == "__main__":
    main()