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
            [4,1,1,0,1,1,1,3,4],
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
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 3):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.personaje_columna += 1
            print("personaje,meta")

        # 7. personaje , caja , espacio
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2
        and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 1):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 2
            self.personaje_columna += 1
            print("personaje,caja,espacio")

        # 8. personaje, caja , meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2
        and self.mapa[self.personaje_fila][self.personaje_columna + 3] == 4):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
            self.personaje_columna += 1
            print("personaje,caja,meta")


        # 9. personaje ,caja_meta , espacio
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 2
            self.personaje_columna *= 1
            print("personaje , caja_meta, meta")

        # 10. persoanje , caja_meta , meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
            self.personaje_columna += 1
            print("personaje , caja_meta, meta")

        # 11. personaje_meta, espacio
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5
        and self.mapa[self.persoanje_fila][self.persoanje_columna +1] == 1):

            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.persoanje_fila][self.personaje_columna + 1] = 0
            self.persoanje_columna += 1
            print("persoanje_meta , espacio")

        # 12.  persoanje_meta, meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4):

            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.persoanje_columna += 1
            print("persoanje_meta, meta")

        # 13. personaje_meta ,caja ,espacio
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5
        and self.mapa[self.personaje_fila][self.personaje_columna] == 2
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1):

            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna] = 0
            self.mapa[self.perosnaje_fila][self.personaje_columna + 1] = 2
            self.persoanje_columna += 1
            print("personaje_meta , caja ,espacio")

         # 14 . personaje_meta , caja , meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5
        and self.mapa[self.personaje_fila][self.personaje_columna] == 2
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4):

            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.persoanje_fila][self.personaje_columna] = 0
            self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6
            self.personaje_columna += 1
            print("personaje_meta , caja ,meta")

        # 15. personaje_meta , caja , espacio 
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5
        and self.mapa[self.personaje_fila][self.personaje_columna] == 6
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1):

            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna] = 5
            self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2
            self.personaje_columna += 1
            print("personaje_meta ,caja ,espacio")

        # 16. personaje_meta , caja_meta , meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5
        and self.mapa[self.personaje_fila][self.personaje_columna] == 6
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4):

            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna] = 5
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 6
            print("perosnaje_meta , caja_meta , meta")

        #Movimientos Izquierda
            
        # 17. personaje, espacio
        if (self.mapa[self.personaje_fila][self.personaje_columna] == 0  
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] =  0
            self.personaje_columna += 1
            print("personaje,espacio")

        # 6. personaje, meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 3):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.personaje_columna += 1
            print("personaje,meta")

        # 7. personaje , caja , espacio
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2
        and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 1):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 2
            self.personaje_columna += 1
            print("personaje,caja,espacio")

        # 8. personaje, caja , meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2
        and self.mapa[self.personaje_fila][self.personaje_columna +  2] == 4):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
            self.personaje_columna += 1
            print("personaje,caja,meta")


        # 9. personaje ,caja_meta , espacio
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 2
            self.personaje_columna *= 1
            print("personaje , caja_meta, meta")

        # 10. persoanje , caja_meta , meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
            self.personaje_columna += 1
            print("personaje , caja_meta, meta")

        # 11. personaje_meta, espacio
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5
        and self.mapa[self.persoanje_fila][self.persoanje_columna +1] == 1):

            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.persoanje_fila][self.personaje_columna + 1] = 0
            self.persoanje_columna += 1
            print("persoanje_meta , espacio")

        # 12.  persoanje_meta, meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4):

            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.persoanje_columna += 1
            print("persoanje_meta, meta")

        # 13. personaje_meta ,caja ,espacio
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5
        and self.mapa[self.personaje_fila][self.personaje_columna] == 2
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1):

            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna] = 0
            self.mapa[self.perosnaje_fila][self.personaje_columna + 1] = 2
            self.persoanje_columna += 1
            print("personaje_meta , caja ,espacio")

         # 14 . personaje_meta , caja , meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5
        and self.mapa[self.personaje_fila][self.personaje_columna] == 2
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4):

            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.persoanje_fila][self.personaje_columna] = 0
            self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6
            self.personaje_columna += 1
            print("personaje_meta , caja ,meta")

        # 15. personaje_meta , caja , espacio 
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5
        and self.mapa[self.personaje_fila][self.personaje_columna] == 6
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1):

            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna] = 5
            self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2
            self.personaje_columna += 1
            print("personaje_meta ,caja ,espacio")

        # 16. personaje_meta , caja_meta , meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5
        and self.mapa[self.personaje_fila][self.personaje_columna] == 6
        and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4):

            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna] = 5
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 6
            print("perosnaje_meta , caja_meta , meta")
            
            




















    
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


    
       





        
            

        