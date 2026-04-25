def multiply_matrix_vector(a, x):
    """Pomocná funkce simulující matrix.MulVec(a, x)"""
    n = len(a)
    ax = [0.0] * n
    for i in range(n):
        for j in range(len(a[i])):
            ax[i] += a[i][j] * x[j]
    return ax

def transpose(a):
    """Transpozice matice."""
    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]

def multiply_matrices(a, b):
    """Násobení dvou matic."""
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])
    res = [[0.0 for _ in range(cols_b)] for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                res[i][j] += a[i][k] * b[k][j]
    return res


#stavět matici A a vektor b.


def build_matrix(N):
    """
    Sestaví matici A (N×N) kde A[i][j] = 1 - 1/(i+j+1).
    Výjimka: A[0][0] = 0 (i+j+1=1, výsledek 1-1/1=0).

    :param N: Rozměr matice
    :return: Matice A jako seznam seznamů
    """
    A = []
    for i in range(N):
        row = []
        for j in range(N):
            if i == 0 and j == 0:
                row.append(0.0)  # i+j+1 = 1, 1 - 1/1 = 0
            else:
                row.append(1 - 1 / (i + j + 1))
        A.append(row)
    return A


def build_vector(N):
    """
    Sestaví vektor b délky N, kde každý prvek = 1.

    :param N: Délka vektoru
    :return: Vektor b jako seznam
    """
    b = []
    for _ in range(N):
        b.append(1)
    return b


if __name__ == "__main__":
    a = build_matrix(10)
    b = build_vector(10)
