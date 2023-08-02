# kullanıcıdan isim , yaş ve eğitim bilgilerini alıp ehliyet alabilme durumunu kontrol etme uygulaması.
# ehliyet alma koşulu yaş en az 18 ve eğitim durumu lise veya üniversite olmalıdır.
isim =input('isminiz : ')
yas=int(input('yasiniz: '))
egitim=input('eğitim: ')
if (yas>=18):
    if (egitim=='lise') or (egitim=='üniversite'):
      print(f'{isim} ehliyetinizi alabilirsiniz')
    else: 
      print(f'{isim} alamazsiniz egitim durumunuz yetersiz')
else:
    print(f'{isim} alamazsiniz yasiniz tutmuyor')