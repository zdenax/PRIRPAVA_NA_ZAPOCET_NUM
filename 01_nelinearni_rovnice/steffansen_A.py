import math

def steffensen(f, x0, tol, max_iter, verbose=False):
    """
    Hledání kořene funkce f(x)=0 pomocí Steffensenovy metody.

    :param f: Funkce, jejíž kořen hledáme (není třeba derivace)
    :param x0: Počáteční odhad kořene
    :param tol: Tolerance (přesnost)
    :param max_iter: Maximální počet iterací
    :param verbose: Vypisovat průběh iterací (default False)
    :return: Odhad kořene nebo None při selhání metody
    """
    if f is None or x0 is None or tol is None or max_iter is None:
        print("Chyba: Vstupní hodnoty nesmí být None.")
        return None
    x = x0
    for i in range(max_iter):
        f_x = f(x)
        f_x1 = f(x + f_x)
        denominator = f_x1 - f_x
        if abs(denominator) < 1e-12:
            print("Chyba: Nulový jmenovatel ve Steffensenově metodě.")
            return None
        x_new = x - (f_x * f_x) / denominator
        if math.isnan(x_new) or math.isinf(x_new):
            print("Chyba: Metoda divergovala (NaN/Inf).")
            return None

        if verbose:
            print(f"Iterace {i+1:3d}: x = {x_new:.10f}, f(x) = {f(x_new):.4e}, krok = {abs(x_new-x):.4e}")

        if abs(x_new - x) < tol or abs(f(x_new)) < tol:
            if verbose:
                print(f"Konvergoval v iteraci {i+1}.")
            return x_new
        x = x_new
    print("Chyba: Metoda neskonvergovala v daném počtu iterací.")
    return None
