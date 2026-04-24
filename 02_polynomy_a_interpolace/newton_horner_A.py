import math

def newton_horner(coefs, x0, tol, max_iter, verbose=False):
    """
    Hledání kořene polynomu pomocí Newtonovy metody s Hornerovým schématem.

    :param coefs: Koeficienty polynomu od nejnižší po nejvyšší mocninu
    :param x0: Počáteční odhad kořene
    :param tol: Tolerance (přesnost)
    :param max_iter: Maximální počet iterací
    :param verbose: Vypisovat průběh iterací (default False)
    :return: Odhad kořene polynomu nebo None při selhání metody
    """
    if coefs is None or x0 is None or tol is None or max_iter is None:
        print("Chyba: Vstupní hodnoty nesmí být None.")
        return None
    if len(coefs) == 0:
        print("Chyba: Vstupní hodnoty nesmí být None.")
        return None
    if len(coefs) == 1:
        if abs(coefs[0]) < 1e-12:
            return x0
        else:
            print("Chyba: Konstantní polynom nemá kořen.")
            return None
    x = x0
    deg = len(coefs) - 1
    for iteration in range(max_iter):
        p_val = coefs[deg]
        p_der = 0.0
        for j in range(deg - 1, -1, -1):
            p_der = p_der * x + p_val
            p_val = p_val * x + coefs[j]
        if abs(p_der) < 1e-12:
            print("Chyba: Nulová derivace v metodě Newton-Horner.")
            return None
        x_new = x - p_val / p_der
        if math.isnan(x_new) or math.isinf(x_new):
            print("Chyba: Metoda divergovala (NaN/Inf).")
            return None

        if verbose:
            print(f"Iterace {iteration+1:3d}: x = {x_new:.10f}, P(x) = {p_val:.4e}, krok = {abs(x_new-x):.4e}")

        if abs(x_new - x) < tol or abs(p_val) < tol:
            if verbose:
                print(f"Konvergoval v iteraci {iteration+1}.")
            return x_new
        x = x_new
    print("Chyba: Metoda neskonvergovala v daném počtu iterací.")
    return None
