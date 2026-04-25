import math

def gauss_pivot(a, b):
    n = len(b)
    ab = [list(a[i]) + [b[i]] for i in range(n)]
    for k in range(n - 1):
        pivot_row = max(range(k, n), key=lambda r: abs(ab[r][k]))
        if pivot_row != k:
            ab[k], ab[pivot_row] = ab[pivot_row], ab[k]
        for i in range(k + 1, n):
            if ab[k][k] == 0:
                return None
            c = -ab[i][k] / ab[k][k]
            for j in range(k, n + 1):
                ab[i][j] += c * ab[k][j]
    x = [0.0] * n
    x[n - 1] = ab[n - 1][n] / ab[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = (ab[i][n] - sum(ab[i][j] * x[j] for j in range(i + 1, n))) / ab[i][i]
    return x

def lsa(x, y, n):
    """
    Aproximace dat polynomem stupně (n-1) pomocí metody nejmenších čtverců.

    n=2 → lineární:
        koefs = lsa(x, y, 2)
        y_pred = koefs[0] + koefs[1]*x

    n=3 → kvadratický:
        koefs = lsa(x, y, 3)
        y_pred = koefs[0] + koefs[1]*x + koefs[2]*x**2

    n=4 → kubický:
        koefs = lsa(x, y, 4)
        y_pred = koefs[0] + koefs[1]*x + koefs[2]*x**2 + koefs[3]*x**3

    Obecně: y_pred = sum(koefs[i] * x**i for i in range(len(koefs)))

    :param x: Vstupní data (nezávislá proměnná)
    :param y: Naměřené hodnoty (závislá proměnná)
    :param n: Počet koeficientů (stupeň + 1)
    :return: Koeficienty polynomu [a0, a1, ..., an-1]
    """
    if len(x) == 0 or len(y) == 0:
        print("Chyba: Vstupní hodnoty nesmí být None.")
        return None

    if len(x) != len(y):
        print("Chyba: Nesouhlasí délky X a Y.")
        return None

    if n <= 0:
        print("Chyba: Nepodporovaná hodnota n.")
        return None

    # Inicializace matice A (n x n) a vektoru b (n)
    A = [[0.0 for _ in range(n)] for _ in range(n)]
    b = [0.0] * n

    # Sestavení normální soustavy rovnic
    for i in range(n):
        # Naplnění matice soustavy (sumy mocnin x)
        for j in range(n):
            s = 0.0
            for k in range(len(x)):
                s += math.pow(x[k], float(i + j))
            A[i][j] = s
        
        # Naplnění pravé strany (sumy součinů y * x^i)
        s = 0.0
        for k in range(len(x)):
            s += y[k] * math.pow(x[k], float(i))
        b[i] = s

    # Vyřešení soustavy pomocí Gausse s pivotací
    return gauss_pivot(A, b)