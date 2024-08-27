from personas import Personas

#Velocistas: Tienen que tener club al que pertenecenm, mejor marca en 100 metros y en 200mt
# pueden correr carreras y si el tiempo supera la mejor marca pasa a ser la mejor
class Velocistas(Personas):
    def __init__(self,nombre,apellido,edad,estado_civil,club,mejor_marca_100_m,mejor_marca_200_m):
      super().__init__(nombre,apellido,edad,estado_civil)
      self.club = club
      self.mejor_marca_100_m = mejor_marca_100_m
      self.mejor_marca_200_m = mejor_marca_200_m
    
    def correr_carrera(self,distancia,tiempo):
      if distancia == 100:
        if tiempo < self.mejor_marca_100_m:
          self.mejor_marca_100_m = tiempo
          print(f'Nueva mejor marca en 100 metros {self.mejor_marca_100_m}')
        else:
          print(f'Tiempo en 100 metros: {tiempo} \nNo se superó la mejor marca.')
      elif distancia == 200:
        if tiempo < self.mejor_marca_200_m:
          self.mejor_marca_200_m = tiempo
          print(f'Nueva mejor marca en 200 metros {self.mejor_marca_200_m}')
        else:
          print(f'Tiempo en 200 metros: {tiempo} \nNo se superó la mejor marca.')
      else:
        print('Distancia no valida, solo se permiten carreras de 100 o 200 metros.')
    
    def __str__(self):
      return (f'Nombre: {self.nombre} {self.apellido}\n'
             f'Edad: {self.edad}\n'
             f'Estado civil: {self.estado_civil}\n'
             f'Club: {self.club}\n'
             f'Mejor marca en 100 metros: {self.mejor_marca_100_m}\n'
             f'Mejor marca en 200 metros: {self.mejor_marca_200_m}\n'
             ) 