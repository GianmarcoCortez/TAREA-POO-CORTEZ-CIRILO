class pelicula:
    def __init__(self,tit,cre,año):
        self.titulo=tit
        self.creador=cre
        self.año=año

peli1=pelicula("Star Wars EP I","George Lucas",1999)
peli2=pelicula("Star Wars EP III","George Lucas",2005)
peli3=pelicula("The Avengers","Marvel",2012)

print(peli1.titulo," / ",peli1.creador," / ",peli1.año)
print(peli2.titulo," / ",peli2.creador," / ",peli2.año)
print(peli3.titulo," / ",peli3.creador," / ",peli3.año)


class videojuego(pelicula):
    def __init__(self,tit,cre,año):
        super(). __init__(tit,cre,año)


juego1=videojuego("Starcraf II","Bliizzard",2010)


print(juego1.titulo," / ",juego1.creador," / ",juego1.año)





