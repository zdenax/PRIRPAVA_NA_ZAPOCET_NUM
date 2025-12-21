def steffensen(f, x0, tol, max_iter):
    """
    Hledání kořene funkce f(x)=0 pomocí Steffensenovy metody.

    :param f: Funkce, jejíž kořen hledáme (není třeba derivace)
    :param x0: Počáteční odhad kořene
    :param tol: Tolerance (přesnost)
    :param max_iter: Maximální počet iterací
    :return: Odhad kořene nebo None při selhání metody
    """
    import math
    if f is None or x0 is None or tol is None or max_iter is None:
        print("Error: Nil values are not supported.")
        return None
    x = x0
    for i in range(max_iter):
        f_x = f(x)
        f_x1 = f(x + f_x)
        denominator = f_x1 - f_x
        if abs(denominator) < 1e-12:  # nulový jmenovatel
            print("Error: Zero denominator in Steffensen method.")
            return None
        x_new = x - (f_x * f_x) / denominator
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