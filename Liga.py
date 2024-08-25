import random

#Creamos la clase para los equipos y que se inician en 0Puntos, 0 goles a favor, 0 en contra.
class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0
        self.goles_a_favor = 0
        self.goles_en_contra = 0

#Creamos un metodo que actualizara los goles a favor y goles en contra para sumar los puntos
    def puntos_update(self, goles_favor, goles_contra):
        if goles_favor > goles_contra:
            self.puntos +=3
        elif goles_favor == goles_contra:
            self.puntos += 1

        self.goles_a_favor += goles_favor
        self.goles_en_contra += goles_contra


#Simulamos el partido donde se tomaran los equipos a participar y el resultado de cada partido
class Partido:
    def __init__(self, equipo1, equipo2):
        self.equipo1 = equipo1
        self.equipo2 = equipo2

#tomamos de manera aleatoria los goles realizados por el equipo de esta forma actualizar los puntos y mostrar el resultado
    def jugar(self):
        goles_equipo1 = random.randint(0,7)
        goles_equipo2 = random.randint(0,7)
        self.equipo1.puntos_update(goles_equipo1, goles_equipo2)
        self.equipo2.puntos_update(goles_equipo2, goles_equipo1)
        print(f"{self.equipo1.nombre} {goles_equipo1}-{self.equipo2.nombre} {goles_equipo2}") 

#Clase Liga donde haremos que se enfrenten los equipos
class Liga:
    def __init__(self, equipos):
        self.equipos = equipos

#recorreremos cada equipo y los haremos enfrentarse 1 vs 1
    def todos_contra_todos(self):
        #iterando en la lista equipos
        for i in range(len(self.equipos)):
            #iterando en i que representaria el equipo elegido contra j el equipo en contra
            for j in range(i + 1, len(self.equipos)):   
                partido = Partido(self.equipos[i], equipos[j])
                partido.jugar()

#tabla de posiciones que se ordenara de mayor a menor
    def tabla_posiciones(self):
        self.equipos.sort(key=lambda x: x.puntos, reverse = True)
        print("Tablas de posiciones")
        for equipo in self.equipos:
            print(f"{equipo.nombre}: {equipo.puntos} puntos / GF = {equipo.goles_a_favor} / GC = {equipo.goles_en_contra}")

#indicamos el nombre de los equipos, en este caso utlice nombres de lenguajes :)
python = Equipo("Python")
java = Equipo("Java")
c = Equipo("C#")
javaScript = Equipo("JavaScript")

#activamos
equipos = [python, java, c, javaScript]
liga = Liga(equipos)
liga.todos_contra_todos()
liga.tabla_posiciones()
