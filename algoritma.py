def Sıkıştır(metin): #fonksiyon tek parametre olan metni alıyor
    if not metin: #metin boşsa uyarı veriyor eğer boş değilse sıkıştırma işlemi yapılıyor
        return "Boş metin girildi\n"
    else:
        sıkıştırılmış_metin=""  #sıkıştırılmış metnin tutulacağı değişken
        sayac=1 #karakter tekrar sayısını tutan değişken

        for i in range(0,len(metin)): #0. indexten metnin son karakterine kadar döngü
            if(i==len(metin)-1): #eğer ki son karaktere gelindiyse son karakteri de ekleyip kullanıcıya sonucu gösteriyoruz
                    sıkıştırılmış_metin+=str(sayac)+metin[-1]
                    print(f"Sıkıştırılmış metin: {sıkıştırılmış_metin}")
                    print(f"Orijinal uzunluk: {len(metin)}")
                    print(f"Sıkıştırılmış uzunluk: {len(sıkıştırılmış_metin)}")
                    print(f"Küçülme oranı: %{100-(len(sıkıştırılmış_metin)/len(metin))*100:.2f}\n")
                    return
            elif(metin[i]==metin[i+1]): #eğer ki şu anki karakter bir sonraki karaktere eşitse sayaç bir arttırılır
                sayac+=1
            else: #eğen şuanki karakter son karakter değil ve sonraki karaktere eşit değilse sıkıştırılmış metne ekleme yapılır
                sıkıştırılmış_metin+=str(sayac)+metin[i]  
                sayac=1 # ve sayaç değeri tekrardan bir olur
        

def Ayıkla(açılacak_metin):   #fonksiyon tek parametre olan açılacak metni alıyor
    if not açılacak_metin:
        return "Boş metin girildi\n"  #metin boşsa uyarı veriyor eğer boş değilse ayıklama işlemi yapılıyor
    else:
        ayıklanmış_metin=""   #ayıklanmış metnin tutulacağı değişken
        katsayı="" #karakter tekrar sayısını tutan değişken

        for i in range(0,len(açılacak_metin)): #0. indexten metnin son karakterine kadar döngü
            if(açılacak_metin[i].isdigit()): #eğer ki şu anki karakter bir sayı ise 
                katsayı+=açılacak_metin[i]   #katsayı değişkenine eklenir değilse
            else:
                ayıklanmış_metin+=açılacak_metin[i]*int(katsayı) #kendinden önceki katsayı ile karakter stringi çarpılır
                katsayı="" # ayıklanmış metne eklenir ve katsayı değişkeni tekrardan boş olur

        return print(f"Ayıklanmış metin: {ayıklanmış_metin}\n")  #son olarak ayıklanmış metin kullanıcıya gösterilir

while True:  #ana program döngüsü
    print("1.     Metni sıkıştır")
    print("2.     Sıkıştırılmış metni ayıkla")
    choice=int(input("Seçiminiz(1 or 2): "))    #kullanıcıdan sıkıştırma yada ayıklama seçimi alıyoruz
    if(choice==1):
        metin=input("Sıkştırılacak metni girin(örn: aaabbbcc): ")
        print("\n")
        Sıkıştır(metin)
    
    elif(choice==2):
        açılacak_metin=input("Ayıklayacağınız metni girin(örn: 3a2b1c): ") 
        print("\n")
        Ayıkla(açılacak_metin)

    else:
        print("Hatalı seçim, Lütfen tekrar deneyin!\n")  #hatalı seçim durumunda uyarı gönderilir

