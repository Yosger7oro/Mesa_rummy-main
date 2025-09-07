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

        for idx, carta in enumerate(self.mano):
            if carta in imagenes_cartas:
                # Si es el jugador 1 (índice 0), tamaño normal y separación normal
                if self.nro_jugador == 1:
                    carta_img = pygame.transform.scale(imagenes_cartas[carta], (60, 90))
                    pantalla.blit(carta_img, (x + idx*70, y))
                else:
                    # Cartas más pequeñas y superpuestas (50%)
                    carta_img = pygame.transform.scale(imagenes_cartas[carta], (40, 60))
                    pantalla.blit(carta_img, (x + idx*20, y))
            else:
                # Si no hay imagen, dibuja un rectángulo
                if self.nro_jugador == 1:
                    pygame.draw.rect(pantalla, (255,255,255), (x + idx*70, y, 60, 90))
                else:
                    pygame.draw.rect(pantalla, (255,255,255), (x + idx*20, y, 40, 60))