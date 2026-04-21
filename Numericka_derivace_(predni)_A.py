def forward_difference(f, x, h):
    """
    Numerická derivace pomocí dopředné diference.

    :param f: Funkce f(x), kterou derivujeme
    :param x: Bod, ve kterém počítáme derivaci
    :param h: Krok (malé číslo) pro diferencování
    :return: Odhad f'(x) nebo None při chybě
    """
    import math
    if f is None or x is None or h is None:
        print("Error: Nil values are not supported.")
        return None
    if h == 0:
        print("Error: Zero step size.")
        return None
    f_x = f(x)
    f_xh = f(x + h)
    if math.isnan(f_x) or math.isnan(f_xh) or math.isinf(f_x) or math.isinf(f_xh):
        print("Error: Function returned NaN or Inf.")
        return None
    result = (f_xh - f_x) / h
    if math.isnan(result) or math.isinf(result):
        print("Error: Numerical differentiation failed.")
        return None
    return result