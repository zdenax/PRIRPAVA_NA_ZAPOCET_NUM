def regula_falsi(f, a, b, tol, max_iter):
    """
    Hledání kořene funkce f(x)=0 pomocí metody regula falsi (metoda falešné polohy).

    :param f: Funkce, jejíž kořen hledáme
    :param a: Levá mez intervalu
    :param b: Pravá mez intervalu
    :param tol: Tolerance (přesnost)
    :param max_iter: Maximální počet iterací
    :return: Odhad kořene nebo None při selhání metody
    """
    fa = f(a)
    fb = f(b)

    # Kontrola, zda v intervalu může být kořen (změna znaménka)
    if fa * fb > 0:
        print("Error: No sign change, can't guarantee a root.")
        return None

    for i in range(max_iter):
        # Výpočet průsečíku sečny s osou x
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)

        # Kontrola konvergence
        if abs(fc) < tol:
            return c

        # Rozhodnutí, kterou část intervalu si ponecháme
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    print("Error: Did not converge within max iterations.")
    return None

# Příklad použití:
# root = regula_falsi(lambda x: x**2 - 4, 0, 5, 1e-6, 100)
# print(f"Kořen je: {root}")
