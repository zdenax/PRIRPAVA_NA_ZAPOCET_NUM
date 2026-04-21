
def halley(f, f_prime, f_double, x0, tol, max_iter):
    """
    Hledání kořene funkce f(x)=0 pomocí Halleyho metody (využívá 1. a 2. derivaci).

    :param f: Funkce, jejíž kořen hledáme
    :param f_prime: První derivace funkce f
    :param f_double: Druhá derivace funkce f
    :param x0: Počáteční odhad kořene
    :param tol: Tolerance (přesnost)
    :param max_iter: Maximální počet iterací
    :return: Odhad kořene nebo None při selhání metody
    """
    import math
    if f is None or f_prime is None or f_double is None or x0 is None or tol is None or max_iter is None:
        print("Error: Nil values are not supported.")
        return None
    x = x0
    for i in range(max_iter):
        fx = f(x)
        fpx = f_prime(x)
        fdpx = f_double(x)
        denominator = 2 * (fpx ** 2) - fx * fdpx
        if abs(denominator) < 1e-12:  # ochrana proti dělení nulou
            print("Error: Zero denominator in Halley method.")
            return None
        x_new = x - (2 * fx * fpx) / denominator
        # Kontrola na NaN/Inf
        if math.isnan(x_new) or math.isinf(x_new):
            print("Error: Did not converge (diverged to NaN/Inf).")
            return None
        # Kontrola konvergence
        if abs(x_new - x) < tol or abs(f(x_new)) < tol:
            return x_new
        x = x_new
    print("Error: Did not converge within max iterations.")
    return None
