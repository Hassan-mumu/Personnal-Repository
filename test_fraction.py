import unittest
from Fraction import Fraction, DenominatorIsZero, WrongTypeError


class TestFraction(unittest.TestCase):
    """Unit tests for the Fraction class."""

    def test_fraction_creation(self):
        """Test the creation of a valid Fraction."""
        # Cas de réduction
        f = Fraction(3, 6)
        self.assertEqual(f.numerator, 1)
        self.assertEqual(f.denominator, 2)

        # Cas où le numérateur est zéro
        f_zero = Fraction(0, 5)
        self.assertEqual(f_zero.numerator, 0)
        self.assertEqual(f_zero.denominator, 1)

        # Cas de nombre négatif (numérateur négatif)
        f_neg_num = Fraction(-4, 6)
        self.assertEqual(f_neg_num.numerator, -2)
        self.assertEqual(f_neg_num.denominator, 3)

        # Cas de nombre négatif (dénominateur négatif)
        f_neg_den = Fraction(4, -6)
        self.assertEqual(f_neg_den.numerator, -2)
        self.assertEqual(f_neg_den.denominator, 3)

        # Cas où les deux sont négatifs
        f_both_neg = Fraction(-4, -6)
        self.assertEqual(f_both_neg.numerator, 2)
        self.assertEqual(f_both_neg.denominator, 3)

        # Cas où la fraction est déjà sous forme réduite
        f_simple = Fraction(3, 5)
        self.assertEqual(f_simple.numerator, 3)
        self.assertEqual(f_simple.denominator, 5)

        # Cas où le dénominateur est 1
        f_whole = Fraction(7, 1)
        self.assertEqual(f_whole.numerator, 7)
        self.assertEqual(f_whole.denominator, 1)

    def test_invalid_fraction_creation(self):
        """Test invalid fraction creation scenarios."""
        # Cas où le dénominateur est zéro
        with self.assertRaises(DenominatorIsZero):
            Fraction(3, 0)

        # Cas où les types des paramètres sont invalides
        with self.assertRaises(TypeError):
            Fraction(3.5, 2)  # Numérateur float
        with self.assertRaises(TypeError):
            Fraction(3, "2")  # Dénominateur string
        with self.assertRaises(TypeError):
            Fraction("3", 2)  # Numérateur string

    def test_large_values(self):
        """Test fractions with large integer values."""
        f_large = Fraction(123456789, 987654321)
        self.assertEqual(f_large.numerator, 13717421)
        self.assertEqual(f_large.denominator, 109739369)

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
        # Fraction simple
        f = Fraction(3, 4)
        self.assertEqual(str(f), "3/4")

        # Fraction réduite
        f_reduced = Fraction(6, 8)
        self.assertEqual(str(f_reduced), "3/4")

        # Fraction entière (dénominateur = 1)
        f_integer = Fraction(5, 1)
        self.assertEqual(str(f_integer), "5")

        # Fraction négative (numérateur négatif)
        f_negative_num = Fraction(-3, 4)
        self.assertEqual(str(f_negative_num), "-3/4")

        # Fraction négative (dénominateur négatif)
        f_negative_den = Fraction(3, -4)
        self.assertEqual(str(f_negative_den), "-3/4")

        # Fraction négative (numérateur et dénominateur négatifs)
        f_both_negative = Fraction(-3, -4)
        self.assertEqual(str(f_both_negative), "3/4")

        # Fraction où le numérateur est 1 (cas d'unité)
        f_unit = Fraction(1, 5)
        self.assertEqual(str(f_unit), "1/5")

        # Fraction où le numérateur est -1 (cas d'unité négative)
        f_negative_unit = Fraction(-1, 7)
        self.assertEqual(str(f_negative_unit), "-1/7")

        # Fraction zéro
        f_zero = Fraction(0, 5)
        self.assertEqual(str(f_zero), "0")

    def test_fraction_string_representation_integer(self):
        """Test the string representation of an integer fraction."""
        f = Fraction(4, 2)
        self.assertEqual(str(f), "2")

    def test_fraction_as_mixed_number(self):
        """Test the representation of a fraction as a mixed number."""
        # Cas standard : fraction impropre
        f = Fraction(7, 3)
        self.assertEqual(f.as_mixed_number(), "2 + 1/3")

        # Cas où le numérateur est zéro
        f_zero = Fraction(0, 5)
        self.assertEqual(f_zero.as_mixed_number(), "0")

        # Cas où la fraction est un entier exact
        f_integer = Fraction(6, 3)
        self.assertEqual(f_integer.as_mixed_number(), "2")

        # Cas de fraction impropre négative
        f_neg_improper = Fraction(-7, 3)
        self.assertEqual(f_neg_improper.as_mixed_number(), "-2 - 1/3")

        # Cas de fraction impropre avec un numérateur positif et un dénominateur négatif
        f_den_neg = Fraction(7, -3)
        self.assertEqual(f_den_neg.as_mixed_number(), "-2 - 1/3")

        # Cas de fraction unitaire
        f_unit = Fraction(1, 3)
        self.assertEqual(f_unit.as_mixed_number(), "0 + 1/3")

        # Cas de fraction unitaire négative
        f_neg_unit = Fraction(-1, 3)
        self.assertEqual(f_neg_unit.as_mixed_number(), "0 - 1/3")

        # Cas où la fraction est un entier exact avec un dénominateur de 1
        f_den_one = Fraction(7, 1)
        self.assertEqual(f_den_one.as_mixed_number(), "7")

    # Tests des opérations de base

    def test_fraction_addition(self):
        """Test addition of fractions and other numeric types."""
        # Addition de deux fractions simples
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result1 = f1 + f2
        self.assertEqual(result1.numerator, 5)
        self.assertEqual(result1.denominator, 6)

        # Addition avec un entier
        val1 = 5
        result2 = f1 + val1
        self.assertEqual(result2.numerator, 11)
        self.assertEqual(result2.denominator, 2)

        # Addition avec un float
        val2 = 0.6
        result3 = f2 + val2
        self.assertEqual(result3.numerator, 14)
        self.assertEqual(result3.denominator, 15)

        # Addition avec une fraction négative
        f3 = Fraction(-2, 3)
        result4 = f1 + f3
        self.assertEqual(result4.numerator, -1)
        self.assertEqual(result4.denominator, 6)

        # Addition avec un float négatif
        val3 = -1.25
        result5 = f1 + val3
        self.assertEqual(result5.numerator, -3)
        self.assertEqual(result5.denominator, 4)

        # Addition avec zéro
        result6 = f1 + Fraction(0, 1)
        self.assertEqual(result6.numerator, 1)
        self.assertEqual(result6.denominator, 2)

        # Addition de deux fractions ayant un dénominateur commun
        f4 = Fraction(1, 4)
        f5 = Fraction(3, 4)
        result7 = f4 + f5
        self.assertEqual(result7.numerator, 1)
        self.assertEqual(result7.denominator, 1)  # Résultat entier

        # Addition de deux fractions négatives
        f6 = Fraction(-1, 2)
        f7 = Fraction(-1, 3)
        result8 = f6 + f7
        self.assertEqual(result8.numerator, -5)
        self.assertEqual(result8.denominator, 6)

        # Vérification avec des grandes valeurs
        f8 = Fraction(1000, 2001)
        f9 = Fraction(3000, 4001)
        result9 = f8 + f9
        self.assertTrue(isinstance(result9, Fraction))  # Assurer que c'est bien une fraction

    def test_fraction_subtraction(self):
        """Test subtraction of fractions and other numeric types."""
        # Soustraction de deux fractions simples
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result1 = f1 - f2
        self.assertEqual(result1.numerator, 1)
        self.assertEqual(result1.denominator, 6)

        # Soustraction avec un entier
        val1 = 5
        result2 = f1 - val1
        self.assertEqual(result2.numerator, -9)
        self.assertEqual(result2.denominator, 2)

        # Soustraction avec un float
        val2 = 0.6
        result3 = f2 - val2
        self.assertEqual(result3.numerator, -4)
        self.assertEqual(result3.denominator, 15)

        # Soustraction avec une fraction négative
        f3 = Fraction(-2, 3)
        result4 = f1 - f3
        self.assertEqual(result4.numerator, 7)
        self.assertEqual(result4.denominator, 6)

        # Soustraction avec un float négatif
        val3 = -1.25
        result5 = f1 - val3
        self.assertEqual(result5.numerator, 7)
        self.assertEqual(result5.denominator, 4)

        # Soustraction avec zéro
        result6 = f1 - Fraction(0, 1)
        self.assertEqual(result6.numerator, 1)
        self.assertEqual(result6.denominator, 2)

        # Soustraction de deux fractions ayant un dénominateur commun
        f4 = Fraction(3, 4)
        f5 = Fraction(1, 4)
        result7 = f4 - f5
        self.assertEqual(result7.numerator, 1)
        self.assertEqual(result7.denominator, 2)

        # Soustraction de deux fractions négatives
        f6 = Fraction(-1, 2)
        f7 = Fraction(-1, 3)
        result8 = f6 - f7
        self.assertEqual(result8.numerator, -1)
        self.assertEqual(result8.denominator, 6)

        # Vérification avec des grandes valeurs
        f8 = Fraction(1000, 2001)
        f9 = Fraction(3000, 4001)
        result9 = f8 - f9
        self.assertTrue(isinstance(result9, Fraction))  # Assurer que c'est bien une fraction

        # Cas où le résultat est négatif
        f10 = Fraction(1, 4)
        f11 = Fraction(3, 4)
        result10 = f10 - f11
        self.assertEqual(result10.numerator, -1)
        self.assertEqual(result10.denominator, 2)

    def test_fraction_multiplication(self):
        """Test multiplication of fractions and other numeric types."""
        # Multiplication de deux fractions simples
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 * f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 6)

        # Multiplication avec un entier
        val1 = 5
        result2 = f1 * val1
        self.assertEqual(result2.numerator, 5)
        self.assertEqual(result2.denominator, 2)

        # Multiplication avec un float
        val2 = 0.6
        result3 = f2 * val2
        self.assertEqual(result3.numerator, 1)
        self.assertEqual(result3.denominator, 5)

        # Multiplication avec une fraction négative
        f3 = Fraction(-2, 3)
        result4 = f1 * f3
        self.assertEqual(result4.numerator, -1)
        self.assertEqual(result4.denominator, 3)

        # Multiplication avec un entier négatif
        val3 = -4
        result5 = f1 * val3
        self.assertEqual(result5.numerator, -2)
        self.assertEqual(result5.denominator, 1)

        # Multiplication donnant une fraction unitaire (1/x)
        f4 = Fraction(1, 2)
        f5 = Fraction(2, 1)
        result6 = f4 * f5
        self.assertEqual(result6.numerator, 1)
        self.assertEqual(result6.denominator, 1)

        # Multiplication avec zéro
        result7 = f1 * Fraction(0, 1)
        self.assertEqual(result7.numerator, 0)
        self.assertEqual(result7.denominator, 1)

        # Multiplication avec des fractions réduites à leur forme la plus simple
        f6 = Fraction(4, 6)
        f7 = Fraction(9, 12)
        result8 = f6 * f7
        self.assertEqual(result8.numerator, 1)
        self.assertEqual(result8.denominator, 2)

        # Multiplication avec des grandes valeurs
        f8 = Fraction(1000, 2001)
        f9 = Fraction(2000, 4003)
        result9 = f8 * f9
        self.assertTrue(isinstance(result9, Fraction))  # Assurer que c'est bien une fraction

        # Multiplication donnant un résultat négatif
        f10 = Fraction(3, 4)
        f11 = Fraction(-1, 4)
        result10 = f10 * f11
        self.assertEqual(result10.numerator, -3)
        self.assertEqual(result10.denominator, 16)

    def test_fraction_division(self):
        """Test division of fractions and other numeric types."""
        # Division de deux fractions simples
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 / f2
        self.assertEqual(result.numerator, 3)
        self.assertEqual(result.denominator, 2)

        # Division par un entier
        val1 = 5
        result2 = f1 / val1
        self.assertEqual(result2.numerator, 1)
        self.assertEqual(result2.denominator, 10)

        # Division par un float
        val2 = 0.6
        result3 = f2 / val2
        self.assertEqual(result3.numerator, 5)
        self.assertEqual(result3.denominator, 9)

        # Division par une fraction négative
        f3 = Fraction(-1, 4)
        result4 = f1 / f3
        self.assertEqual(result4.numerator, -2)
        self.assertEqual(result4.denominator, 1)

        # Division par un entier négatif
        val3 = -3
        result5 = f2 / val3
        self.assertEqual(result5.numerator, -1)
        self.assertEqual(result5.denominator, 9)

        # Division par 1
        result6 = f1 / Fraction(1, 1)
        self.assertEqual(result6.numerator, 1)
        self.assertEqual(result6.denominator, 2)

        # Division donnant une fraction unitaire
        f4 = Fraction(3, 4)
        f5 = Fraction(3, 4)
        result7 = f4 / f5
        self.assertEqual(result7.numerator, 1)
        self.assertEqual(result7.denominator, 1)

        # Division par une fraction ayant un numérateur plus grand
        f6 = Fraction(2, 3)
        f7 = Fraction(5, 3)
        result8 = f6 / f7
        self.assertEqual(result8.numerator, 2)
        self.assertEqual(result8.denominator, 5)

        # Division par zéro
        with self.assertRaises(DenominatorIsZero):
            _ = f1 / Fraction(0, 1)

        # Division d'une fraction négative par une fraction positive
        f8 = Fraction(-3, 5)
        f9 = Fraction(2, 7)
        result9 = f8 / f9
        self.assertEqual(result9.numerator, -21)
        self.assertEqual(result9.denominator, 10)

        # Division d'une fraction positive par une fraction négative
        result10 = f9 / f8
        self.assertEqual(result10.numerator, -10)
        self.assertEqual(result10.denominator, 21)

    def test_fraction_power(self):
        """Test power of fractions with various cases."""
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        val1 = 5  # Exposant entier positif
        val2 = 0.5  # Exposant fractionnaire
        val3 = -2  # Exposant entier négatif
        val4 = 0  # Exposant zéro
        val5 = "invalid"  # Exposant non valide

        # Puissance positive entière
        result1 = f1 ** val1
        self.assertEqual(result1.numerator, 1)
        self.assertEqual(result1.denominator, 32)

        # Puissance fractionnaire
        result2 = f2 ** val2
        self.assertAlmostEqual(float(result2), (1 / 3) ** 0.5)
        self.assertTrue(isinstance(result2, Fraction))

        # Puissance négative entière
        result3 = f1 ** val3
        self.assertEqual(result3.numerator, 4)
        self.assertEqual(result3.denominator, 1)

        # Puissance zéro
        result4 = f1 ** val4
        self.assertEqual(result4.numerator, 1)
        self.assertEqual(result4.denominator, 1)

        # Test que les types invalides lèvent une exception
        with self.assertRaises(TypeError):
            f1 ** val5

        # Puissance fractionnaire aboutissant à une simplification
        f3 = Fraction(9, 16)
        result5 = f3 ** val2  # Racine carrée
        self.assertEqual(result5.numerator, 3)
        self.assertEqual(result5.denominator, 4)

        # Puissance négative d'une fraction négative
        f4 = Fraction(-1, 2)
        result6 = f4 ** 2
        self.assertEqual(result6.numerator, 1)
        self.assertEqual(result6.denominator, 4)

        result7 = f4 ** 3
        self.assertEqual(result7.numerator, -1)
        self.assertEqual(result7.denominator, 8)

        # Vérification avec des fractions impropres
        f5 = Fraction(5, 2)
        result8 = f5 ** 2
        self.assertEqual(result8.numerator, 25)
        self.assertEqual(result8.denominator, 4)

        # Puissance négative avec fraction impropre
        result9 = f5 ** -1
        self.assertEqual(result9.numerator, 2)
        self.assertEqual(result9.denominator, 5)

    # Tests des comparaisons et des vérifications
    def test_fraction_equality(self):
        """Test equality between fractions and other types."""
        f1 = Fraction(2, 4)  # Équivalent à 1/2
        f2 = Fraction(1, 2)  # Équivalent à 1/2
        f3 = Fraction(3, 4)
        f4 = Fraction(-2, -4)  # Équivalent à 1/2
        f5 = Fraction(-1, 2)  # Fraction négative
        f6 = Fraction(0, 1)  # Fraction nulle
        f7 = Fraction(0, 5)  # Autre représentation de zéro
        val1 = 3  # Entier
        val2 = 0.5  # Float équivalent à 1/2
        val3 = 0  # Zéro entier
        val4 = "not a fraction"  # Chaîne de caractères

        # Égalité entre fractions simplifiées
        self.assertTrue(f1 == f2)
        self.assertTrue(f1 == f4)  # -2/-4 = 1/2
        self.assertFalse(f1 == f3)

        # Comparaison avec zéro
        self.assertTrue(f6 == f7)  # 0/1 == 0/5
        self.assertTrue(f6 == val3)  # Fraction zéro == zéro entier
        self.assertFalse(f1 == f6)  # 1/2 != 0

        # Comparaison avec floats et entiers
        self.assertTrue(f2 == val2)  # 1/2 == 0.5
        self.assertFalse(f1 == val1)  # 1/2 != 3
        self.assertTrue(f5 == -0.5)  # -1/2 == -0.5

        # Comparaison avec une chaîne ou un type invalide
        with self.assertRaises(WrongTypeError):
            f1 == val4

        # Comparaison réflexive et avec des fractions identiques
        self.assertTrue(f1 == Fraction(4, 8))  # Vérification réflexive

        # Comparaison avec des fractions opposées
        self.assertFalse(f1 == f5)  # 1/2 != -1/2

        # Vérification avec des fractions impropres égales
        f8 = Fraction(10, 20)
        self.assertTrue(f1 == f8)  # 1/2 == 10/20

    def test_fraction_as_float(self):
        """Test conversion of a fraction to a float."""

        # Cas de base : fraction positive simple
        f1 = Fraction(1, 2)
        self.assertAlmostEqual(float(f1), 0.5)

        # Cas de fraction négative
        f2 = Fraction(-1, 2)
        self.assertAlmostEqual(float(f2), -0.5)

        # Cas de fraction avec numérateur 0
        f3 = Fraction(0, 5)
        self.assertEqual(float(f3), 0.0)  # Toute fraction avec numérateur 0 doit être 0.0

        # Cas de fraction entière
        f4 = Fraction(4, 2)
        self.assertEqual(float(f4), 2.0)  # 4/2 == 2

        # Cas de fraction avec grand numérateur et dénominateur
        f5 = Fraction(100000, 200000)
        self.assertEqual(float(f5), 0.5)  # 100000/200000 == 0.5

        # Cas de fraction négative entière
        f6 = Fraction(-7, 1)
        self.assertEqual(float(f6), -7.0)  # -7/1 == -7

        # Cas de fraction avec numérateur et dénominateur négatifs
        f7 = Fraction(-5, -10)
        self.assertEqual(float(f7), 0.5)  # -5/-10 == 0.5

        # Cas avec un float très proche
        f8 = Fraction(1, 3)
        self.assertAlmostEqual(float(f8), 0.3333333333333333, places=15)  # 1/3 est un nombre décimal périodique

    def test_is_zero(self):
        """Test if a fraction is zero."""

        # Cas de fraction avec numérateur égal à 0
        f1 = Fraction(0, 3)
        self.assertTrue(f1.is_zero())  # 0/3 devrait être zéro

        # Cas de fraction non nulle (numérateur non égal à zéro)
        f2 = Fraction(2, 3)
        self.assertFalse(f2.is_zero())  # 2/3 n'est pas zéro

        # Cas de fraction négative mais non nulle
        f3 = Fraction(-2, 3)
        self.assertFalse(f3.is_zero())  # -2/3 n'est pas zéro

        # Cas de fraction réduite, numérateur égal à zéro
        f4 = Fraction(0, -5)
        self.assertTrue(f4.is_zero())  # 0/-5 devrait être zéro

        # Cas de fraction avec numérateur nul et dénominateur négatif
        f5 = Fraction(0, -1)
        self.assertTrue(f5.is_zero())  # 0/-1 est toujours zéro

    def test_is_integer(self):
        """Test if a fraction is an integer."""

        # Cas où la fraction est un entier (4/2 = 2)
        f1 = Fraction(4, 2)
        self.assertTrue(f1.is_integer())  # 4/2 est un entier, soit 2

        # Cas où la fraction est déjà un entier (6/1 = 6)
        f2 = Fraction(6, 1)
        self.assertTrue(f2.is_integer())  # 6/1 est un entier

        # Cas où la fraction est un entier négatif (-8/4 = -2)
        f3 = Fraction(-8, 4)
        self.assertTrue(f3.is_integer())  # -8/4 est un entier, soit -2

        # Cas où la fraction est un entier avec un dénominateur négatif (-9/-3 = 3)
        f4 = Fraction(-9, -3)
        self.assertTrue(f4.is_integer())  # -9/-3 est un entier, soit 3

        # Cas où la fraction n'est pas un entier (3/4 n'est pas un entier)
        f5 = Fraction(3, 4)
        self.assertFalse(f5.is_integer())  # 3/4 n'est pas un entier

        # Cas où la fraction est une fraction propre (1/3 n'est pas un entier)
        f6 = Fraction(1, 3)
        self.assertFalse(f6.is_integer())  # 1/3 n'est pas un entier

        # Cas de fraction avec numérateur égal à zéro (0/5 = 0)
        f7 = Fraction(0, 5)
        self.assertTrue(f7.is_integer())  # 0/5 est un entier, soit 0

    def test_is_proper(self):
        """Test if a fraction is proper."""

        # Cas où la fraction est propre (numérateur < dénominateur)
        f1 = Fraction(1, 2)
        self.assertTrue(f1.is_proper())  # 1/2 est une fraction propre

        # Cas où la fraction est propre mais avec un numérateur négatif (-1/2)
        f2 = Fraction(-1, 2)
        self.assertTrue(f2.is_proper())  # -1/2 est une fraction propre

        # Cas où la fraction est propre avec des valeurs plus grandes (1/3)
        f3 = Fraction(1, 3)
        self.assertTrue(f3.is_proper())  # 1/3 est une fraction propre

        # Cas où la fraction est impropre (numérateur > dénominateur)
        f4 = Fraction(3, 2)
        self.assertFalse(f4.is_proper())  # 3/2 n'est pas une fraction propre

        # Cas où la fraction est impropre mais avec des valeurs négatives (-3/2)
        f5 = Fraction(-3, 2)
        self.assertFalse(f5.is_proper())  # -3/2 n'est pas une fraction propre

        # Cas où la fraction est un entier (numérateur = dénominateur, 2/2 = 1)
        f6 = Fraction(2, 2)
        self.assertFalse(f6.is_proper())  # 2/2 n'est pas une fraction propre (équivaut à 1)

        # Cas où la fraction est un entier négatif (-3/-3 = 1)
        f7 = Fraction(-3, -3)
        self.assertFalse(f7.is_proper())  # -3/-3 n'est pas une fraction propre (équivaut à 1)

        # Cas où la fraction est un entier avec un dénominateur 1 (4/1 = 4)
        f8 = Fraction(4, 1)
        self.assertFalse(f8.is_proper())  # 4/1 n'est pas une fraction propre (équivaut à 4)

        # Cas où la fraction est équivalente à zéro (0/5 = 0)
        f9 = Fraction(0, 5)
        self.assertTrue(f9.is_proper())  # 0/5 est une fraction propre (0 est considéré comme propre)

    def test_is_unit(self):
        """Test if a fraction is a unit fraction."""

        # Cas où la fraction est une fraction unitaire (numérateur = 1)
        f1 = Fraction(1, 3)
        self.assertTrue(f1.is_unit())  # 1/3 est une fraction unitaire

        # Cas où la fraction est une fraction unitaire avec numérateur négatif (-1/3)
        f2 = Fraction(-1, 3)
        self.assertTrue(f2.is_unit())  # -1/3 est une fraction unitaire

        # Cas où la fraction est une fraction unitaire avec numérateur négatif mais à valeur absolue égale à 1 (-1/4)
        f3 = Fraction(-1, 4)
        self.assertTrue(f3.is_unit())  # -1/4 est une fraction unitaire

        # Cas où la fraction n'est pas une fraction unitaire (numérateur > 1)
        f4 = Fraction(3, 4)
        self.assertFalse(f4.is_unit())  # 3/4 n'est pas une fraction unitaire

        # Cas où la fraction n'est pas une fraction unitaire (numérateur < -1)
        f5 = Fraction(-5, 6)
        self.assertFalse(f5.is_unit())  # -5/6 n'est pas une fraction unitaire

        # Cas où la fraction est un entier (numérateur égal au dénominateur)
        f6 = Fraction(4, 4)
        self.assertTrue(f6.is_unit())  # 4/4 est un entier (valeur égale à 1)

        # Cas où la fraction est zéro (numérateur = 0)
        f7 = Fraction(0, 5)
        self.assertFalse(f7.is_unit())  # 0/5 n'est pas une fraction unitaire

        # Cas où la fraction est une fraction unitaire, mais avec un grand dénominateur
        f8 = Fraction(1, 1000)
        self.assertTrue(f8.is_unit())  # 1/1000 est une fraction unitaire

        # Cas où la fraction est une fraction unitaire avec un grand numérateur négatif
        f9 = Fraction(-1, 500)
        self.assertTrue(f9.is_unit())  # -1/500 est une fraction unitaire

    def test_is_adjacent_to(self):
        """Test if two fractions are adjacent."""

        # Cas où les fractions sont adjacentes
        f1 = Fraction(1, 3)  # 1/3
        f2 = Fraction(2, 3)  # 2/3
        self.assertTrue(f1.is_adjacent_to(f2))  # Les fractions sont adjacentes (différence de 1/3)

        # Cas où les fractions ne sont pas adjacentes
        f3 = Fraction(1, 4)  # 1/4
        f4 = Fraction(2, 5)  # 2/5
        self.assertFalse(f3.is_adjacent_to(f4))  # Les fractions ne sont pas adjacentes

        # Cas où les fractions sont adjacentes avec des numérateurs négatifs
        f5 = Fraction(-1, 3)  # -1/3
        f6 = Fraction(1, 3)  # 1/3
        self.assertFalse(f5.is_adjacent_to(f6))  # Les fractions sont adjacentes (-1/3 et 1/3)

        # Cas où les fractions sont adjacentes mais une des fractions est un nombre entier
        f7 = Fraction(1, 2)  # 1/2
        f8 = Fraction(3, 2)  # 3/2
        self.assertTrue(f7.is_adjacent_to(f8))  # 1/2 et 3/2 sont adjacentes

        # Cas où une fraction est un entier et l'autre est une fraction (adjacentes)
        f9 = 3  # Entier
        f10 = Fraction(7, 2)  # 7/2
        self.assertTrue(f10.is_adjacent_to(f9))  # 3 et 7/2 sont adjacents

        # Cas où une fraction est un entier et l'autre est une fraction (non adjacentes)
        f11 = 2  # Entier
        f12 = Fraction(5, 2)  # 5/2
        self.assertTrue(f12.is_adjacent_to(f11))  # 2 et 5/2 ne sont pas adjacents

        # Cas avec des valeurs proches mais non adjacentes
        f13 = Fraction(1, 5)  # 1/5
        f14 = Fraction(2, 5)  # 2/5
        self.assertTrue(f13.is_adjacent_to(f14))  # 1/5 et 2/5 ne sont pas adjacents

        # Cas avec des fractions unitaires adjacentes
        f15 = Fraction(1, 5)  # 1/5
        f16 = Fraction(1, 6)  # 1/6
        self.assertTrue(f15.is_adjacent_to(f16))  # 1/5 et 1/6 sont adjacentes

        # Cas avec des fractions adjacentes qui sont proches d'un entier
        f17 = Fraction(3, 4)  # 3/4
        f18 = Fraction(4, 4)  # 4/4 (qui est égal à 1)
        self.assertTrue(f17.is_adjacent_to(f18))  # 3/4 et 4/4 (ou 1) sont adjacentes

    def test_convert_to_fraction_unsupported_type(self):
        """Test that unsupported types raise a TypeError in convert_to_fraction."""

        # Liste invalide (devrait échouer)
        with self.assertRaises(TypeError):
            Fraction.convert_to_fraction([1, 2])  # Liste invalide

        # Dictionnaire invalide (devrait échouer)
        with self.assertRaises(TypeError):
            Fraction.convert_to_fraction({'key': 'value'})  # Dictionnaire invalide

        # Chaîne de caractères (devrait échouer)
        with self.assertRaises(TypeError):
            Fraction.convert_to_fraction("invalid_string")  # Chaîne invalide

        # Un objet complexe (devrait échouer)
        with self.assertRaises(TypeError):
            Fraction.convert_to_fraction(object())  # Objet invalide

        # Booléen (devrait échouer, si la méthode n'accepte pas les booléens)
        with self.assertRaises(TypeError):
            Fraction.convert_to_fraction(True)  # Booléen invalide

        # None (devrait échouer)
        with self.assertRaises(TypeError):
            Fraction.convert_to_fraction(None)  # Valeur None invalide


if __name__ == '__main__':
    unittest.main()