import unittest
from main import readmolecule_test

class MoleculeTest(unittest.TestCase):
    def testMolecule(self):
        molecules = ["Na",
        "H2O"
        ]
        for molecule in molecules:
            self.assertEqual(readmolecule_test(molecule), "Formeln är syntaktiskt korrekt")
    def testFalse(self):
        inputs =[
        ("H0", "För litet tal vid radslutet "),
        ("a", "Saknad stor bokstav vid radslutet a"),
        ]
        for input in inputs:
            self.assertEqual(readmolecule_test(input[0]), input[1])

if __name__ == '__main__':
    unittest.main()