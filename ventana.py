import pygame
import sys

import constantes
import acciones
from boton import Elemento_texto,Boton,BotonRadio, EntradaTexto
from menu import Menu
from mesa import Mesa

"""Clase ventana donde estaran todos los diseños e interacciones"""
class Ventana:
    """Inicializar pygame, fuentes, crear pantalla, nombre de la misma, cargar imagenes, crear menus y botones"""
    def __init__(self):
        
        pygame.init()
        pygame.font.init()
        self.pantalla = pygame.display.set_mode((constantes.ANCHO_VENTANA,constantes.ALTO_VENTANA))
        pygame.display.set_caption("Rummy500")
        
        #Definimos los valores a guardar (importante para crear el servidor)
        self.lista_elementos = {
            "cantidad_jugadores":0,
            "nombre_creador":"",
            "nombres_jugadores":[]
        }
        self.logo_rummy = pygame.image.load("assets/Imagenes/Logos/Logo(1).png")
        self.menu_instrucciones = self.Menu_instrucciones()
        self.menu_inicio = self.Menu_inicio()
        self.boton_jugar = self.Boton_jugar()
        self.menu_Cantidad_Jugadores = self.Menu_Cantidad_Jugadores()
        self.menu_nombre_usuario = self.Menu_nombre_usuario()

        self.menu_inicio = self.Menu_inicio()
        self.boton_jugar = self.Boton_jugar()
        self.clock = pygame.time.Clock()
        
    """Funcion para centrar en la ventana"""
    def centrar(self,ancho_elemento,alto_elemento):
        x = (constantes.ANCHO_VENTANA - ancho_elemento)/2
        y = (constantes.ALTO_VENTANA - alto_elemento)/2
        return (x,y)

    """Funcion que crea el boton Jugar, se pasa por parametros las constantes, las posiciones se definen manualemente"""
    def Boton_jugar(self):
        x,y = self.centrar(constantes.ELEMENTO_MEDIANO_ANCHO,constantes.ELEMENTO_MEDIANO_ALTO)
        boton_jugar = Boton(
            un_juego= self,
            texto= "JUGAR",
            ancho= constantes.ELEMENTO_MEDIANO_ANCHO,
            alto= constantes.ELEMENTO_MEDIANO_ALTO,
            x= x,
            y= y,
            tamaño_fuente= constantes.F_MEDIANA,
            fuente= constantes.FUENTE_LLAMATIVA,
            color= constantes.ELEMENTO_FONDO_PRINCIPAL,
            radio_borde= constantes.REDONDEO_NORMAL,
            color_texto= constantes.COLOR_TEXTO_PRINCIPAL,
            color_borde= constantes.ELEMENTO_BORDE_PRINCIPAL,
            grosor_borde= constantes.BORDE_PRONUNCIADO,
            color_borde_hover= constantes.ELEMENTO_HOVER_PRINCIPAL,
            color_borde_clicado= constantes.ELEMENTO_CLICADO_PRINCIPAL,
            accion= lambda: acciones.Mostrar_seccion(boton_jugar, self.menu_inicio)
            )
        
        return boton_jugar
    def Menu_instrucciones(self):
        x_menu,y_menu = self.centrar(constantes.ANCHO_MENU_INSTRUCCIONES,constantes.ALTO_MENU_INSTRUCCIONES)
        menu_instrucciones = Menu(
            un_juego= self,
            ancho= constantes.ANCHO_MENU_INSTRUCCIONES,
            alto= constantes.ALTO_MENU_INSTRUCCIONES,
            x= x_menu,
            y= y_menu,
            fondo_color= constantes.ELEMENTO_FONDO_PRINCIPAL,
            borde_color= constantes.ELEMENTO_BORDE_PRINCIPAL,
            grosor_borde= constantes.BORDE_PRONUNCIADO,
            redondeo= constantes.REDONDEO_PRONUNCIADO
            )
        x_elemento_txt,y_elemento_txt = (constantes.BORDE_PRONUNCIADO*2)/2,(constantes.ALTO_MENU_INSTRUCCIONES*0.05)
        menu_instrucciones.crear_elemento(
            Clase=Elemento_texto,
            x=x_elemento_txt,
            y=y_elemento_txt,
            un_juego=self,
            texto="1. El último jugador en acumular menos de 500 puntos al acabar todos los juegos de la partida, gana la partida. \n2. El primer jugador en alcanzar o superar los 500 puntos es eliminado. \n3. En cada turno, cada jugador en su turno puede robar una carta del mazo o del descarte.\n4. Puedes robar una carta fuera de tu turno (Compra) pero de penalización debes robar otra carta.\n5. El objetivo es formar tríos o seguidillas de cartas para bajarse.\n6. Los tríos debe tener mínimo 3 cartas del mismo valor y no más de un Joker.\n7. Las seguidillas deben de ser de mínimo 4 cartas del mismo palo y valor ascendente, sin tener dos Jokers juntos.\n8. Cada juego consta de 4 rondas, cada ronda termina cuando un jugador consigue bajar todas sus cartas.\n9. Al finalizar cada ronda, los jugadores que no consiguieron bajarse suman las cartas en sus manos según su valor.",
            ancho=constantes.ANCHO_MENU_INSTRUCCIONES-(constantes.BORDE_PRONUNCIADO*2),
            alto=constantes.ALTO_MENU_INSTRUCCIONES*0.75,
            tamaño_fuente=constantes.F_MEDIANA,
            fuente=constantes.FUENTE_ESTANDAR,
            color=constantes.ELEMENTO_FONDO_PRINCIPAL,
            radio_borde=constantes.REDONDEO_INTERMEDIO,
            color_texto=constantes.COLOR_TEXTO_PRINCIPAL,
            color_borde=constantes.BLANCO,
            grosor_borde=constantes.BORDE_LIGERO,
            alineacion_vertical="arriba",
            alineacion ="izquierda"
        )
        x_boton = (constantes.ANCHO_MENU_INSTRUCCIONES-constantes.ELEMENTO_PEQUENO_ANCHO*0.75)*0.5
        y_boton = (constantes.ALTO_MENU_INSTRUCCIONES-constantes.ELEMENTO_PEQUENO_ALTO*0.9)*0.97
        menu_instrucciones.crear_elemento(
            Clase=Boton,
            x=x_boton,
            y=y_boton,
            un_juego=self,
            texto="VOLVER",
            ancho=constantes.ELEMENTO_PEQUENO_ANCHO*0.75,
            alto=constantes.ELEMENTO_PEQUENO_ALTO*0.9,
            tamaño_fuente=constantes.F_MEDIANA,
            fuente=constantes.FUENTE_LLAMATIVA,
            color=constantes.ELEMENTO_FONDO_PRINCIPAL,
            radio_borde=constantes.REDONDEO_NORMAL,
            color_texto=constantes.COLOR_TEXTO_PRINCIPAL,
            color_borde=constantes.ELEMENTO_BORDE_PRINCIPAL,
            grosor_borde=constantes.BORDE_INTERMEDIO,
            color_borde_hover=constantes.ELEMENTO_HOVER_PRINCIPAL,
            color_borde_clicado=constantes.ELEMENTO_CLICADO_PRINCIPAL,
            accion=lambda: acciones.Mostrar_seccion(menu_instrucciones,self.menu_inicio)
        )
        return menu_instrucciones

    """Funcion Menu de inicio define un menu con sus parametros, y se crean los botones necesarios."""
    def Menu_inicio(self):
        x,y = self.centrar(constantes.ANCHO_MENU_I,constantes.ALTO_MENU_I)
        menu_inicio = Menu(
            un_juego= self,
            ancho= constantes.ANCHO_MENU_I,
            alto= constantes.ALTO_MENU_I,
            x= x,
            y= y,
            fondo_color= constantes.FONDO_VENTANA,
            borde_color= constantes.SIN_COLOR,
            grosor_borde= constantes.SIN_BORDE,
            redondeo= constantes.REDONDEO_PRONUNCIADO
            )
        texto_menu_inicio = ("CREAR SALA","UNIRSE A LA SALA","COMO JUGAR","SALIR DEL JUEGO")
        funciones_menu_inicio = (lambda: acciones.Mostrar_seccion(menu_inicio,self.menu_Cantidad_Jugadores),acciones.Unirse_sala,lambda: acciones.Mostrar_seccion(menu_inicio,self.menu_instrucciones), self.salir)
        incremetar_y = 0
        for i,t in enumerate(texto_menu_inicio):
            x,y = (constantes.ANCHO_MENU_I-constantes.ELEMENTO_GRANDE_ANCHO)*0.9,(constantes.ALTO_MENU_I-constantes.ELEMENTO_GRANDE_ALTO)*(0.17+incremetar_y)
            menu_inicio.crear_elemento(
                Clase=Boton,
                x=x,
                y=y,
                un_juego=self,
                texto=t,
                ancho=constantes.ELEMENTO_GRANDE_ANCHO,
                alto=constantes.ELEMENTO_GRANDE_ALTO,
                tamaño_fuente=constantes.F_MEDIANA,
                fuente=constantes.FUENTE_LLAMATIVA,
                color=constantes.ELEMENTO_FONDO_PRINCIPAL,
                radio_borde=constantes.REDONDEO_NORMAL,
                color_texto=constantes.COLOR_TEXTO_PRINCIPAL,
                color_borde=constantes.ELEMENTO_BORDE_PRINCIPAL,
                grosor_borde=constantes.BORDE_PRONUNCIADO,
                color_borde_hover=constantes.ELEMENTO_HOVER_PRINCIPAL,
                color_borde_clicado=constantes.ELEMENTO_CLICADO_PRINCIPAL,
                accion=funciones_menu_inicio[i]
            )
            incremetar_y += 0.25
        posicion_logo = (constantes.ANCHO_MENU_I*0.05,constantes.ALTO_MENU_I*0.1)
        menu_inicio.agregar_imagen(self.logo_rummy,posicion_logo,constantes.SCALA)
        return menu_inicio
    
    def Menu_nombre(self):
        x_menu, y_menu = self.centrar(constantes.ANCHO_MENU_NOM_USUARIO, constantes.ALTO_MENU_NOM_USUARIO)
        menu_nombre = Menu(
            self,
            constantes.ANCHO_MENU_NOM_USUARIO,
            constantes.ALTO_MENU_NOM_USUARIO,
            x_menu,
            y_menu,
            constantes.ELEMENTO_FONDO_SECUNDARO,
            constantes.ELEMENTO_BORDE_SECUNDARIO,
            constantes.BORDE_PRONUNCIADO,
            constantes.REDONDEO_PRONUNCIADO
        )
    
        # Botón de título
        ancho_nombre = constantes.BT_GRANDE_ANCHO * 1.9
        alto_nombre = constantes.BT_MEDIANO_ALTO * 0.95
        x_nombre = (constantes.ANCHO_MENU_NOM_USUARIO - ancho_nombre) * 0.5
        y_nombre = (constantes.ALTO_MENU_NOM_USUARIO - alto_nombre) * 0.10
    
        menu_nombre.crear_boton(
            ClaseBoton=Boton,
            x=x_nombre,
            y=y_nombre,
            un_juego=self,
            texto="INGRESA TU NOMBRE",
            ancho=ancho_nombre,
            alto=alto_nombre,
            tamaño_fuente=constantes.F_GRANDE,  
            fuente=constantes.FUENTE_ESTANDAR,
            color=constantes.ELEMENTO_FONDO_PRINCIPAL,
            radio_borde=constantes.REDONDEO_NORMAL,
            color_texto=constantes.COLOR_TEXTO_PRINCIPAL,
            color_borde=constantes.ELEMENTO_BORDE_PRINCIPAL,
            grosor_borde=constantes.BORDE_PRONUNCIADO,
        )

        # Campo de entrada de texto
        ancho_input = constantes.BT_GRANDE_ANCHO * 1.9
        alto_input = constantes.BT_MEDIANO_ALTO * 0.95
        x_input = (constantes.ANCHO_MENU_NOM_USUARIO - ancho_input) * 0.5
        y_input = (constantes.ALTO_MENU_NOM_USUARIO - alto_input) * 0.50
    
        menu_nombre.crear_boton(
            ClaseBoton=EntradaTexto, 
            x=x_input,
            y=y_input,
            un_juego=self, 
            texto="Nombre de usuario",
            ancho=ancho_input,
            alto=alto_input,
            tamaño_fuente=constantes.F_MEDIANA,  
            fuente=constantes.FUENTE_ESTANDAR,
            color=constantes.ELEMENTO_FONDO_PRINCIPAL,
            radio_borde=constantes.REDONDEO_NORMAL,
            color_texto=constantes.COLOR_TEXTO_PRINCIPAL,
            color_borde=constantes.ELEMENTO_BORDE_PRINCIPAL,
            grosor_borde=constantes.BORDE_PRONUNCIADO,
            color_borde_hover=constantes.ELEMENTO_HOVER_PRINCIPAL,
            color_borde_clicado=constantes.ELEMENTO_FONDO_PRINCIPAL,
            limite_caracteres=20  
        )

        # Botón volver
        x_boton_volver = constantes.BT_MEDIANO_ANCHO / 3
        y_boton_volver = (constantes.ALTO_MENU_NOM_USUARIO - constantes.BT_MEDIANO_ALTO) * 0.8
    
        menu_nombre.crear_boton(
            ClaseBoton=Boton,
            x=x_boton_volver,
            y=y_boton_volver,
            un_juego=self,
            texto="VOLVER",
            ancho=constantes.BT_MEDIANO_ANCHO,
            alto=constantes.BT_MEDIANO_ALTO,
            tamaño_fuente=constantes.F_MEDIANA,
            fuente=constantes.FUENTE_LLAMATIVA,
            color=constantes.ELEMENTO_FONDO_PRINCIPAL,
            radio_borde=constantes.REDONDEO_NORMAL,
            color_texto=constantes.COLOR_TEXTO_PRINCIPAL,
            color_borde=constantes.ELEMENTO_BORDE_SECUNDARIO,
            grosor_borde=constantes.BORDE_PRONUNCIADO,
            color_borde_hover=constantes.ELEMENTO_HOVER_PRINCIPAL,
            color_borde_clicado=constantes.ELEMENTO_CLICADO_PRINCIPAL,
            accion=lambda: acciones.Mostrar_seccion(menu_nombre, self.menu_inicio)
        )

        return menu_nombre
    def Menu_Cantidad_Jugadores(self):
        x_menu,y_menu = self.centrar(constantes.ANCHO_MENU_CNT_J,constantes.ALTO_MENU_CNT_J)
        
        menu_cantidad = Menu(
            self,
            constantes.ANCHO_MENU_CNT_J,
            constantes.ALTO_MENU_CNT_J,
            x_menu,
            y_menu,
            constantes.ELEMENTO_FONDO_SECUNDARO,
            constantes.ELEMENTO_BORDE_SECUNDARIO,
            constantes.BORDE_PRONUNCIADO,
            constantes.REDONDEO_PRONUNCIADO
        )

        ancho_seleccion = constantes.ELEMENTO_GRANDE_ANCHO*2
        alto_seleccion = constantes.ELEMENTO_MEDIANO_ALTO*0.95
        x_seleccion = (constantes.ANCHO_MENU_CNT_J - ancho_seleccion)*(0.5)
        y_seleccion = (constantes.ALTO_MENU_CNT_J - alto_seleccion)*(0.10)
        menu_cantidad
        menu_cantidad.crear_elemento(
            Clase=Elemento_texto,
            x=x_seleccion,
            y=y_seleccion,
            un_juego=self,
            texto="SELECCIONE EL NUMERO DE JUGADORES",
            ancho=ancho_seleccion,
            alto=alto_seleccion,
            tamaño_fuente=constantes.F_GRANDE,
            fuente=constantes.FUENTE_ESTANDAR,
            color=constantes.ELEMENTO_FONDO_PRINCIPAL,
            radio_borde=constantes.REDONDEO_NORMAL,
            color_texto=constantes.COLOR_TEXTO_PRINCIPAL,
            color_borde=constantes.ELEMENTO_BORDE_SECUNDARIO,
            grosor_borde=constantes.BORDE_INTERMEDIO,
        )

        # Generador de textos para cada boton
        texto_menu = (f"{i} JUGADORES" for i in range(2, 8))
        # Lista de botones para el grupo de radio

        botones_radio = []
        posiciones_x = [0.04, 0.50, 0.96] #ubicacion de cada columna
        for i, texto in enumerate(texto_menu):
            columna = i % 3
            fila = i // 3
            posicion_x = posiciones_x[columna]
            posicion_y = 0.30 + (0.30 * fila)
            
            menu_cantidad.crear_elemento(
                Clase=BotonRadio,
                x=(constantes.ANCHO_MENU_CNT_J-constantes.ELEMENTO_PEQUENO_ANCHO) * posicion_x,
                y=(constantes.ALTO_MENU_CNT_J-constantes.ELEMENTO_PEQUENO_ALTO)* posicion_y,
                un_juego=self,
                texto=texto,
                ancho=constantes.ELEMENTO_PEQUENO_ANCHO,
                alto=constantes.ELEMENTO_PEQUENO_ALTO,
                tamaño_fuente=constantes.F_GRANDE,
                fuente=constantes.FUENTE_ESTANDAR,
                color=constantes.ELEMENTO_FONDO_PRINCIPAL,
                radio_borde=constantes.REDONDEO_NORMAL,
                color_texto=constantes.COLOR_TEXTO_PRINCIPAL,
                color_borde=constantes.ELEMENTO_BORDE_SECUNDARIO,
                grosor_borde=constantes.BORDE_LIGERO,
                color_borde_hover=constantes.ELEMENTO_HOVER_PRINCIPAL,
                color_borde_clicado=constantes.ELEMENTO_CLICADO_PRINCIPAL,
                grupo=botones_radio,  # para que funcionen como boton tipo radio
                valor=(i+2)
            )
            # Agregamos el ultimo boton creado al grupo
            botones_radio.append(menu_cantidad.botones[-1])

        # Boton de Volver a Inicio
        x_boton_volver = (constantes.ELEMENTO_MEDIANO_ANCHO) / 3
        y_boton_volver = (constantes.ALTO_MENU_CNT_J - constantes.ELEMENTO_MEDIANO_ALTO) * (posicion_y+0.3)
        menu_cantidad.crear_elemento(
                Clase=Boton,
                x=x_boton_volver,
                y=y_boton_volver,
                un_juego=self,
                texto="VOLVER",
                ancho=constantes.ELEMENTO_MEDIANO_ANCHO,
                alto=constantes.ELEMENTO_MEDIANO_ALTO,
                tamaño_fuente=constantes.F_MEDIANA,
                fuente=constantes.FUENTE_LLAMATIVA,
                color=constantes.ELEMENTO_FONDO_PRINCIPAL,
                radio_borde=constantes.REDONDEO_NORMAL,
                color_texto=constantes.COLOR_TEXTO_PRINCIPAL,
                color_borde=constantes.ELEMENTO_BORDE_SECUNDARIO,
                grosor_borde=constantes.BORDE_PRONUNCIADO,
                color_borde_hover=constantes.ELEMENTO_HOVER_PRINCIPAL,
                color_borde_clicado=constantes.ELEMENTO_CLICADO_PRINCIPAL,
                accion=lambda: acciones.Mostrar_seccion(menu_cantidad, self.menu_inicio)
        )

        # Boton de confirmar
        x_boton_confirmar = (constantes.ANCHO_MENU_CNT_J - constantes.ELEMENTO_MEDIANO_ANCHO) * 0.8
        y_boton_confirmar = (constantes.ALTO_MENU_CNT_J - constantes.ELEMENTO_MEDIANO_ALTO) * (posicion_y+0.3)
        menu_cantidad.crear_elemento(
                Clase=Boton,
                x=x_boton_confirmar,
                y=y_boton_confirmar,
                un_juego=self,
                texto="CONFIRMAR",
                ancho=constantes.ELEMENTO_MEDIANO_ANCHO,
                alto=constantes.ELEMENTO_MEDIANO_ALTO,
                tamaño_fuente=constantes.F_MEDIANA,
                fuente=constantes.FUENTE_LLAMATIVA,
                color=constantes.ELEMENTO_FONDO_PRINCIPAL,
                radio_borde=constantes.REDONDEO_NORMAL,
                color_texto=constantes.COLOR_TEXTO_PRINCIPAL,
                color_borde=constantes.ELEMENTO_BORDE_SECUNDARIO,
                grosor_borde=constantes.BORDE_PRONUNCIADO,
                color_borde_hover=constantes.ELEMENTO_HOVER_PRINCIPAL,
                color_borde_clicado=constantes.ELEMENTO_CLICADO_PRINCIPAL,
                accion=lambda: acciones.Confirmar_cantidad_jugadores(self,menu_cantidad,self.menu_nombre_usuario)
        )

        return menu_cantidad
    def Menu_nombre_usuario(self):
        
        x_menu,y_menu = self.centrar(constantes.ANCHO_MENU_NOM_USUARIO,constantes.ALTO_MENU_NOM_USUARIO)
        
        menu_nombre_usuario = Menu(
            self,
            constantes.ANCHO_MENU_NOM_USUARIO,
            constantes.ALTO_MENU_NOM_USUARIO,
            x_menu,
            y_menu,
            constantes.ELEMENTO_FONDO_SECUNDARO,
            constantes.ELEMENTO_BORDE_SECUNDARIO,
            constantes.BORDE_PRONUNCIADO,
            constantes.REDONDEO_PRONUNCIADO
        )
        
        ancho_nombre = constantes.ELEMENTO_GRANDE_ANCHO*1.9
        alto_nombre = constantes.ELEMENTO_MEDIANO_ALTO*0.95
        x_nombre = (constantes.ANCHO_MENU_NOM_USUARIO - ancho_nombre)*(0.5)
        y_nombre = (constantes.ALTO_MENU_NOM_USUARIO - alto_nombre)*(0.10)
        menu_nombre_usuario.crear_elemento(
            Clase=Boton,
            x=x_nombre,
            y=y_nombre,
            un_juego=self,
            texto="INGRESA TU NOMBRE",
            ancho=ancho_nombre,
            alto=alto_nombre,
            tamaño_fuente=constantes.F_GRANDE,
            fuente=constantes.FUENTE_ESTANDAR,
            color=constantes.ELEMENTO_FONDO_PRINCIPAL,
            radio_borde=constantes.REDONDEO_NORMAL,
            color_texto=constantes.COLOR_TEXTO_PRINCIPAL,
            color_borde=constantes.ELEMENTO_BORDE_SECUNDARIO,
            grosor_borde=constantes.BORDE_INTERMEDIO,
        )
        ancho_ingresar = constantes.ELEMENTO_GRANDE_ANCHO*1.4
        alto_ingresar = constantes.ELEMENTO_MEDIANO_ALTO*0.88
        x_ingresar = (constantes.ANCHO_MENU_NOM_USUARIO - ancho_ingresar)*(0.5)
        y_ingresar = (constantes.ALTO_MENU_NOM_USUARIO - alto_ingresar)*(0.50)
        menu_nombre_usuario.crear_elemento(
            Clase=EntradaTexto,
            x=x_ingresar,
            y=y_ingresar,
            limite_caracteres = 20,
            un_juego = self,
            texto = "nombre",
            ancho = ancho_ingresar,
            alto = alto_ingresar,
            tamaño_fuente = constantes.F_MEDIANA,
            fuente = constantes.FUENTE_ESTANDAR,
            color = constantes.ELEMENTO_FONDO_PRINCIPAL,
            radio_borde=constantes.REDONDEO_NORMAL,
            color_texto=constantes.COLOR_TEXTO_PRINCIPAL,
        )

        # Boton de Volver a Inicio
        x_boton_volver = (constantes.ANCHO_MENU_NOM_USUARIO - constantes.ELEMENTO_MEDIANO_ANCHO)*0.25
        y_boton_volver = (constantes.ALTO_MENU_NOM_USUARIO - constantes.ELEMENTO_MEDIANO_ALTO) * 0.8
        menu_nombre_usuario.crear_elemento(
                Clase=Boton,
                x=x_boton_volver,
                y=y_boton_volver,
                un_juego=self,
                texto="VOLVER",
                ancho=constantes.ELEMENTO_MEDIANO_ANCHO,
                alto=constantes.ELEMENTO_MEDIANO_ALTO,
                tamaño_fuente=constantes.F_MEDIANA,
                fuente=constantes.FUENTE_LLAMATIVA,
                color=constantes.ELEMENTO_FONDO_PRINCIPAL,
                radio_borde=constantes.REDONDEO_NORMAL,
                color_texto=constantes.COLOR_TEXTO_PRINCIPAL,
                color_borde=constantes.ELEMENTO_BORDE_SECUNDARIO,
                grosor_borde=constantes.BORDE_PRONUNCIADO,
                color_borde_hover=constantes.ELEMENTO_HOVER_PRINCIPAL,
                color_borde_clicado=constantes.ELEMENTO_CLICADO_PRINCIPAL,
                accion=lambda: acciones.Mostrar_seccion(menu_nombre_usuario, self.menu_Cantidad_Jugadores)
        )
        
        x_boton_confirmar = (constantes.ANCHO_MENU_NOM_USUARIO - constantes.ELEMENTO_MEDIANO_ANCHO)*0.8
        y_boton_confirmar = (constantes.ALTO_MENU_NOM_USUARIO - constantes.ELEMENTO_MEDIANO_ALTO) * 0.8
        menu_nombre_usuario.crear_elemento(
                Clase=Boton,
                x=x_boton_confirmar,
                y=y_boton_confirmar,
                un_juego=self,
                texto="CONFIRMAR",
                ancho=constantes.ELEMENTO_MEDIANO_ANCHO,
                alto=constantes.ELEMENTO_MEDIANO_ALTO,
                tamaño_fuente=constantes.F_MEDIANA,
                fuente=constantes.FUENTE_LLAMATIVA,
                color=constantes.ELEMENTO_FONDO_PRINCIPAL,
                radio_borde=constantes.REDONDEO_NORMAL,
                color_texto=constantes.COLOR_TEXTO_PRINCIPAL,
                color_borde=constantes.ELEMENTO_BORDE_SECUNDARIO,
                grosor_borde=constantes.BORDE_PRONUNCIADO,
                color_borde_hover=constantes.ELEMENTO_HOVER_PRINCIPAL,
                color_borde_clicado=constantes.ELEMENTO_CLICADO_PRINCIPAL,
                accion=lambda: acciones.Crear_sevidor(self,menu_nombre_usuario)
        )
    
        return menu_nombre_usuario
    
    """Boton de salir del juego"""
    def salir(self):
        pygame.quit()
        sys.exit()

    """Funciones auxiliares para el ciclo principal del juego"""
    def ejecutar_manejo_eventos(self, evento):
        # Solo el botón jugar si está visible
        if self.boton_jugar.visible:
            self.boton_jugar.manejar_evento(evento)
        
        # Solo procesar eventos de menús visibles
        if self.menu_instrucciones.visible:
            self.menu_instrucciones.manejar_eventos(evento)
        if self.menu_inicio.visible:
            self.menu_inicio.manejar_eventos(evento)
        if self.menu_Cantidad_Jugadores.visible:
            self.menu_Cantidad_Jugadores.manejar_eventos(evento)
        if self.menu_nombre_usuario.visible:
            self.menu_nombre_usuario.manejar_eventos(evento)

    def ejecutar_verificacion_hovers(self, posicion_raton):
        # Solo verificar hovers en elementos visibles
        if self.boton_jugar.visible:
            self.boton_jugar.verificar_hover(posicion_raton)
        if self.menu_instrucciones.visible:
            self.menu_instrucciones.verificar_hovers(posicion_raton)
        if self.menu_inicio.visible:
            self.menu_inicio.verificar_hovers(posicion_raton)
        if self.menu_Cantidad_Jugadores.visible:
            self.menu_Cantidad_Jugadores.verificar_hovers(posicion_raton)
        if self.menu_nombre_usuario.visible:
            self.menu_nombre_usuario.verificar_hovers(posicion_raton)
        
    def ejecutar_dibujado(self):
        self.boton_jugar.dibujar()
        self.menu_instrucciones.dibujar_menu()
        self.menu_inicio.dibujar_menu()
        self.menu_Cantidad_Jugadores.dibujar_menu()
        self.menu_nombre_usuario.dibujar_menu()
    
    def inicializar_mazo(self): #a ver si esto funciona
        print("Cartas encontradas:", list(self.imagenes_cartas.keys()))  # Depuración
        for nombre_carta in self.imagenes_cartas.keys():
            self.mazo.agregar_cartas(nombre_carta)
        print("Cartas en el mazo:", len(self.mazo.cartas))  # Depuración
        self.mazo.revolver_mazo()

    def Correr_juego(self): # aqui lo modifique para probar mesa directamete
        ejecutar = True
        mesa = Mesa(self.pantalla, 6)  #el numero son el de los jugadores
        while ejecutar:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    ejecutar = False

            self.pantalla.fill(constantes.VERDE)  # Fondo verde de mesa 
            mesa.dibujar()  # Dibuja la mesa y las cartas

            pygame.display.flip()
            self.clock.tick(constantes.FPS)
        pygame.quit() 
    # def Correr_juego(self):
      #  ejecutar = True
      #  while ejecutar:
      #      posicion_raton = pygame.mouse.get_pos()
     #       eventos = pygame.event.get()

     #       for evento in eventos:
      #          if(evento.type == pygame.QUIT):
     #               ejecutar = False
     #           self.ejecutar_manejo_eventos(evento)
#
     #       
     #       self.ejecutar_verificacion_hovers(posicion_raton)
     #       
     #       self.pantalla.fill(constantes.FONDO_VENTANA)

     #       self.ejecutar_dibujado()
#
      #      pygame.display.flip()
     #       self.clock.tick(constantes.FPS)
    #    pygame.quit()


ventana = Ventana()
ventana.Correr_juego()