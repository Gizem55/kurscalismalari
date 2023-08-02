# class yapıları uygulama
class person:
    adress= 'no information'
#constructor(yapıcı metod)
    def _init_(self,name,year):
        self.name = name
        self.year= year
        print('init metodu çalisti')
#object
p1= person(name='gizem',year=2003)
p2=person(name='golive',year=1990)
print(f'p1:name: {p1.name} year :{p1.year} address: {p1.adress}')
print(f'p2:name: {p2.name} year :{p2.year} address: {p2.adress}')
print(p1)
print(p2)
print(type(p1))
print(type(p2))