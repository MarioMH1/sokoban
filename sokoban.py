class sokoban:

    personaje= 0
    espacio = 1
    caja = 2
    meta = 3
    pared = 4
    personaje_meta = 5
    caja_meta = 6

    mapa =[]

    personaje_fila = 0
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
        self.personaje_fila = 2
        self.personaje_columna = 3

    def imprimirmapa (self):
        for fila in self.mapa:
            print(fila)

    def moverderecha(self):
        print("mover derecha")

        #Movimientos Derecha

        # 5. personaje, espacio
        if (self.mapa[self.personaje_fila][self.personaje_columna] == 0  
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] =  0
            self.personaje_columna += 1
            print("personaje,espacio")
      

      

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
            movimiento = input("mover hacia:")
            if movimiento == "d":
                self.moverderecha()
                

juego = sokoban()
juego.jugar()


    
       





        
            

        