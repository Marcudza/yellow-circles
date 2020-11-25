import sys
from random import randint, choice

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._shapes = list()
        self.pushButton.clicked.connect(self.randomClick)

    def paintEvent(self, event):
        painter = QPainter(self)
        for shape in self._shapes:
            painter.setBrush(QBrush(shape[3], Qt.SolidPattern))
            painter.setPen(QPen(shape[3], 8, Qt.SolidLine))
            painter.drawEllipse(shape[0], shape[1], shape[2], shape[2])

    def randomClick(self):
        rand = randint(1, 300)
        rand_x = randint(0, 400)
        rand_y = randint(0, 400)
        self._shapes.append([rand_x, rand_y, rand, self.pickColor()])
        self.update()

    def pickColor(self):
        colors = [Qt.black, Qt.white, Qt.darkGray, Qt.gray, Qt.lightGray, Qt.red, Qt.green, Qt.blue, Qt.cyan,
                  Qt.magenta, Qt.yellow, Qt.darkRed, Qt.darkGreen, Qt.darkBlue, Qt.darkCyan, Qt.darkMagenta,
                  Qt.darkYellow]
        return choice(colors)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
