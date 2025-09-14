class Jugador:
    def __init__(self, nro, nombre):
        self.nro_jugador = nro
        self.nombre_jugador = nombre
        self.primera_jugada_hecha = False

'''
Clase jugador vieja
- Nelson

import pygame
class Jugador:
    def __init__(self, nro, nombre, mano):
        self.nro_jugador = nro
        self.nombre_jugador = nombre
        self.primera_jugada_hecha = False
        self.mano = mano

    def dibujar(self, pantalla, x, y, imagenes_cartas):
        fuente = pygame.font.SysFont(None, 28)
        texto = fuente.render(self.nombre_jugador, True, (255,255,255))
        pantalla.blit(texto, (x, y - 30))  # Muestra el nombre encima de las cartas

        self.cartas_rects = [] # Guarda los racts de las cartas

        for idx, carta in enumerate(self.mano):
            if carta in imagenes_cartas:
                # Si es el jugador 1 (índice 0), tamaño normal y separación normal
                if self.nro_jugador == 1:
                    carta_img = pygame.transform.scale(imagenes_cartas[carta], (60, 90))
                    pos = (x + idx*70, y)
                    pantalla.blit(carta_img, (x + idx*70, y))
                    rect = pygame.Rect(pos, (60, 90))
                else:
                    # Cartas más pequeñas y superpuestas (50%)
                    carta_img = pygame.transform.scale(imagenes_cartas[carta], (40, 60))
                    post = (x + idx*20, y)
                    pantalla.blit(carta_img, (x + idx*20, y))
                    rect = pygame.Rect(post, (40, 60))
            else:
                # Si no hay imagen, dibuja un rectángulo
                if self.nro_jugador == 1:
                    pos = (x + idx*70, y)
                    pygame.draw.rect(pantalla, (255,255,255), (pos[0], pos[1], 60, 90))
                    rect = pygame.Rect(pos, (60, 90))
                else:
                    pos = (x + idx*20, y)
                    pygame.draw.rect(pantalla, (255,255,255), (pos[0], pos[1], 40, 60))
                    rect = pygame.Rect(pos, (40, 60))
            self.cartas_rects.append((rect, carta))  # Guarda el rect y la carta correspondiente'''  