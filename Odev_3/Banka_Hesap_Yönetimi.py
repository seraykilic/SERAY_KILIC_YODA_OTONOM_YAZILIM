
# Banka hesap fonksiyonları ve sınıf tanımı

class Hesap:
    def __init__(self, hesap_sahibi, hesap_no, bakiye=0):
        self.hesap_sahibi = hesap_sahibi
        self.hesap_no = hesap_no
        self.bakiye = bakiye

    def para_yatir(self, miktar):
        if miktar > 0:
            self.bakiye += miktar
            print(f"{miktar} TL hesabınıza yatırıldı. Yeni bakiye: {self.bakiye} TL ")
        else: 
            print("Geçersiz miktar! Lütfen geçerli bir miktar giriniz.")

    def para_cek(self, miktar):
        if miktar <= 0:
            print("Geçersiz miktar! Lütfen geçerli bir miktar giriniz.")
        elif miktar > self.bakiye:
                print("Yetersiz bakiye! Lütfen geçerli bir miktar giriniz.")
        else: self.bakiye <= miktar
        self.bakiye -= miktar
        print(f"{miktar} TL hesabınızdan çekildi. Kalan bakiye: {self.bakiye} TL ") 
    
# Kulanıcıdan bilgi alma ve hesap oluşturma

print("Banka Hesap Yönetim Sistemine Hoşgeldiniz!" )

hesap_sahibi = input("Hesap sahibinin adını giriniz: " )
hesap_no = input("Hesap numarasını giriniz: " ) 
hesap = Hesap(hesap_sahibi, hesap_no)

# İşlem menüsü

while True:
     print("Lütfen yapmak istediğiniz işlemi seçiniz: ")
     print("1 - Para Yatırma")
     print("2 - Para Çekme")    
     print("3 - Bakiye Sorgulama")  
     print("4 - Çıkış") 

     secim = input("Seçiminiz (1-4):")
     if secim == "1":
            miktar = float(input("Yatırmak istediğiniz miktarı giriniz: "))
            hesap.para_yatir(miktar)    
     elif secim == "2":
            miktar = float(input("Çekmek istediğiniz miktarı giriniz: "))
            hesap.para_cek(miktar)
     elif secim == "3":
            print(f"Hesap bakiyeniz: {hesap.bakiye} TL")
     elif secim == "4":
            print("Hesap yönetim sisteminden çıkış yapılıyor. Kendinize iyi bakın!")
            break
            


        
