def gauss_lu(a, b):
    """
    Řešení soustavy Ax = b pomocí LU rozkladu (bez pivotace).
    Rozloží matici A = L * U, pak řeší Ly = b a Ux = y.

    :param a: Matice soustavy (seznam seznamů, čtvercová n×n)
    :param b: Vektor pravé strany (délka n)
    :return: Vektor řešení x nebo None při selhání
    """
    n = len(b)
    if n != len(a) or any(len(row) != n for row in a):
        print("Error: Mismatched lengths")
        return None

    # Inicializace L (jednotková) a U (kopie A)
    L = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    U = [list(row) for row in a]

    # LU rozklad (Doolittleova metoda)
    for k in range(n):
        if abs(U[k][k]) < 1e-12:
            print("Error: Zero pivot - matice je singulární nebo je nutná pivotace")
            return None
        for i in range(k + 1, n):
            L[i][k] = U[i][k] / U[k][k]
            for j in range(k, n):
                U[i][j] -= L[i][k] * U[k][j]

    # Přímá substituce: Ly = b
    y = [0.0] * n
    for i in range(n):
        sum_val = b[i]
        for j in range(i):
            sum_val -= L[i][j] * y[j]
        y[i] = sum_val  # L[i][i] = 1 vždy

    # Zpětná substituce: Ux = y
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        sum_val = y[i]
        for j in range(i + 1, n):
            sum_val -= U[i][j] * x[j]
        x[i] = sum_val / U[i][i]

    return x


if __name__ == "__main__":
    # Příklad: 2x + y = 5, x + 3y = 10  => x=1, y=3
    A = [[2, 1], [1, 3]]
    b = [5, 10]
    x = gauss_lu(A, b)
    print("Řešení x:", x)
