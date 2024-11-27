import pyxel

def setup_melody():
    """
    Configura la melodía del Cara al Sol en Pyxel.
    """
    # Frase 1
    pyxel.sounds[0].set(
        notes="G4A4B4C5C5B4A4",  # Corrected notes
        tones="T",
        volumes="4444444",  
        effects="N",
        speed=20
    )

    # Frase 2
    pyxel.sounds[1].set(
        notes="A4A4G4F4G4A4B4",  # Corrected notes
        tones="T",
        volumes="4444444",
        effects="N",
        speed=20
    )

    # Frase 3
    pyxel.sounds[2].set(
        notes="C5C5B4A4B4C5D5",  # Corrected notes
        tones="T",
        volumes="4444444",
        effects="N",
        speed=20
    )

    # Frase 4 (Final Phrase)
    pyxel.sounds[3].set(
        notes="E5E5D5C5D5E5F5",  # Corrected notes
        tones="T",
        volumes="4444444",
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
        pyxel.init(160, 120, title="Cara al Sol")
        setup_melody()  # Configurar la melodía
        play_melody()   # Reproducir la melodía
        pyxel.run(self.update, self.draw)

    def update(self):
        # Salir del programa con Q
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(10, 50, "Playing: Cara al Sol", 7)

App()