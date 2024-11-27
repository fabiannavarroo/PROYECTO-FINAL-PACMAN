import pyxel

def setup_melody():
    # Frase 1: "We wish you a Merry Christmas"
    pyxel.sounds[0].set(
        notes="E4D4C4C4C4G3C4D4E4D4C4           C4F4            F4E4D4C4E4D4",  # Notas de la frase
        tones="T",
        volumes="4",
        effects="N",
        speed=25  # Velocidad ajustada para la melodía
    )

    # Frase 2: "We wish you a Merry Christmas"
    pyxel.sounds[1].set(
        notes="G3G3A3G3D4C4",
        tones="T",
        volumes="4",
        effects="N",
        speed=25
    )

    # Frase 3: "Good tidings we bring"
    pyxel.sounds[2].set(
        notes="E4E4F4E4G4F4",
        tones="T",
        volumes="4",
        effects="N",
        speed=25
    )

    # Frase 4: "To you and your kin"
    pyxel.sounds[3].set(
        notes="D4D4E4D4C4B3",
        tones="T",
        volumes="4",
        effects="N",
        speed=25
    )

    # Frase 5: "We wish you a Merry Christmas and a Happy New Year"
    pyxel.sounds[4].set(
        notes="G3G3A3G3C4B3 G3G3A3G3D4C4",
        tones="T",
        volumes="4",
        effects="N",
        speed=25
    )

def play_melody():
    # Reproducir las frases en secuencia
    pyxel.play(0, [0], loop=True)

class App:
    def __init__(self):
        pyxel.init(160, 120, title="We Wish You a Merry Christmas")
        setup_melody()  # Configurar la melodía
        play_melody()   # Reproducir la melodía
        pyxel.run(self.update, self.draw)

    def update(self):
        # Salir del programa con Q
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(10, 50, "Playing: We Wish You a Merry Christmas", 7)

App()