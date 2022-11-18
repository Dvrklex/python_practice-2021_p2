from fuimba import *
from dataclasses import dataclass
class Video():
    def __init__(self, name, views, actors):
        self.name = name
        self.views = views
        self.actors = actors

class Serie(Video):
    def __init__(self, name, views, actors, seasons):
        Video.__init__(self, name, views, actors)
        self.seasons = seasons

class Pelicula(Video):
    def __init__(self, name, views, actors, duration):
        Video.__init__(self, name, views, actors)
        self.duration = duration

class Neflis():
    def __init__(self):
        self.lPelis = []
        self.lSeries = []
        series = [["Peaky Blinders", 1234567, 'Cillian Murphy,Paul Anderson,Helen McCrory', 5],
                    ["The Umbrella Academy", 2434908, 'Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda', 2]]

        pelis = [["Inception", 4760183, 'Leonardo DiCaprio,Ellen Page,Joseph Gordon-Levitt', 148],
                    ["Batman Begins", 17319533, 'Christian Bale,Cillian Murphy,Michael Caine', 140],       
                    ["Inmortales", 35, 'Mirtha Legrand,Leonardo DiCaprio,Elizabeth The Second', 30]]

        for s in series:
            nombre, view, actores, temporadas = s
            serie = Serie(nombre, view, actores.split(","), temporadas)
            self.lSeries.append(serie)

        for p in pelis:
            name, view, actors, duration = p
            pelicula = Pelicula(name, view, actors.split(","), duration)
            self.lPelis.append(pelicula)

    def masVisu(self):
        lTotal = self.lPelis + self.lSeries
        maxCantViews = max([objeto.views for objeto in lTotal])
        for objeto in lTotal:
            if objeto.views == maxCantViews:
                return objeto.name

    def promedioDuracionPelis(self):
        total = 0
        for peli in self.lPelis:
            total += peli.duration
        return int(total / len(self.lPelis))

    def actoresDeAmbas(self):
        def obtenerListaActores(listaVideos):
            listaDeListasDeActores = [video.actors for video in listaVideos]
            listaPlanaDeActores = [actor for lActores in listaDeListasDeActores for actor in lActores]
            return listaPlanaDeActores

        return [actor for actor in obtenerListaActores(self.lSeries) if actor in obtenerListaActores(self.lPelis)]

    def seriesMasDe3Temporadas(self):
        return [serie.name for serie in self.lSeries  if serie.seasons > 3]
        
plataforma = Neflis()
subrayar()
print(f"El video mas visto: {plataforma.masVisu()}")

print(f"Promedio de duración de las películas: {plataforma.promedioDuracionPelis()} minutos")

print("Actores que trabajan en series y películas:", end=" ")
for actor in plataforma.actoresDeAmbas():
    print(f"- {actor} ", end=" ")
print()

print("Series que tienen más de 3 temporadas:", end=" ")
for serie in plataforma.seriesMasDe3Temporadas(): 
    print(f"- {serie}", end="")



