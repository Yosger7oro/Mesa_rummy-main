import pygame

"""Accion que se ejecuta al presionar un boton de la ventana"""
def Mostrar_seccion(seccion_ocultar,seccion_mostrar):
    seccion_ocultar.ocultar()
    # pygame.time.delay(500)
    seccion_mostrar.mostrar()

def Como_jugar():
    print("explicando como jugar...")

def Confirmar_cantidad_jugadores(un_juego,menu_ocultar,menu_mostrar):
    """Recorremos todos los botones del menu, y verificamos que el boton tenga el atributo "valor" y el "seleccionado" con hasattr, luego verificamos si efectivamente el boton esta seleccionado"""
    for boton in menu_ocultar.botones:
        if hasattr(boton, 'valor') and hasattr(boton, 'seleccionado'):
            if boton.seleccionado:
                un_juego.lista_elementos["cantidad_jugadores"] = boton.valor
    print(un_juego.lista_elementos["cantidad_jugadores"])
    Mostrar_seccion(menu_ocultar,menu_mostrar)

def Crear_sevidor(un_juego,menu):
    for boton in menu.botones:
        if hasattr(boton, 'valor'):
            if boton.valor != "" and boton.valor is not None:
                un_juego.lista_elementos["nombre_creador"] = boton.valor
    print("Creando servidor...")
    print(un_juego.lista_elementos["nombre_creador"])

def Unirse_sala(menu_ocultar,menu_mostrar):
    menu_ocultar.ocultar()
    menu_mostrar.mostrar()
    print("uniendose...")