import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from UI import Window


class Example(Window):
    def __init__(self):
        Window.__init__(self)
        self.btn.clicked.connect(self.paint)

    def paint(self):
        self.update()

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        num = random.randint(10, 300)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.qp.setBrush(QColor(r, g, b))
        self.qp.drawEllipse(random.randint(10, 600), random.randint(10, 400), num, num)
        self.qp.end()

app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())