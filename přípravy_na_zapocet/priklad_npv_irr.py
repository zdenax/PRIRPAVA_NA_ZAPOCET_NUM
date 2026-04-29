"""
Výpočet NPV a IRR metodou regula falsi.

Zadání:
  Diskontní sazba nižší: 10%
  Diskontní sazba vyšší: 30%
  Cash flow A: rok 0 = -8, roky 1-3 = +4
"""

CF  = [-8, 4, 4, 4]
in_ = 0.10
iv  = 0.30


def npv(i):
    return sum(CF[t] / (1 + i) ** t for t in range(len(CF)))


def regula_falsi(f, a, b, tol, max_iter):
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        print("Error: NPV nemění znaménko v zadaném intervalu.")
        return None
    for _ in range(max_iter):
        c = a - fa * (b - a) / (fb - fa)
        fc = f(c)
        if abs(fc) < tol:
            return c
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    return None


# tabulka DCF
print(f"{'Rok':<6} {'CF':>6} {'DCF 10%':>10} {'DCF 30%':>10}")
print("-" * 36)
for t in range(len(CF)):
    print(f"{t:<6} {CF[t]:>6} {CF[t]/(1+in_)**t:>10.4f} {CF[t]/(1+iv)**t:>10.4f}")
print("-" * 36)
print(f"{'NPV':<13} {npv(in_):>10.4f} {npv(iv):>10.4f}")
print()

irr = regula_falsi(npv, in_, iv, tol=1e-6, max_iter=100)
print(f"IRR = {irr * 100:.4f} %")

# alternativa - volání hotové metody z repozitáře (stejný výsledek):
# exec(open('01_nelinearni_rovnice/regula_falsi_A.py').read())
# irr = regula_falsi(npv, in_, iv, tol=1e-6, max_iter=100)
