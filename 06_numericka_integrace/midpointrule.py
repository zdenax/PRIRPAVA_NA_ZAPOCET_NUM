import math

def test_f(x):
    """Testovací funkce: x^2 * sin(x)"""
    return math.pow(x, 2) * math.sin(x)

def midpoint_rule(f, a, b, n):
    """
    Numerický výpočet určitého integrálu funkce f na intervalu [a, b].
    
    :param f: Integrovaná funkce
    :param a: Dolní mez
    :param b: Horní mez
    :param n: Počet dělení (obdélníků)
    :return: Přibližná hodnota integrálu
    """
    if n < 1:
        print("Chyba: n musí být >= 1.")
        return None

    # Šířka jednoho obdélníku
    h = (b - a) / n
    total_sum = 0.0
    
    # Procházíme n podintervalů
    for i in range(n):
        # Výpočet středu aktuálního obdélníku
        midpoint = a + (i + 0.5) * h
        total_sum += f(midpoint)
    
    # Celkový obsah je šířka krát součet výšek
    approximation = h * total_sum
    return approximation

# Příklad použití:
if __name__ == "__main__":
    vysledek = midpoint_rule(test_f, 0, math.pi, 100)
    print(f"Integrál je přibližně: {vysledek}")