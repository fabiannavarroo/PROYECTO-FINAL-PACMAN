import pyxel

def setup_melody():
    # Frase 1: "We wish you a Merry Christmas"
    pyxel.sound(0).set(
        note="G3E3F3G3G3G3F3E3",  # Notas principales
        tone="T",                # Triángulo
        volume="4",              # Volumen
        effect="N",              # Sin efecto
        speed=10                 # Velocidad
    )

    # Frase 2: "And a Happy New Year"
    pyxel.sound(1).set(
        note="A3F3G3A3B3B3C4",   # Notas principales
        tone="T",
        volume="4",
        effect="N",
        speed=10
    )

    # Frase 3: Final repetitivo
    pyxel.sound(2).set(
        note="C4B3A3G3",         # Final
        tone="T",
        volume="4",
        effect="N",
        speed=15
    )

def play_melody():
    # Reproducir las frases en secuencia
    pyxel.play(0, [0, 1, 2], loop=True)  # Reproducir en bucle

class App:
    def __init__(self):
        pyxel.init(160, 120, title="Merry Christmas Melody")
        setup_melody()  # Configurar los sonidos
        play_melody()   # Reproducir la melodía
        pyxel.run(self.update, self.draw)

    def update(self):
        # Salir del programa con Q
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(40, 60, "Playing: Merry Christmas", pyxel.frame_count % 16)

App()