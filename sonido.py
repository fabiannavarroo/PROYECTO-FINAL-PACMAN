import pyxel

def setup_melody():
    """
    Configura la melodía del Cara al Sol en Pyxel.
    """
    # Frase 1
    pyxel.sounds[0].set(
        notes="C4RE4RG4RA4RA4RG4RF4",  # Primera parte simplificada
        tones="T",              # Tono: Triangular
        volumes="6666666",      # Volumen constante
        effects="N",            # Sin efectos
        speed=20                # Velocidad
    )

    # Frase 2
    pyxel.sounds[1].set(
        notes="G3A3B3C4C4B3A3",  # Segunda parte
        tones="T",
        volumes="6666666",
        effects="N",
        speed=20
    )

    # Frase 3
    pyxel.sounds[2].set(
        notes="D4F4A4G4A4F4E4",  # Tercera parte
        tones="T",
        volumes="6666666",
        effects="N",
        speed=20
    )

    # Frase 4 (final)
    pyxel.sounds[3].set(
        notes="C4C4D4E4F4G4A4",  # Final
        tones="T",
        volumes="6666666",
        effects="N",
        speed=20
    )

def play_melody():
    """
    Reproduce la melodía configurada en bucle.
    """
    pyxel.play(0, [0], loop=True)

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