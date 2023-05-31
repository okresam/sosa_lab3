import unittest
import Dodatak_A

class Dodatak_A_Test(unittest.TestCase):
	
    def test_perform_division1(self):
        self.assertEqual(Dodatak_A.OperationsManager(10, 2).perform_division(), 5)

    def test_perform_division2(self):
        self.assertEqual(Dodatak_A.OperationsManager(5, 2.5).perform_division(), 2)

    def test_perform_division3(self):
        self.assertEqual(Dodatak_A.OperationsManager(5, 0).perform_division(), None)

    def test_perform_division4(self):
        with self.assertRaises(ValueError):
            Dodatak_A.OperationsManager("ABC", 5).perform_division()
    
    def test_square_root1(self):
        self.assertEqual(Dodatak_A.square_root(9), 3)

    def test_square_root2(self):
        self.assertEqual(Dodatak_A.square_root(-9), None)

    def test_square_root3(self):
        with self.assertRaises(ValueError):
            Dodatak_A.square_root("abcd")

    def test_validate_string_length1(self):
        self.assertEqual(Dodatak_A.validate_string_length("abc"), "abc")

    def test_validate_string_length2(self):
        self.assertEqual(Dodatak_A.validate_string_length("abcdefgh"), "abcde")

    def test_validate_string_length3(self):
        with self.assertRaises(ValueError):
            Dodatak_A.validate_string_length(123)

    def test_validate_string_length4(self):
        with self.assertRaises(ValueError):
            Dodatak_A.validate_string_length([10, 2, 4])
    

if __name__ == '__main__':
    unittest.main()