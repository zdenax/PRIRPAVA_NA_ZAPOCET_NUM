# 📘 Příprava na zápočet – Numerické metody

Repozitář obsahuje implementace numerických metod k zápočtu z NUM.
Odkazy vedou **přímo na konkrétní kód v podsložkách**.

---

## 📑 Obsah (proklik na kód)

### I. Nelineární rovnice
- [Metoda bisekce](metody/nelinearni_rovnice/bisekce.py)
- [Newtonova metoda – analytická derivace](metody/nelinearni_rovnice/newtonroot.py)
- [Newtonova metoda – numerická derivace](metody/nelinearni_rovnice/newtoneval.py)
- [Metoda sečen](metody/nelinearni_rovnice/secant.py)
- [Steffensenova metoda](metody/nelinearni_rovnice/steffensen.py)
- [Halleyho metoda](metody/nelinearni_rovnice/halley.py)

---

### II. Polynomy a interpolace
- [Hornerovo schéma – vyčíslení polynomu](metody/polynomy/horner.py)
- [Lagrangeova interpolace](metody/polynomy/lagrange.py)
- [Newtonova interpolace – výpočet koeficientů](metody/polynomy/newtoninterpolation.py)
- [Newtonova interpolace – vyčíslení](metody/polynomy/newtoneval.py)
- [Vandermondova interpolace](metody/polynomy/voldemort.py)

---

### III. Soustavy lineárních rovnic
- [Gaussova eliminace](metody/lin_rovnice/gauss.py)
- [Gaussova eliminace s částečnou pivotací](metody/lin_rovnice/gausspivot.py)
- [LU rozklad](metody/lin_rovnice/gausslu.py)
- [Jacobiho metoda](metody/lin_rovnice/jacobi.py)
- [Gauss–Seidelova metoda](metody/lin_rovnice/gausssiedel.py)

---

### IV. Aproximace
- [Metoda nejmenších čtverců – LSA](metody/aproximace/lsa.py)
- [Řešení LSS (normální rovnice)](metody/aproximace/lss.py)

---

### V. Numerická integrace
- [Obdélníkové pravidlo (Midpoint rule)](metody/integrace/midpointrule.py)
- [Simpsonovo pravidlo](metody/integrace/simpson.py)

---

### VI. Obyčejné diferenciální rovnice (ODE)
- [Eulerova metoda](metody/ode/eulerstep.py)

---

### VII. Nelineární regrese
- [Nelineární regrese – grid search](metody/regrese/nonlinearregression.py)

---

## 📌 Poznámka
- Struktura odpovídá **reálným podsložkám**
- `voldemort.py` = **POUZE Vandermondova interpolace**
- Každý odkaz → **1 konkrétní metoda**
