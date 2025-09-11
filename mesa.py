import pygame
import os
import constantes
from jugador import Jugador
from mazo import Mazo

class Mesa:
    def __init__(self, pantalla, cantidad_jugadores):
        self.pantalla = pantalla
        self.mazo = Mazo()
        self.cantidad_jugadores = cantidad_jugadores
        self.imagenes_cartas = {}
        self.cargar_imagenes_cartas()
        
        # Definir posiciones según cantidad de jugadores
        self.posiciones_jugadores = self.obtener_posiciones_jugadores(self.cantidad_jugadores)

        self.jugadores = []
        for i in range(self.cantidad_jugadores):
            self.jugadores.append(Jugador(i + 1, f"J{i+1}", [])) 

        self.inicializar_mazos()
        self.repartir_cartas()

    def cargar_imagenes_cartas(self):
        ruta_cartas = "assets/Imagenes/Cartas"
        for archivo in os.listdir(ruta_cartas):
            if archivo.endswith(".png"):
                imagen = pygame.image.load(os.path.join(ruta_cartas, archivo)).convert_alpha()
                self.imagenes_cartas[archivo] = pygame.transform.smoothscale(imagen, (60, 90))

    def inicializar_mazos(self):
        nro_mazos = self.mazo.calcular_nro_mazos(self.cantidad_jugadores)
        cartas_un_mazo = list(self.imagenes_cartas.keys())
        for _ in range(nro_mazos):
            for nombre_carta in cartas_un_mazo:
                self.mazo.agregar_cartas(nombre_carta)
        self.mazo.revolver_mazo()

    def repartir_cartas(self):
        manos = self.mazo.repartir_cartas(self.jugadores)
        for i, mano in enumerate(manos):
            self.jugadores[i].mano = mano

    def obtener_posiciones_jugadores(self, cantidad):
        if cantidad == 2:
            return {
                0: (constantes.ANCHO_VENTANA // 2 - 339, constantes.ALTO_VENTANA - 120),
                1: (constantes.ANCHO_VENTANA // 2 - 110, 60)
            }
        elif cantidad == 3:
            return {
                0: (constantes.ANCHO_VENTANA // 2 - 339, constantes.ALTO_VENTANA - 120),
                1: (constantes.ANCHO_VENTANA // 2 + 325, constantes.ALTO_VENTANA // 2 - 45),
                2: (constantes.ANCHO_VENTANA // 2 - 110, 60)           
            }
        elif cantidad == 4:
            return {
                0: (constantes.ANCHO_VENTANA // 2 - 339, constantes.ALTO_VENTANA - 120),
                1: (constantes.ANCHO_VENTANA // 2 + 325, constantes.ALTO_VENTANA // 2 - 45),
                2: (constantes.ANCHO_VENTANA // 2 - 110, 60),
                3: (constantes.ANCHO_VENTANA // 2 - 540, constantes.ALTO_VENTANA // 2 - 45)
            }
        elif cantidad == 5:
            return {
                0: (constantes.ANCHO_VENTANA // 2 - 339, constantes.ALTO_VENTANA - 120),
                1: (constantes.ANCHO_VENTANA // 2 + 325, constantes.ALTO_VENTANA // 2 + 60),
                2: (constantes.ANCHO_VENTANA // 2 + 325, constantes.ALTO_VENTANA // 2 - 120),
                3: (constantes.ANCHO_VENTANA // 2 + 100, constantes.ALTO_VENTANA // 2 - 300),
                4: (constantes.ANCHO_VENTANA // 2 - 300, constantes.ALTO_VENTANA // 2 - 300)
            }
        elif cantidad == 6:
            return {
                0: (constantes.ANCHO_VENTANA // 2 - 339, constantes.ALTO_VENTANA - 120),
                1: (constantes.ANCHO_VENTANA // 2 + 325, constantes.ALTO_VENTANA // 2 + 60),
                2: (constantes.ANCHO_VENTANA // 2 + 325, constantes.ALTO_VENTANA // 2 - 120),
                3: (constantes.ANCHO_VENTANA // 2 + 100, constantes.ALTO_VENTANA // 2 - 300),
                4: (constantes.ANCHO_VENTANA // 2 - 300, constantes.ALTO_VENTANA // 2 - 300),
                5: (constantes.ANCHO_VENTANA // 2 - 540, constantes.ALTO_VENTANA // 2 - 120) 
            }
        elif cantidad == 7:
            return {
                0: (constantes.ANCHO_VENTANA // 2 - 339, constantes.ALTO_VENTANA - 120),
                1: (constantes.ANCHO_VENTANA // 2 + 325, constantes.ALTO_VENTANA // 2 + 60),
                2: (constantes.ANCHO_VENTANA // 2 + 325, constantes.ALTO_VENTANA // 2 - 120),
                3: (constantes.ANCHO_VENTANA // 2 + 100, constantes.ALTO_VENTANA // 2 - 300),
                4: (constantes.ANCHO_VENTANA // 2 - 300, constantes.ALTO_VENTANA // 2 - 300),
                5: (constantes.ANCHO_VENTANA // 2 - 540, constantes.ALTO_VENTANA // 2 - 120),                
                6: (constantes.ANCHO_VENTANA // 2 - 540, constantes.ALTO_VENTANA // 2 + 60)          
            }
    def dibujar(self):

        color_borde = (101, 67, 33)         # Marrón
        color_verde_oscuro = (30, 90, 50)   # Verde oscuro
        grosor_borde = 10

        # Dibuja el borde marrón (rellena toda la pantalla)
        self.pantalla.fill(color_borde)
        # Dibuja el rectángulo verde oscuro encima, dejando el borde visible
        pygame.draw.rect(
            self.pantalla,
            color_verde_oscuro,
            (grosor_borde, grosor_borde,
            constantes.ANCHO_VENTANA - 2 * grosor_borde,
            constantes.ALTO_VENTANA - 2 * grosor_borde),
            border_radius = constantes.REDONDEO_NORMAL
        )

       
        for i, jugador in enumerate(self.jugadores):
            if i in self.posiciones_jugadores:
                x, y = self.posiciones_jugadores[i]
                jugador.dibujar(self.pantalla, x, y, self.imagenes_cartas)

