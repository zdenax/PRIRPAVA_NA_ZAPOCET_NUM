
def newton_horner(coefs, x0, tol, max_iter):
    """
    Hledání kořene polynomu pomocí Newtonovy metody s Hornerovým schématem.

    :param coefs: Koeficienty polynomu od nejnižší po nejvyšší mocninu
    :param x0: Počáteční odhad kořene
    :param tol: Tolerance (přesnost)
    :param max_iter: Maximální počet iterací
    :return: Odhad kořene polynomu nebo None při selhání metody
    """
    import math
    if coefs is None or x0 is None or tol is None or max_iter is None:
        print("Error: Nil values are not supported.")
        return None
    if len(coefs) == 0:
        print("Error: Nil values are not supported.")
        return None
    # Pokud je polynom konstantní:
    if len(coefs) == 1:
        if abs(coefs[0]) < 1e-12:
            # Polynom je nulový, každé x je kořen - vrátíme počáteční hodnotu
            return x0
        else:
            print("Error: Constant polynomial has no root.")
            return None
    x = x0
    deg = len(coefs) - 1
    for i in range(max_iter):
        # Hornerovo schéma pro výpočet hodnoty polynomu a jeho derivace
        p_val = coefs[deg]
        p_der = 0.0
        for j in range(deg-1, -1, -1):
            p_der = p_val + x * p_der
            p_val = coefs[j] + x * p_val
        # Pozn: Po skončení cyklu p_val = p(x), p_der = p'(x)
        if abs(p_der) < 1e-12:
            print("Error: Zero derivative in Newton-Horner method.")
            return None
        x_new = x - p_val / p_der
        # Kontrola na NaN/Inf
        if math.isnan(x_new) or math.isinf(x_new):
            print("Error: Did not converge (diverged to NaN/Inf).")
            return None
        # Kontrola konvergence
        if abs(x_new - x) < tol or abs(p_val) < tol:
            return x_new
        x = x_new
    print("Error: Did not converge within max iterations.")
    return None