# Conversion entre binaire et décimal (nombres entiers et fractionnaires)

## 1. Conversion de la partie entière

### 1.1 De décimal à binaire (partie entière)

Pour convertir la partie entière décimale en binaire :

- Divise le nombre par 2.
- Le **reste** (0 ou 1) devient le bit le moins significatif (LSB).
- Prends le quotient et recommence.
- Répète jusqu'à obtenir un quotient de 0.
- Lis les bits de bas en haut pour obtenir le résultat.

Exemple avec 13 :
- 13 ÷ 2 = 6 reste 1 → LSB = 1
- 6 ÷ 2 = 3 reste 0 → bit = 0  
- 3 ÷ 2 = 1 reste 1 → bit = 1
- 1 ÷ 2 = 0 reste 1 → MSB = 1
- Résultat : 1101₂

### 1.2 De binaire à décimal (partie entière)

Pour convertir un nombre binaire entier en décimal :

- Chaque bit représente une puissance de 2, selon sa position (de droite à gauche).
- Additionne la somme des bits × 2^position.

Exemple avec 1101₂ :
- 1×2³ + 1×2² + 0×2¹ + 1×2⁰ = 8 + 4 + 0 + 1 = 13₁₀

---

## 2. Conversion de la partie fractionnaire

### 2.1 De décimal à binaire (fraction)

Pour convertir la partie fractionnaire décimale (ex: 0.625) en binaire :

- Multiplie la fraction par 2.
- Le **bit entier** obtenu devient le prochain chiffre binaire après la virgule.
- Garde la partie fractionnaire et recommence.
- Répète jusqu'à obtenir 0 ou la précision souhaitée.

Exemple :  
0.625 × 2 = 1.25 → bit = 1  
0.25 × 2 = 0.5 → bit = 0  
0.5 × 2 = 1.0 → bit = 1  
Résultat : 0.101

### 2.2 De binaire à décimal (fraction)

Pour convertir une fraction binaire (ex: 0.101) en décimal :

- Chaque bit représente une puissance négative de 2, selon sa position après la virgule.  
- Additionne la somme des bits × \(2^{-position}\).

Exemple :  
\(0.101_2 = 1 \times 2^{-1} + 0 \times 2^{-2} + 1 \times 2^{-3} = 0.5 + 0 + 0.125 = 0.625\)

---

## 3. Conversion de nombres mixtes

Pour convertir un nombre décimal avec partie entière et fractionnaire (ex: 13.625) :

1. **Convertis la partie entière** (13 → 1101₂)
2. **Convertis la partie fractionnaire** (0.625 → 0.101₂)
3. **Combine les résultats** : 1101.101₂

Pour la conversion inverse :
1. **Convertis la partie entière** (1101₂ → 13₁₀)
2. **Convertis la partie fractionnaire** (0.101₂ → 0.625₁₀)
3. **Combine les résultats** : 13.625₁₀

---

