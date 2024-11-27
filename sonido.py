import pyxel

def setup_melody():
    """
    Configura la melodía del Cara al Sol en Pyxel.
    """
    # Frase 1
    pyxel.sounds[0].set(
        notes="C4RE4RRG4RA4RA4RG4RF4",  # Primera parte simplificada
        tones="T",              # Tono: Triangular
        volumes="6666666",      # Volumen constante
        effects="N",            # Sin efectos
        speed=20                # Velocidad
    )

    # Frase 2
    pyxel.sounds[1].set(
        notes="RRG3RRA3RRB3RC4RC4RB3RRA3RR",  # Segunda parte
        tones="T",
        volumes="6666666",
        effects="N",
        speed=20
    )

    # Frase 3
    pyxel.sounds[2].set(
        notes="D4RF4RA4RG4RA4RF4RE4",  # Tercera parte
        tones="T",
        volumes="6666666",
        effects="N",
        speed=20
    )

    # Frase 4 (final)
    pyxel.sounds[3].set(
        notes="C4RC4RD4RE4RF4RG4RA4",  # Final
        tones="T",
        volumes="6666666",
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