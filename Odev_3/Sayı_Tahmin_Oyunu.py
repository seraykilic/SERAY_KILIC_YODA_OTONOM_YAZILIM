import random

print("Sayı Tahmin Oyununa Hoş Geldiniz!")
print("1 ile 100 arasında bir sayı tutacağım ve sizden bu sayıyı tahmin etmenizi isteyeceğim. 10 tahmin hakkınız var. Başarılar!")

# 1-100 arası random bir sayı tutar
sayi = random.randint(1,100)
tahmin_hakki = 10 

for deneme in range(1, tahmin_hakki + 1):
    # Oyuncudan tahmin alır
    tahmin = int(input(f"{deneme}. tahmininizi girin:"))

    # Tahmini kontrol eder
    if tahmin == sayi:
        print(f"Tebrikler! {deneme}. denemedeki tahmininiz doğru!")
        break
    elif tahmin < sayi:
        print("Daha yüksek bir sayı deneyiniz.")
    else: print("Daha düşük bir sayı deneyiniz.")

    # Tahmin hakkı biterse oyunu sonlandırır
    if deneme == tahmin_hakki:
        print(f"Maalesef tahmin hakkınız bitti. Tuttuğum sayı {sayi} idi.")

