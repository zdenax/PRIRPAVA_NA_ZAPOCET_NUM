import math

def gauss_seidel(a, b, max_iter, tol, verbose=False):
    """
    Řešení soustavy Ax = b pomocí Gauss-Seidelovy iterativní metody.
    Rozdíl oproti Jacobimu: nové hodnoty x[i] se používají ihned v téže iteraci.

    :param a: Matice soustavy (seznam seznamů, čtvercová n×n)
    :param b: Vektor pravé strany (délka n)
    :param max_iter: Maximální počet iterací
    :param tol: Tolerance konvergence
    :param verbose: Vypisovat průběh iterací (default False)
    :return: Vektor řešení x nebo None při selhání
    """
    n = len(a)
    if n != len(b) or any(len(row) != n for row in a):
        print("Chyba: Nesouhlasí délky vstupních dat.")
        return None

    x = [0.0] * n

    for k in range(max_iter):
        x_prev = list(x)

        for i in range(n):
            if abs(a[i][i]) < 1e-12:
                print("Chyba: Nulový diagonální prvek.")
                return None
            sum_val = 0.0
            for j in range(n):
                if j != i:
                    sum_val += a[i][j] * x[j]
            x[i] = (b[i] - sum_val) / a[i][i]

        diff = max(abs(x[i] - x_prev[i]) for i in range(n))

        if any(math.isnan(v) or math.isinf(v) for v in x):
            print("Chyba: Metoda neskonvergovala.")
            return None

        if verbose:
            print(f"Iterace {k+1:3d}: x = {[round(v,6) for v in x]}, max_diff = {diff:.4e}")

        if diff < tol:
            if verbose:
                print(f"Konvergoval v iteraci {k+1}.")
            return x

    print("Chyba: Metoda neskonvergovala.")
    return None


if __name__ == "__main__":
    A = [[4, 1], [1, 3]]
    b = [9, 7]
    x = gauss_seidel(A, b, max_iter=100, tol=1e-6)
    print("Řešení x:", x)
