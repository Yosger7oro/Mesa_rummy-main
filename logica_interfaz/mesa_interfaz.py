import pygame
from random import choice
import os
from recursos_graficos import constantes
from logica_interfaz.archivo_de_importaciones import importar_desde_carpeta

#Importaciones de clases de interfaz
Mazo = importar_desde_carpeta(
    nombre_archivo="mazo_interfaz.py",
    nombre_clase="Mazo_interfaz",
    nombre_carpeta="logica_interfaz"
)
Jugador = importar_desde_carpeta(
    nombre_archivo="jugador_interfaz.py",
    nombre_clase="Jugador_interfaz",
    nombre_carpeta="logica_interfaz"
)
Carta = importar_desde_carpeta(
    nombre_archivo="cartas_interfaz.py",
    nombre_clase="Cartas_interfaz",
    nombre_carpeta="logica_interfaz"
)


#Importar recursos graficos
Menu = importar_desde_carpeta("menu.py","Menu","recursos_graficos")
Boton = importar_desde_carpeta("elementos_de_interfaz_de_usuario.py","Boton","recursos_graficos")

class Menu_adaptado(Menu):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def dibujar_fondo(self):
        """Dibuja solo el fondo y el borde del menú(recto)"""
        pygame.draw.rect(self.pantalla, self.fondo_color, self.menu, border_radius=self.redondeo)
        if self.grosor_borde > 0 :
            return
        # constantes.FONDO_VENTANA = constantes.ELEMENTO_BORDE_TERCIARIO


