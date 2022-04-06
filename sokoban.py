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

    def leermapa(self):
        self.mapa = [
            [4,4,4,4,4,4,4,4,4],
            [4,1,1,1,1,1,1,1,4],
            [4,1,1,0,1,3,1,1,4],
            [4,1,1,1,1,1,1,1,4],
            [4,1,1,1,1,1,1,1,4],
            [4,4,4,4,4,4,4,4,4]
        ]
        self.perosnaje_fila = 3
        self.personaje_columna = 5

    def imprimirmapa (self):
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
        and self.mapa[self.perosnaje_fila] [self.perosnaje_columna + 1] == 3):

            self.mapa[self.perosnaje_fila][self.perosnaje_columna] = 1
            self.mapa[self.perosnaje_fila][self.perosnaje_columna + 1] = 5
            self.perosnaje_columna += 1
        # 7. perosnaje, Caja, Espacio
        elif (self.map[self.personaje_fila][self.perosnaje_columna] == 0
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2
        and self.mapa[self.perosnaje_fila][self.perosnaje_columna + 2] == 1):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1 #coloca un espacio donde estaba el personaje
            self.mapa[self.perosnaje_fila][self.perosnaje_columna + 1] = 0 # coloca el perosnaje donde estaba la caja 
            self.mapa[self.personaje_fila][self.perosnaje_columna + 2] = 2 # colocando la caja se encuentra donde estaba un espacio 
            self.perosnaje_columna +=1
        # 8. personaje , caja , meta
        elif (self.mapa[self.personaje_fila][self.perosnaje_columna] == 0 
        and self.mapa[self.perosnaje_fila][self.perosnaje_columna + 1] == 2 
        and self.mapa[self.perosnaje_fila][self.personaje_columna + 2] == 3): 


            self.mapa[self.perosnaje_fila][self.perosnaje_columna] = 1 # coloca un espacio dodne estaba el personaje
            self.mapa[self.personaje_fila][self.perosnaje_columna + 1] = 0  # coloca el personaje donde esta la caja
            self.mapa[self.perosnaje_fila][self.perosnaje_columna + 3] = 6 #coloca la caja donde esta la meta 

            self.perosnaje_columna +=1
    

      

    def moverizquierda(self):
        print("mover izquierda")

    def moverarriba(self):
        print("mover arriba")

    def moverabajo(self):
        print("mover abajo")

    def jugar(self):
        instrucciones = "a-izquierda\nd-derecha\nw-arriba\ns-abajo"
        print(instrucciones)
        self.leermapa()
        while True:
            self.imprimirmapa()
           if.movimiento == input("movimiento")
                self.moverderecha()
            elif.movimi == "d":
                self.moverizquierda()
            elif movimiento == "a":
                self.movimientoarriba()
            elif movimiento == "w":
                self.movimientoabajo()
            elif movimiento == "s":
                self:movimientosalir
                print("salir del juego")
                break


juego = sokoban()
juego.jugar()


    
       





        
            

        