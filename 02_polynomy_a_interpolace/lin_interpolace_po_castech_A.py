



def linear_interpolation(x_vals, y_vals, t):
    """
    Lineární interpolace po částech pro zadané body.

    :param x_vals: Seznam uzlů x (musí mít stejnou délku jako y_vals)
    :param y_vals: Seznam uzlů y (hodnot funkce v bodech x_vals)
    :param t: Bod nebo seznam bodů, ve kterých chceme interpolovat
    :return: Interpolovaná hodnota (nebo seznam hodnot) nebo None při chybě
    """
    if x_vals is None or y_vals is None or t is None:
        print("Error: Nil values are not supported.")
        return None
    n = len(x_vals)
    if n == 0 or n != len(y_vals):
        print("Error: Mismatched lengths of input lists.")
        return None
    # Pokud t není seznam, zabalíme ho do seznamu pro jednotné zpracování
    t_list = t if isinstance(t, list) else [t]
    x_min = x_vals[0]
    x_max = x_vals[-1]
    # Kontrola, zda všechny body t jsou v rozsahu [x_min, x_max]
    for val in t_list:
        if val < x_min or val > x_max:
            print("Error: Interpolation point out of range.")
            return None
    result = []
    for val in t_list:
        interpolated_val = None
        # Najdeme interval [x_i, x_{i+1}], v němž leží hodnota val
        for i in range(n - 1):
            if x_vals[i] <= val <= x_vals[i + 1]:
                if val == x_vals[i]:
                    interpolated_val = y_vals[i]
                elif val == x_vals[i + 1]:
                    interpolated_val = y_vals[i + 1]
                else:
                    interpolated_val = y_vals[i] + (y_vals[i+1] - y_vals[i]) * ((val - x_vals[i]) / (x_vals[i+1] - x_vals[i]))
                break
        if interpolated_val is None:
            # Pokud nastane (val == x_max), vezmeme poslední bod
            if val == x_max:
                interpolated_val = y_vals[-1]
            else:
                # Mimo rozsah (nemělo by nastat díky kontrole výše)
                print("Error: Interpolation point out of range.")
                return None
        result.append(interpolated_val)
    # Pokud vstup nebyl seznam, vracíme skalární hodnotu místo seznamu
    if not isinstance(t, list):
        return result[0] if result else None
    return result
