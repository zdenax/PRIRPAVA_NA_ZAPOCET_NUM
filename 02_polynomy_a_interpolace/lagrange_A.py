def lagrange(x_vals, y_vals, t):
    """
    Lagrangeova interpolace — vyhodnotí interpolační polynom v bodě t.

    Každý bázový polynom L_i(t) = ∏(t - x_j)/(x_i - x_j) pro j ≠ i.
    Výsledek: P(t) = Σ y_i * L_i(t)

    :param x_vals: Uzlové body x (seznam, délka n)
    :param y_vals: Hodnoty funkce v uzlech (seznam, délka n)
    :param t: Bod nebo seznam bodů pro vyhodnocení
    :return: Interpolovaná hodnota (nebo seznam hodnot)
    """
    if len(x_vals) != len(y_vals) or len(x_vals) == 0:
        print("Chyba: Nesouhlasí délky nebo prázdný vstup.")
        return None

    n = len(x_vals)
    t_list = t if isinstance(t, list) else [t]
    result = []

    for val in t_list:
        p = 0.0
        for i in range(n):
            L = 1.0
            for j in range(n):
                if j != i:
                    denom = x_vals[i] - x_vals[j]
                    if abs(denom) < 1e-14:
                        print("Chyba: Duplicitní uzly.")
                        return None
                    L *= (val - x_vals[j]) / denom
            p += y_vals[i] * L
        result.append(p)

    return result if isinstance(t, list) else result[0]


if __name__ == "__main__":
    x = [0, 1, 2, 3]
    y = [1, 2, 5, 10]
    print(lagrange(x, y, 1.5))   # ≈ 3.125
    print(lagrange(x, y, [0.5, 2.5]))
