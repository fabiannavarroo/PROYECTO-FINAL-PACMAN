import pyxel

def setup_melody():
    """
    Configura la melodía de 'We Wish You a Merry Christmas' con silencios.
    """
    # Frase 1: "We wish you a Merry Christmas..."
    pyxel.sounds[0].set(
        notes="G4R G4A4G4F4E4R C4C4D4C4B4A4R",  # Incluye silencios entre frases
        tones="T",
        volumes="6666666666666",
        effects="N",
        speed=20
    )

    # Frase 2: "And a Happy New Year..."
    pyxel.sounds[1].set(
        notes="D4R D4E4D4C4B4R G4G4A4G4F4E4R",  # Silencios tras repeticiones
        tones="T",
        volumes="6666666666666",
        effects="N",
        speed=20
    )

    # Frase 3: Final "Good tidings we bring..."
    pyxel.sounds[2].set(
        notes="C4D4E4F4G4R G4A4B4C4R B4A4G4F4R",
        tones="T",
        volumes="6666666666666",
        effects="N",
        speed=20
    )

    # Frase 4: Final repetitivo
    pyxel.sounds[3].set(
        notes="D4R D4E4D4C4B4R G4G4A4G4F4E4R",
        tones="T",
        volumes="6666666666666",
        effects="N",
        speed=20
    )

def play_melody():
    """
    Reproduce la melodía configurada en bucle.
    """
    pyxel.play(0, [0, 1, 2, 3], loop=True)

class App:
    def __init__(self):
        pyxel.init(160, 120, title="Merry Christmas")
        setup_melody()  # Configura la melodía
        play_melody()   # Reproduce la melodía
        pyxel.run(self.update, self.draw)

    def update(self):
        # Salir con la tecla Q
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(10, 50, "Playing: Merry Christmas", 7)

# Ejecutar la aplicación
App()