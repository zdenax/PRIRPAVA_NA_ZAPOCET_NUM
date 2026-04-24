import math
import sys
import os
try:
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
except NameError:
    pass  # spuštění přímo v notebooku — BASE už je na sys.path
from obecne_operace import multiply_matrix_vector

def jacobi(a, b, max_iter, tol, verbose=False):
    """
    Řešení soustavy Ax = b pomocí Jacobiho iterativní metody.

    :param a: Matice soustavy (seznam seznamů, čtvercová n×n)
    :param b: Vektor pravé strany (délka n)
    :param max_iter: Maximální počet iterací
    :param tol: Tolerance konvergence (reziduální norma)
    :param verbose: Vypisovat průběh iterací (default False)
    :return: Vektor řešení x nebo None při selhání
    """
    n = len(a)
    if n != len(b) or any(len(row) != n for row in a):
        print("Chyba: Nesouhlasí délky vstupních dat.")
        return None

    x  = [0.0] * n
    x0 = [0.0] * n

    for k in range(max_iter):
        for i in range(n):
            sum_val = 0.0
            for j in range(n):
                if j != i:
                    sum_val += a[i][j] * x0[j]
            if a[i][i] == 0:
                print("Chyba: Nulový diagonální prvek.")
                return None
            x[i] = (b[i] - sum_val) / a[i][i]

        x0 = list(x)
        ax = multiply_matrix_vector(a, x0)

        if any(math.isnan(v) or math.isinf(v) for v in ax):
            print("Chyba: Metoda neskonvergovala.")
            return None

        diff_sum = sum(abs(ax[i] - b[i]) for i in range(n))

        if verbose:
            print(f"Iterace {k+1:3d}: x = {[round(v,6) for v in x0]}, reziduum = {diff_sum:.4e}")

        if diff_sum < tol:
            if verbose:
                print(f"Konvergoval v iteraci {k+1}.")
            return x0

    print("Chyba: Metoda neskonvergovala.")
    return None
