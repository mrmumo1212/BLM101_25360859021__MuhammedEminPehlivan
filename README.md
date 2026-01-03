# BLM101_25360859021__MuhammedEminPehlivan
BLM101 – Bilgisayar Mühendisliğine Giriş Dersi 1. Dönem Projesi


Ad = Muhammed Emin

Soyad = Pehlivan

Okul_No = 25360859021

Proje_Konusu=Veri Depolama ve Sıkıştırma Algoritmaları

Youtube_Linki = https://youtu.be/acGJ2ll_Jv0?si=rLqVq7zyop8lKyIp

Açıklama=Projede bizden istenenler temel olarak metin, resim ve ses verilerinin bit düzeyinde temsili; veri sıkıştırmanın gerekliliği, temel sıkıştırma mantıkları üzerine bir 
sunum hazırlayıp daha sonra python üzerinden RLE sıkıştırma yöntemine göre stringleri sıkıştıran veya sıkıştırılmış stringleri tekrar eski haline çeviren,aynı zamanda da sıkıştırılma oranını gösteren bir algoritma yazmak ve bu algoritmanın kısaca içeriğini gösterip daha sonra çıktısını video ile kaydetmek.

sunum.pdf içerisinde pdf formatında sunum dosyası bulunmaktadır,
src içinde .py içeriğinde algoritma dosyası  bulunuyor ve doğrudan açıp kullanılabilir

algoritmanın mantığı: 


# Metin Sıkıştırma ve Ayıklama Algoritması

Bu doküman, verilen Python kodunda yer alan **metin sıkıştırma** ve **sıkıştırılmış metni geri açma (ayıklama)** algoritmalarını adım adım açıklamak amacıyla hazırlanmıştır.

---

## Genel Amaç

Kod, iki temel işlem yapar:

1. **Sıkıştırma (Run-Length Encoding benzeri)**
   Ardışık tekrar eden karakterleri, tekrar sayısı + karakter biçiminde ifade eder.

   Örnek:

   ```
   aaabbbcc  →  3a3b2c
   ```

2. **Ayıklama (Decompression)**
   Sıkıştırılmış metni tekrar orijinal haline döndürür.

   Örnek:

   ```
   3a3b2c  →  aaabbbcc
   ```

---

##  `Sıkıştır(metin)` Fonksiyonu

### Görevi

Verilen bir metni karakter tekrar sayılarını kullanarak sıkıştırır ve:

* Sıkıştırılmış metni
* Orijinal uzunluğu
* Sıkıştırılmış uzunluğu
* Küçülme oranını

yazdırır.

---

### Çalışma Mantığı

1. **Boş Metin Kontrolü**

   ```python
   if not metin:
       return "Boş metin girildi"
   ```

   Eğer kullanıcı boş metin girerse işlem yapılmaz.

2. **Başlangıç Değişkenleri**

   ```python
   sıkıştırılmış_metin = ""
   sayac = 1
   ```

   * `sıkıştırılmış_metin`: Sonuç tutulur
   * `sayac`: Aynı karakterin kaç kez tekrar ettiğini tutar

3. **Metin Üzerinde Döngü**

   ```python
   for i in range(0, len(metin)):
   ```

4. **Son Karakter Kontrolü**

   ```python
   if i == len(metin) - 1:
   ```

   Döngünün sonuna gelindiyse, kalan sayaç ve karakter eklenir ve sonuçlar yazdırılır.

5. **Tekrar Eden Karakterler**

   ```python
   elif metin[i] == metin[i+1]:
       sayac += 1
   ```

   Aynı karakter devam ediyorsa sayaç artırılır.

6. **Karakter Değişimi**

   ```python
   else:
       sıkıştırılmış_metin += str(sayac) + metin[i]
       sayac = 1
   ```

   Karakter değiştiğinde önceki karakter ve sayısı eklenir.

---

### Üretilen Çıktılar

* Sıkıştırılmış metin
* Orijinal metin uzunluğu
* Sıkıştırılmış metin uzunluğu
* Yüzdelik küçülme oranı

---

##  `Ayıkla(açılacak_metin)` Fonksiyonu

### Görevi

Sıkıştırılmış metni alır ve tekrar orijinal metni oluşturur.

---

### Çalışma Mantığı

1. **Boş Metin Kontrolü**

   ```python
   if not açılacak_metin:
       return "Boş metin girildi"
   ```

2. **Başlangıç Değişkenleri**

   ```python
   ayıklanmış_metin = ""
   katsayı = ""
   ```

   * `katsayı`: Karakterden önce gelen sayı(lar)

3. **Metin Üzerinde Döngü**

   ```python
   for i in range(0, len(açılacak_metin)):
   ```

4. **Sayı Kontrolü**

   ```python
   if açılacak_metin[i].isdigit():
       katsayı += açılacak_metin[i]
   ```

   Birden fazla basamaklı sayılar için string olarak biriktirilir.

5. **Karakter Geldiğinde**

   ```python
   else:
       ayıklanmış_metin += açılacak_metin[i] * int(katsayı)
       katsayı = ""
   ```

   Karakter, kendinden önceki sayı kadar tekrar edilerek eklenir.

---

### Çıktı

Fonksiyon sonunda ayıklanmış (orijinal) metin ekrana yazdırılır.

---

##  Ana Program Döngüsü

```python
while True:
```

Program sürekli çalışır ve kullanıcıdan seçim alır:

### Menü

* **1** → Metni sıkıştır
* **2** → Sıkıştırılmış metni ayıkla

### Hatalı Seçim

Geçersiz giriş yapılırsa kullanıcı uyarılır ve döngü devam eder.

---

## Genel Değerlendirme

* Algoritma, **Run-Length Encoding (RLE)** mantığına dayanır
* Ardışık tekrarlar fazla olduğunda verimlidir
* Eğitim ve temel algoritma mantığını göstermek için uygundur
* Gerçek dünyada büyük veriler için optimize edilmesi gerekir

---

 Bu dosya, kodun **mantığını açıklamak** amacıyla hazırlanmıştır; kodun birebir kopyası değildir.
