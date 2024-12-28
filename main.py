import sys
import random

from PyQt6.QtCore import QPoint
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton("Создание круга", self)
        self.setGeometry(500, 300, 600, 600)
        self.point = QPoint(300, 250)
        self.setWindowTitle('Рисование')
        self.btn.move(250, 500)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        random_color_r = random.randrange(0, 256)
        random_color_g = random.randrange(0, 256)
        random_color_b = random.randrange(0, 256)
        qp.setBrush(QColor(random_color_r, random_color_g, random_color_b))
        random_range = random.randrange(5, 200)
        qp.drawEllipse(self.point, random_range, random_range)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
