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

        # 6. personaje, meta
        if (self.mapa[self.personaje_fila][self.personaje_columna] == 0
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 3):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.personaje_columna += 1
            print("personaje,meta")

        # 7. personaje , caja , espacio
        if (self.mapa[self.personaje_fila][self.personaje_columna] == 0
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2
        and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 1):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 2
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
            self.personaje_columna += 1
            print("personaje,caja,espacio")

        # 8. personaje, caja , meta
        if (self.mapa[self.personaje_fila][self.personaje_columna] == 0
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2
        and self.mapa[self.personaje_fila][self.personaje_columna +  2] == 3):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 3
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
            self.personaje_columna += 1
            print("personaje,caja,meta")


        # 9. personaje ,caja_meta , espacio
        if (self.mapa[self.personaje_fila][self.personaje_columna] == 0
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
            self.personaje_columna *= 1
            print("personaje , caja_meta, meta")

        # 10. persoanje , caja_meta , meta
        if (self.mapa[self.personaje_fila][self.personaje_columna] == 0
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 3):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
            self.personaje_columna += 1
            print("personaje , caja_meta, meta")

        # 11. personaje_meta, espacio
        if (self.mapa[self.personaje.fila][self.personaje_columna] == 5
        and self.mapa[self.persoanje_fila][self.persoanje_columna +1] == 1):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.persoanje_fila][self.personaje_columna + 1] = 1
            self.persoanje_columna += 1
            print("persoanje_meta , espacio")

        # 12.  persoanje_meta, meta
        if (self.mapa[self.persoanje_fila][self.persoanje_columna] == 5
        and self.mapa[self.persoanje_fila][self.persoanje_columna + 1] == 3):

            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 3
            self.persoanje_columna += 1
            print("persoanje_meta, meta")

        # 13. personaje_meta ,caja ,espacio
        if (self.mapa[self.persoanje_fila][self.perosnaje_columna] == 5
        and self.mapa[self.personaje_fila][self.persoanje_columna] == 2
        and self.mapa[self.persoanje_fila][self.persoanje_columna + 1] == 1):

            self.mapa[self.personaje_fila][self.persoanje_columna] = 1
            self.mapa[self.personaje_fila][self.persoanje_columna] = 2
            self.mapa[self.perosnaje_fila][self.persoanje_columna + 1] =1
            self.persoanje_columna += 1
            print("personaje_meta , caja ,espacio")

        # 14 . personaje_meta , caja , meta

            

            
            
        
        
        



    
            

      

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


    
       





        
            

        