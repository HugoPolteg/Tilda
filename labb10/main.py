# Syntaxkontroll
from linkedQFile import LinkedQ
import sys
from molgrafik import Molgrafik

ATOMS = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Fl', 'Lv']
class Syntaxfel(Exception):
    '''Byter namn/inheritar från exception, basically för att visa vad som var fel'''
    pass
class Ruta:
    def __init__(self, atom="( )", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None
    def weight(self):
        '''Räknar ut vikten av en molekyl genom att rekursivt kalla sin next och down'''
        weight = 0
        if self.down:
            #För paranteser
            weight += self.down.weight()*self.num
        if self.atom in ATOMS:
            #För atomer
            weight += skapaAtomlista()[self.atom] * self.num
        if self.next:
            #För att gå vidare i molekylen
            weight += self.next.weight()
        return weight
def skapaAtomlista():
    """Skapar och returnerar en dictionary med atomer och deras vikter"""
    atomdata = "H  1.00794;\
    He 4.002602;\
    Li 6.941;\
    Be 9.012182;\
    B  10.811;\
    C  12.0107;\
    N  14.0067;\
    O  15.9994;\
    F  18.9984032;\
    Ne 20.1797;\
    Na 22.98976928;\
    Mg 24.3050;\
    Al 26.9815386;\
    Si 28.0855;\
    P  30.973762;\
    S  32.065;\
    Cl 35.453;\
    K  39.0983;\
    Ar 39.948;\
    Ca 40.078;\
    Sc 44.955912;\
    Ti 47.867;\
    V  50.9415;\
    Cr 51.9961;\
    Mn 54.938045;\
    Fe 55.845;\
    Ni 58.6934;\
    Co 58.933195;\
    Cu 63.546;\
    Zn 65.38;\
    Ga 69.723;\
    Ge 72.64;\
    As 74.92160;\
    Se 78.96;\
    Br 79.904;\
    Kr 83.798;\
    Rb 85.4678;\
    Sr 87.62;\
    Y  88.90585;\
    Zr 91.224;\
    Nb 92.90638;\
    Mo 95.96;\
    Tc 98;\
    Ru 101.07;\
    Rh 102.90550;\
    Pd 106.42;\
    Ag 107.8682;\
    Cd 112.411;\
    In 114.818;\
    Sn 118.710;\
    Sb 121.760;\
    I  126.90447;\
    Te 127.60;\
    Xe 131.293;\
    Cs 132.9054519;\
    Ba 137.327;\
    La 138.90547;\
    Ce 140.116;\
    Pr 140.90765;\
    Nd 144.242;\
    Pm 145;\
    Sm 150.36;\
    Eu 151.964;\
    Gd 157.25;\
    Tb 158.92535;\
    Dy 162.500;\
    Ho 164.93032;\
    Er 167.259;\
    Tm 168.93421;\
    Yb 173.054;\
    Lu 174.9668;\
    Hf 178.49;\
    Ta 180.94788;\
    W  183.84;\
    Re 186.207;\
    Os 190.23;\
    Ir 192.217;\
    Pt 195.084;\
    Au 196.966569;\
    Hg 200.59;\
    Tl 204.3833;\
    Pb 207.2;\
    Bi 208.98040;\
    Po 209;\
    At 210;\
    Rn 222;\
    Fr 223;\
    Ra 226;\
    Ac 227;\
    Pa 231.03588;\
    Th 232.03806;\
    Np 237;\
    U  238.02891;\
    Am 243;\
    Pu 244;\
    Cm 247;\
    Bk 247;\
    Cf 251;\
    Es 252;\
    Fm 257;\
    Md 258;\
    No 259;\
    Lr 262;\
    Rf 265;\
    Db 268;\
    Hs 270;\
    Sg 271;\
    Bh 272;\
    Mt 276;\
    Rg 280;\
    Ds 281;\
    Cn 285"

    atomlista = {}
    lista = atomdata.split(";")
    for namn_vikt in lista:
        namn, vikt = namn_vikt.split()
        atomlista[namn] = float(vikt)
    return atomlista
def readformula(input:str):
    '''Tar formatet <formel>::= <mol> \n och fixar det till en lista genom split -> iterera'''
    mols = []
    for mol in input.splitlines():
        q = LinkedQ()
        for char in mol:
            q.enqueue(char)
        mols.append(readmol(q))
    return mols
def readmol(q:LinkedQ, parentheses = False):
    '''Läser in molekyl med syntax: <mol> ::= <group> | <group><mol>
    (basically antingen en grupp eller en grupp med en molekyl efter)
    Använder parentheses för att kolla om det är en molekyl inom paranteser
    skickar vidare den om den kallas rekursivt'''
    mol = readgroup(q)
    if q.peek() == ")" and parentheses:
        return mol
    if not q.isempty():
        mol.next = readmol(q, parentheses)
    return mol
def checkgroupstart(char):
    return (char >= "A" and char <= "Z") or char == "(" or (char >= "a" and char <= "z")
def readgroup(q:LinkedQ):
    '''Läser in grupp med syntax: <group> ::= <atom> |<atom><num> | (<mol>) <num>
 (basically antingen en atom eller en atom med antal efter eller en molekyl inom parantes med nummer efter)'''
    if not q.isempty():
        rutan = Ruta()
        group_start = q.peek()
        if not checkgroupstart(group_start):
            raise Syntaxfel("Felaktig gruppstart vid radslutet " + str(q))
        if group_start == "(":
            q.dequeue()
            rutan.down = readmol(q, True)
            if q.peek() != ")":
                raise Syntaxfel("Saknad högerparentes vid radslutet " + str(q))
            q.dequeue()
            rutan.num = readnum(q)
        else:
            rutan.atom = readatom(q)
            if not q.isempty():
                if q.peek().isdigit():
                    rutan.num = readnum(q)
        return rutan

def readatom(q:LinkedQ):
    '''Läser in en atmom som: <atom>  ::= <LETTER> | <LETTER><letter> (basically antingen en stor bokstav eller en stor följt av en liten)'''
    char = readuppercase(q)
    if not q.peek():
        if char not in ATOMS:
            q.dequeue()
            raise Syntaxfel("Okänd atom vid radslutet " + str(q))
    elif char + q.peek() not in ATOMS:
        if char not in ATOMS:
            if q.peek() >= "a" and q.peek() <= "z":
                q.dequeue()
            raise Syntaxfel("Okänd atom vid radslutet " + str(q))
    else:
        second_char = q.dequeue()
        return char + second_char
    return char

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
        return int(num)
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
            mols = readformula(line)
            print("Formeln är syntaktiskt korrekt")
            for mol in mols:
                print(mol.weight())
                molgrafik = Molgrafik()
                molgrafik.show(mol)
        except Syntaxfel as msg:
            print(msg)
if __name__ == "__main__":
    main()