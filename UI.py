from PyQt5.QtWidgets import QMainWindow, QPushButton


class Window(QMainWindow):
    def __init__(self,):
        super().__init__()
        self.setGeometry(300, 300, 700, 500)
        self.btn = QPushButton('Click', self)
        self.btn.setGeometry(200, 200, 50, 25)
        self.setWindowTitle('Git и случайные окружности')
