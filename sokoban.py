class sokoban:

    personaje= 0
    espacio = 1
    caja = 2
    meta = 3
    pared = 4
    personaje_meta = 5
    caja_meta = 6

    mapa =[]

    perosnaje_fila = 0
    personaje_columna = 0

    def __init__(self):
        pass

    def leerMapa(self):
        self.mapa = [
            [3,3,3,3,3,3,3,3,3],
            [3,1,1,1,1,1,1,1,3],
            [3,1,1,0,1,4,1,3,3],
            [3,1,1,1,1,1,1,1,3],
            [3,1,1,1,1,1,1,1,3],
            [3,3,3,3,3,3,3,3,3]
        ]
        self.perosnaje_fila = 3
        self.personaje_columna = 5

    def imprimirMapa (self):
        for fila in self.mapa:
            print(fila)

    def moverderecha(self):
        print("mover derecha")

        # 5. personaje, espacio
        if (self.mapa[self.perosnaje_fila][self.personaje_columna] == self.personaje and              self.mapa[self.personaje_fila][self.personaje_columna + 1] ==self.espacio):

            self.mapa[self.perosnaje_fila][self.personaje_columna] = self.espacio
            self.mapa[self.perosnaje_fila][self.personaje_columna + 1] = self.personaje
            self.perosnaje_columna += 1
        # 6. peronaje, meta
        elif (self.mapa[self.personaje_fila][self.perosnaje_columna] == 0
        and self.mapa[self.perosnaje_fila][self.perosnaje_columna + 1] == 4):

            self.mapa[self.perosnaje_fila][self.perosnaje_columna] = 1
            self.mapa[self.perosnaje_fila][self.perosnaje_columna + 1] = 5
            self.perosnaje_columna += 1

    def moverizquierda(self):
        print("mover izquierda")

    def moverarriba(self):
        print("mover arriba")

    def moverabajo(self):
        print("mover abajo")

    def jugar(self):
        instrucciones = "a-izquierda\nd-derecha\nw-arriba\ns-abajo"
        print(instrucciones)
        self.leerMapa()
        while True:
            self.imprimirMapa()
            movimiento = input("mover hacia:")
            if movimiento == "d":
                self.derecha()
            elif movimiento == "a":
                self.moverizquierda()
            elif movimiento == "w":
                self.movimientoarriba()
            elif movimiento == "s":
                self.movimientoabajo()
            elif movimiento == "q":
                print("salir del juego")
                break


juego = sokoban()
juego.jugar()


        
            

        
       





        
            

        