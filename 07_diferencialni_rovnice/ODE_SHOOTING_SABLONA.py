import math
import sys
import os




# ============================================================
# 1. PŘEPIS ODE ZE ZADÁNÍ
#    y' = f(x, y)  →  return <vzorec ze zadání>
# ============================================================
def f_ode(x, y):
    return y - x          # <-- ZDE DOSAĎ VZOREC ZE ZADÁNÍ


# ============================================================
# 2. RESIDUAL FUNKCE
#    Spočítá integrál y(x) na [x0, xk] pro dané y(0) = s
#    a vrátí rozdíl od cílové hodnoty TARGET
# ============================================================
TARGET = 2                # <-- ZDE DOSAĎ CÍLOVOU HODNOTU ZE ZADÁNÍ
X0 = 0                    # počáteční bod intervalu
XK = 1                    # koncový bod intervalu
H = 0.1                   # krok integrace
N = int((XK - X0) / H)    # počet kroků


def residual(s):
    """
    :param s: střelecká počáteční podmínka y(x0) = s
    :return: integral y(x) dx - TARGET
    """
    #body = runge_kutta_4(f_ode, X0, s, H, N)
    body = heun(f_ode, X0, s, H, N)

    ys = [y for x, y in body]

    # lichoběžníkové pravidlo
    integral = H * (ys[0]/2 + sum(ys[1:-1]) + ys[-1]/2)

    # Simpson (přesnější, N musí být sudé)
    # integral = (H/3) * (ys[0] + 4*sum(ys[1::2]) + 2*sum(ys[2:-1:2]) + ys[-1])

    return integral - TARGET


# ============================================================
# 3. BISEKCE — najde s takové aby residual(s) = 0
#    Uprav interval [a, b] podle zadání
# ============================================================
A = -10                   # <-- ZDE UPRAV interval pro bisekci
B = 10                    # <-- ZDE UPRAV interval pro bisekci

s = bisection(residual, A, B, 1e-8, 100)

print(f"y(0) = {s:.10f}")
print(f"ověření: integral = {residual(s) + TARGET:.6f}  (má být {TARGET})")