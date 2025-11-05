# Kullanıcıdan metin girişi alır
metin = input("Bir metin(cümle veya paragraf) giriniz:")

# Metindeki tüm kelimeleri küçük harfe çevirir ve "Kelime" ve "kelime" gibi farklı yazılışları aynı sözcük olarak sayar. 
metin = metin.lower()

# Metni sözcüklere ayırır
sözcükler = metin.split()

# Toplam kelime sayısını hesaplar
toplam_sözcük_sayısı = len(sözcükler)

# Boşluklar dahil olmak üzere toplam karakter sayısını hesaplar
toplam_karakter_sayısı = len(metin)

# En uzun kelimenin uzunluğunu bulur
en_uzun_sözcük = max(len(sözcük) for sözcük in sözcükler)

# Her kelimenin metindeki kaç kez geçtiğini sayar
sözcük_sayacı = {}
for sözcük in sözcükler:
    if sözcük in sözcük_sayacı:
        sözcük_sayacı[sözcük] += 1
    else: 
        sözcük_sayacı[sözcük] = 1

# Sonuçları ekrana yazdırır
print("Kelime Sayacı Sonuçları:")
print(f"Toplam sözcük sayısı: {toplam_sözcük_sayısı}")
print(f"Toplam karakter sayısı (boşluklar dahil): {toplam_karakter_sayısı}")  
print(f"En uzun sözcüğün uzunluğu: {en_uzun_sözcük} karakter")  
print("Her sözcüğün tekrar sayısı:") 

for sözcük, sayı in sözcük_sayacı.items():
    print(f"{sözcük} - {sayı} kez")


