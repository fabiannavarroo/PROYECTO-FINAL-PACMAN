import pyxel

def setup_melody():
    """
    Configura la melodía del Cara al Sol en Pyxel.
    """
    # Frase 1: "Cara al sol con la camisa nueva..."
    pyxel.sounds[0].set(
        notes="G4G4G4G4A4B4C5C5RG4G4G4RG4G4G4F4",  
        tones="T",
        volumes="6666666666666666",
        effects="N",
        speed=20
    )

    # Frase 2: "Que tú bordaste en rojo ayer..."
    pyxel.sounds[1].set(
        notes="F4F4F4G4A4A4G4F4RG4F4E4D4C4RG4A4",
        tones="T",
        volumes="6666666666666666",
        effects="N",
        speed=20
    )

    # Frase 3: "Me hallará la muerte si me llega..."
    pyxel.sounds[2].set(
        notes="B3C4D4E4F4F4E4D4C4RG4A4B4C5D5RG4",
        tones="T",
        volumes="6666666666666666",
        effects="N",
        speed=20
    )

    # Frase 4: Final "Y no te vuelvo a ver..."
    pyxel.sounds[3].set(
        notes="E4F4G4A4B4C5B4A4G4F4E4F4G4A4R",
        tones="T",
        volumes="666666666666666",
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