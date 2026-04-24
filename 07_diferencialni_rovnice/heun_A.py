import math

def heun(f, x0, y0, h, n):
    """
    Řešení ODR y' = f(x, y) Heunovou metodou (zpřesněná Eulerova metoda, RK2).

    Heun = prediktor (Euler krok) + korektor (průměr sklonů).
    Vzorec:
        k1 = f(x, y)
        k2 = f(x + h, y + h*k1)
        y_new = y + (h/2) * (k1 + k2)

    :param f: Funkce f(x, y) definující y' = f(x, y)
    :param x0: Počáteční hodnota x
    :param y0: Počáteční hodnota y
    :param h: Krok integrace
    :param n: Počet kroků
    :return: Seznam bodů [(x0,y0), (x1,y1), ...] nebo None při chybě
    """
    if n < 1:
        print("Chyba: Počet kroků n musí být >= 1.")
        return None

    points = [(x0, y0)]
    x = x0
    y = y0

    for i in range(n):
        k1 = f(x, y)
        k2 = f(x + h, y + h * k1)

        if any(math.isnan(k) or math.isinf(k) for k in (k1, k2)):
            print("Chyba: Metoda divergovala (NaN/Inf).")
            return None

        y_new = y + (h / 2) * (k1 + k2)
        x_new = x + h

        if math.isnan(y_new) or math.isinf(y_new):
            print("Chyba: Metoda divergovala (NaN/Inf).")
            return None

        points.append((x_new, y_new))
        x, y = x_new, y_new

    return points


if __name__ == "__main__":
    # y' = y, y(0) = 1 => y(1) = e ≈ 2.71828
    r = heun(lambda x, y: y, 0, 1, 0.1, 10)
    print(f"y(1) ≈ {r[-1][1]:.6f}  (referenční e = {math.e:.6f})")
