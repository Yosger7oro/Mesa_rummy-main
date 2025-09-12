import pygame
import os
from recursos_graficos import constantes
from logica_interfaz.archivo_de_importaciones import importar_desde_carpeta

# Importamos las clases de interfaz que ya creaste
from logica_interfaz.mazo_intefaz import Mazo_interfaz as Mazo
from logica_interfaz.jugador_interfaz import Jugador_interfaz 
from logica_interfaz.cartas_interfaz import Cartas_interfaz  # si la mueves a su propio archivo

class Mesa_interfaz:
    def __init__(self, pantalla, cantidad_jugadores):
        self.pantalla = pantalla
        self.cantidad_jugadores = cantidad_jugadores
        
        # 🔹 Pasamos la referencia al juego/pantalla al mazo de interfaz
        self.mazo = Mazo(un_juego=self)

        # Diccionario de imágenes de cartas
        self.imagenes_cartas = {}
        self.cargar_imagenes_cartas()
        
        # Posiciones según número de jugadores
        self.posiciones_jugadores = self.obtener_posiciones_jugadores(self.cantidad_jugadores)

        # Jugadores con interfaz
        self.jugadores = []
        for i in range(self.cantidad_jugadores):
            x, y = self.posiciones_jugadores[i]
            self.jugadores.append(
                Jugador_interfaz(
                    nro=i + 1,
                    nombre=f"J{i+1}",
                    un_juego=self,
                    x=x,
                    y=y,
                    ancho=150,
                    alto=50
                )
            )



        # Inicializar y repartir
        self.inicializar_mazos()
        self.repartir_cartas()

    def cargar_imagenes_cartas(self):
        ruta_cartas = os.path.join("assets", "Imagenes", "Cartas")
        for archivo in os.listdir(ruta_cartas):
            if archivo.endswith(".png"):
                ruta_completa = os.path.join(ruta_cartas, archivo)
                imagen = pygame.image.load(ruta_completa).convert_alpha()
                self.imagenes_cartas[archivo] = pygame.transform.scale(imagen, (60, 90))

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
        else:
            raise ValueError(f"No hay posiciones definidas para {cantidad} jugadores")

    def dibujar(self):
        self.pantalla.fill((0, 128, 0))
        for jugador in self.jugadores:
            jugador.usuario.dibujar()  # usa el Elemento_texto del jugador
