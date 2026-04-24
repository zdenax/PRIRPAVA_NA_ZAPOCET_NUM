import math

def romberg_quadrature(f, a, b, tol, max_iter, verbose=False):
    """
    Numerická integrace pomocí Rombergovy metody.

    :param f: Integrovaná funkce f(x)
    :param a: Dolní mez integrace
    :param b: Horní mez integrace
    :param tol: Tolerance požadované přesnosti
    :param max_iter: Maximální počet iterací (hloubka extrapolace)
    :param verbose: Vypisovat průběh iterací (default False)
    :return: Odhad integrálu na [a, b] nebo None při selhání
    """
    if f is None or a is None or b is None or tol is None or max_iter is None:
        print("Chyba: Vstupní hodnoty nesmí být None.")
        return None
    if a == b:
        return 0.0
    if a > b:
        print("Chyba: a musí být menší než b.")
        return None
    R = []
    h = (b - a)
    fa = f(a)
    fb = f(b)
    if math.isnan(fa) or math.isinf(fa) or math.isnan(fb) or math.isinf(fb):
        print("Chyba: Funkce vrátila NaN nebo Inf.")
        return None
    R.append([0.5 * h * (fa + fb)])
    if verbose:
        print(f"Úroveň  0: R[0][0] = {R[0][0]:.10f}")
    for k in range(1, max_iter):
        h /= 2.0
        sum_new = 0.0
        num_new = 2 ** (k - 1)
        for i in range(1, 2 * num_new, 2):
            x_mid = a + i * h
            fxm = f(x_mid)
            if math.isnan(fxm) or math.isinf(fxm):
                print("Chyba: Funkce vrátila NaN nebo Inf.")
                return None
            sum_new += fxm
        R_k0 = 0.5 * R[k-1][0] + h * sum_new
        R.append([R_k0])
        for j in range(1, k + 1):
            R_kj = R[k][j-1] + (R[k][j-1] - R[k-1][j-1]) / (4**j - 1)
            R[k].append(R_kj)
        if verbose:
            print(f"Úroveň {k:2d}: R[k][k] = {R[k][k]:.10f}, změna = {abs(R[k][k] - R[k-1][k-1]):.4e}")
        if abs(R[k][k] - R[k-1][k-1]) < tol:
            if verbose:
                print(f"Konvergoval na úrovni {k}.")
            return R[k][k]
    print("Chyba: Metoda neskonvergovala v daném počtu iterací.")
    return None
