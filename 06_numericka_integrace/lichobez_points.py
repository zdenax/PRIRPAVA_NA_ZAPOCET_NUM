def trapezoid_points(body):
    """
    Lichoběžníkové pravidlo přímo na seznamu bodů (x, y).
    
    :param body: Seznam dvojic (x, y)
    :return: Odhad integrálu
    """
    result = 0.0
    for i in range(len(body) - 1):
        x1, y1 = body[i]
        x2, y2 = body[i+1]
        result += 0.5 * (y1 + y2) * (x2 - x1)
    return result