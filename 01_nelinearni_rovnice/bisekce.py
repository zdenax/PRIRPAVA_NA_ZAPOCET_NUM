def bisection(f, a, b, tol, max_iter, verbose=False):
    """
    Numerické hledání kořene funkce pomocí metody půlení intervalu.

    :param f: Funkce, jejíž kořen hledáme
    :param a: Levá mez intervalu
    :param b: Pravá mez intervalu
    :param tol: Tolerance (přesnost)
    :param max_iter: Maximální počet iterací
    :param verbose: Vypisovat průběh iterací (default False)
    :return: Kořen funkce nebo None, pokud metoda selže
    """
    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        print("Error: No sign change, can't guarantee a root.")
        return None

    c = a
    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)

        if verbose:
            print(f"Iterace {i+1:3d}: c = {c:.10f}, f(c) = {fc:.4e}, délka intervalu = {(b-a)/2:.4e}")

        if abs(fc) < tol or (b - a) / 2 < tol:
            if verbose:
                print(f"Konvergoval v iteraci {i+1}.")
            return c

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    print("Error: Did not converge.")
    return None

# Příklad použití:
# root = bisection(lambda x: x**2 - 4, 0, 5, 1e-6, 100)
# print(f"Kořen je: {root}")
