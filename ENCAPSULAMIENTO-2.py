class Cprogramacion:
    def __init__(self,cur,niv,est):
        self._nombre=cur
        self._nivel=niv
        self._estudiantes=est

    def set__nivel(self,new_nivel):
         self._nivel=new_nivel


curso1=Cprogramacion("Java","Avanzado", 15)
curso2=Cprogramacion("Python","Medio", 12)
curso3=Cprogramacion("C++","Básico", 20)

print(curso1._nombre," / ",curso1._nivel," / ",curso1._estudiantes)
print(curso2._nombre," / ",curso2._nivel," / ",curso2._estudiantes)
print(curso3._nombre," / ",curso3._nivel," / ",curso3._estudiantes)


curso3.set__nivel("Medio")
print(curso3._nombre," / ",curso3._nivel," / ",curso3._estudiantes)
