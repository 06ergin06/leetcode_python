# https://leetcode.com/problems/add-digits/description/
class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return 0
        if num % 9 == 0 :
            return 9
        else:
            return num % 9
        
"""
### **Türkçe (Turkish)**  
**Neden İşe Yarar?**  
Dijital kök, bir sayının 9 ile bölünebilme kuralına dayanır. Bir sayının basamakları toplamı 9'un katı ise, o sayı 9'a tam bölünür. Bu nedenle:  
- **9'a bölünen sayılar:** Basamakları toplamı 9'un katıdır, dijital kök **9** olur.  
- **Diğer sayılar:** Sayının 9'a bölümünden kalan, dijital kökü verir.  

**Matematiksel Mantık:**  
- Herhangi bir sayı `n`, `n = 9k + r` şeklinde yazılabilir (burada `r` kalandır ve `0 ≤ r < 9`).  
- Dijital kök, `r`'ye eşittir. Eğer `r = 0` ise, sayı 9'a bölünür ve dijital kök **9** olur.  

---

### **English**  
**Why Does It Work?**  
The digital root is based on the divisibility rule for 9. If the sum of a number's digits is a multiple of 9, the number is divisible by 9. Therefore:  
- **Numbers divisible by 9:** Their digit sum is a multiple of 9, so the digital root is **9**.  
- **Other numbers:** The remainder when divided by 9 gives the digital root.  

**Mathematical Logic:**  
- Any number `n` can be written as `n = 9k + r` (where `r` is the remainder and `0 ≤ r < 9`).  
- The digital root is equal to `r`. If `r = 0`, the number is divisible by 9, and the digital root is **9**.  

---

### **Örnekler (Examples)**  
- **Türkçe:**  
  - 27 → 2 + 7 = 9 → 9'a bölünür → Dijital kök **9**.  
  - 100 → 100 % 9 = 1 → Dijital kök **1**.  

- **English:**  
  - 27 → 2 + 7 = 9 → Divisible by 9 → Digital root is **9**.  
  - 100 → 100 % 9 = 1 → Digital root is **1**.  

---

**Kısaca (In Short):**  
Dijital kök, 9 ile bölünebilme kuralının bir sonucudur ve matematiksel olarak `n % 9` ile hesaplanır.  
The digital root is a result of the divisibility rule for 9 and is mathematically calculated as `n % 9`.
"""