class Mesa_interfaz():
    _cartas_imagenes = None  # cache estático
    def __init__(self,jugadores,un_juego):
        self.jugadores = jugadores
        # self.un_juego = un_juego
        self.mesa = self.crear_mesa(un_juego)
    def jugador_mano_orden(self,lista_jugadores):
        indice_del_jugador_mano, nom_jug_mano = choice(list(enumerate(lista_jugadores)))
        print(f"El jugador mano es: {nom_jug_mano.nombre_jugador}")
        jugadores_reordenados = []
        provisional = []

        for x in range(0, indice_del_jugador_mano + 1):
            jugadores_reordenados.insert(0, lista_jugadores[x])

        for x in range(indice_del_jugador_mano + 1, len(lista_jugadores)):
            provisional.insert(0, lista_jugadores[x])

        for p in provisional:
            jugadores_reordenados.append(p)

        return jugadores_reordenados

    def crear_mesa(self,un_juego):
        x_menu,y_menu = un_juego.centrar(constantes.ANCHO_MENU_MESA_ESPERA,constantes.ALTO_MENU_MESA_ESPERA)
        mesa = Menu_adaptado(
            un_juego,
            constantes.ANCHO_MENU_MESA_ESPERA,
            constantes.ALTO_MENU_MESA_ESPERA,
            x_menu,
            y_menu,
            constantes.ELEMENTO_FONDO_TERCIARIO,
            constantes.ELEMENTO_BORDE_TERCIARIO,
            constantes.BORDE_PRONUNCIADO,
            constantes.REDONDEO_NORMAL
        )
        self.iniciar_partida(un_juego,mesa)
        un_juego.fondo_ventana = constantes.ELEMENTO_BORDE_TERCIARIO
        return mesa
    def iniciar_partida(self,un_juego,mesa):
        lista_jugadores = self.cargar_jugadores(un_juego,mesa)
        self.cargar_cartas(mesa,lista_jugadores) # Repartir cartas y colocarlas automáticamente
        
    """Metodos para la carga de jugadores"""
    def dimensiones_jugador(self):
        alto_jugador = constantes.ELEMENTO_PEQUENO_ALTO * 0.50
        ancho_jugador = constantes.ELEMENTO_GRANDE_ANCHO * 0.40
        posiciones = [
            ("abajo", 0.5),  # jugador 0
            ("derecha", 0.7),  # jugador 1
            ("arriba", 0.5),  # jugador 2
            ("izquierda", 0.7),  # jugador 3
        ]
        return alto_jugador,ancho_jugador,posiciones
    def cargar_jugadores(self, un_juego, mesa):
        alto_jugador,ancho_jugador,posiciones = self.dimensiones_jugador()
        cantidad_jugadores = len(self.jugadores)
        lista_objeto_jugador = []

        for i in range(cantidad_jugadores):
            direccion, alineacion = posiciones[i]

            if direccion == "abajo":
                x, y = self.alinear_abajo(ancho_jugador, alto_jugador, alineacion)
                fila_cartas = "horizontal"
            elif direccion == "arriba":
                x, y = self.alinear_arriba(ancho_jugador, alto_jugador, alineacion)
                fila_cartas = "horizontal"
            elif direccion == "izquierda":
                x, y = self.alinear_izquierda(ancho_jugador, alto_jugador, alineacion)
                fila_cartas = "vertical"
            elif direccion == "derecha":
                x, y = self.alinear_derecha(ancho_jugador, alto_jugador, alineacion)
                fila_cartas = "vertical"

            jugador = Jugador(
                un_juego=un_juego,
                x=x,
                y=y,
                ancho=ancho_jugador,
                alto=alto_jugador,
                nro=(i + 1),
                nombre=self.jugadores[i],
            )

            mesa.botones.append(jugador.usuario)
            lista_objeto_jugador.append(jugador)

            # Guardar disposición de cartas
            jugador.fila_cartas = fila_cartas
            jugador.offset_cartas = 30  # separación entre cartas
        return lista_objeto_jugador
    """fin de los metodos para la carga de jugadores"""

    """Inicio de los metodos para cargar_cartas"""
    @classmethod
    def preparar_imagenes_cartas(cls):
        if cls._cartas_imagenes is not None:
            return cls._cartas_imagenes  # ya están cargadas

        palos = ('Pica', 'Corazon', 'Diamante', 'Trebol')
        nro_carta = ('A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K')
        cartas_imagenes = {}

        for palo in palos:
            for carta in nro_carta:
                ruta = importar_desde_carpeta(
                    nombre_archivo=f"Imagenes/Cartas/{palo} ({carta}).png",
                    nombre_carpeta="assets"
                )
                cart = pygame.image.load(ruta).convert_alpha()
                cartas_imagenes[f"{palo} ({carta})"] = cart

        # Joker
        ruta = importar_desde_carpeta(
            nombre_archivo="Imagenes/Cartas/!Joker.png",
            nombre_carpeta="assets"
        )
        cartas_imagenes["Joker (Especial)"] = pygame.image.load(ruta).convert_alpha()

        cls._cartas_imagenes = (palos, nro_carta, cartas_imagenes)
        return cls._cartas_imagenes
    def cargar_cartas(self, mesa, lista_jugadores):
        palos,nro_carta,cartas_imagenes = self.preparar_imagenes_cartas()
        cantidad_de_jugadores = len(lista_jugadores)

        mazo = Mazo()
        nro_mazos = mazo.calcular_nro_mazos(cantidad_de_jugadores)
        
        # Crear mazo
        for _ in range(nro_mazos):
            for palo in palos:
                for carta in nro_carta:
                    cart = Carta(
                        ruta_imagen=None,
                        numero=carta,
                        figura=palo
                    )
                    cart.imagen = cartas_imagenes.get(f'{palo} ({carta})')
                    mazo.agregar_cartas(cart)
            # Joker
            cart = Carta(
                ruta_imagen=None,
                numero='Joker',
                figura='Especial'
            )
            cart.imagen = cartas_imagenes.get("Joker (Especial)")
            mazo.agregar_cartas(cart)
        #revolver el mazo
        mazo.revolver_mazo()
        lista_jugadores_reordenado = self.jugador_mano_orden(lista_jugadores)
        #repartir cartas
        manos = mazo.repartir_cartas(lista_jugadores_reordenado)
        
        #mostrar las cartas
        mazo.mostrar_cartas("Las cartas en el mazo son: ")
        
        #mostrar el nro de cartas restantes
        mazo.mostrar_numero_cartas("El número de cartas en el mazo: ")
        
        # jugadores_reordenados = cls.jugador_mano_orden()
        
        #Mostrar visualmente la mano de cada jugador
        self.mostrar_manos(manos,mesa,lista_jugadores_reordenado)
    def mostrar_manos(self,manos,mesa,lista_jugadores):
        # Colocar cartas automáticamente
        for i, mano in enumerate(manos):
            jugador = lista_jugadores[i]

            dx, dy = (jugador.offset_cartas, 0) if jugador.fila_cartas == "horizontal" else (0, jugador.offset_cartas)

            match jugador.nro_jugador:
                case 1:  # Abajo
                    x, y = jugador.x*0.86, jugador.y*1.1
                case 2:  # Derecha
                    x, y = jugador.x*1.2, jugador.y*0.8  
                    dy = -jugador.offset_cartas
                case 3:  # Arriba
                    x, y = jugador.x*1.4, jugador.y*-0.7
                    dx = -jugador.offset_cartas
                case 4:  # Izquierda
                    x, y = jugador.x*-0.7, jugador.y*0.18

            print(f'\nCartas del jugador {jugador.nro_jugador} - {jugador.nombre_jugador}:')

            for carta in mano:
                print(carta)
                cart_imagen = carta.imagen_asociada()

                if jugador.fila_cartas == "vertical":
                    rotacion = -90 if jugador.nro_jugador == 2 else 90
                    cart_imagen = pygame.transform.rotate(cart_imagen, rotacion)

                mesa.agregar_imagen(cart_imagen, (x, y), 0.05)
                x += dx
                y += dy
    """fin de metodos para la creacion de manos"""

    def alinear_abajo(self,ancho,alto,alineacion_x):
        x = (constantes.ANCHO_MENU_MESA_ESPERA-ancho)*alineacion_x
        y = (constantes.ALTO_MENU_MESA_ESPERA-alto)*0.87
        return (x,y)
    def alinear_arriba(self,ancho,alto,alineacion_x):
        x = (constantes.ANCHO_MENU_MESA_ESPERA-ancho)*alineacion_x
        y = (constantes.ALTO_MENU_MESA_ESPERA-alto)*0.13
        return (x,y)
    def alinear_izquierda(self,ancho,alto,alineacion_y):
        x = (constantes.ANCHO_MENU_MESA_ESPERA-ancho)*0.05
        y = (constantes.ALTO_MENU_MESA_ESPERA-alto)*alineacion_y
        return (x,y)
    def alinear_derecha(self,ancho,alto,alineacion_y):
        x = (constantes.ANCHO_MENU_MESA_ESPERA-ancho)*0.95
        y = (constantes.ALTO_MENU_MESA_ESPERA-alto)*alineacion_y
        return (x,y)
