from logica_interfaz.archivo_de_importaciones import importar_desde_carpeta
import pygame
Mazo = importar_desde_carpeta("mazo.py","Mazo")
Menu = importar_desde_carpeta("menu.py","Menu","recursos_graficos")

CartelAlerta = importar_desde_carpeta(
    nombre_archivo="elementos_de_interfaz_de_usuario.py",
    nombre_clase="CartelAlerta",
    nombre_carpeta="recursos_graficos",
)
BotonRadioImagenes = importar_desde_carpeta(
    nombre_archivo="elementos_de_interfaz_de_usuario.py",
    nombre_clase="BotonRadioImagenes",
    nombre_carpeta="recursos_graficos",
)
constantes = importar_desde_carpeta(
    nombre_archivo="constantes.py",
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
        self.mazo_lleno = pygame.image.load(imagenes_mazo[0])

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
    def Elemento_mazo(self,imagen,scala,accion):
        elemento_mazo = BotonRadioImagenes(
            un_juego=self.un_juego,imagen=imagen,scala=scala,x=0, y=0,radio_borde=5,color_borde=None,color_borde_hover=None,color_borde_clicado=None,grupo=None,valor=self.cartas,deshabilitado=False,accion=None,lift_offset=0)
        ancho = elemento_mazo.ancho
        alto = elemento_mazo.alto
        x = (constantes.ANCHO_MENU_MESA_ESPERA - ancho) // 2
        y = (constantes.ALTO_MENU_MESA_ESPERA - alto) // 2
        elemento_mazo = BotonRadioImagenes(
            un_juego=self.un_juego,
            imagen=imagen,
            scala=scala,
            x=x, y=y,
            radio_borde=5,
            color_borde=constantes.ELEMENTO_FONDO_TERCIARIO,
            color_borde_hover=constantes.ELEMENTO_FONDO_TERCIARIO,
            color_borde_clicado=constantes.ELEMENTO_FONDO_TERCIARIO,
            grupo=None,
            valor=self.cartas,
            deshabilitado=False,
            accion=accion,
            lift_offset=0
        )
        return elemento_mazo


