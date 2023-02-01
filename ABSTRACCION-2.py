class Cprogramacion:
    def __init__(self,cur,niv,est):
        self.nombre=cur
        self.nivel=niv
        self.estudiantes=est

curso1=Cprogramacion("Java","Avanzado", 15)
curso2=Cprogramacion("Python","Medio", 12)
curso3=Cprogramacion("C++","Básico", 20)

print(curso1.nombre," / ",curso1.nivel," / ",curso1.estudiantes)
print(curso2.nombre," / ",curso2.nivel," / ",curso2.estudiantes)
print(curso3.nombre," / ",curso3.nivel," / ",curso3.estudiantes)