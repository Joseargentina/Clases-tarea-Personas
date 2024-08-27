from personas import Personas

# acordate que los rivales son una lista de otros tenistas
class Tenistas(Personas):
    def __init__(self,nombre,apellido,edad,estado_civil,ranking_atp,marca_raqueta,record_partido_ganados,record_partido_perdidos,rival=None):
      super().__init__(nombre,apellido,edad,estado_civil)
      self.ranking_atp = ranking_atp
      self.marca_raqueta = marca_raqueta
      self.estado_civil = estado_civil
      self.record_partido_ganados = record_partido_ganados
      self.record_partido_perdidos = record_partido_perdidos
      self.rival = rival if rival is not None else []
      
    def agregar_rival(self,rival):
      self.rival.append(rival)
    
    def mostrar_rivales(self):
      print(f'El rival de {self.nombre} {self.apellido} es:')
      for rival in self.rival:
        print(f'- {rival.nombre} {rival.apellido} \nRanking: {rival.ranking_atp}')
    
    def __str__(self):
        return (f'Nombre: {self.nombre} {self.apellido}\n'
                f'Edad: {self.edad}\n'
                f'Estado Civil: {self.estado_civil}\n'
                f'Ranking ATP: {self.ranking_atp}\n'
                f'Marca de Raqueta: {self.marca_raqueta}\n'
                f'Récord de Partidos Ganados: {self.record_partido_ganados}\n'
                f'Récord de Partidos Perdidos: {self.record_partido_perdidos}')