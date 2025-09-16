from logica_interfaz.archivo_de_importaciones import importar_desde_carpeta
import pygame

Cartas = importar_desde_carpeta(
    nombre_archivo= "cartas.py",
    nombre_clase= "Cartas")
BotonRadioImagenes = importar_desde_carpeta("elementos_de_interfaz_de_usuario.py","BotonRadioImagenes","recursos_graficos")


class Cartas_interfaz(Cartas):
    def __init__(self, *args, un_juego = None,ruta_imagen=None,reverso=False,**kwargs):
        # Pasar todos los argumentos posicionales y nombrados al padre
        super().__init__(*args, **kwargs)
        self.un_juego = un_juego
        self.ruta_imagen = ruta_imagen
        # self.grupo = grupo
        self.parte_superior = pygame.image.load(self.ruta_imagen) if ruta_imagen is not None else None
        self.parte_trasera = None
        self.reverso = reverso
    def Elemento_carta(self,grupo,x,y,scala,imagen):
        carta = BotonRadioImagenes(
            un_juego=self.un_juego,
            imagen=imagen,
            scala=scala,
            x=x, y=y,
            radio_borde=5,
            color_borde=(0, 0, 0),
            color_borde_hover=(255, 0, 0),
            color_borde_clicado=(0, 255, 0),
            grupo=grupo,
            valor=self.__str__(),
            deshabilitado=False,
            accion=None,
            lift_offset=20
        )
        grupo.append(carta)
        return carta
    def imagen_asociada(self,reverso=False):
        if reverso:
            return self.parte_trasera
        return self.parte_superior



# import pygame
# pygame.init()

# # --- Configuración de la pantalla ---
# pantalla = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("Demo BotonRadioModificado")

# # --- Cargar imágenes (o usar superficies de prueba) ---
# # Aquí se pueden cargar imágenes reales con pygame.image.load("ruta")
# imagen1 = pygame.image.load(importar_desde_carpeta(nombre_carpeta="assets",nombre_archivo="Imagenes/Cartas/Corazon (2).png"))
# imagen2 = pygame.image.load(importar_desde_carpeta(nombre_carpeta="assets",nombre_archivo="Imagenes/Cartas/Corazon (4).png"))



# # --- Grupo de botones ---
# grupo_cartas = []

# # --- Crear botones ---
# # Nota: `un_juego` puede ser cualquier objeto que tenga `pantalla` como atributo
# class JuegoMock:
#     def __init__(self, pantalla):
#         self.pantalla = pantalla

# un_juego = JuegoMock(pantalla)

# carta1 = BotonRadioModificado(
#     un_juego=un_juego,
#     imagen=imagen1,
#     ancho=100, alto=150,
#     x=100, y=300,
#     radio_borde=5,
#     color_borde=(0, 0, 0),
#     color_borde_hover=(255, 0, 0),
#     color_borde_clicado=(0, 255, 0),
#     grupo=grupo_cartas,
#     valor="carta1",
#     deshabilitado=False,
#     accion=None,
#     lift_offset=20
# )
# grupo_cartas.append(carta1)
# carta2 = BotonRadioModificado(
#     un_juego=un_juego,
#     imagen=imagen2,
#     ancho=100, alto=150,
#     x=250, y=300,
#     radio_borde=5,
#     color_borde=(0, 0, 0),
#     color_borde_hover=(255, 0, 0),
#     color_borde_clicado=(0, 255, 0),
#     grupo=grupo_cartas,
#     valor="carta2",
#     deshabilitado=False,
#     accion=None,
#     lift_offset=20
# )
# grupo_cartas.append(carta2)


# # --- Bucle principal ---
# running = True
# while running:
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             running = False
        
#         # Manejar eventos de los botones
#         carta1.manejar_evento(evento)
#         carta2.manejar_evento(evento)

#         # Actualizar hover (opcional)
#         carta1.verificar_hover(pygame.mouse.get_pos())
#         carta2.verificar_hover(pygame.mouse.get_pos())

#     # --- Dibujar ---
#     pantalla.fill((30, 30, 30))  # fondo gris oscuro
#     carta1.dibujar()
#     carta2.dibujar()

#     pygame.display.flip()

# pygame.quit()