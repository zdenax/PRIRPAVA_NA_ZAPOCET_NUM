# Příprava na zápočet – Numerické metody (NUM)

Repozitář obsahuje implementace numerických metod rozdělené přesně podle kapitol
v teorii k zápočtu [NUM_TEORIE_ZDENĚK_TOUŠKA.pdf](NUM_TEORIE_ZDENĚK_TOUŠKA.pdf).

---

## Obsah (proklik na složky a soubory)

### 01 – Nelineární rovnice
- Složka: [`01_nelinearni_rovnice/`](01_nelinearni_rovnice)
- Metoda bisekce
- Newtonova metoda (kořen rovnice)

---

### 02 – Polynomy a interpolace
- Složka: [`02_polynomy_a_interpolace/`](02_polynomy_a_interpolace)
- Lagrangeova interpolace
- Newtonova interpolace
- Vandermondova interpolace
- Hornerovo schéma (vyčíslení polynomu)

---

### 03 – Soustavy lineárních rovnic
- Složka: [`03_soustavy_linearnich_rovnic/`](03_soustavy_linearnich_rovnic)
- Gaussova eliminace
- Gaussova eliminace s pivotací
- LU rozklad

---

### 04 – Aproximace
- Složka: [`04_aproximace/`](04_aproximace)
- Metoda nejmenších čtverců (MNC)
- Maticová varianta MNC
- Aproximace dat

---

### 05 – Iterační metody pro soustavy lineárních rovnic
- Složka: [`05_iter_metody_soustav_lin_rovnic/`](05_iter_metody_soustav_lin_rovnic)
- Jacobiho metoda
- Gauss–Seidelova metoda

---

### 06 – Numerická integrace
- Složka: [`06_numericka_integrace/`](06_numericka_integrace)
- Obdélníkové pravidlo (Midpoint rule)
- Simpsonovo pravidlo
- Univerzální Simpsonovo pravidlo

---

### 07 – Diferenciální rovnice
- Složka: [`07_diferencialni_rovnice/`](07_diferencialni_rovnice)
- Eulerova metoda

---

## Společné soubory
- [`obecne_operace.py`](obecne_operace.py) – pomocné maticové a vektorové operace
- [`graphs.py`](graphs.py) – pomocné funkce pro vykreslování

---

## Poznámky
- Složky a názvy odpovídají **přesně názvům kapitol v PDF**
- Každá metoda je implementována samostatně
- Složky `__pycache__/` nejsou součástí logiky projektu a lze je mazat
- Označení _A == AI přepis z officiálních skript do Pythonu.