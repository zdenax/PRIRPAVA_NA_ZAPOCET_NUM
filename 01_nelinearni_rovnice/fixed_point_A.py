import math

def fixed_point_iteration(phi, x0, tol, max_iter, verbose=False):
    """
    Hledání pevného bodu funkce phi metodou prosté iterace.

    :param phi: Iterační funkce g(x), jejíž pevný bod hledáme
    :param x0: Počáteční odhad řešení
    :param tol: Tolerance (přesnost)
    :param max_iter: Maximální počet iterací
    :param verbose: Vypisovat průběh iterací (default False)
    :return: Odhad pevného bodu nebo None, pokud iterace selže
    """
    if phi is None or x0 is None or tol is None or max_iter is None:
        print("Error: Nil values are not supported.")
        return None
    x = x0
    for i in range(max_iter):
        x_new = phi(x)
        if math.isnan(x_new) or math.isinf(x_new):
            print("Error: Did not converge (diverged to NaN/Inf).")
            return None

        if verbose:
            print(f"Iterace {i+1:3d}: x = {x_new:.10f}, změna = {abs(x_new-x):.4e}")

        if abs(x_new - x) < tol:
            if verbose:
                print(f"Konvergoval v iteraci {i+1}.")
            return x_new
        x = x_new
    print("Error: Did not converge within max iterations.")
    return None
