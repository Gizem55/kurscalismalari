# bir öğrencinin 2 yazılı 1 sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisini yazdıran uygulama.
# 0-24 ise 0
# 25-44 ise 1
# 45-54 ise 2
# 55-69 ise 3
# 70-84 ise 4
# 85-100 ise 5
yazili1=float(input('1.yaziliniz: '))
yazili2=float(input('2.yaziliniz: '))
sozlu=float(input('sözlünüz: '))
ortalama=(yazili1+yazili2+sozlu)/3 
if (ortalama>=0) and (ortalama<25):
    print(f'ortalamaniz: {ortalama} notunuz:0')
elif (ortalama>=25) and (ortalama<45):
    print(f'ortalamaniz: {ortalama} notunuz:1')
elif (ortalama>=45) and (ortalama<55):
    print(f'ortalamaniz: {ortalama} notunuz:2')
elif (ortalama>=55) and (ortalama<70):
    print(f'ortalamaniz: {ortalama} notunuz:3')
elif (ortalama>=70) and (ortalama<85):
    print(f'ortalamaniz: {ortalama} notunuz:4')
elif (ortalama>=85) and (ortalama<=100):
    print(f'ortalamaniz: {ortalama} notunuz:5')
else :
    print('bilgileriniz yanliş')