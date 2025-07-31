# Binary and Decimal Conversion (Integer and Fractional Numbers)

## 🔢 1. Integer Part Conversion

### 1.1 Decimal to Binary (Integer Part)

To convert a decimal integer to binary:

1. **Divide** the number by 2
2. The **remainder** (0 or 1) becomes the least significant bit (LSB)
3. Take the **quotient** and repeat
4. Continue until you get a quotient of 0
5. Read the bits from bottom to top to get the result

**Example: Converting 13 to binary**
```
13 ÷ 2 = 6 remainder 1 → LSB = 1
6 ÷ 2 = 3 remainder 0 → bit = 0  
3 ÷ 2 = 1 remainder 1 → bit = 1
1 ÷ 2 = 0 remainder 1 → MSB = 1
```
**Result: 13₁₀ = 1101₂**

### 1.2 Binary to Decimal (Integer Part)

To convert a binary integer to decimal:

- Each bit represents a power of 2 based on its position (from right to left)
- Add up the sum of: bit × 2^position

**Example: Converting 1101₂ to decimal**
```
1101₂ = 1×2³ + 1×2² + 0×2¹ + 1×2⁰
      = 1×8 + 1×4 + 0×2 + 1×1
      = 8 + 4 + 0 + 1
      = 13₁₀
```

---

## 🔄 2. Fractional Part Conversion

### 2.1 Decimal to Binary (Fraction)

To convert a decimal fraction (e.g., 0.625) to binary:

1. **Multiply** the fraction by 2
2. The **integer part** becomes the next binary digit after the decimal point
3. Keep the **fractional part** and repeat
4. Continue until you get 0 or reach desired precision

**Example: Converting 0.625 to binary**
```
0.625 × 2 = 1.25 → bit = 1
0.25 × 2 = 0.5  → bit = 0
0.5 × 2 = 1.0   → bit = 1
```
**Result: 0.625₁₀ = 0.101₂**

### 2.2 Binary to Decimal (Fraction)

To convert a binary fraction (e.g., 0.101) to decimal:

- Each bit represents a negative power of 2 based on its position after the decimal point
- Add up the sum of: bit × 2^(-position)

**Example: Converting 0.101₂ to decimal**
```
0.101₂ = 1×2⁻¹ + 0×2⁻² + 1×2⁻³
       = 1×0.5 + 0×0.25 + 1×0.125
       = 0.5 + 0 + 0.125
       = 0.625₁₀
```

---

## 🎯 3. Mixed Number Conversion

To convert a decimal number with both integer and fractional parts (e.g., 13.625):

### Forward Conversion (Decimal → Binary)
1. **Convert the integer part**: 13₁₀ → 1101₂
2. **Convert the fractional part**: 0.625₁₀ → 0.101₂
3. **Combine the results**: 13.625₁₀ = 1101.101₂

### Reverse Conversion (Binary → Decimal)
1. **Convert the integer part**: 1101₂ → 13₁₀
2. **Convert the fractional part**: 0.101₂ → 0.625₁₀
3. **Combine the results**: 1101.101₂ = 13.625₁₀

---

## 📝 Summary

| Conversion Type | Method | Example |
|----------------|--------|---------|
| **Decimal → Binary (Integer)** | Divide by 2, collect remainders | 13₁₀ → 1101₂ |
| **Binary → Decimal (Integer)** | Sum of bits × 2^position | 1101₂ → 13₁₀ |
| **Decimal → Binary (Fraction)** | Multiply by 2, collect integer parts | 0.625₁₀ → 0.101₂ |
| **Binary → Decimal (Fraction)** | Sum of bits × 2^(-position) | 0.101₂ → 0.625₁₀ |

---

*💡 **Tip**: Always verify your conversions by converting back to the original number system!*

