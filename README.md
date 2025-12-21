# 📘 Příprava na zápočet – Numerické metody

Repozitář obsahuje implementace numerických metod používaných u zápočtu z NUM.
Každý odkaz vede **přímo na konkrétní Python soubor**, který danou metodu skutečně implementuje.

---

## 📑 Obsah (proklik na kód)

### I. Nelineární rovnice
- [Metoda bisekce](metody/bisekce.py)
- [Newtonova metoda – analytická derivace](metody/newtonroot.py)
- [Newtonova metoda – numerická derivace](metody/newtoneval.py)
- [Metoda sečen](metody/voldemort.py)
- [Steffensenova metoda](metody/voldemort.py)
- [Halleyho metoda](metody/voldemort.py)

> ⚠️ Poznámka: soubor `voldemort.py` obsahuje **více metod pro hledání kořenů**  
> (sečny, Steffensen, Halley).

---

### II. Polynomy a interpolace
- [Hornerovo schéma – vyčíslení polynomu](metody/horner.py)
- [Lagrangeova interpolace](metody/lagrange.py)
- [Newtonova interpolace – výpočet koeficientů](metody/newtoninterpolation.py)
- [Newtonova interpolace – vyčíslení polynomu](metody/newtoneval.py)
- [Vandermondova interpolace](metody/voldemort.py)

---

### III. Soustavy lineárních rovnic
- [Gaussova eliminace](metody/gauss.py)
- [Gaussova eliminace s částečnou pivotací](metody/gausspivot.py)
- [LU rozklad](metody/gausslu.py)
- [Jacobiho metoda](metody/jacobi.py)
- [Gauss–Seidelova metoda](metody/gausssiedel.py)

---

### IV. Aproximace
- [Metoda nejmenších čtverců – LSA (polynomická aproximace)](metody/lsa.py)
- [Řešení LSS pomocí normálních rovnic](metody/lss.py)

---

### V. Numerická integrace
- [Obdélníkové pravidlo (Midpoint rule)](metody/midpointrule.py)
- [Simpsonovo pravidlo](metody/simpson.py)

---

### VI. Obyčejné diferenciální rovnice (ODE)
- [Eulerova metoda](metody/eulerstep.py)

---

### VII. Nelineární regrese
- [Nelineární regrese – grid search](metody/nonlinearregression.py)

---

## 📌 Poznámky ke struktuře
- Každý soubor odpovídá **reálnému algoritmu v kódu**
- Názvy metod odpovídají **tomu, co bys řekl u zkoušky**
- Repo je vhodné jako **rychlá mapa: teorie → kód**
