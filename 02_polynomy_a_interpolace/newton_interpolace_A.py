def divided_differences(x_vals, y_vals):
    """
    Sestaví tabulku dělených diferencí pro Newtonovu interpolaci.

    :param x_vals: Uzlové body x
    :param y_vals: Hodnoty funkce v uzlech
    :return: Koeficienty Newtonova polynomu [f[x0], f[x0,x1], ...]
    """
    n = len(x_vals)
    coefs = list(y_vals)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            denom = x_vals[i] - x_vals[i - j]
            if abs(denom) < 1e-14:
                print("Chyba: Duplicitní uzly.")
                return None
            coefs[i] = (coefs[i] - coefs[i - 1]) / denom
    return coefs


def newton_interpolation(x_vals, y_vals, t):
    """
    Newtonova interpolace pomocí dělených diferencí.

    Polynom: P(t) = c0 + c1*(t-x0) + c2*(t-x0)*(t-x1) + ...
    kde c_i jsou dělené diference.

    Použití:
        koefs = newton_interpolation(x_vals, y_vals, t)

    :param x_vals: Uzlové body x (seznam, délka n)
    :param y_vals: Hodnoty funkce v uzlech (seznam, délka n)
    :param t: Bod nebo seznam bodů pro vyhodnocení
    :return: Interpolovaná hodnota (nebo seznam hodnot)
    """
    if len(x_vals) != len(y_vals) or len(x_vals) == 0:
        print("Chyba: Nesouhlasí délky nebo prázdný vstup.")
        return None

    coefs = divided_differences(x_vals, y_vals)
    if coefs is None:
        return None

    n = len(x_vals)
    t_list = t if isinstance(t, list) else [t]
    result = []

    for val in t_list:
        # Hornerovo schéma pro Newtonův polynom
        p = coefs[n - 1]
        for i in range(n - 2, -1, -1):
            p = p * (val - x_vals[i]) + coefs[i]
        result.append(p)

    return result if isinstance(t, list) else result[0]


if __name__ == "__main__":
    x = [0, 1, 2, 3]
    y = [1, 2, 5, 10]
    print(newton_interpolation(x, y, 1.5))        # ≈ 3.125
    print(newton_interpolation(x, y, [0.5, 2.5]))
