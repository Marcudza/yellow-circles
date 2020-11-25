import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self._shapes = list()
        self.pushButton.clicked.connect(self.randomClick)

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setPen(QPen(Qt.yellow, 8, Qt.SolidLine))

        painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))

        for shape in self._shapes:
            painter.drawEllipse(shape[0], shape[1], shape[2], shape[2])

    def randomClick(self):
        rand = randint(1, 300)
        rand_x = randint(0, 400)
        rand_y = randint(0, 400)
        self._shapes.append([rand_x, rand_y, rand])
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
