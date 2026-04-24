
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
        print("Chyba: Vstupní hodnoty nesmí být None.")
        return None
    if len(coefs) == 0:
        print("Chyba: Vstupní hodnoty nesmí být None.")
        return None
    # Pokud je polynom konstantní:
    if len(coefs) == 1:
        if abs(coefs[0]) < 1e-12:
            # Polynom je nulový, každé x je kořen - vrátíme počáteční hodnotu
            return x0
        else:
            print("Chyba: Konstantní polynom nemá kořen.")
            return None
    x = x0
    deg = len(coefs) - 1
    for iteration in range(max_iter):
        # Hornerovo schéma pro výpočet hodnoty polynomu a jeho derivace
        # Koeficienty jsou od nejnižší (coefs[0]) po nejvyšší (coefs[deg])
        # Horner vyhodnocuje od nejvyššího stupně dolů
        p_val = coefs[deg]
        p_der = 0.0
        for j in range(deg - 1, -1, -1):
            p_der = p_der * x + p_val
            p_val = p_val * x + coefs[j]
        # Po skončení cyklu: p_val = p(x), p_der = p'(x)
        if abs(p_der) < 1e-12:
            print("Chyba: Nulová derivace v metodě Newton-Horner.")
            return None
        x_new = x - p_val / p_der
        # Kontrola na NaN/Inf
        if math.isnan(x_new) or math.isinf(x_new):
            print("Chyba: Metoda divergovala (NaN/Inf).")
            return None
        # Kontrola konvergence
        if abs(x_new - x) < tol or abs(p_val) < tol:
            return x_new
        x = x_new
    print("Chyba: Metoda neskonvergovala v daném počtu iterací.")
    return None