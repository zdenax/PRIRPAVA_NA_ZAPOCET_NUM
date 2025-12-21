# KI-NUM

## Table of Content
1. [**Usecases**](usecases.md)
    - [Numerická integrace](usecases.md#numerick%c3%a1-integrace)
    - [Řešení lineárních soustav](usecases.md#re%c5%a1en%c3%ad-line%c3%a1rn%c3%adch-soustav)
    - [Rozklad matice](usecases.md#rozklad-matice)
    - [Polynomická interpolace](usecases.md#polynomick%c3%a1-interpolace)
    - [Vyhodnocení polynomu](usecases.md#vyhodnocen%c3%ad-polynomu)
    - [Aproximace a regrese](usecases.md#aproximace-a-regrese)
    - [Hledání kořenů](usecases.md#hled%c3%a1n%c3%ad-ko%c5%99en%c5%af)
    - [Řešení ODR](usecases.md#re%c5%a1en%c3%ad-odr)
    - [Nelineární regrese](usecases.md#neline%c3%a1rn%c3%ad-regrese)
2. [**Methods**](methods.md)
    - [MidpointRule](methods.md#midpointrule)
    - [Simpson](methods.md#simpson)
    - [SimpsonUniversal](methods.md#simpsonuniversal)
    - [Gauss](methods.md#gauss)
    - [GaussPivot](methods.md#gaussspivot)
    - [GaussLU](methods.md#gausslu)
    - [GaussSeidel](methods.md#gausssiedel)
    - [Jacobi](methods.md#jacobi)
    - [Lagrange](methods.md#lagrange)
    - [NewtonInterpolation](methods.md#newtoninterpolation)
    - [Valdemort](methods.md#voldemort)
    - [Horner](methods.md#horner)
    - [NewtonEvaluation](methods.md#newtoneval)
    - [MNČ](methods.md#mnc)
    - [MNČsmall](methods.md#mncsmall)
    - [NelineárníRegrese](methods.md#nlinearni_regrese)
    - [Bisekce](methods.md#bisekce)
    - [NewtonRoot](methods.md#newtonroot)
    - [Euler](methods.md#euler)
    - [Graphs](methods.md#graphs)
    - [ObecnéOperace](methods.md#obecne_operace)
3. [**Documents**](#documents)

## Quick Guide: How to Choose Numerical Methods

Rychlý přehled pro správný výběr numerické metody podle typu úlohy.

---

### 1. Numerická integrace

**Znaky:**  
- Výpočet určitého integrálu, ∫, plocha pod křivkou.

**Doporučené metody:**  
- `simpson.py`  
- `simpson_universal.py`  
- `midpointrule.py`

---

### 2. Řešení lineárních soustav (Ax = b)

**Znaky:**  
- Matice A, vektor b, řešení x.

**Doporučené metody:**  
- `gauss.py`  
- `gaussspivot.py`  
- `gausssiedel.py`  
- `jacobi.py`

---

### 3. Rozklad matice

**Znaky:**  
- Opakované řešení stejné matice, LU rozklad.

**Doporučené metody:**  
- `gausslu.py`

---

### 4. Polynomická interpolace

**Znaky:**  
- Polynom procházející daty.

**Doporučené metody:**  
- `lagrange.py`  
- `newtoninterpolation.py`  
- `voldemort.py`

---

### 5. Vyhodnocení polynomu

**Znaky:**  
- Rychlé vyhodnocení polynomu v daném x.

**Doporučené metody:**  
- `horner.py`  
- `newtoneval.py`

---

### 6. Aproximace a regrese

**Znaky:**  
- „Best fit“, trend, minimalizace chyb.

**Doporučené metody:**  
- `MNC.py`  
- `MNCsmall.py`

---

### 7. Nelineární regrese

**Znaky:**  
- Fit nelineárního modelu na data.

**Doporučené metody:**  
- `NLINEARNI_REGRESE.py`

---

### 8. Hledání kořenů

**Znaky:**  
- Najít x tak, že f(x)=0, průsečíky.

**Doporučené metody:**  
- `bisekce.py`  
- `newtonroot.py`

---

### 9. Řešení ODR

**Znaky:**  
- Řešení obyčejných diferenciálních rovnic.

**Doporučené metody:**  
- `euler.py`

---

### 10. Utility a vizualizace

**Znaky:**  
- Grafy, pomocné matematické funkce.

**Doporučené moduly:**  
- `graphs.py`  
- `obecne_operace.py`
