#Crear clase Personas con: Nombre ,Apellido, Edad, Estado civil, velocidad = 0,Velocidad Maxima
#- Caminar: Mostrar un mensaje que estan caminando. Velocidad + 0.1km
#- Hablar: metodo donde le pasan un parametro y retorna el texto o lo imprime
#- Casarse, divorciarse, o enviudar (cambia el estado civil)

# Tres clases que heredan
# 1- Basquetbolistas. aparte tienen numero de jugador, equipo y numero de camiseta
# los basquetbolistas pueden ser transferidos a otros equipos y pueden cambiar de numero de camiseta
# en el main van a crear varios juagadores, van a ir haciendo operaciones. van a listar los jugadores que juegan en Ferro

# 2- Tenistas: Tienen aparte ranking ATP, marca de raqueta, record de partidos ganados y perdidos, y un rival.
# Los rivales son una lista de otros tenistas.

# 3- Velocistas: Tienen que tener club al que pertenecen, mejor marca en 100 metros y en 200mt
# pueden correr carreras y si el tiempo supera la mejor marca pasa a ser la mejor

from personas import Personas
from basquetbolistas import Basquetbolista
from tenistas import Tenistas
from velocistas import Velocistas

#Instancia de la clase Personas
jose = Personas('Jose','Garcia',36,'soltero')

# Llamo al método caminar
caminar = jose.caminar()

# Llamo al metodo hablar pasandole un texto como parametro
hablar = jose.hablar('Hola me llamo Jose y estoy estudiando programacion')

# Llamo al metodo cambiar_estado_civil para casarse, divorciarse 7 enviudar
casarse = jose.cambiar_estado_civil('casarse')
divorciarse = jose.cambiar_estado_civil('Divorciarse')
soltero = jose.cambiar_estado_civil('Soltero')
enviudar = jose.cambiar_estado_civil('enviudar')

# Imprimo los resultados en la consola
# print(f'{caminar}\n{hablar}')

#Funcion para listar jugadores
def listar_jugadores(jugadores, equipo):
      print(f'\nLos jugadores del equipo {equipo} son: ')
      for jugador in jugadores:
        if jugador.equipo == equipo:
          print('-' * 40)
          print(f'Nombre: {jugador.nombre} {jugador.apellido} \nEdad: {jugador.edad} \nEquipo: {jugador.equipo} \nNumero de camiseta: {jugador.num_camiseta}')

# Instancias de jugadores de Basquet
jugador1 = Basquetbolista('Jose','Curwen',28,'soltero',115,'Ferro',22)
jugador2 = Basquetbolista('Andres','Berti',24,'casado',137,'Ferro',53)
jugador3 = Basquetbolista('Juan','Esteves',19,'casado',989,'San Lorenzo',44)
jugador4 = Basquetbolista('Fernando','Sanchez',22,'soltero',709,'Aldosivil',39)
jugador5 = Basquetbolista('Critian','Lopez',29,'soltero',777,'Ferro',29)
jugador6 = Basquetbolista('Fabian','Ulloa',23,'soltero',444,'Velez',33)
jugador7 = Basquetbolista('Adrian','Fernandez',31,'divorciado',115,'Ferro',55)
jugador8 = Basquetbolista('Manuel','Diaz',26,'soltero',173,'Ferro',18)
jugador9 = Basquetbolista('Gonzalo','Duarte',22,'casado',128,'River',10)
jugador10 = Basquetbolista('Franco','Perez',20,'soltero',225,'Ferro',13)

# Lista de jugadores
lista_jugadores = [jugador1, jugador2, jugador3, jugador4, jugador5, 
                   jugador6, jugador7, jugador8, jugador9, jugador10]

#Listo los jugadores de 'Ferro'
listar_jugadores(lista_jugadores, 'Ferro')

#Transferir jugador
transferir = jugador1.transferir_jugador('San Lorenzo')
print(transferir)

#Cambiar numero de camiseta 
cambiar_numero = jugador2.cambiar_num_camiseta(99)
print(cambiar_numero)

# Verifica la transferencia listando los jugadores nuevamente
listar_jugadores(lista_jugadores, 'San Lorenzo')


# Creación de instancias de Tenistas
tenista1 = Tenistas('Serena', 'Williams', 42, 'Casada', 1, 'Wilson', 850, 150,)
tenista2 = Tenistas('Simona', 'Halep', 32, 'Casada', 7, 'Wilson', 400, 120)
tenista3 = Tenistas('Naomi', 'Osaka', 26, 'Soltera', 4, 'Yonex', 250, 70)
tenista4 = Tenistas('Ashleigh', 'Barty', 28, 'Casada', 2, 'Head', 300, 60)
tenista5 = Tenistas('Iga', 'Swiatek', 23, 'Soltera', 1, 'Tecnifibre', 200, 50)

# Agregando rivales a cada tenista
tenista1.agregar_rival(tenista4)
tenista4.agregar_rival(tenista1)
tenista2.agregar_rival(tenista3)
tenista3.agregar_rival(tenista2)
tenista5.agregar_rival(tenista1)

# Mostrar información de los tenistas
print('-' * 40)
print("Información de los Tenistas:")
print(tenista1)
print('-' * 40)
print(tenista2)
print('-' * 40)
print(tenista3)
print('-' * 40)
print(tenista4)

# Mostrar rivales de Serena Williams
print('-' * 40)
tenista1.mostrar_rivales()

# Mostrar rivales de Naomi Osaka
print('-' * 40)
tenista3.mostrar_rivales()

#Instancias de Velocistas
velocista1 = Velocistas('Ricardo', 'Mendez', 34, 'Soltero', 'Gimnasia', 9.58, 19.19)
velocista2 = Velocistas('Juan', 'Colombo', 31, 'Soltero', 'Racing', 9.69, 19.26)

#Mostrar informacion de velocistas
print('-' * 40)
print("Información de los Velocistas:")
print(velocista1)
print(velocista2)

# Correr una carrera
print('-' * 40)
print('Resultado carrera en 100 mt')
velocista1.correr_carrera(100, 9.26)
print('Resultado carrera en 200 mt')
velocista2.correr_carrera(200, 19.26)

