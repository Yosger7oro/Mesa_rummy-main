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
BotonImagen = importar_desde_carpeta("elementos_de_interfaz_de_usuario.py", "BotonImagen", "recursos_graficos")

class Menu_adaptado(Menu):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def dibujar_fondo(self):
        """Dibuja un rectángulo de fondo más grande que el menú, sin borde, y luego el menú centrado."""
        # Tamaño del rectángulo de fondo (un poco más grande que el menú)
        rect_fondo = pygame.Rect(
            0,
            0,
            constantes.ANCHO_VENTANA,
            constantes.ALTO_VENTANA,
        )

        # Dibujar rectángulo de fondo
        pygame.draw.rect(self.pantalla, self.borde_color, rect_fondo, border_radius=0)

        # Dibujar menú encima del fondo (solo el rect del menú, sin borde)
        pygame.draw.rect(self.pantalla, self.fondo_color, self.menu, border_radius=self.redondeo)



class Mesa_interfaz():
    _cartas_imagenes = None  # cache estático
    def __init__(self,jugadores,un_juego,id_jugador):
        self.lista_informacion_mesa = {
            1
        }

        #atributos de logica
        self.id_jugador = id_jugador
        self.jugadores = jugadores
        # self.un_juego = un_juego
        self.mesa = self.crear_mesa(un_juego)
        self.descarte = []

    """Metodos netamente logica"""
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
    """fin de los metodos netamente logica"""
    
    """Metodos netamente interfaz"""
    def dimensiones_jugador(self):
        alto_jugador = constantes.ELEMENTO_PEQUENO_ALTO * 0.50
        ancho_jugador = constantes.ELEMENTO_GRANDE_ANCHO * 0.40
        if len(self.jugadores) < 5:
            posiciones = [
                ("abajo", 0.5),      # Abajo centrado
                ("derecha", 0.7),    # derecha abajo
                ("arriba", 0.5),     # arriba centrado
                ("izquierda", 0.7),  # izquierda abajo
            ]
        else:
            posiciones = [
                ("abajo", 0.5),      # abajo-centrado
                ("derecha", 1),      # derecha-abajo     
                ("derecha", 0.5),    # derecha-enmedio
                ("arriba", 0.65),    # arriba-derecha
                ("arriba", 0.25),    # arriba-izquierda
                ("izquierda", 0.5),  # izquierda-enmedio
                ("izquierda", 1),    # izquierda-abajo
            ]
        return alto_jugador, ancho_jugador, posiciones
    def reordenar_jugadores(self, lista_jugadores):
        """
        Rota la lista de jugadores de modo que el jugador local (self.id)
        quede siempre en la primera posición (abajo).
        """
        # OJO: aquí self.id no es el nombre, sino el índice del jugador local
        # (ejemplo: si self.id == 3, significa que el jugador 3 debe ir abajo)
        indice_local = self.id_jugador - 1  # convertir id a índice de lista (0-based)

        return lista_jugadores[indice_local:] + lista_jugadores[:indice_local] 
    
    def determinar_alineacion_jugador(self,direccion,ancho_jugador,alto_jugador,alineacion):
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
        return x,y,fila_cartas
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
        
        # Reverso
        ruta2 = importar_desde_carpeta(
            nombre_archivo="Imagenes/Cartas/!Reverso.png",
            nombre_carpeta="assets"
        )
        cartas_imagenes["Reverso"] = pygame.image.load(ruta2).convert_alpha()

        cls._cartas_imagenes = (palos, nro_carta, cartas_imagenes)
        return cls._cartas_imagenes
    def determinar_ubicacion_mano(self,jugador,dx,dy):
        if jugador.fila_cartas == "horizontal":
            if jugador.direccion == "abajo":
                x, y = jugador.x - (jugador.ancho/2), jugador.y + (jugador.alto + 10)
            elif jugador.direccion == "arriba":
                x, y = jugador.x + (jugador.ancho - 50), jugador.y - (jugador.alto + 75)
                dx = -jugador.offset_cartas
        elif jugador.fila_cartas == "vertical":
            if jugador.direccion == "derecha":
                x, y = jugador.x + (jugador.ancho - 50), jugador.y - (jugador.alto + 25)
                dy = -jugador.offset_cartas
            elif jugador.direccion == "izquierda":
                x, y = jugador.x - (jugador.ancho - 150), jugador.y - (jugador.alto + 220)
        return x,y,dx,dy

    def mostrar_manos(self, manos, mesa, lista_jugadores):
        # Colocar cartas automáticamente
        for i, mano in enumerate(manos):
            jugador = lista_jugadores[i]

            dx, dy = (jugador.offset_cartas, 0) if jugador.fila_cartas == "horizontal" else (0, jugador.offset_cartas)

            # Decidir posición inicial según dirección
            x,y,dx,dy = self.determinar_ubicacion_mano(jugador,dx,dy)

            # Para depurar
            print(f"\nJugador: {jugador.nombre_jugador} nro {jugador.nro_jugador} "
                f"dx={dx} dy={dy} fila={jugador.fila_cartas}")

            # Escala (ejemplo: jugador local más grande)
            escala = 0.05 if jugador.nro_jugador == self.id_jugador else 0.035

            for carta in mano:
                print(carta)

                reverso = False
                if self.id_jugador != jugador.nro_jugador:
                    reverso = True
                cart_imagen = carta.imagen_asociada(reverso)

                # Rotar si está en vertical
                if jugador.fila_cartas == "vertical":
                    rotacion = -90 if jugador.direccion == "derecha" else 90
                    cart_imagen = pygame.transform.rotate(cart_imagen, rotacion)

                mesa.agregar_imagen(cart_imagen, (x, y), escala)
                x += dx
                y += dy
    def alinear_abajo(self,ancho,alto,alineacion_x):
        x = (constantes.ANCHO_MENU_MESA_ESPERA-ancho)*alineacion_x
        y = (constantes.ALTO_MENU_MESA_ESPERA-alto)*0.87
        return (x,y)
    def alinear_arriba(self,ancho,alto,alineacion_x):
        x = (constantes.ANCHO_MENU_MESA_ESPERA-ancho)*alineacion_x
        y = (constantes.ALTO_MENU_MESA_ESPERA-alto)*0.13
        return (x,y)
    def alinear_izquierda(self,ancho,alto,alineacion_y):
        x = (constantes.ANCHO_MENU_MESA_ESPERA-ancho)*0.02
        y = (constantes.ALTO_MENU_MESA_ESPERA-alto)*alineacion_y
        return (x,y)
    def alinear_derecha(self,ancho,alto,alineacion_y):
        x = (constantes.ANCHO_MENU_MESA_ESPERA-ancho)
        y = (constantes.ALTO_MENU_MESA_ESPERA-alto)*alineacion_y
        return (x,y)
    """fin de los metodos netamente interfaz"""

    """metodos interfaz-logica"""
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

        ruta_mazo = importar_desde_carpeta(
            nombre_archivo="Imagenes/Mazo/mazo1.png",
            nombre_carpeta="assets"
        )
        imagen_mazo = pygame.image.load(ruta_mazo).convert_alpha()
        # Tamaño del botón (ajusta aquí el tamaño) :)
        ancho, alto = 100, 140

        x_centro = (constantes.ANCHO_MENU_MESA_ESPERA - ancho) // 2
        y_centro = (constantes.ALTO_MENU_MESA_ESPERA - alto) // 2
        boton_mazo = BotonImagen(
            un_juego=un_juego,
            imagen=imagen_mazo,
            x=x_centro,
            y=y_centro,
            ancho=ancho,
            alto=alto,
            accion=lambda: print("se ha seleccionado el mazo")
        )
        mesa.botones.append(boton_mazo)

        self.iniciar_partida(un_juego,mesa)
        return mesa
    def iniciar_partida(self,un_juego,mesa):
        lista_jugadores = self.cargar_jugadores(un_juego,mesa)
        print([jugador.nombre_jugador for jugador in lista_jugadores])#para depurar
        self.cargar_cartas(mesa,lista_jugadores) # Repartir cartas y colocarlas automáticamente

    """Metodos para la carga de jugadores"""
    def cargar_jugadores(self, un_juego, mesa):
        
        alto_jugador, ancho_jugador, posiciones = self.dimensiones_jugador()

        # Rotamos solo para saber quién va en "abajo", "arriba", etc.
        jugadores_rotados = self.reordenar_jugadores(self.jugadores)

        lista_objeto_jugador = []

        for i, nombre in enumerate(self.jugadores):  # mantener orden de entrada a partida
            # buscamos dónde debería ir gráficamente este jugador
            indice_rotado = jugadores_rotados.index(nombre)
            direccion, alineacion = posiciones[indice_rotado]

            x,y,fila_cartas = self.determinar_alineacion_jugador(direccion,ancho_jugador,alto_jugador,alineacion)

            jugador = Jugador(
                un_juego=un_juego,
                x=x, y=y,
                ancho=ancho_jugador,
                alto=alto_jugador,
                nro=(i + 1),      # orden de entrada a partida
                nombre=nombre     # es string, no objeto
            )

            mesa.botones.append(jugador.usuario)
            lista_objeto_jugador.append(jugador)

            jugador.fila_cartas = fila_cartas
            jugador.direccion = direccion
            jugador.offset_cartas = 40 if jugador.nro_jugador == self.id_jugador else 20

        return lista_objeto_jugador
    """fin de los metodos para la carga de jugadores"""

    
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
                    cart.parte_superior = cartas_imagenes.get(f'{palo} ({carta})')
                    cart.parte_trasera = cartas_imagenes.get('Reverso')
                    mazo.agregar_cartas(cart)
            # Joker
            cart = Carta(
                ruta_imagen=None,
                numero='Joker',
                figura='Especial'
            )
            cart.parte_superior = cartas_imagenes.get("Joker (Especial)")
            cart.parte_trasera = cartas_imagenes.get('Reverso')
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
        
        
        #Mostrar visualmente la mano de cada jugador
        self.mostrar_manos(manos,mesa,lista_jugadores_reordenado)
        
        # if mazo.cartas:
        #     self.descarte.append(mazo.cartas.pop(-1))
