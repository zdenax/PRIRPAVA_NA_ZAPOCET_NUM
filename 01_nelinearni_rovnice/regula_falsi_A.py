import math

def regula_falsi(f, a, b, tol, max_iter):
    """
    Hledání kořene rovnice f(x)=0 metodou regula falsi (sečnová metoda s intervalem).
    Rozdíl od bisekce: nový bod c je průsečík sečny, ne střed intervalu.

    :param f: Funkce, jejíž kořen hledáme
    :param a: Levá mez intervalu
    :param b: Pravá mez intervalu
    :param tol: Tolerance (přesnost)
    :param max_iter: Maximální počet iterací
    :return: Odhad kořene nebo None při selhání metody
    """
    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        print("Error: No sign change, can't guarantee a root.")
        return None

    c = a
    for i in range(max_iter):
        if abs(fb - fa) < 1e-12:
            print("Error: Zero denominator (f(a) == f(b)).")
            return None

        c = a - fa * (b - a) / (fb - fa)
        fc = f(c)

        if math.isnan(fc) or math.isinf(fc):
            print("Error: Did not converge (NaN/Inf).")
            return None

        if abs(fc) < tol:
            return c

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    print("Error: Did not converge within max iterations.")
    return None


if __name__ == "__main__":
    # f(x) = x^2 - 2, kořen = sqrt(2) ≈ 1.41421
    r = regula_falsi(lambda x: x**2 - 2, 1, 2, 1e-6, 100)
    print(f"Kořen: {r:.8f}  (referenční: {math.sqrt(2):.8f})")
