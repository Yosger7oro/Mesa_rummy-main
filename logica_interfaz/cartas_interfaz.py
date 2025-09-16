from logica_interfaz.archivo_de_importaciones import importar_desde_carpeta
import pygame

Cartas = importar_desde_carpeta(
    nombre_archivo= "cartas.py",
    nombre_clase= "Cartas")


class Cartas_interfaz(Cartas):
    def __init__(self, *args, ruta_imagen=None,**kwargs):
        # Pasar todos los argumentos posicionales y nombrados al padre
        super().__init__(*args, **kwargs)

        self.ruta_imagen = ruta_imagen
        self.parte_superior = pygame.image.load(self.ruta_imagen) if ruta_imagen is not None else None
        self.parte_trasera = None
    def imagen_asociada(self,reverso=False):
        if reverso:
            return self.parte_trasera
        return self.parte_superior



# #Ejemplo de uso:
# img_corazon_2 = importar_desde_carpeta(
#     nombre_archivo="Imagenes/Cartas/Corazon (2).png",
#     nombre_carpeta="assets")

# carta1 = Cartas_interfaz(ruta_imagen=img_corazon_2,numero=2,figura="picas")
# print(carta1)
# print(carta1.imagen_asociada())