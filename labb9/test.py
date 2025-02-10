import unittest
from main import *
class MoleculeTest(unittest.TestCase):
    def testMolecule(self):
        molecules = ["Na",
        "H2O",
        "Si(C3(COOH)2)4(H2O)7",
        "Na332",
        ]
        for molecule in molecules:
            self.assertEqual(readformula_test(molecule), "Formeln är syntaktiskt korrekt")
    def testFalse(self):
        inputs = [("C(Xx4)5", "Okänd atom vid radslutet 4)5"),
        ("C(OH4)C","Saknad siffra vid radslutet C"),
        ("C(OH4C", "Saknad högerparentes vid radslutet "),
        ("H2O)Fe", "Felaktig gruppstart vid radslutet )Fe"),
        ("H0", "För litet tal vid radslutet "),
        ("H1C", "För litet tal vid radslutet C"),
        ("H02C", "För litet tal vid radslutet 2C"),
        ("Nacl", "Saknad stor bokstav vid radslutet cl"),
        ("a", "Saknad stor bokstav vid radslutet a"),
        ("(Cl)2)3", "Felaktig gruppstart vid radslutet )3"),
        (")", "Felaktig gruppstart vid radslutet )"),
        ("2", "Felaktig gruppstart vid radslutet 2")]
        for input in inputs:
            self.assertEqual(readformula_test(input[0]), input[1])
if __name__ == '__main__':
    unittest.main()
