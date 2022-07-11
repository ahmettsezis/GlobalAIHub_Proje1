import pandas as pd

ogr_ad = str
ogr_soyad = str
ogr_no = int
ogr_vize = int
ogr_final = int
ortalama = float

ogr_ad = input("Öğrenci adını giriniz: ")
ogr_soyad = input("Öğrenci soyadını giriniz: ")
ogr_no = input("Öğrenci numarasını giriniz: ")
ogr_vize = input("Vize notunu giriniz: ")
ogr_final = input("Final notunu giriniz: ")

ortalama = float(ogr_vize) + float(ogr_final)

ogr_durum = "GEÇTİ"

if ortalama < 50 :
    print("KALDI: F")
    ogr_durum = "KALDI" 
elif ortalama <= 60 :
    print("GEÇTİ: E")
elif ortalama <= 70 :
    print("GEÇTİ: D")
elif ortalama <= 80 :
    print("GEÇTİ: C")
elif ortalama <= 90 :
    print("GEÇTİ: B")
elif ortalama <= 100 :
    print("GEÇTİ: A")
print(ortalama)

listem = []
listem.append((ogr_ad,ogr_soyad,ogr_no,ogr_vize,ogr_final,ogr_durum))

df = pd.DataFrame(listem,columns=['Adi','Soyadi','Numarasi','Vize','Final','Durum'])
print(df)

# create excel writer object
writer = pd.ExcelWriter('output.xlsx')

df.to_excel(writer)
# save the excel
writer.save()

