def newton(f, fd, x0, tol, max_iter):
    """
    Hledání kořene funkce f(x)=0 pomocí Newtonovy (Newton-Raphsonovy) metody.

    :param f: Funkce, jejíž kořen hledáme
    :param fd: Derivace funkce f
    :param x0: Počáteční odhad kořene
    :param tol: Tolerance (přesnost)
    :param max_iter: Maximální počet iterací
    :return: Odhad kořene nebo None při selhání metody
    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        fdx = fd(x) # Derivace
        
        if abs(fdx) < 1e-12: # Ochrana proti dělení nulou
            return None
            
        x_new = x - fx / fdx
        
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x