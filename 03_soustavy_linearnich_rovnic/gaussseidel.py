import math

def gauss_seidel(a, b, max_iter, tol):
    """
    Řešení soustavy Ax = b pomocí Gauss-Seidelovy iterativní metody.
    Rozdíl oproti Jacobimu: nové hodnoty x[i] se používají ihned v téže iteraci.

    :param a: Matice soustavy (seznam seznamů, čtvercová n×n)
    :param b: Vektor pravé strany (délka n)
    :param max_iter: Maximální počet iterací
    :param tol: Tolerance konvergence
    :return: Vektor řešení x nebo None při selhání
    """
    n = len(a)
    if n != len(b) or any(len(row) != n for row in a):
        print("Error: Mismatched lengths")
        return None

    x = [0.0] * n

    for k in range(max_iter):
        x_prev = list(x)

        for i in range(n):
            if abs(a[i][i]) < 1e-12:
                print("Error: Zero diagonal element")
                return None

            sum_val = 0.0
            for j in range(n):
                if j != i:
                    sum_val += a[i][j] * x[j]  # používáme aktuální x (ne x_prev)

            x[i] = (b[i] - sum_val) / a[i][i]

        # Kontrola konvergence: maximální změna mezi iteracemi
        diff = max(abs(x[i] - x_prev[i]) for i in range(n))

        if any(math.isnan(v) or math.isinf(v) for v in x):
            print("Error: Did not converge")
            return None

        if diff < tol:
            return x

    print("Error: Did not converge")
    return None


if __name__ == "__main__":
    # Příklad: 4x + y = 9, x + 3y = 7  => x=2, y=1... správně x=20/11, y=19/11
    # Diagonálně dominantní soustava pro zaručenou konvergenci
    A = [[4, 1], [1, 3]]
    b = [9, 7]
    x = gauss_seidel(A, b, max_iter=100, tol=1e-6)
    print("Řešení x:", x)
