
# ahorcado.py
from tablero import Tablero
from jugador import Jugador

class Ahorcado:
    @staticmethod
    def jugar():
        archivo_palabras = "palabras.json"
        palabra_a_adivinar = Jugador.seleccionar_palabra(archivo_palabras)
        huecos = ["_" for _ in palabra_a_adivinar]
        errores = 0

        Tablero.dibujar_muneco(errores)

        while "_" in huecos and errores < 6:
            Jugador.pintar_palabra(huecos)
            huecos, errores = Jugador.introducir_letra(palabra_a_adivinar, huecos, errores)
            Tablero.dibujar_muneco(errores)

        if errores == 6:
            print("Game over 💀")
        else:
            print("¡Felicidades! :D")

if __name__ == "__main__":
    Ahorcado.jugar()



