import unittest
from Fraction import Fraction, DenominatorIsZero, WrongTypeError

class TestFraction(unittest.TestCase):
    """Unit tests for the Fraction class."""

    # Tests de création
    def test_fraction_creation(self):
        """Test the creation of a valid Fraction."""
        f = Fraction(3, 6)
        self.assertEqual(f.numerator, 1)
        self.assertEqual(f.denominator, 2)

    def test_fraction_zero_denominator(self):
        """Test that a zero denominator raises an exception."""
        with self.assertRaises(DenominatorIsZero):
            Fraction(1, 0)

    def test_fraction_invalid_types(self):
        """Test that invalid types raise a TypeError."""
        with self.assertRaises(TypeError):
            Fraction("1", 2)
        with self.assertRaises(TypeError):
            Fraction(1, "2")

    def test_fraction_Wrong_values(self):
        f1 = Fraction(1, 2)
        with self.assertRaises(WrongTypeError):
            f1 + "invalid"
        with self.assertRaises(WrongTypeError):
            f1 - "invalid"
        with self.assertRaises(WrongTypeError):
            f1 * "invalid"
        with self.assertRaises(WrongTypeError):
            f1 / "invalid"
        with self.assertRaises(WrongTypeError):
            f1.is_adjacent_to("invalid")

    # Tests des représentations
    def test_fraction_string_representation(self):
        """Test the string representation of a fraction."""
        f = Fraction(3, 4)
        self.assertEqual(str(f), "3/4")

    def test_fraction_string_representation_integer(self):
        """Test the string representation of an integer fraction."""
        f = Fraction(4, 2)
        self.assertEqual(str(f), "2/1")

    def test_fraction_as_mixed_number(self):
        """Test the representation of a fraction as a mixed number."""
        f = Fraction(7, 3)
        self.assertEqual(f.as_mixed_number(), "2 + 1/3")

    def test_fraction_as_mixed_number_no_fraction_part(self):
        """Test the mixed number representation when there's no fraction part."""
        f = Fraction(6, 3)
        self.assertEqual(f.as_mixed_number(), "2 + 0/1")  # Peut être ajusté si on souhaite éviter cette forme

    # Tests des opérations de base
    def test_fraction_addition(self):
        """Test addition of two fractions."""
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result1 = f1 + f2
        self.assertEqual(result1.numerator, 5)
        self.assertEqual(result1.denominator, 6)

        val1 = 5
        val2 = 0.6
        result2 = f1 + val1
        self.assertEqual(result2.numerator, 11)
        self.assertEqual(result2.denominator, 2)

        result3 = f2 + val2
        self.assertEqual(result3.numerator, 14)
        self.assertEqual(result3.denominator, 15)


    def test_fraction_subtraction(self):
        """Test subtraction of two fractions."""
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result1 = f1 - f2
        self.assertEqual(result1.numerator, 1)
        self.assertEqual(result1.denominator, 6)

        val1 = 5
        val2 = 0.6
        result2 = f1 - val1
        self.assertEqual(result2.numerator, -9)
        self.assertEqual(result2.denominator, 2)

        result3 = f2 - val2
        self.assertEqual(result3.numerator, -4)
        self.assertEqual(result3.denominator, 15)


    def test_fraction_multiplication(self):
        """Test multiplication of two fractions."""
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 * f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 6)

        val1 = 5
        val2 = 0.6
        result2 = f1 * val1
        self.assertEqual(result2.numerator, 5)
        self.assertEqual(result2.denominator, 2)

        result3 = f2 * val2
        self.assertEqual(result3.numerator, 1)
        self.assertEqual(result3.denominator, 5)


    def test_fraction_division(self):
        """Test division of two fractions."""
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 / f2
        self.assertEqual(result.numerator, 3)
        self.assertEqual(result.denominator, 2)

        val1 = 5
        val2 = 0.6
        result2 = f1 / val1
        self.assertEqual(result2.numerator, 1)
        self.assertEqual(result2.denominator, 10)

        result3 = f2 / val2
        self.assertEqual(result3.numerator, 5)
        self.assertEqual(result3.denominator, 9)


    def test_fraction_power(self):
        """Test power of a fractions."""
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        val1 = 5
        val2 = 0.5
        val3 = "invalid"

        result1 = f1 ** val1
        self.assertEqual(result1.numerator, 1)
        self.assertEqual(result1.denominator, 32)

        result2 = f2 ** val2
        self.assertEqual(result2.numerator, 2886751345948129)
        self.assertEqual(result2.denominator, 5000000000000000)

        """Test that invalid Types raise a TypeError """
        with self.assertRaises(TypeError):
                f1 ** val3

    # Tests des comparaisons et des vérifications
    def test_fraction_equality(self):
        """Test equality between fractions."""
        f1 = Fraction(2, 4)
        f2 = Fraction(1, 2)
        val1 = 3
        val2 = 0.5

        self.assertTrue(f1 == f2)
        self.assertFalse(f1 == val1)
        self.assertTrue(f2 == val2)

    def test_fraction_as_float(self):
        """Test conversion of a fraction to a float."""
        f = Fraction(1, 2)
        self.assertAlmostEqual(float(f), 0.5)

    def test_is_zero(self):
        """Test if a fraction is zero."""
        f = Fraction(0, 3)
        self.assertTrue(f.is_zero())

    def test_is_integer(self):
        """Test if a fraction is an integer."""
        f = Fraction(4, 2)
        self.assertTrue(f.is_integer())

    def test_is_proper(self):
        """Test if a fraction is proper."""
        f = Fraction(1, 2)
        self.assertTrue(f.is_proper())

    def test_is_unit(self):
        """Test if a fraction is a unit fraction."""
        f = Fraction(1, 3)
        self.assertTrue(f.is_unit())

    def test_is_adjacent_to(self):
        """Test if two fractions are adjacent."""
        f1 = Fraction(1, 3)
        f2 = Fraction(1, 2)
        val1 = 1
        val2 = 0.5
        self.assertTrue(f1.is_adjacent_to(f2))
        self.assertFalse(f1.is_adjacent_to(val1))
        self.assertTrue(f1.is_adjacent_to(val2))

    def test_convert_to_fraction_unsupported_type(self):
        with self.assertRaises(TypeError):
            Fraction.convert_to_fraction([1, 2])  # Liste invalide
        with self.assertRaises(TypeError):
            Fraction.convert_to_fraction({'key': 'value'})  # Dictionnaire invalide

if __name__ == '__main__':
    unittest.main()