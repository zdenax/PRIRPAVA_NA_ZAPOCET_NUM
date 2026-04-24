def newton(f, fd, x0, tol, max_iter, verbose=False):
    """
    Hledání kořene funkce f(x)=0 pomocí Newtonovy (Newton-Raphsonovy) metody.

    :param f: Funkce, jejíž kořen hledáme
    :param fd: Derivace funkce f
    :param x0: Počáteční odhad kořene
    :param tol: Tolerance (přesnost)
    :param max_iter: Maximální počet iterací
    :param verbose: Vypisovat průběh iterací (default False)
    :return: Odhad kořene nebo None při selhání metody
    """
    x = x0
    for i in range(max_iter):
        fx  = f(x)
        fdx = fd(x)

        if abs(fdx) < 1e-12:
            print("Error: Zero derivative, metoda selhala.")
            return None

        x_new = x - fx / fdx

        if verbose:
            print(f"Iterace {i+1:3d}: x = {x_new:.10f}, f(x) = {f(x_new):.4e}, krok = {abs(x_new-x):.4e}")

        if abs(x_new - x) < tol:
            if verbose:
                print(f"Konvergoval v iteraci {i+1}.")
            return x_new

        x = x_new

    return x
