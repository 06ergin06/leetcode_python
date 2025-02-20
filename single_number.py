# https://leetcode.com/problems/single-number/description/
class Solution(object):
    def singleNumber(self, nums):
        j = 0
        for num in nums:
            j ^= num #XOR
        return j

"""
-------
Türkçe
-------

### XOR İşlemi Nedir?
XOR (exclusive OR), bit düzeyinde bir işlemdir. İki bit üzerinde çalışır ve şu kurallara sahiptir:
- Aynı bitler için: `0 ^ 0 = 0` ve `1 ^ 1 = 0`
- Farklı bitler için: `0 ^ 1 = 1` ve `1 ^ 0 = 1`

Örneğin:
- `5 ^ 3` işlemi:
  - `5` in binary: `0101`
  - `3` in binary: `0011`
  - Sonuç: `0110` (yani `6`)

---

### XOR'un Özellikleri
1. **Değişme Özelliği**: `a ^ b = b ^ a`
2. **Birleşme Özelliği**: `a ^ (b ^ c) = (a ^ b) ^ c`
3. **Kendisiyle XOR**: `a ^ a = 0`
4. **Sıfırla XOR**: `a ^ 0 = a`

Bu özellikler, XOR işleminin tekrarlanmayan öğeyi bulmak için kullanılmasını sağlar.

---

### Tekrarlanmayan Öğeyi Bulma Mantığı
Bir listede tüm sayılar çift sayıda tekrarlanıyor ve sadece bir sayı tek sayıda (genellikle bir kez) bulunuyorsa, XOR işlemi bu sayıyı bulmamızı sağlar. İşte nasıl çalıştığı:

1. **Başlangıç Değeri**: `result = 0` (XOR işlemi için nötr eleman).
2. **Listedeki Her Sayı İçin**:
   - `result ^= num` işlemi yapılır.
3. **Sonuç**:
   - Tekrarlanan sayılar birbirini iptal eder (`a ^ a = 0`).
   - Sadece tekrarlanmayan sayı kalır (`0 ^ a = a`).

---

### Örnek Üzerinde Adım Adım İşleyiş
Liste: `[4, 1, 2, 1, 2]`

1. **Başlangıç**: `result = 0`
2. **Adım 1**: `0 ^ 4 = 4`
   - `result = 4`
3. **Adım 2**: `4 ^ 1 = 5`
   - `result = 5`
4. **Adım 3**: `5 ^ 2 = 7`
   - `result = 7`
5. **Adım 4**: `7 ^ 1 = 6`
   - `result = 6`
6. **Adım 5**: `6 ^ 2 = 4`
   - `result = 4`

Sonuç: `4` (tekrarlanmayan öğe).

---

### Neden XOR Kullanıyoruz?
1. **Zaman Verimliliği**: O(n) zaman karmaşıklığı ile çalışır.
2. **Bellek Verimliliği**: O(1) bellek kullanır, çünkü sadece bir değişken (`result`) tutar.
3. **Basit ve Etkili**: Kod kısa ve anlaşılırdır.

---

### XOR'un Sınırlamaları
- Bu yöntem sadece **bir tane** tekrarlanmayan öğe olduğunda çalışır.
- Eğer birden fazla tekrarlanmayan öğe varsa, bu yöntem doğru sonucu vermez.

---

-------
English
-------

### What is the XOR Operation?
XOR (exclusive OR) is a bitwise operation. It works on two bits and follows these rules:
- For the same bits: `0 ^ 0 = 0` and `1 ^ 1 = 0`
- For different bits: `0 ^ 1 = 1` and `1 ^ 0 = 1`

For example:
- `5 ^ 3`:
  - `5` in binary: `0101`
  - `3` in binary: `0011`
  - Result: `0110` (which is `6`)

---

### Properties of XOR
1. **Commutative Property**: `a ^ b = b ^ a`
2. **Associative Property**: `a ^ (b ^ c) = (a ^ b) ^ c`
3. **Self-Inverse**: `a ^ a = 0`
4. **Identity Element**: `a ^ 0 = a`

These properties make XOR useful for finding the unique element in a list.

---

### Logic for Finding the Unique Element
If all numbers in a list appear an even number of times except for one number that appears an odd number of times (usually once), the XOR operation can help us find that unique number. Here's how it works:

1. **Initial Value**: `result = 0` (the neutral element for XOR).
2. **For Each Number in the List**:
   - Perform `result ^= num`.
3. **Result**:
   - Repeated numbers cancel each other out (`a ^ a = 0`).
   - Only the unique number remains (`0 ^ a = a`).

---

### Step-by-Step Example
List: `[4, 1, 2, 1, 2]`

1. **Start**: `result = 0`
2. **Step 1**: `0 ^ 4 = 4`
   - `result = 4`
3. **Step 2**: `4 ^ 1 = 5`
   - `result = 5`
4. **Step 3**: `5 ^ 2 = 7`
   - `result = 7`
5. **Step 4**: `7 ^ 1 = 6`
   - `result = 6`
6. **Step 5**: `6 ^ 2 = 4`
   - `result = 4`

Result: `4` (the unique element).

---

### Why Use XOR?
1. **Time Efficiency**: It runs in O(n) time complexity.
2. **Space Efficiency**: It uses O(1) space since it only requires a single variable (`result`).
3. **Simple and Effective**: The code is short and easy to understand.

---

### Limitations of XOR
- This method only works when there is **exactly one** unique element.
- If there are multiple unique elements, this method will not produce the correct result.

---


(DeepSeek)
"""
        