import math

def regula_falsi(f, a, b, tol, max_iter, verbose=False):
    """
    Hledání kořene rovnice f(x)=0 metodou regula falsi (sečnová metoda s intervalem).
    Rozdíl od bisekce: nový bod c je průsečík sečny, ne střed intervalu.

    :param f: Funkce, jejíž kořen hledáme
    :param a: Levá mez intervalu
    :param b: Pravá mez intervalu
    :param tol: Tolerance (přesnost)
    :param max_iter: Maximální počet iterací
    :param verbose: Vypisovat průběh iterací (default False)
    :return: Odhad kořene nebo None při selhání metody
    """
    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        print("Chyba: Žádná změna znaménka, kořen v intervalu nelze zaručit.")
        return None

    c = a
    for i in range(max_iter):
        if abs(fb - fa) < 1e-12:
            print("Chyba: Nulový jmenovatel (f(a) == f(b)).")
            return None

        c = a - fa * (b - a) / (fb - fa)
        fc = f(c)

        if math.isnan(fc) or math.isinf(fc):
            print("Chyba: Metoda divergovala (NaN/Inf).")
            return None

        if verbose:
            print(f"Iterace {i+1:3d}: c = {c:.10f}, f(c) = {fc:.4e}")

        if abs(fc) < tol:
            if verbose:
                print(f"Konvergoval v iteraci {i+1}.")
            return c

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    print("Chyba: Metoda neskonvergovala v daném počtu iterací.")
    return None


if __name__ == "__main__":
    r = regula_falsi(lambda x: x**2 - 2, 1, 2, 1e-6, 100)
    print(f"Kořen: {r:.8f}  (referenční: {math.sqrt(2):.8f})")
