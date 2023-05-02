# SINAV NOTLARI

#m ("lütfen kullanici adini girdikten sonra vize ve final sinav notunu giriniz!"))
kullanici_adi= str(input("isim_soyisim_giriniz: "))
vize_notu: int = int(input("vize_notunuzu_giriniz: "))
finaL_notu: int= int(input("final_notunuzu_giriniz: "))

sonuc = float((vize_notu * 0.4)) + ((finaL_notu * 0.6))
print(f"ortalama : {sonuc}")

if sonuc >=90 :
        print("AA")
elif 79.9 < sonuc < 90:
        print("BA")
elif 74.9 < sonuc < 80:
        print("BB")
elif 69.9 < sonuc < 75:
        print("CB")
elif 59.9 < sonuc < 70:
        print("CC")
elif 49.9 < sonuc < 60:
        print("DC")
elif 39.9 < sonuc < 50:
        print("DD")
elif 39.9 < sonuc < 40:
        print("FD")
else :
        print("FF")


if sonuc =="AA" or sonuc=="BA" or sonuc=="BB" or sonuc=="CB" or sonuc== "CC":
    print("basari_durumunu : Basarili")
else :
    print("basari_durumunu : basarisiz")

if sonuc in ("AA","BB","CC","BA","CB"):
    print("basari_durumunu : Basarili")
else:
    print("basari_durumunu : basarisiz")
