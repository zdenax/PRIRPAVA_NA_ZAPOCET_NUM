def euler_step(f, x0, y0, h, n, verbose=False):
    """
    Numerické řešení ODE pomocí Eulerovy metody.

    :param f: Funkce f(x, y) představující derivaci dy/dx
    :param x0: Počáteční hodnota x
    :param y0: Počáteční hodnota y
    :param h: Délka kroku
    :param n: Počet kroků
    :param verbose: Vypisovat průběh kroků (default False)
    :return: Pole hodnot y (vektor)
    """
    if n < 1:
        print("Error: Number of steps n must be >= 1.")
        return None

    ys = [0.0] * (n + 1)
    ys[0] = y0

    x = x0
    y = y0

    if verbose:
        print(f"Krok   0: x = {x:.4f}, y = {y:.10f}")

    for i in range(1, n + 1):
        y = y + h * f(x, y)
        x = x + h
        ys[i] = y
        if verbose:
            print(f"Krok {i:3d}: x = {x:.4f}, y = {y:.10f}")

    return ys
