import sys
import os
_base = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(_base, '..', '03_soustavy_linearnich_rovnic'))
sys.path.insert(0, os.path.join(_base, '..'))
from gausspivot import gauss_pivot
from obecne_operace import multiply_matrix_vector, transpose, multiply_matrices

def lss(a, y):
    """
    Řeší problém nejmenších čtverců pro soustavu Ax = y.
    Vrací vektor x, který minimalizuje ||Ax - y||^2.

    :param a: Matice soustavy (seznam seznamů, m×n)
    :param y: Vektor pravé strany (délka m)
    :return: Vektor řešení x (délka n) nebo None při selhání
    """
    # 1. Transpozice matice A -> A^T
    at = transpose(a)
    
    # 2. Součin A^T * A (vytvoří čtvercovou matici)
    ata = multiply_matrices(at, a)
    
    # 3. Součin A^T * y (vytvoří vektor pravé strany)
    aty = multiply_matrix_vector(at, y)
    
    # 4. Vyřešení soustavy (A^T * A) * x = A^T * y pomocí Gausse s pivotací
    return gauss_pivot(ata, aty)