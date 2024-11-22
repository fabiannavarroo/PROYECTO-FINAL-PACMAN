import pyxel  # type: ignore

class App:
    def __init__(self):
        pyxel.init(160,120,"Hello World")
        pyxel.run(self.update, self.draw)
    def update(self):
        if pyxel.btn(pyxel.KEY_1):
            for i in range (150):
                for j in range(110):
                    pyxel.fill(i,j,7)
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
    def draw(self):
        pyxel.cls(0)
        pyxel.text(15,15,"Buenos dias",15)
App()