from multiprocessing.sharedctypes import Value
import unittest
from pycpfcnpj import cpfcnpj


class CPFCNPJTests(unittest.TestCase):
    """docstring for CPFCNPJTests"""

    def setUp(self):
        self.valid_cpf = "11144477735"
        self.invalid_cpf = "11144477736"
        self.invalid_cpf_size = "111444777"
        self.invalid_cpf_whitespaces = "111444 77735"
        self.valid_cnpj = "11444777000161"
        self.invalid_cnpj = "11444777000162"
        self.invalid_cnpj_size = "114447770001"
        self.invalid_cnpj_whitespaces = "11444 777000161"
        self.invalid_cpf_with_alphabetic = "111444A77735"
        self.invalid_cnpj_with_alphabetic = "11444d777000161"

        self.mascared_valid_cpf = "111.444.777-35"
        self.mascared_invalid_cpf = "111.444.777-36"
        self.mascared_invalid_cpf_size = "111.444.777"
        self.mascared_valid_cnpj = "11.444.777/0001-61"
        self.mascared_invalid_cnpj = "11.444.777/0001-62"
        self.mascared_invalid_cnpj_size = "114.447/7700-01"

    def test_validate_cpf_true(self):
        self.assertTrue(cpfcnpj.validate(self.valid_cpf))

    def test_validate_cpf_false(self):
        self.assertFalse(cpfcnpj.validate(self.invalid_cpf))

    def test_validate_unicode_cpf_tru(self):
        self.assertTrue(cpfcnpj.validate(u"11144477735"))

    def test_validate_cnpj_true(self):
        self.assertTrue(cpfcnpj.validate(self.valid_cnpj))

    def test_validate_cnpj_false(self):
        self.assertFalse(cpfcnpj.validate(self.invalid_cnpj))

    def test_validate_unicode_cnpj_true(self):
        self.assertTrue(cpfcnpj.validate(u"11444777000161"))

    def test_wrong_cpf_size(self):
        self.assertFalse(cpfcnpj.validate(self.invalid_cpf_size))

    def test_wrong_cnpj_size(self):
        self.assertFalse(cpfcnpj.validate(self.invalid_cnpj_size))

    def mascared_test_validate_cpf_true(self):
        self.assertTrue(cpfcnpj.validate(self.mascared_valid_cpf))

    def mascared_test_validate_cpf_false(self):
        self.assertFalse(cpfcnpj.validate(self.mascared_invalid_cpf))

    def mascared_test_validate_cnpj_true(self):
        self.assertTrue(cpfcnpj.validate(self.mascared_valid_cnpj))

    def mascared_test_validate_cnpj_false(self):
        self.assertFalse(cpfcnpj.validate(self.mascared_invalid_cnpj))

    def mascared_test_wrong_cpf_size(self):
        self.assertFalse(cpfcnpj.validate(self.mascared_invalid_cpf_size))

    def mascared_test_wrong_cnpj_size(self):
        self.assertFalse(cpfcnpj.validate(self.mascared_invalid_cnpj_size))

    def test_validate_cnpj_with_whitespace(self):
        self.assertFalse(cpfcnpj.validate(self.invalid_cnpj_whitespaces))

    def test_validate_cpf_with_whitespace(self):
        self.assertFalse(cpfcnpj.validate(self.invalid_cpf_whitespaces))

    def test_validate_cnpj_with_alphabetic_characters(self):
        self.assertFalse(cpfcnpj.validate(self.invalid_cnpj_with_alphabetic))

    def test_validate_cpf_with_alphabetic_characters(self):
        self.assertFalse(cpfcnpj.validate(self.invalid_cpf_with_alphabetic))


if __name__ == "__main__":
    unittest.main(verbosity=2)
