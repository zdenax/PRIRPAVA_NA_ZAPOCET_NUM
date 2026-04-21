
def runge_kutta_4(f, x0, y0, h, n):
    """
    Řešení obyčejné diferenciální rovnice y' = f(x, y) pomocí Runge-Kutta 4. řádu.

    :param f: Funkce f(x, y) definující pravou stranu ODR (y' = f(x, y))
    :param x0: Počáteční bod x
    :param y0: Počáteční hodnota y pro x0
    :param h: Krok integrace
    :param n: Počet kroků (iterací) metody
    :return: Seznam bodů (x, y) řešení nebo None při chybě
    """
    import math
    if f is None or x0 is None or y0 is None or h is None or n is None:
        print("Error: Nil values are not supported.")
        return None
    if n < 0:
        print("Error: n must be non-negative.")
        return None
    points = [(x0, y0)]
    x = x0
    y = y0
    for i in range(n):
        k1 = f(x, y)
        k2 = f(x + 0.5*h, y + 0.5*h*k1)
        k3 = f(x + 0.5*h, y + 0.5*h*k2)
        k4 = f(x + h, y + h*k3)
        if any(math.isnan(k) or math.isinf(k) for k in (k1, k2, k3, k4)):
            print("Error: Function returned NaN or Inf during RK4 computation.")
            return None
        y_new = y + (h/6.0) * (k1 + 2*k2 + 2*k3 + k4)
        x_new = x + h
        if math.isnan(y_new) or math.isinf(y_new) or math.isnan(x_new) or math.isinf(x_new):
            print("Error: RK4 method diverged (NaN or Inf).")
            return None
        points.append((x_new, y_new))
        x, y = x_new, y_new
    return points
