from Fraction import *


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
