class DenominatorIsZero(Exception):
    """Exception raised when the denominator is zero."""
    pass


class WrongTypeError(Exception):
    """Exception raised when the input type is incorrect."""
    pass


class Fraction:
    """Class representing a fraction and operations on it

    Author : D. Alhssanesanee
    Date : October 2024
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE :
        POST :
            - créer une fraction "numerateur"/"denominateur" sous sa forme réduite
        RAISE :
            - TypError si le type des parametres est différent d'un entier
            - DenominatorIsZero si le denominateur est 0
        """
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError("Le numérateur et le dénominateur doivent être des entiers ")
        if den == 0:
            raise DenominatorIsZero("le dénominateur ne peut pas être égal à zero ")

        pgcd = self.pgcd(num, den)
        self.__denominator = den // pgcd
        self.__numerator = num // pgcd

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : -
        POST :
            - renvoie la chaine "numerator/denominator"
        """
        return f"{self.numerator}" if self.is_integer() else f"{self.numerator}/{self.denominator}"

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : -
        POST :
            - renvoie la chaine "numerator + 1/denominator"
        """
        entier = int(self.numerator / self.denominator)
        reste = abs(self.numerator) % abs(self.denominator)
        signe = "-" if self.numerator < 0 else "+"

        return f"{entier} {signe} {reste}/{self.denominator}" if reste != 0 else str(entier)

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE :
         POST :
            - renvoie la somme de la fraction de type Fraction
         RAISE:
            - WrongTypeError si other est différent de int, float ou une Fraction
         """

        self.is_correct(other)
        if isinstance(other, (int, float)):
            other = self.convert_to_fraction(other)

        den = other.denominator * self.denominator
        num = self.numerator * other.denominator + other.numerator * self.denominator
        return Fraction(num, den)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

         PRE :
         POST :
            - renvoie la différence de la fraction de type Fraction
         RAISE:
            - WrongTypeError si other est différent de int, float ou une Fraction
         """

        self.is_correct(other)
        if isinstance(other, (int, float)):
            other = self.convert_to_fraction(other)

        den = other.denominator * self.denominator
        num = self.numerator * other.denominator - other.numerator * self.denominator

        return Fraction(num, den)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

         PRE :
         POST :
            - renvoie la multiplication de la fraction de type Fraction
         RAISE:
            - WrongTypeError si other est différent de int, float ou une Fraction
         """

        self.is_correct(other)
        if isinstance(other, (int, float)):
            other = self.convert_to_fraction(other)

        num = self.numerator * other.numerator
        den = self.denominator * other.denominator

        return Fraction(num, den)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions
        PRE :
         POST :
            - renvoie la division entière de la fraction de type Fraction
        RAISE:
            - WrongTypeError si other est différent de int, float ou une Fraction
            - DivisionZeroError si other.numérateur est égal à  zero
         """

        self.is_correct(other)
        if isinstance(other, (int, float)):
            other = self.convert_to_fraction(other)
        return self.__mul__(Fraction(other.denominator, other.numerator))

    def __pow__(self, other):

        """Overloading of the ** operator for fractions

        PRE : -
        POST :
            - renvoie la fraction à la puissance other
        RAISES :
            - TypeError si other est différent de int ou float
        """

        if not isinstance(other, (int, float)):
            raise TypeError(f"{other} is not a float or integer")
        num = self.numerator ** other
        den = self.denominator ** other
        return self.convert_to_fraction(num / den)

    def __eq__(self, other):
        """Overloading of the == operator for fractions
        PRE :
        POST :
            - Renvoie un booleen True si les numérateur et le denominateur des
                fractions sous leur formes réduites sont égaux et False sinon
        RAISES :
            - WrongTypeError si other est différent de int, float ou une Fraction
        """
        self.is_correct(other)
        if isinstance(other, (int, float)):
            other = self.convert_to_fraction(other)
        return (self.numerator == other.numerator and
                self.denominator == other.denominator)

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : -
        POST : renvoie la division du numerator sur le dénominateur sous forme d'un float
        """
        return self.numerator / self.denominator

    # ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : -
        POST : renvoie un booleen True si le numérateur vaut 0 et False sinon
        """
        return self.numerator == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : -
        POST : renvoie un boleen True si le denominateur vaut 1 et False sinon
        """
        return self.denominator == 1

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : -
        POST : renvoie un booleen True si la fraction est propre et False sinon
        """
        return abs(self.numerator) < abs(self.denominator)

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE :   -
        POST :  renvoie True si le numérateur vaut 1 sous sa forme réduite et False sinon
        """
        return abs(self.numerator) == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction.

        PRE :
        POST :
            - Renvoie True si |self - other| = 1/(n) pour un entier n > 0
        """

        self.is_correct(other)
        if isinstance(other, (int, float)):
            other = self.convert_to_fraction(other)

        diff = self - other  # Différence entre les deux fractions
        return diff.is_unit()

    # ------------------------------------------------------Ajouts personnel pour me simplifier la tache------------------------------------------------------------------

    @staticmethod
    def pgcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    @staticmethod
    def is_correct(other):
        if not isinstance(other, (Fraction, int, float)):
            raise WrongTypeError(
                f"{other} n'est pas de type Fraction mais de type {type(other)}")  # Suppression des parenthèses inutiles

    @staticmethod
    def convert_to_fraction(other):
        """Converti un integer ou un float en une Fraction.
        PRE :
        POST :
        - renvoie une instance Fraction équivalente à other
        - si other ne peut pas etre convertit en Fraction, soulève une erreur
        """
        numerator = other
        denominator = 1
        if isinstance(other, int) and not isinstance(other, bool):
            pass
        elif isinstance(other, float):
            # Convert float to fraction
            decimal_places = len(str(other).split(".")[1])  # Nombre de chiffres après la virgule
            denominator = 10 ** decimal_places
            numerator = int(other * denominator)
        else:
            raise TypeError(f"Cannot convert {type(other)} to Fraction")

        return Fraction(numerator, denominator)

    # Ajout d'une ligne vide à la fin du fichier
