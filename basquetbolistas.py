from personas import Personas;

# 1- Basquetbolistas. aparte tienen numero de jugador, equipo y numero de camiseta
# los basquetbolistas pueden ser transferidos a otros equipos y pueden cambiar de numero de camiseta
# en el main van a crear varios juagadores, van a ir haciendo operaciones. van a listar los jugadores que juegan en Ferro
class Basquetbolista(Personas):
    def __init__(self,nombre,apellido,edad,estado_civil,num_jugador,equipo,num_camiseta):
      super().__init__(nombre,apellido,edad,estado_civil)
      self.num_jugador = num_jugador
      self.equipo = equipo
      self.num_camiseta = num_camiseta
      
    def transferir_jugador(self,nuevo_equipo):
       # Verifica si nuevo_equipo es una cadena de texto (str)
      if not isinstance(nuevo_equipo, str) :
        print('\nDebe ingresar un nombre de equipo válido')
        return None
      
      self.equipo = nuevo_equipo
      print('-' * 40)
      print(f'\nTransfiriendo jugador...')
      return f'El jugador {self.nombre} {self.apellido} \nEdad: {self.edad} \nCamiseta numero: {self.num_camiseta} \nAhora pertenece al club {self.equipo}\n'

    def cambiar_num_camiseta(self,nuevo_num):
        self.num_camiseta = nuevo_num
        print('-' * 40)
        print(f'Cambiando numero de camiseta')
        return f'El juagador {self.nombre} {self.apellido} ahora tiene la camiseta numero: {self.num_camiseta}\n'
    



          

      