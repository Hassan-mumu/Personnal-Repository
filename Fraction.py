class DenominatorIsZero(Exception):
    pass
class NotAFractionError(Exception):
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
            - num prend un entier et den prend un entier != de 0
        POST :
            - créer une fraction "numerateur"/"denominateur" sous sa forme réduite
            - soulève une erreur si le denminateur est 0
            - soulève une erreur si le type des parametres est diffèrent d'un entier
        """
        if not isinstance(num,int) or not isinstance(den,int):
            raise TypeError("Le numérateur et le dénominateur doivent etre des entiers ")
        if den == 0 :
            raise DenominatorIsZero(f"le dénominateur ne peut pas etre égal à zero ")


        pgcd = self.pgcd(num,den)
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
        return f"{self.numerator}/{self.denominator}"


    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : -
        POST :
            - renvoie la chaine "numerator + 1/denominator"
        """
        return f"{self.numerator//self.denominator} + 1/{self.denominator}"

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE :
            - other doit etre de type Fraction
            - other doit avoir un dénominateur != 0
            - other doit avoir un numerator qui est un entier
         POST :
            - renvoie la somme de la fraction de type Fraction
            - sinon soulève une erreur
         """
        if isinstance(other, (int, float)):
            other = self.convert_to_fraction(other)
        self.is_correct(other)
        den = other.denominator * self.denominator
        num = self.numerator * other.denominator + other.numerator * self.denominator
        return Fraction(num, den)


    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE :
            - other doit etre de type Fraction
            - other doit avoir un dénominateur != 0
            - other doit avoir un numerator qui est un entier
         POST :
            - renvoie la différence de la fraction de type Fraction
            - sinon soulève une erreur
         """

        if isinstance(other, (int, float)):
            other = self.convert_to_fraction(other)
        self.is_correct(other)

        den = other.denominator * self.denominator
        num = self.numerator * other.denominator - other.numerator * self.denominator

        return Fraction(num, den)


    def __mul__(self, other):
        """Overloading of the * operator for fractions

         PRE :
            - other doit etre de type Fraction
            - other doit avoir un dénominateur != 0
            - other doit avoir un numerator qui est un entier
         POST :
            - renvoie la multiplication de la fraction de type Fraction
            - sinon soulève une erreur
        """
        if isinstance(other, (int, float)):
            other = self.convert_to_fraction(other)
        self.is_correct(other)

        num = self.numerator * other.numerator
        den = self.denominator * other.denominator

        return Fraction(num, den)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE :
            - other doit etre de type Fraction
            - other doit avoir un dénominateur != 0
            - other doit avoir un numerator qui est un entier
         POST :
            - renvoie la division entière de la fraction de type Fraction
            - sinon soulève une erreur
        """
        if isinstance(other, (int, float)):
            other = self.convert_to_fraction(other)
        self.is_correct(other)

        return self.__mul__(Fraction(other.denominator, other.numerator))

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE :
            - other doit etre de type int ou float
        POST :
            - renvoie la fraction à la puissance other
            - sinon soulève une erreur
        """
        if not isinstance(other, (int,float)):
            raise TypeError(f"{other} is not a float or integer")
        num = self.numerator ** other
        den = self.denominator ** other
        return Fraction(num, den)


    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE :
            - other doit etre de type Fraction
            - other doit avoir un dénominateur != 0
            - other doit avoir un numerator qui est un entier
        POST :
            - Renvoie un booleen True si les numérateur et le denominateur des
                fractions sous leur formes réduites sont égaux et False sinon
            - Soulève une erreur si other ne respecte pas les précondition

        """
        if isinstance(other, (int, float)):
            other = self.convert_to_fraction(other)
        self.is_correct(other)

        redform_other = self.reduced_form(other)

        return  (self.numerator == redform_other.numerator and
                 self.denominator == redform_other.denominator)

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE :  -
        POST : renvoie la division du numerator sur le dénominateur sous forme d'un float
        """
        return self.numerator / self.denominator

    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

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
            - other doit etre de type Fraction
            - other doit avoir un dénominateur != 0
            - other doit avoir un numerator qui est un entier
        POST :
            - Renvoie True si |self - other| = 1/(n) pour un entier n > 0
        """
        if isinstance(other, (int, float)):
            other = self.convert_to_fraction(other)

        self.is_correct(other)
        diff = self - other  # Différence entre les deux fractions
        return diff.is_unit()

#------------------------------------------------------Ajouts personnel pour me simplifier la tache------------------------------------------------------------------

    @staticmethod
    def pgcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def reduced_form(self, fraction):
        pgcd = self.pgcd(fraction.numerator, fraction.denominator)
        return Fraction(fraction.numerator//pgcd, fraction.denominator//pgcd)

    @staticmethod
    def is_correct(other):
        if not isinstance(other, Fraction):
            raise(NotAFractionError(f"{other} n'est pas de type 'Fraction'"))
        if not isinstance(other.numerator, int) or not isinstance(other.denominator, int):
            raise TypeError(f" les parametres de {other} ne sont pas de type 'int'")
        if other.denominator == 0:
            raise(DenominatorIsZero(f"Le denominateur de {other} est égal à 0"))

    @staticmethod
    def convert_to_fraction(other):
        """Converti un integer ou un float en une Fraction.

        PRE :
        - other est un int ou un float
        POST :
        - renvoie une instance Fraction équivalente à other
        - si other ne peut pas etre convertit en Fraction, soulève une erreur
        """

        if isinstance(other, int):
            return Fraction(other, 1)
        elif isinstance(other, float):
            # Convert float to fraction
            decimal_places = len(str(other).split(".")[1])  # Nombre de chiffres après la virgule
            denominator = 10 ** decimal_places
            numerator = int(other * denominator)
            return Fraction(numerator, denominator)
        raise TypeError(f"Cannot convert {other} to Fraction")

def demo_fraction():
    print("Démonstration de la classe Fraction")
    print("-----------------------------------")

    # Initialisation de fractions valides
    try:
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(7, -5)  # Fraction négative
        print(f"Fraction f1: {f1}")
        print(f"Fraction f2: {f2}")
        print(f"Fraction f3: {f3}")
    except Exception as e:
        print(f"Erreur lors de l'initialisation : {e}")

    # Opérations de base
    try:
        print("\nOpérations de base :")
        print(f"f1 + f2 = {f1 + f2}")
        print(f"f1 - f2 = {f1 - f2}")
        print(f"f1 * f2 = {f1 * f2}")
        print(f"f1 / f2 = {f1 / f2}")
        print(f"f1 ** 2 = {f1 ** 2}")
    except Exception as e:
        print(f"Erreur lors des opérations de base : {e}")

    # Tests de conversion avec int et float
    try:
        print("\nConversion d'entiers et de floats :")
        f4 = f1 + 1
        f5 = f1 * 0.5
        print(f"f1 + 1 = {f4}")
        print(f"f1 * 0.5 = {f5}")
    except Exception as e:
        print(f"Erreur lors de la conversion : {e}")

    # Vérifications de propriétés
    try:
        print("\nPropriétés des fractions :")
        print(f"f1 est zéro : {f1.is_zero()}")
        print(f"f1 est un entier : {f1.is_integer()}")
        print(f"f2 est propre : {f2.is_proper()}")
        print(f"f2 est une fraction unité : {f2.is_unit()}")
        print(f"f1 et f2 sont adjacents : {f1.is_adjacent_to(f2)}")
    except Exception as e:
        print(f"Erreur lors des tests de propriétés : {e}")

    # Représentation mixte
    try:
        print("\nReprésentation mixte :")
        print(f"f1 en nombre mixte : {f1.as_mixed_number()}")
    except Exception as e:
        print(f"Erreur lors de la représentation mixte : {e}")

    # Cas provoquant des erreurs
    try:
        print("\nCas provoquant des erreurs :")
        print("Initialisation avec un dénominateur nul...")
        f_invalid = Fraction(1, 0)
    except Exception as e:
        print(f"Erreur attrapée : {e}")

    try:
        print("Addition avec un type invalide...")
        result = f1 + "invalid"
    except Exception as e:
        print(f"Erreur attrapée : {e}")

    try:
        print("Division par zéro...")
        result = f1 / Fraction(0, 1)
    except Exception as e:
        print(f"Erreur attrapée : {e}")

    try:
        print("Puissance avec un type invalide...")
        result = f1 ** "invalid"
    except Exception as e:
        print(f"Erreur attrapée : {e}")

    try:
        print("Comparaison avec un type invalide...")
        result = f1 == "invalid"
    except Exception as e:
        print(f"Erreur attrapée : {e}")

    print("\nDémonstration terminée.")

if __name__ == "__main__":
    demo_fraction()
