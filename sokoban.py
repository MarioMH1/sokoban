class sokoban:

    personaje= 0
    espacio = 1
    caja = 2
    meta = 3
    pared = 4
    personaje_meta = 5
    caja_meta = 6

    mapa =[]


    def __init__(self):
        pass

    def leermapa(self):
        self.mapa = [
            [4,4,4,4,4,4,4,4,4,4,4,4],
            [4,1,1,1,1,3,1,1,1,1,1,4],
            [4,1,1,1,1,1,1,1,1,1,1,4],
            [4,1,1,1,1,2,1,1,1,1,1,4],
            [4,3,1,2,1,0,1,1,2,1,3,4],
            [4,1,1,1,1,1,1,1,1,1,1,4],
            [4,1,1,1,1,2,1,1,1,1,1,4],
            [4,1,1,1,1,3,1,1,1,1,3,4],
            [4,4,4,4,4,4,4,4,4,4,4,4]
        ]
        self.personaje_fila = 4
        self.personaje_columna = 5

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

    
    def moverizquierda(self):
        print("mover izquierda")

        #Mover Izquierda


        # 17. personaje , espacio
        if (self.mapa[self.personaje_fila][self.personaje_columna] == 0  
        and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna - 1] =  0
            self.personaje_columna -= 1
            print("personaje,espacio")

        # 18. personaje , meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0
        and self.mapa[self.personaje_fila][self.personaje_columna -1] == 3):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje -1] = 5
            self.persoanje_columna -= 1
            print("personaje , meta")

        # 19. personaje , caja , espacio
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0
        and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 2
        and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 1):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 2
            self.personaje_columna -= 1
            print("personaje,caja,espacio")

        # 20. personaje , caja , meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0
        and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 2
        and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 3):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
            self.personaje_columna -= 1
            print("personaje , caja ,meta")

        # 21. perosnaje ,  caja_meta , espacio 
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0
        and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6
        and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 1):

            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
            self.personaje_columna -= 1
            print("personaje , caja_meta , espacio")

        # 22. personaje , caja_meta , meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0
        and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 5
        and self.mapa[self.personaje_fila][self.personaje_columna - 2] ==3):


            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 6
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 3
            self.personaje_columna -= 1
            print("personaje , caja_meta , meta")

        # 23. personaje_meta ,espacio 
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5
        and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1):

            
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.persoanje_columna -= 1
            print("personaje , espacio")

        # 24. personaje_meta , meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 6
        and self.mapa[self.personaje_columna][self.personaje_columna - 1] == 3):

            
            self.mapa[self.personaje_fila][self.personaje_columna] = 5
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 3
            self.personaje_columna -= 1
            print("personaje_meta , meta")

        # 25.personaje_meta , caja ,espacio
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5
        and self.mapa[self.personaje_fila][self.personaje_columna -  1] == 2
        and self.mapa[self.persona_fila][self.personaje_fila - 2] == 1):

            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 2
            self.personaje_columna -=1
            print("personaje_meta , caja ,espacio")

        # 26.personaje_meta , caja , meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5
        and self.mapa[self.personaje_fila][self.personaje_columna -  1] == 2
        and self.mapa[self.persona_fila][self.personaje_fila - 2] == 3):

            self.mapa[self.personaje_fila][self.personaje_columna] = 5
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 2
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
            self.personaje_columna -=1
            print("personaje_meta , caja ,espacio")

        # 27.personaje_meta , caja_meta , espacio
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5
        and self.mapa[self.personaje_fila][self.personaje_columna -  1] == 6
        and self.mapa[self.persona_fila][self.personaje_fila - 2] == 1):

            self.mapa[self.personaje_fila][self.personaje_columna] = 5
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 6
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
            self.personaje_columna -=1
            print("personaje_meta , caja ,espacio")

        # 28.personaje_meta , caja_meta , meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5
        and self.mapa[self.personaje_fila][self.personaje_columna -  1] == 6
        and self.mapa[self.persona_fila][self.personaje_fila - 2] == 3):

            self.mapa[self.personaje_fila][self.personaje_columna] = 5
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 3
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
            self.personaje_columna -=1
            print("personaje_meta , caja ,espacio")
    



    def moverarriba(self):
        print("mover arriba")


        # Mover Arriba

        # 29. espacio , personaje
        if (self.mapa[self.personaje_fila][self.personaje_columna] == 0  and             self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1):        
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila -1][self.personaje_columna] =  0
            self.personaje_fila -= 1
            print("personaje,espacio")

            
        # 30. meta , personaje
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 3 and         
        self.mapa[self.personaje_fila - 1] [self.personaje_columna] == 0):
            
            self.mapa[self.personaje_fila][self.personaje_columna] = 5
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 1
            self.personaje_fila -= 1
            print("meta , personaje")

            
        # 31. espacio, caja , personaje
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0
        and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 2 and 
        self.mapa[self.personaje_fila - 2][self.personaje_columna] == 1):
            
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 2
            self.personaje_fila -= 1
            print("espacio , caja ,personaje")


        # 32. meta , caja , personaje
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0
        and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 2
        and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 3):
            self.mapa[self.personaje_fila][self.personaje_columna]= 1
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
            self.personaje_fila -= 1
            print("meta ,caja ,personaje")


        # 33. espacio , caja_meta , personaje
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 0
        and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6
        and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 1):
            self.mapa[self.personaje_fila][self.personaje_columna]= 2
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
            self.personaje_fila -= 1
            print("meta ,caja ,personaje")


        # 34. meta , caja_meta , personaje
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 3
        and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6
        and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 0):
            self.mapa[self.personaje_fila][self.personaje_columna]= 6
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
            self.personaje_fila -= 1
            print("meta ,caja ,personaje")


        # 35. espacio, personaje_meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5
        and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1):
            self.mapa[self.personaje_fila][self.personaje_columna]= 1
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.personaje_fila -= 1
            print("meta ,caja ,personaje")


        # 36. meta , personaje_meta 
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5
        and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 3):
            self.mapa[self.personaje_fila][self.personaje_columna]= 3
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.personaje_fila -= 1
            print("meta ,caja ,personaje")

            
        # 37. espacio , caja , personaje_meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5
        and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 2
        and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 1):

            self.mapa[self.personaje_fila][self.personaje_columna]= 2
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 3
            self.personaje_fila -= 1
            print("meta ,caja ,personaje")

        # 38. meta, caja , personaje_meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 3
        and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 2
        and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 5):

            self.mapa[self.personaje_fila][self.personaje_columna]= 6
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 3
            self.personaje_fila -= 1
            print("meta ,caja ,personaje")


        # 39. espacio , caja_meta , personaje_meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5
        and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6
        and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 1):

            self.mapa[self.personaje_fila][self.personaje_columna]= 2
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 3
            self.personaje_fila -= 1
            print("meta ,caja ,personaje")


        # 40. meta , caja_meta , personaje_meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 5
        and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6
        and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 3):

            self.mapa[self.personaje_fila][self.personaje_columna]= 6
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 3
            self.personaje_fila -= 1
            print("meta ,caja ,personaje")
            
            
    def moverabajo(self):
        print("mover abajo")

        #Mover Abajo


        # 41. personaje , espacio
        if (self.mapa[self.personaje_fila][self.personaje_columna] == 0
        and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1):
        
            self.mapa[self.personaje_fila][self.personaje_columna]= 1
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            self.personaje_fila += 1
            print("meta ,caja ,personaje")


            
        # 42. personaje, meta 
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 1
        and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 3):
        
            self.mapa[self.personaje_fila][self.personaje_columna]= 1
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
            self.personaje_fila += 1
            print("meta ,caja ,personaje")


        # 43. personaje , caja , espacio
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 1
        and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 2
        and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 0):

            self.mapa[self.personaje_fila][self.personaje_columna]= 1
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 2
            self.personaje_fila += 1
            print("meta ,caja ,personaje")


        # 44. personaje , caja , meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 3
        and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 2
        and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 0):

            self.mapa[self.personaje_fila][self.personaje_columna]= 1
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
            self.personaje_fila += 1
            print("meta ,caja ,personaje")


         # 45. personaje , caja_meta , espacio
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 1
        and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 5
        and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 0):

            self.mapa[self.personaje_fila][self.personaje_columna]= 1
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 2
            self.personaje_fila += 1
            print("meta ,caja ,personaje")

        # 46. personaje , caja_meta , meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 3
        and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6
        and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 1):

            self.mapa[self.personaje_fila][self.persoanje_columna] = 1
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila + 2][self.persoanje_columna] =  6
            self.personaje_fila += 1
            print("personaje , caja_meta , meta")


        # 47. personaje_meta  , espacio
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 1
        and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 5):
        
            self.mapa[self.personaje_fila][self.personaje_columna]= 3
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            self.personaje_fila += 1
            print("meta ,caja ,personaje")

        
        # 48. personaje_meta  , meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 3
        and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 5):
        
            self.mapa[self.personaje_fila][self.personaje_columna]= 5
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 3
            self.personaje_fila += 1
            print("meta ,caja ,personaje")


        # 49. personaje_meta  , caja , espacio
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 1
        and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 2
        and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 5):
        
            self.mapa[self.personaje_fila][self.personaje_columna]= 3
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 2
            self.personaje_fila += 1
            print("meta ,caja ,personaje")


            
        # 50. personaje_meta  , caja , meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 3
        and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 2
        and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 5):
        
            self.mapa[self.personaje_fila][self.personaje_columna]= 3
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 5
            self.personaje_fila += 1
            print("meta ,caja ,personaje")



        # 51. personaje_meta  , caja_meta , espacio
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 1
        and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6
        and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 5):
        
            self.mapa[self.personaje_fila][self.personaje_columna]= 3
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 2
            self.personaje_fila += 1
            print("meta ,caja ,personaje")


        
        # 52. personaje_meta  , caja_meta , Meta
        elif (self.mapa[self.personaje_fila][self.personaje_columna] == 3
        and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6
        and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 5):
        
            self.mapa[self.personaje_fila][self.personaje_columna]= 3
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
            self.personaje_fila += 1
            print("meta ,caja ,personaje")
        

    def jugar(self):
        instrucciones = "a-izquierda\nd-derecha\nw-arriba\ns-abajo"
        print(instrucciones)
        self.leermapa()
        while True:
            self.imprimirmapa()
            movimiento = input("mover hacia:")
            if movimiento == "d":
                self.moverderecha()
            elif movimiento == "a":
                self.moverizquierda()
            elif movimiento == "w":
                self.moverarriba()
            elif movimiento == "s":
                self.moverabajo()
            


            
juego = sokoban()
juego.jugar()


    
       





        
            

        