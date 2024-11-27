import pyxel

def setup_melody():
    """
    Configura la melodía del Cara al Sol en Pyxel.
    """
    # Frase 1
    pyxel.sounds[0].set(
        notes="G4G4G4G4RG4F4E4RG4G4G4G4RG4F4E4R",  # Primera parte
        tones="T",
        volumes="666666666666666",
        effects="N",
        speed=20
    )

    # Frase 2
    pyxel.sounds[1].set(
        notes="F4E4D4E4RF4D4C4RG4F4E4RG4F4E4",  # Segunda parte
        tones="T",
        volumes="66666666666666",
        effects="N",
        speed=20
    )

    # Frase 3
    pyxel.sounds[2].set(
        notes="C4C4C4C4RE4F4E4RD4E4F4E4RD4C4",  # Tercera parte
        tones="T",
        volumes="66666666666666",
        effects="N",
        speed=20
    )

    # Frase 4 (final)
    pyxel.sounds[3].set(
        notes="C4RD4RE4F4RG4F4RD4C4R",  # Final
        tones="T",
        volumes="66666666",
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
        setup_melody()  # Configura la melodía
        play_melody()   # Reproduce la melodía
        pyxel.run(self.update, self.draw)

    def update(self):
        # Salir del programa con la tecla Q
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(10, 50, "Playing: Cara al Sol", 7)

# Ejecutar la aplicación
App()