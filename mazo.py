from random import sample, shuffle
class Mazo:
    def __init__(self):
        self.cartas = []
    def agregar_cartas(self,carta):
        self.cartas.append(carta)
    def calcular_nro_mazos(self,numero_de_jugadores):
        resultado = numero_de_jugadores // 3  
        if numero_de_jugadores % 3 != 0:
            resultado += 1
        return resultado
    def revolver_mazo(self):
        shuffle(self.cartas)

    def mostrar_cartas(self,mensaje):
        print(mensaje)
        for carta in self.cartas:
            print(carta)
    def mostrar_numero_cartas(self,mensaje):
        print(str(mensaje) + str(len(self.cartas)))

    def repartir_cartas(self, lista_de_jugadores):    #solo para pruebass de interfaz
        num_jugadores = len(lista_de_jugadores)
        print(f"Número de jugadores: {num_jugadores}")
        print(f"Cartas a repartir: {10 * num_jugadores}")
        print(f"Cartas disponibles en el mazo: {len(self.cartas)}")

        if 10 * num_jugadores > len(self.cartas):
            raise ValueError("¡Error! No hay suficientes cartas en el mazo para repartir a los jugadores.")

        cartas_indice_repartidas = sample(list(enumerate(self.cartas)), 10 * num_jugadores)
        cartas_repartidas = []
        indice_de_cartas_eliminar = []
        for x in cartas_indice_repartidas:
            cartas_repartidas.append(x[1])
            indice_de_cartas_eliminar.append(x[0])
        jugadores = [[] for _ in range(num_jugadores)]
        for index, carta in enumerate(cartas_repartidas):
            indice_de_jugador = index % num_jugadores
            jugadores[indice_de_jugador].append(carta)

        for indice in sorted(indice_de_cartas_eliminar, reverse=True):
            self.cartas.pop(indice)

        return jugadores