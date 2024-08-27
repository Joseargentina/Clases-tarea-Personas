class Personas:
    def __init__(self,nombre,apellido,edad,estado_civil):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.estado_civil = estado_civil
        self.velocidad = 0
        self.velocidad_maxima = 5
    
    def caminar(self):
        # Incrementa la velocidad en 0.1 al caminar
        nueva_velocidad = self.velocidad + 0.1
        return f'{self.nombre} esta caminando a una velocidad de {nueva_velocidad} km/h'
    
    def hablar(self, texto):
        if texto.isnumeric():
            return "El texto es un número."
        return texto
    
    def cambiar_estado_civil(self, nuevo_estado):
        try:
            estados = {'casarse': 'casado', 'divorciarse': 'divorciado', 'enviudar': 'viudo','soltero':'soltero'}
            nuevo_estado = nuevo_estado.lower()
            if nuevo_estado not in estados:
                return f"No existe el estado civil '{nuevo_estado}'."
            elif estados[nuevo_estado] == self.estado_civil:
                return f'{self.nombre} ya se encuentra {self.estado}.'
            else:
                self.estado = estados[nuevo_estado]
                return f"Estado civil de {self.nombre} a cambiado a '{self.estado_civil}'."
        except Exception as e:
            print(f"Error: {e}")