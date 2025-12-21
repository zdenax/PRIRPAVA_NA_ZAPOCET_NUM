





def romberg_quadrature(f, a, b, tol, max_iter):
    """
    Numerická integrace pomocí Rombergovy metody.

    :param f: Integrovaná funkce f(x)
    :param a: Dolní mez integrace
    :param b: Horní mez integrace
    :param tol: Tolerance požadované přesnosti
    :param max_iter: Maximální počet iterací (hloubka extrapolace)
    :return: Odhad integrálu na [a, b] nebo None při selhání
    """
    import math
    if f is None or a is None or b is None or tol is None or max_iter is None:
        print("Error: Nil values are not supported.")
        return None
    if a == b:
        return 0.0
    if a > b:
        print("Error: a must be less than b.")
        return None
    R = []
    h = (b - a)
    fa = f(a)
    fb = f(b)
    if math.isnan(fa) or math.isinf(fa) or math.isnan(fb) or math.isinf(fb):
        print("Error: Function returned NaN or Inf.")
        return None
    R.append([0.5 * h * (fa + fb)])
    for k in range(1, max_iter):
        h /= 2.0
        sum_new = 0.0
        # Přidání nových bodů: 2^(k-1) nových uzlů
        num_new = 2 ** (k - 1)
        for i in range(1, 2 * num_new, 2):
            x_mid = a + i * h
            fxm = f(x_mid)
            if math.isnan(fxm) or math.isinf(fxm):
                print("Error: Function returned NaN or Inf.")
                return None
            sum_new += fxm
        R_k0 = 0.5 * R[k-1][0] + h * sum_new
        R.append([R_k0])
        for j in range(1, k + 1):
            R_kj = R[k][j-1] + (R[k][j-1] - R[k-1][j-1]) / (4**j - 1)
            R[k].append(R_kj)
        if abs(R[k][k] - R[k-1][k-1]) < tol:
            return R[k][k]
    print("Error: Did not converge within max iterations.")
    return None
