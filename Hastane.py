#Halime Unal 20010011092
def menu():
    print('Hasta Kayit uygulamasi')
    while True:
        print("Hasta eklemek icin: 1\n"
              "Hasta silmek icin: 2\n"
              "Hasta guncellemek icin: 3\n"
              "Hasta listelemek icin: 4\n"
              "Hasta aramak icin: 5\n"
              "Ucret hesaplamak icin: 6\n"
              "Cikis yapmak icin: 7\n")
        secim = input("Seciminiz : ")
        if secim == "1":
            hasta_ekle()
        elif secim == "2":
            hasta_sil()
        elif secim == "3":
            hasta_guncelle()
        elif secim == "4":
            hasta_listele()
        elif secim == "5":
            hasta_ara()
        elif secim == "6":
            ucret_hesapla()
        elif secim == "7":
            break
        else:
            print("Hatali secim yaptiniz")
def dosya_oku():
    hasta = {}
    try:
        with open("20010011092.txt", "r", encoding="utf-8") as dosya:
            for satir in dosya.readlines():
                kelime = satir.split(" ")
                key = int(kelime[0])
                temp_values = {}
                temp_values["AdSoyad"] = kelime[1]
                temp_values["Hasta ID"] = kelime[2]
                temp_values["Yas"] = kelime[3]
                hasta[key] = temp_values
    except Exception as e:
        pass
    return hasta
def dosya_yaz(hastaler):
    with open("20010011092.txt", "w", encoding="utf-8") as dosya:
        for key in hastaler.keys():
            dosya.write(str(key) + " ")
            for value in hastaler[key].values():
                dosya.write(str(value) + " ")
            dosya.write("\n")
def ekrana_yaz(baslik=None, hastaler=None):
    print("Hasta No\t Ad Soyad\t Hasta ID\t Yas\t")
    for key in hastaler:
        print(f"{key}\t\t{hastaler[key]['AdSoyad']}\t {hastaler[key]['Hasta ID']}\t{hastaler[key]['Yas']}\n")
def hasta_ekle():
    hasta_num = 100
    hasta = dosya_oku()
    if len(hasta) != 0:
        ogrenci_num = max(hasta.keys())
        pass
    hasta_say = int(input("Hasta sayisini giriniz: "))
    for i in range(1, hasta_say + 1):
        bilgi = dict()
        adsoyad = input("{}. hasta Ad Soyad: ".format(i))
        bilgi["AdSoyad"] = adsoyad
        hastaid = input("{}. hasta id: ".format(i))
        bilgi["Hasta ID"] = hastaid
        yas = int(input("{}. hasta yasi: ".format(i)))
        bilgi["Yas"] = yas
        hasta[hasta_num + i] = bilgi
    dosya_yaz(hasta)
print()
def hasta_sil():
    hasta_num = 100
    kontrol = 0
    hasta = dosya_oku()
    numara = int(input("Silmek istediginiz hastanin  numarasini giriniz: "))
    if len(hasta) != 0:
        for key in hasta.keys():
            if key == numara:
                kontrol = 1
                hasta.pop(numara)
                break
    if kontrol:
        dosya_yaz(hasta)
        print("Silme islemi gerceklesmistir.")
    else:
        print("Aradiginiz hasta bulunmamaktadir.")
def hasta_guncelle():
    kontrol = 0
    hastalar = dosya_oku()
    numara = int(input("Guncellemek istediginiz hastanin numarasini giriniz: "))
    for key in hastalar:
        if key == numara:
            kontrol = 1
            adsoyad = input(f"{numara} numarali ogrencinin yeni adi soyadi: ")
            hastaid = input(f"{numara} numarali ogrencinin yeni id numarasi: ")
            yas = input(f"{numara} numarali ogrencinin yeni yasi: ")
            hastalar[key]['AdSoyad'] = adsoyad
            hastalar[key]['Hasta ID'] = hastaid
            hastalar[key]['Yas'] = yas
    if kontrol:
        dosya_yaz(hastalar)
        print("Güncelleme islemi tamamlandi.")
    else:
        print("Aradığını kayıt bulunamadi.")
def hasta_listele():
    hastalar = dosya_oku()
    ekrana_yaz("Hasta Listesi", hastalar)
def hasta_ara():
    hastalar = dosya_oku()
    aranan_num = int(input("Aranacak hastanın numarasini giriniz: "))
    if aranan_num in hastalar:
        hasta = hastalar[aranan_num]
        if hasta:
            print("Aranan Numara: %d \n" % (aranan_num))
            ekrana_yaz("Arama Sonucu ", {aranan_num: hasta})
    else:
        print("Aranan kayit bulunamadi.\n")
def ucret_hesapla():
    ucret = int(input("Ucreti giriniz: "))
    sec = input("Sigorta Turunu seciniz: Yok(1), SGK (2), Yesil Kart (3), GSS (4), Ozel (5), Cikis(6) \n")
    ksayisi = int(input("Kardes sayisini giriniz:"))

    while True:
        if sec == "1":
            ucret = ucret * 2
            ucret-=ksayisi*10
            print(f"Ucret: {ucret}")
        elif sec == "2":
            ucret = (ucret * 80) / 100
            ucret -= ksayisi * 10
            print(f"Ucret: {ucret}")
        elif sec == "3":
            ucret = 0
            print(f"Ucret: {ucret}")
        elif sec == "4":
            ucret = (ucret * 90) / 100
            ucret -= ksayisi * 10
            print(f"Ucret: {ucret}")
        elif sec == "5":
            ucret = 0
            print(f"Ucret: {ucret}")
        elif sec == "6":
            exit()
        else:
            print("Gecersiz giris yapildi.")
menu()