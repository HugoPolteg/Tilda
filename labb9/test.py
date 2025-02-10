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
        
        additional_molecules = [
            "C6H12O6",
            "CH3COOH",
            "C12H22O11",
            "Fe2(SO4)3",
            "H2SO4",
            "NH3",
            "C2H5OH",
            "C60",
            "C7H5(NO2)3",
            "(C6H5)2CH2",
            ""
        ]
        for molecule in additional_molecules:
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
        
        additional_inputs = [
            ("C12H22O11(", "Saknad högerparentes vid radslutet "),
            ("Fe2(SO4)3)", "Felaktig gruppstart vid radslutet )"),
            ("K4[ON(SO3)2]2", "Felaktig gruppstart vid radslutet [ON(SO3)2]2"),
            ("(NH4)2[Fe(CN)6", "Felaktig gruppstart vid radslutet [Fe(CN)6"),
            ("Mg(OH", "Saknad högerparentes vid radslutet "),
            ("H2O2)", "Felaktig gruppstart vid radslutet )"),
            ("(CH3)2CHCH2CH3)", "Felaktig gruppstart vid radslutet )"),
            ("(CH3(CH2)4CH3", "Saknad högerparentes vid radslutet "),
            ("(C6H5)2CH2)", "Felaktig gruppstart vid radslutet )"),
            ("()", "Felaktig gruppstart vid radslutet )"),
            ("F\nEH", "Okänd atom vid radslutet H"),
        ]
        for input in additional_inputs:
            self.assertEqual(readformula_test(input[0]), input[1])

    def testMultiLine(self):
        multi_line_molecules = [
            "H2O\nNaCl",
            "C6H12O6\nCH3COOH",
            "Fe2(SO4)3\nH2SO4"
        ]
        for molecule in multi_line_molecules:
            self.assertEqual(readformula_test(molecule), "Formeln är syntaktiskt korrekt")

if __name__ == '__main__':
    unittest.main()
