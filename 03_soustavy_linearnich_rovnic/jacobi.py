import math
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from obecne_operace import multiply_matrix_vector

def jacobi(a, b, max_iter, tol):
    """
    Řešení soustavy Ax = b pomocí Jacobiho iterativní metody.
    """
    n = len(a)
    if n != len(b) or any(len(row) != n for row in a):
        print("Error: Mismatched lengths")
        return None

    x = [0.0] * n   # Nové hodnoty
    x0 = [0.0] * n  # Hodnoty z předchozí iterace (k-té)

    for k in range(max_iter):
        for i in range(n):
            sum_val = 0.0
            # Všimni si: používáme výhradně hodnoty z x0
            for j in range(n):
                if j != i:
                    sum_val += a[i][j] * x0[j]
            
            if a[i][i] == 0:
                print("Error: Zero diagonal element")
                return None
            
            # Výpočet nové hodnoty x[i]
            # Vzorec: (b[i] - suma(A[i][j]*x0[j] pro j != i)) / A[i][i]
            x[i] = (b[i] - sum_val) / a[i][i]

        # Aktualizace x0 pro další iteraci (copy v Go)
        x0 = list(x)

        # Kontrola konvergence
        ax = multiply_matrix_vector(a, x0)
        
        # Kontrola na chyby (NaN/Inf)
        if any(math.isnan(v) or math.isinf(v) for v in ax):
            print("Error: Did not converge")
            return None

        # Výpočet rezidua (rozdílu od pravé strany)
        diff_sum = sum(abs(ax[i] - b[i]) for i in range(n))

        if diff_sum < tol:
            return x0

    print("Error: Did not converge")
    return None