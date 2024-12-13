import unittest

from Fraction import Fraction, DenominatorIsZero, WrongTypeError


class TestFraction(unittest.TestCase):
    """Unit tests for the Fraction class."""

    """Test the creation of a valid Fraction."""

    def test_reduction_case(self):
        """Test the case where the fraction is reduced."""
        f = Fraction(3, 6)
        self.assertEqual(f.numerator, 1)
        self.assertEqual(f.denominator, 2)

    def test_zero_numerator(self):
        """Test the case where the numerator is zero."""
        f = Fraction(0, 5)
        self.assertEqual(f.numerator, 0)
        self.assertEqual(f.denominator, 1)

    def test_negative_numerator(self):
        """Test the case where the numerator is negative."""
        f = Fraction(-4, 6)
        self.assertEqual(f.numerator, -2)
        self.assertEqual(f.denominator, 3)

    def test_negative_denominator(self):
        """Test the case where the denominator is negative."""
        f = Fraction(4, -6)
        self.assertEqual(f.numerator, -2)
        self.assertEqual(f.denominator, 3)

    def test_both_negative(self):
        """Test the case where both the numerator and denominator are negative."""
        f = Fraction(-4, -6)
        self.assertEqual(f.numerator, 2)
        self.assertEqual(f.denominator, 3)

    def test_already_simplified(self):
        """Test the case where the fraction is already in its simplest form."""
        f = Fraction(3, 5)
        self.assertEqual(f.numerator, 3)
        self.assertEqual(f.denominator, 5)

    def test_denominator_one(self):
        """Test the case where the denominator is one."""
        f = Fraction(7, 1)
        self.assertEqual(f.numerator, 7)
        self.assertEqual(f.denominator, 1)

    def test_large_values(self):
        """Test fractions with large integer values."""
        f = Fraction(123456789, 987654321)
        self.assertEqual(f.numerator, 13717421)
        self.assertEqual(f.denominator, 109739369)

    """Test invalid fraction creation scenarios."""

    def test_zero_denominator(self):
        """Test the case where the denominator is zero."""
        with self.assertRaises(DenominatorIsZero):
            f = Fraction(3, 0)

    def test_invalid_numerator_type(self):
        """Test the case where the numerator is of an invalid type."""
        with self.assertRaises(TypeError):
            f = Fraction(3.5, 2)  # Numérateur float

    def test_invalid_denominator_type(self):
        """Test the case where the denominator is of an invalid type."""
        with self.assertRaises(TypeError):
            f = Fraction(3, "2")  # Dénominateur string

    def test_invalid_both_types(self):
        """Test the case where both numerator and denominator are of invalid types."""
        with self.assertRaises(TypeError):
            f = Fraction("3", "2")  # Numérateur string

    # Tests des représentations
    def test_str_simple_fraction(self):
        """Test the string representation of a simple fraction."""
        f = Fraction(3, 4)
        self.assertEqual(str(f), "3/4")

    def test_str_reduced_fraction(self):
        """Test the string representation of a reduced fraction."""
        f = Fraction(6, 8)
        self.assertEqual(str(f), "3/4")

    def test_str_integer_fraction(self):
        """Test the string representation of an integer fraction (denominator = 1)."""
        f = Fraction(5, 1)
        self.assertEqual(str(f), "5")

    def test_str_negative_numerator(self):
        """Test the string representation of a negative fraction (negative numerator)."""
        f = Fraction(-3, 4)
        self.assertEqual(str(f), "-3/4")

    def test_str_negative_denominator(self):
        """Test the string representation of a negative fraction (negative denominator)."""
        f = Fraction(3, -4)
        self.assertEqual(str(f), "-3/4")

    def test_str_both_negative(self):
        """Test the string representation of a negative fraction (both negative numerator and denominator)."""
        f = Fraction(-3, -4)
        self.assertEqual(str(f), "3/4")

    def test_str_unit_numerator(self):
        """Test the string representation of a fraction where the numerator is 1 (unit fraction)."""
        f = Fraction(1, 5)
        self.assertEqual(str(f), "1/5")

    def test_str_negative_unit_numerator(self):
        """Test the string representation of a negative unit fraction (numerator = -1)."""
        f = Fraction(-1, 7)
        self.assertEqual(str(f), "-1/7")

    def test_str_zero_fraction(self):
        """Test the string representation of a zero fraction."""
        f = Fraction(0, 5)
        self.assertEqual(str(f), "0")

    def test_str_reduced_fraction_integer(self):
        """Test the string representation of an integer fraction."""
        f = Fraction(4, 2)
        self.assertEqual(str(f), "2")

    """Test the representation of a fraction as a mixed number."""

    def test_str_improper_fraction(self):
        """Test the mixed number representation of an improper fraction."""
        f = Fraction(7, 3)
        self.assertEqual(f.as_mixed_number(), "2 + 1/3")

    def test_str_zero_numerator(self):
        """Test the mixed number representation of a fraction with a zero numerator."""
        f = Fraction(0, 5)
        self.assertEqual(f.as_mixed_number(), "0")

    def test_str_exact_integer_fraction(self):
        """Test the mixed number representation of an exact integer fraction."""
        f = Fraction(6, 3)
        self.assertEqual(f.as_mixed_number(), "2")

    def test_str_negative_improper_fraction(self):
        """Test the mixed number representation of a negative improper fraction."""
        f = Fraction(-7, 3)
        self.assertEqual(f.as_mixed_number(), "-2 - 1/3")

    def test_mixed_number_negative_denominator_improper_fraction(self):
        """Test the mixed number representation of an improper fraction with a negative denominator."""
        f = Fraction(7, -3)
        self.assertEqual(f.as_mixed_number(), "-2 - 1/3")

    def test_mixed_number_unit_fraction(self):
        """Test the mixed number representation of a unit fraction."""
        f = Fraction(1, 3)
        self.assertEqual(f.as_mixed_number(), "0 + 1/3")

    def test_mixed_number_negative_unit_fraction(self):
        """Test the mixed number representation of a negative unit fraction."""
        f = Fraction(-1, 3)
        self.assertEqual(f.as_mixed_number(), "0 - 1/3")

    def test_mixed_number_integer_with_denominator_one(self):
        """Test the mixed number representation of an integer with denominator 1."""
        f = Fraction(7, 1)
        self.assertEqual(f.as_mixed_number(), "7")

    # Tests des opérations de base
    """Test addition of fractions and other numeric types."""

    def test_addition_of_two_simple_fractions(self):
        """Test addition of two simple fractions."""
        f = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f + f2
        self.assertEqual(result.numerator, 5)
        self.assertEqual(result.denominator, 6)

    def test_addition_with_integer(self):
        """Test addition of a fraction with an integer."""
        f = Fraction(1, 2)
        val = 5
        result = f + val
        self.assertEqual(result.numerator, 11)
        self.assertEqual(result.denominator, 2)

    def test_addition_with_float(self):
        """Test addition of a fraction with a float."""
        f = Fraction(1, 3)
        val = 0.6
        result = f + val
        self.assertEqual(result.numerator, 14)
        self.assertEqual(result.denominator, 15)

    def test_addition_with_negative_fraction(self):
        """Test addition of a fraction with a negative fraction."""
        f = Fraction(1, 2)
        f2 = Fraction(-2, 3)
        result = f + f2
        self.assertEqual(result.numerator, -1)
        self.assertEqual(result.denominator, 6)

    def test_addition_with_negative_float(self):
        """Test addition of a fraction with a negative float."""
        f = Fraction(1, 2)
        val = -1.25
        result = f + val
        self.assertEqual(result.numerator, -3)
        self.assertEqual(result.denominator, 4)

    def test_addition_with_zero(self):
        """Test addition of a fraction with zero."""
        f = Fraction(1, 2)
        f2 = Fraction(0, 1)
        result = f + f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 2)

    def test_addition_of_fractions_with_common_denominator(self):
        """Test addition of two fractions with a common denominator."""
        f = Fraction(1, 4)
        f2 = Fraction(3, 4)
        result = f + f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 1)  # Result is an integer

    def test_addition_of_two_negative_fractions(self):
        """Test addition of two negative fractions."""
        f = Fraction(-1, 2)
        f2 = Fraction(-1, 3)
        result = f + f2
        self.assertEqual(result.numerator, -5)
        self.assertEqual(result.denominator, 6)

    def test_addition_with_large_values(self):
        """Test addition with large fraction values."""
        f = Fraction(1000, 2001)
        f2 = Fraction(3000, 4001)
        result = f + f2
        self.assertTrue(isinstance(result, Fraction))  # Ensure the result is a Fraction

    def test_addition_with_invalid_type(self):
        """Test that adding a fraction to an invalid type raises WrongTypeError."""
        f = Fraction(1, 2)
        with self.assertRaises(WrongTypeError):
            result = f + "invalid"  # Invalid type for addition

    """Test subtraction of fractions and other numeric types."""

    def test_subtraction_of_two_simple_fractions(self):
        """Test subtraction of two simple fractions."""
        f = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f - f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 6)

    def test_subtraction_with_integer(self):
        """Test subtraction of a fraction with an integer."""
        f = Fraction(1, 2)
        val = 5
        result = f - val
        self.assertEqual(result.numerator, -9)
        self.assertEqual(result.denominator, 2)

    def test_subtraction_with_float(self):
        """Test subtraction of a fraction with a float."""
        f = Fraction(1, 3)
        val = 0.6
        result = f - val
        self.assertEqual(result.numerator, -4)
        self.assertEqual(result.denominator, 15)

    def test_subtraction_with_negative_fraction(self):
        """Test subtraction of a fraction with a negative fraction."""
        f = Fraction(1, 2)
        f2 = Fraction(-2, 3)
        result = f - f2
        self.assertEqual(result.numerator, 7)
        self.assertEqual(result.denominator, 6)

    def test_subtraction_with_negative_float(self):
        """Test subtraction of a fraction with a negative float."""
        f = Fraction(1, 2)
        val = -1.25
        result = f - val
        self.assertEqual(result.numerator, 7)
        self.assertEqual(result.denominator, 4)

    def test_subtraction_with_zero(self):
        """Test subtraction of a fraction with zero."""
        f = Fraction(1, 2)
        f2 = Fraction(0, 1)
        result = f - f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 2)

    def test_subtraction_of_fractions_with_common_denominator(self):
        """Test subtraction of two fractions with a common denominator."""
        f = Fraction(3, 4)
        f2 = Fraction(1, 4)
        result = f - f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 2)

    def test_subtraction_of_two_negative_fractions(self):
        """Test subtraction of two negative fractions."""
        f = Fraction(-1, 2)
        f2 = Fraction(-1, 3)
        result = f - f2
        self.assertEqual(result.numerator, -1)
        self.assertEqual(result.denominator, 6)

    def test_subtraction_with_large_values(self):
        """Test subtraction with large fraction values."""
        f = Fraction(1000, 2001)
        f2 = Fraction(3000, 4001)
        result = f - f2
        self.assertTrue(isinstance(result, Fraction))  # Ensure the result is a Fraction

    def test_subtraction_result_is_negative(self):
        """Test subtraction where the result is negative."""
        f = Fraction(1, 4)
        f2 = Fraction(3, 4)
        result = f - f2
        self.assertEqual(result.numerator, -1)
        self.assertEqual(result.denominator, 2)

    def test_subtraction_with_invalid_type(self):
        """Test that subtracting a fraction with an invalid type raises WrongTypeError."""
        f = Fraction(1, 2)
        with self.assertRaises(WrongTypeError):
            result = f - "invalid"  # Invalid type for subtraction

    """Test multiplication of fractions and other numeric types."""

    def test_multiplication_of_two_simple_fractions(self):
        """Test multiplication of two simple fractions."""
        f = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f * f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 6)

    def test_multiplication_with_integer(self):
        """Test multiplication of a fraction with an integer."""
        f = Fraction(1, 2)
        val = 5
        result = f * val
        self.assertEqual(result.numerator, 5)
        self.assertEqual(result.denominator, 2)

    def test_multiplication_with_float(self):
        """Test multiplication of a fraction with a float."""
        f = Fraction(1, 3)
        val = 0.6
        result = f * val
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 5)

    def test_multiplication_with_negative_fraction(self):
        """Test multiplication of a fraction with a negative fraction."""
        f = Fraction(1, 2)
        f2 = Fraction(-2, 3)
        result = f * f2
        self.assertEqual(result.numerator, -1)
        self.assertEqual(result.denominator, 3)

    def test_multiplication_with_negative_integer(self):
        """Test multiplication of a fraction with a negative integer."""
        f = Fraction(1, 2)
        val = -4
        result = f * val
        self.assertEqual(result.numerator, -2)
        self.assertEqual(result.denominator, 1)

    def test_multiplication_resulting_in_unit_fraction(self):
        """Test multiplication of fractions resulting in a unit fraction (1/x)."""
        f = Fraction(1, 2)
        f2 = Fraction(2, 1)
        result = f * f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 1)

    def test_multiplication_with_zero(self):
        """Test multiplication of a fraction with zero."""
        f = Fraction(1, 2)
        f2 = Fraction(0, 1)
        result = f * f2
        self.assertEqual(result.numerator, 0)
        self.assertEqual(result.denominator, 1)

    def test_multiplication_with_simplified_fractions(self):
        """Test multiplication with fractions already simplified to their simplest form."""
        f = Fraction(4, 6)
        f2 = Fraction(9, 12)
        result = f * f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 2)

    def test_multiplication_with_large_values(self):
        """Test multiplication of fractions with large values."""
        f = Fraction(1000, 2001)
        f2 = Fraction(2000, 4003)
        result = f * f2
        self.assertTrue(isinstance(result, Fraction))  # Ensure the result is a Fraction

    def test_multiplication_resulting_in_negative_fraction(self):
        """Test multiplication of two fractions resulting in a negative fraction."""
        f = Fraction(3, 4)
        f2 = Fraction(-1, 4)
        result = f * f2
        self.assertEqual(result.numerator, -3)
        self.assertEqual(result.denominator, 16)

    def test_multiplication_with_invalid_type(self):
        """Test that multiplying a fraction with an invalid type raises WrongTypeError."""
        f = Fraction(1, 2)
        with self.assertRaises(WrongTypeError):
            result = f * "invalid"  # Invalid type for multiplication

    """Test division of fractions and other numeric types."""

    def test_division_of_two_simple_fractions(self):
        """Test division of two simple fractions."""
        f = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f / f2
        self.assertEqual(result.numerator, 3)
        self.assertEqual(result.denominator, 2)

    def test_division_by_integer(self):
        """Test division of a fraction by an integer."""
        f = Fraction(1, 2)
        val1 = 5
        result = f / val1
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 10)

    def test_division_by_float(self):
        """Test division of a fraction by a float."""
        f = Fraction(1, 3)
        val = 0.6
        result = f / val
        self.assertEqual(result.numerator, 5)
        self.assertEqual(result.denominator, 9)

    def test_division_by_negative_fraction(self):
        """Test division of a fraction by a negative fraction."""
        f = Fraction(1, 2)
        f2 = Fraction(-1, 4)
        result = f / f2
        self.assertEqual(result.numerator, -2)
        self.assertEqual(result.denominator, 1)

    def test_division_by_negative_integer(self):
        """Test division of a fraction by a negative integer."""
        f = Fraction(1, 3)
        val = -3
        result = f / val
        self.assertEqual(result.numerator, -1)
        self.assertEqual(result.denominator, 9)

    def test_division_by_one(self):
        """Test division of a fraction by 1."""
        f = Fraction(1, 2)
        f2 = Fraction(1, 2)
        result = f / f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 1)

    def test_division_resulting_in_unit_fraction(self):
        """Test division of two fractions resulting in a unit fraction (1)."""
        f = Fraction(3, 4)
        f2 = Fraction(3, 4)
        result = f / f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 1)

    def test_division_by_fraction_with_larger_numerator(self):
        """Test division of a fraction by a fraction with a larger numerator."""
        f = Fraction(2, 3)
        f2 = Fraction(5, 3)
        result = f / f2
        self.assertEqual(result.numerator, 2)
        self.assertEqual(result.denominator, 5)

    def test_division_by_zero(self):
        """Test division by zero (should raise DenominatorIsZero)."""
        f = Fraction(1, 2)
        f2 = Fraction(0, 1)
        with self.assertRaises(DenominatorIsZero):
            result = f / f2

    def test_division_of_negative_fraction_by_positive_fraction(self):
        """Test division of a negative fraction by a positive fraction."""
        f = Fraction(-3, 5)
        f2 = Fraction(2, 7)
        result = f / f2
        self.assertEqual(result.numerator, -21)
        self.assertEqual(result.denominator, 10)

    def test_division_of_positive_fraction_by_negative_fraction(self):
        """Test division of a positive fraction by a negative fraction."""
        f = Fraction(2, 7)
        f2 = Fraction(-3, 5)
        result = f / f2
        self.assertEqual(result.numerator, -10)
        self.assertEqual(result.denominator, 21)

    def test_division_with_invalid_type(self):
        """Test that dividing a fraction by an invalid type raises WrongTypeError."""
        f = Fraction(1, 2)
        with self.assertRaises(WrongTypeError):
            result = f / "invalid"  # Invalid type for division

    """Test power of fractions with various cases."""

    def test_power_positive_integer_exponent(self):
        """Test power of a fraction with a positive integer exponent."""
        f = Fraction(1, 2)
        val = 5
        result = f ** val
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 32)

    def test_power_fractional_exponent(self):
        """Test power of a fraction with a fractional exponent."""
        f = Fraction(1, 3)
        val = 0.5
        result = f ** val
        self.assertAlmostEqual(float(result), (1 / 3) ** 0.5)
        self.assertTrue(isinstance(result, Fraction))

    def test_power_negative_integer_exponent(self):
        """Test power of a fraction with a negative integer exponent."""
        f = Fraction(1, 2)
        val = -2
        result = f ** val
        self.assertEqual(result.numerator, 4)
        self.assertEqual(result.denominator, 1)

    def test_power_zero_exponent(self):
        """Test power of a fraction with an exponent of zero."""
        f = Fraction(1, 2)
        val = 0
        result = f ** val
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 1)

    def test_power_invalid_exponent(self):
        """Test that an invalid exponent raises an exception."""
        f = Fraction(1, 2)
        val = "invalid"
        with self.assertRaises(TypeError):
            result = f ** val

    def test_power_fractional_root_simplification(self):
        """Test power of a fraction with a fractional exponent resulting in simplification."""
        f = Fraction(9, 16)
        val = 0.5  # Square root
        result = f ** val
        self.assertEqual(result.numerator, 3)
        self.assertEqual(result.denominator, 4)

    def test_power_negative_fraction(self):
        """Test power of a negative fraction with integer exponents."""
        f = Fraction(-1, 2)
        val = 2
        result2 = f ** val
        self.assertEqual(result2.numerator, 1)
        self.assertEqual(result2.denominator, 4)

    def test_power_with_improper_fraction(self):
        """Test power of an improper fraction."""
        f = Fraction(5, 2)
        val = 2
        result = f ** val
        self.assertEqual(result.numerator, 25)
        self.assertEqual(result.denominator, 4)

    def test_power_negative_with_improper_fraction(self):
        """Test negative exponent with an improper fraction."""
        f = Fraction(5, 2)
        val = -1
        result = f ** val
        self.assertEqual(result.numerator, 2)
        self.assertEqual(result.denominator, 5)

    # Tests des comparaisons et des vérifications

    """Test equality between fractions and other types."""

    def test_equality_between_two_simplified_fractions(self):
        """Test if two simplified fractions are considered equal (2/4 == 1/2)."""
        f = Fraction(2, 4)  # Equivalent to 1/2
        f2 = Fraction(1, 2)  # Equivalent to 1/2
        self.assertTrue(f == f2)

    def test_equality_between_positive_and_negative_simplified_fractions(self):
        """Test if a positive fraction and its equivalent negative simplified form are equal (-2/-4 == 1/2)."""
        f = Fraction(2, 4)  # Equivalent to 1/2
        f2 = Fraction(-2, -4)  # Equivalent to 1/2
        self.assertTrue(f == f2)

    def test_inequality_with_different_fractions(self):
        """Test if two different fractions are not considered equal (2/4 != 3/4)."""
        f = Fraction(2, 4)  # Equivalent to 1/2
        f2 = Fraction(3, 4)
        self.assertFalse(f == f2)

    def test_equality_of_two_zero_fractions(self):
        """Test that two zero fractions are considered equal regardless of their representation."""
        f = Fraction(0, 1)  # Zero fraction
        f2 = Fraction(0, 5)  # Another representation of zero
        self.assertTrue(f == f2)  # 0/1 == 0/5

    def test_equality_of_zero_fraction_with_integer_zero(self):
        """Test that a zero fraction is considered equal to the integer zero."""
        f = Fraction(0, 1)  # Zero fraction
        val = 0  # Zero as an integer
        self.assertTrue(f == val)  # Zero fraction == zero integer

    def test_inequality_of_nonzero_fraction_with_zero_fraction(self):
        """Test that a nonzero fraction is not equal to a zero fraction."""
        f = Fraction(1, 2)  # Nonzero fraction
        f2 = Fraction(0, 1)  # Zero fraction
        self.assertFalse(f == f2)  # 1/2 != 0

    def test_equality_of_fraction_with_equivalent_float(self):
        """Test that a fraction is equal to its equivalent float value."""
        f = Fraction(1, 2)  # Equivalent to 0.5
        val = 0.5  # Float equivalent to 1/2
        self.assertTrue(f == val)  # 1/2 == 0.5

    def test_inequality_of_fraction_with_integer(self):
        """Test that a fraction is not equal to an integer with a different value."""
        f = Fraction(1, 2)  # Fraction
        val = 3  # Integer
        self.assertFalse(f == val)  # 1/2 != 3

    def test_equality_of_fraction_with_direct_float_value(self):
        """Test that a fraction is equal to a directly provided float value."""
        f = Fraction(1, 2)  # Equivalent to 0.5
        val = 0.5
        self.assertTrue(f == val)  # 1/2 == 0.5

    def test_fraction_equality_with_invalid_type(self):
        """Test that comparing fractions with invalid types raises an exception."""
        f = Fraction(2, 4)  # Equivalent to 1/2
        val = "not a fraction"  # Invalid type
        with self.assertRaises(WrongTypeError):
            result = f == val

    def test_fraction_equality_reflexive_and_identical(self):
        """Test reflexive equality and equality between identical fractions."""
        f = Fraction(2, 4)  # Equivalent to 1/2
        f2 = Fraction(2, 4)
        self.assertTrue(f == f2)  # Reflexive check

    def test_fraction_equality_with_opposite_fractions(self):
        """Test equality between fractions that are opposites."""
        f = Fraction(2, 4)  # Equivalent to 1/2
        f2 = Fraction(-1, 2)  # Equivalent to -1/2
        self.assertFalse(f == f2)  # 1/2 != -1/2

    def test_fraction_equality_with_improper_fractions(self):
        """Test equality between proper and improper fractions."""
        f = Fraction(2, 4)  # Equivalent to 1/2
        f2 = Fraction(10, 20)  # Equivalent to 1/2
        self.assertTrue(f == f2)  # 1/2 == 10/20

    """Test conversion of a fraction to a float."""

    def test_positive_simple_fraction(self):
        """Test conversion of a simple positive fraction to float."""
        f = Fraction(1, 2)
        self.assertAlmostEqual(float(f), 0.5)

    def test_negative_fraction(self):
        """Test conversion of a negative fraction to float."""
        f = Fraction(-1, 2)
        self.assertAlmostEqual(float(f), -0.5)

    def test_fraction_with_zero_numerator_to_float(self):
        """Test conversion of a fraction with zero numerator to float."""
        f = Fraction(0, 5)
        self.assertEqual(float(f), 0.0)  # Any fraction with a zero numerator should be 0.0

    def test_integer_fraction(self):
        """Test conversion of an integer fraction to float."""
        f = Fraction(4, 2)
        self.assertEqual(float(f), 2.0)  # 4/2 == 2

    def test_large_numerator_and_denominator(self):
        """Test conversion of a fraction with large numerator and denominator to float."""
        f = Fraction(100000, 200000)
        self.assertEqual(float(f), 0.5)  # 100000/200000 == 0.5

    def test_negative_integer_fraction_to_float(self):
        """Test conversion of a negative integer fraction to float."""
        f = Fraction(-7, 1)
        self.assertEqual(float(f), -7.0)  # -7/1 == -7

    def test_negative_fraction_with_negative_values(self):
        """Test conversion of a fraction with both negative numerator and denominator to float."""
        f = Fraction(-5, -10)
        self.assertEqual(float(f), 0.5)  # -5/-10 == 0.5

    def test_fraction_with_periodic_decimal(self):
        """Test conversion of a fraction resulting in a periodic decimal to float."""
        f = Fraction(1, 3)
        self.assertAlmostEqual(float(f), 0.3333333333333333, places=15)  # 1/3 is a repeating decimal

    """Test if a fraction is zero."""

    def test_non_zero_fraction(self):
        """Test that a fraction with a non-zero numerator is not zero."""
        f = Fraction(2, 3)
        self.assertFalse(f.is_zero())  # 2/3 n'est pas zéro

    def test_negative_non_zero_fraction(self):
        """Test that a negative fraction with a non-zero numerator is not zero."""
        f = Fraction(-2, 3)
        self.assertFalse(f.is_zero())  # -2/3 n'est pas zéro

    def test_reduced_fraction_with_zero_numerator(self):
        """Test that a reduced fraction with zero numerator is considered zero."""
        f = Fraction(0, -5)
        self.assertTrue(f.is_zero())  # 0/-5 devrait être zéro

    def test_fraction_with_zero_numerator_and_negative_denominator(self):
        """Test that a fraction with zero numerator and negative denominator is considered zero."""
        f = Fraction(0, -1)
        self.assertTrue(f.is_zero())  # 0/-1 est toujours zéro

    """Test if a fraction is integer."""

    def test_fraction_that_is_integer(self):
        """Test fraction that is an integer (4/2 = 2)."""
        f = Fraction(4, 2)
        self.assertTrue(f.is_integer())  # 4/2 is an integer, 2

    def test_fraction_that_is_already_an_integer(self):
        """Test fraction that is already an integer (6/1 = 6)."""
        f = Fraction(6, 1)
        self.assertTrue(f.is_integer())  # 6/1 is an integer, 6

    def test_negative_integer_fraction(self):
        """Test negative integer fraction (-8/4 = -2)."""
        f = Fraction(-8, 4)
        self.assertTrue(f.is_integer())  # -8/4 is an integer, -2

    def test_integer_fraction_with_negative_denominator(self):
        """Test integer fraction with negative denominator (-9/-3 = 3)."""
        f = Fraction(-9, -3)
        self.assertTrue(f.is_integer())  # -9/-3 is an integer, 3

    def test_fraction_that_is_not_an_integer(self):
        """Test fraction that is not an integer (3/4)."""
        f = Fraction(3, 4)
        self.assertFalse(f.is_integer())  # 3/4 is not an integer

    def test_proper_fraction_that_is_not_an_integer(self):
        """Test proper fraction that is not an integer (1/3)."""
        f = Fraction(1, 3)
        self.assertFalse(f.is_integer())  # 1/3 is not an integer

    def test_fraction_with_zero_numerator(self):
        """Test fraction with zero numerator (0/5 = 0)."""
        f = Fraction(0, 5)
        self.assertTrue(f.is_integer())  # 0/5 is an integer, 0

    """Test if a fraction is proper."""

    def test_proper_fraction_with_positive_numerator(self):
        """Test if the fraction is proper (numerator < denominator)."""
        f = Fraction(1, 2)
        self.assertTrue(f.is_proper())  # 1/2 is a proper fraction

    def test_proper_fraction_with_negative_numerator(self):
        """Test if the fraction is proper with a negative numerator (-1/2)."""
        f = Fraction(-1, 2)
        self.assertTrue(f.is_proper())  # -1/2 is a proper fraction

    def test_proper_fraction_with_larger_denominator(self):
        """Test if the fraction is proper with larger values (1/3)."""
        f = Fraction(1, 3)
        self.assertTrue(f.is_proper())  # 1/3 is a proper fraction

    def test_improper_fraction_with_larger_numerator(self):
        """Test if the fraction is improper (numerator > denominator)."""
        f = Fraction(3, 2)
        self.assertFalse(f.is_proper())  # 3/2 is not a proper fraction

    def test_improper_fraction_with_negative_larger_numerator(self):
        """Test if the fraction is improper with a negative numerator (-3/2)."""
        f = Fraction(-3, 2)
        self.assertFalse(f.is_proper())  # -3/2 is not a proper fraction

    def test_fraction_equivalent_to_an_integer(self):
        """Test if the fraction is an integer (numerator = denominator, 2/2 = 1)."""
        f = Fraction(2, 2)
        self.assertFalse(f.is_proper())  # 2/2 is not a proper fraction (equivalent to 1)

    def test_negative_fraction_equivalent_to_an_integer(self):
        """Test if the negative fraction is an integer (-3/-3 = 1)."""
        f = Fraction(-3, -3)
        self.assertFalse(f.is_proper())  # -3/-3 is not a proper fraction (equivalent to 1)

    def test_integer_fraction_with_denominator_one(self):
        """Test if the fraction is an integer with denominator 1 (4/1 = 4)."""
        f = Fraction(4, 1)
        self.assertFalse(f.is_proper())  # 4/1 is not a proper fraction (equivalent to 4)

    def test_fraction_equivalent_to_zero(self):
        """Test if the fraction is equivalent to zero (0/5 = 0)."""
        f = Fraction(0, 5)
        self.assertTrue(f.is_proper())  # 0/5 is a proper fraction (0 is considered proper)

    """Test if a fraction is a unit fraction."""

    def test_unit_fraction_with_positive_numerator(self):
        """Test if the fraction is a unit fraction with a positive numerator (1/3)."""
        f = Fraction(1, 3)
        self.assertTrue(f.is_unit())  # 1/3 is a unit fraction

    def test_unit_fraction_with_negative_numerator(self):
        """Test if the fraction is a unit fraction with a negative numerator (-1/3)."""
        f = Fraction(-1, 3)
        self.assertTrue(f.is_unit())  # -1/3 is a unit fraction

    def test_unit_fraction_with_negative_numerator_absolute_value_equal_to_1(self):
        """Test if the fraction is a unit fraction with a negative numerator but absolute value equal to 1 (-1/4)."""
        f = Fraction(-1, 4)
        self.assertTrue(f.is_unit())  # -1/4 is a unit fraction

    def test_non_unit_fraction_with_numerator_greater_than_1(self):
        """Test if the fraction is not a unit fraction when the numerator is greater than 1 (3/4)."""
        f = Fraction(3, 4)
        self.assertFalse(f.is_unit())  # 3/4 is not a unit fraction

    def test_non_unit_fraction_with_numerator_less_than_minus_1(self):
        """Test if the fraction is not a unit fraction when the numerator is less than -1 (-5/6)."""
        f = Fraction(-5, 6)
        self.assertFalse(f.is_unit())  # -5/6 is not a unit fraction

    def test_unit_integer_fraction(self):
        """Test if the fraction is considered a unit fraction when it is an integer (4/4 = 1)."""
        f = Fraction(4, 4)
        self.assertTrue(f.is_unit())  # 4/4 is an integer (equivalent to 1)

    def test_zero_fraction(self):
        """Test if the fraction is not a unit fraction when the numerator is 0 (0/5)."""
        f = Fraction(0, 5)
        self.assertFalse(f.is_unit())  # 0/5 is not a unit fraction

    def test_unit_fraction_with_large_denominator(self):
        """Test if the fraction is a unit fraction with a large denominator (1/1000)."""
        f = Fraction(1, 1000)
        self.assertTrue(f.is_unit())  # 1/1000 is a unit fraction

    def test_unit_fraction_with_large_negative_numerator(self):
        """Test if the fraction is a unit fraction with a large negative numerator (-1/500)."""
        f = Fraction(-1, 500)
        self.assertTrue(f.is_unit())  # -1/500 is a unit fraction

    """Test if two fractions are adjacent."""

    def test_fractions_are_adjacent(self):
        """Test if two fractions are adjacent with a difference of 1 (1/3 and 2/3)."""
        f = Fraction(1, 3)
        f2 = Fraction(2, 3)
        self.assertTrue(f.is_adjacent_to(f2))  # Fractions are adjacent

    def test_fractions_are_not_adjacent(self):
        """Test if two fractions are not adjacent (1/4 and 2/5)."""
        f = Fraction(1, 4)
        f2 = Fraction(2, 5)
        self.assertFalse(f.is_adjacent_to(f2))  # Fractions are not adjacent

    def test_fractions_with_negative_numerators_are_not_adjacent(self):
        """Test if two fractions with negative numerators are not adjacent (-1/3 and 1/3)."""
        f = Fraction(-1, 3)
        f2 = Fraction(1, 3)
        self.assertFalse(f.is_adjacent_to(f2))  # Fractions are not adjacent

    def test_fractions_with_one_integer_are_adjacent(self):
        """Test if two fractions are adjacent with one fraction being an integer (1/2 and 3/2)."""
        f = Fraction(1, 2)
        f2 = Fraction(3, 2)
        self.assertTrue(f.is_adjacent_to(f2))  # Fractions are adjacent

    def test_integer_and_fraction_are_adjacent(self):
        """Test if an integer and a fraction are adjacent (3 and 7/2)."""
        f = Fraction(7, 2)
        val = 3
        self.assertTrue(f.is_adjacent_to(val))  # Integer and fraction are adjacent

    def test_integer_and_fraction_are_not_adjacent(self):
        """Test if an integer and a fraction are not adjacent (2 and 5/2)."""
        f = Fraction(5, 2)
        val = 2
        self.assertTrue(f.is_adjacent_to(val))  # Integer and fraction are not adjacent

    def test_fractions_are_close_but_not_adjacent(self):
        """Test if two fractions that are close but not adjacent (1/5 and 2/5)."""
        f = Fraction(1, 5)
        f2 = Fraction(2, 5)
        self.assertTrue(f.is_adjacent_to(f2))  # Fractions are not adjacent

    def test_unit_fractions_are_adjacent(self):
        """Test if two unit fractions are adjacent (1/5 and 1/6)."""
        f = Fraction(1, 5)
        f2 = Fraction(1, 6)
        self.assertTrue(f.is_adjacent_to(f2))  # Unit fractions are adjacent

    def test_fractions_approaching_an_integer_are_adjacent(self):
        """Test if fractions that are close to an integer are adjacent (3/4 and 4/4)."""
        f = Fraction(3, 4)
        f2 = Fraction(4, 4)
        self.assertTrue(f.is_adjacent_to(f2))  # Fractions are adjacent

    def test_is_adjacent_to_with_invalid_type(self):
        """Test that calling is_adjacent_to with an invalid type raises WrongTypeError."""
        f = Fraction(1, 2)
        with self.assertRaises(WrongTypeError):
            result = f.is_adjacent_to("invalid")  # Invalid type for is_adjacent_to

    """Test that unsupported types raise a TypeError in convert_to_fraction."""

    def test_invalid_list(self):
        """Test that a list raises a TypeError when passed to convert_to_fraction."""
        val = [1, 2]
        with self.assertRaises(TypeError):
            result = Fraction.convert_to_fraction(val)  # Invalid list

    def test_invalid_dict(self):
        """Test that a dictionary raises a TypeError when passed to convert_to_fraction."""
        val = {'key': 'value'}
        with self.assertRaises(TypeError):
            result = Fraction.convert_to_fraction(val)  # Invalid dictionary

    def test_invalid_string(self):
        """Test that a string raises a TypeError when passed to convert_to_fraction."""
        val = "invalid_string"
        with self.assertRaises(TypeError):
            result = Fraction.convert_to_fraction(val)  # Invalid string

    def test_invalid_object(self):
        """Test that an object raises a TypeError when passed to convert_to_fraction."""
        val = object()
        with self.assertRaises(TypeError):
            result = Fraction.convert_to_fraction(val)  # Invalid object

    def test_invalid_boolean(self):
        """Test that a boolean raises a TypeError when passed to convert_to_fraction."""
        val = True
        with self.assertRaises(TypeError):
            result = Fraction.convert_to_fraction(val)  # Invalid boolean

    def test_invalid_none(self):
        """Test that None raises a TypeError when passed to convert_to_fraction."""
        val = None
        with self.assertRaises(TypeError):
            result = Fraction.convert_to_fraction(val)  # Invalid None


if __name__ == '__main__':
    unittest.main()
