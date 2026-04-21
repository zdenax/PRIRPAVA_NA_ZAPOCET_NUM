def simpson(y, h):
    """
    Simpsonovo pravidlo nad hodnotami y v ekvidistantních uzlech.
    """
    n = len(y) - 1
    if n < 2 or n % 2 != 0:
        raise ValueError("Počet dílků musí být sudý")

    s = y[0] + y[-1]
    s += 4 * sum(y[i] for i in range(1, n, 2))
    s += 2 * sum(y[i] for i in range(2, n, 2))
    return s * h / 3
