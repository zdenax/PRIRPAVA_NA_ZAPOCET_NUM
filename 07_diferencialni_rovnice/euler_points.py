def euler_step_points(f, x0, y0, h, n, verbose=False):
    """
    Numerické řešení ODE pomocí Eulerovy metody.
    Varianta vracející seznam dvojic (x, y) místo pouze hodnot y.

    :param f: Funkce f(x, y) představující derivaci dy/dx
    :param x0: Počáteční hodnota x
    :param y0: Počáteční hodnota y
    :param h: Délka kroku
    :param n: Počet kroků
    :param verbose: Vypisovat průběh kroků (default False)
    :return: Seznam dvojic (x, y)
    """
    if n < 1:
        print("Chyba: Počet kroků n musí být >= 1.")
        return None

    body = [(x0, y0)]

    x = x0
    y = y0

    if verbose:
        print(f"Krok   0: x = {x:.4f}, y = {y:.10f}")

    for i in range(1, n + 1):
        y = y + h * f(x, y)
        x = x + h
        body.append((x, y))
        if verbose:
            print(f"Krok {i:3d}: x = {x:.4f}, y = {y:.10f}")

    return body