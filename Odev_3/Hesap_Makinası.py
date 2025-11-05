# Giriş ekranı yazdırılır
print("Basit Hesap Makinasına Hoş Geldiniz!")
print("Dört işlem yapma imkanınız var: Toplama (+), Çıkarma (-), Çarpma (*), Bölme (/)")
print("Çıkmak isterseniz 'q' tuşuna basmanız yeterlidir.")

while True:

    # Kullanıcıdan işlem türü alınır
    işlem = input("Yapmak istediğiniz işlemi seçiniz (+, -, *, /) veya çıkmak için 'q': ")

    if işlem == 'q':
        print("Hesap makinasından çıkıyorsunuz. Kendinize iyi bakın!")
        break

    if işlem not in ['+', '-', '*', '/']:
        print("Geçersiz işlem! Lütfen tekrar deneyiniz.")
        continue

    # Kullanıcıdan iki sayı alınır
    try:
        sayi1 = float(input("Birinci sayıyı giriniz: "))
        sayi2 = float(input("İkinci sayıyı giriniz: "))
    
    except ValueError:
        print("Geçersiz sayı girdiniz! Lütfen tekrar deneyiniz.")
        continue

    # İşleme göre sonucu hesaplar ve ekrana yazdırır
    if işlem == '+':
        sonuç = sayi1 + sayi2
        print(f"{sayi1} + {sayi2} = {sonuç}")
    elif işlem == '-':
        sonuç = sayi1 - sayi2
        print(f"{sayi1} - {sayi2} = {sonuç}")
    elif işlem == '*':
        sonuç = sayi1 * sayi2
        print(f"{sayi1} * {sayi2} = {sonuç}")
    elif işlem == '/':
        if sayi2 == 0:
            print("Hatalı işlem: Bir sayı sıfıra bölünemez!")
        else:
            sonuç = sayi1 / sayi2
            print(f"{sayi1} / {sayi2} = {sonuç}")


