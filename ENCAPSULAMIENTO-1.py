class pelicula:
    def __init__(self,tit,cre,año):
        self._titulo=tit
        self._creador=cre
        self._año=año

    def set_titulo(self,new_titulo):
        self._titulo=new_titulo

peli1=pelicula("Star Wars EP I","George Lucas",1999)
peli2=pelicula("Star Wars EP III","George Lucas",2005)
peli3=pelicula("The Avengers","Marvel",2012)

print(peli1._titulo," / ",peli1._creador," / ",peli1._año)
print(peli2._titulo," / ",peli2._creador," / ",peli2._año)
print(peli3._titulo," / ",peli3._creador," / ",peli3._año)


peli1.set_titulo("The Avengers")
print(peli1._titulo)