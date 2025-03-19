import random
import json

class Jugador:
    @staticmethod
    def pintar_palabra(huecos):
    # Muestra en la pantalla la palabra con espacios en blanco
        
        print(" ".join(huecos))

    @staticmethod
    def introducir_letra(palabra_a_adivinar, huecos, errores):
    
    # Permite al jugador introducir una letra y actualiza la lista de huecos y el contador de errores
        letra_introducida = input("Introduce tu letra: ")
        
        posicion = palabra_a_adivinar.find(letra_introducida)
        
        if posicion == -1:
            print("Lo siento no está la letra :c")
            errores += 1
        else:
            
            for i, letra in enumerate(palabra_a_adivinar):
                
                if letra == letra_introducida:
                    huecos[i] = letra
        return huecos, errores

    @staticmethod
    def seleccionar_palabra(archivo_palabras):
        with open(archivo_palabras, 'r') as archivo:
            datos = json.load(archivo)
            palabras = datos.get('palabras', [])

        return random.choice(palabras)