from logica_interfaz.archivo_de_importaciones import importar_desde_carpeta
import pygame
Mazo = importar_desde_carpeta("mazo.py","Mazo")
Menu = importar_desde_carpeta("menu.py","Menu","recursos_graficos")

CartelAlerta = importar_desde_carpeta(
    nombre_archivo="elementos_de_interfaz_de_usuario.py",
    nombre_clase="CartelAlerta",
    nombre_carpeta="recursos_graficos",
)


imagenes_mazo = []
for x in range(1,6):
    imagen_mazo = importar_desde_carpeta(
    nombre_archivo=f"Imagenes/Mazo/mazo{x}.png",
    nombre_carpeta="assets"
    )
    imagenes_mazo.append(imagen_mazo)


class Mazo_interfaz(Mazo):
    def __init__(self, *args, un_juego=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.un_juego = un_juego
        self.imagen_mazo = pygame.image.load(imagenes_mazo[0])

    def MensajeAlerta(self, mensaje, ancho=500, alto=300):
        """
        Crea un cartel de alerta en el centro de la pantalla
        con el mensaje recibido.
        """
        # Instanciar el cartel
        cartel = CartelAlerta(
            pantalla=self.un_juego.pantalla,
            mensaje=mensaje,
            x=0,  # se recalcula en centrar_en_pantalla
            y=0,
            ancho=ancho,
            alto=alto
        )

        # Centrar y mostrar
        cartel.centrar_en_pantalla()
        return cartel
    def mostrar_visual_nro_cartas(self,mensaje):
        self.MensajeAlerta(f'{mensaje} {len(self.cartas)}')
    def reparticion_visual_cartas(self):
        self.MensajeAlerta("Repartiendo cartas")


