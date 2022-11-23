from PyQt5.QtWidgets import QPushButton, QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QPainter, QColor, QPixmap
from UI import Ui_Form
import sys
from random import randint


class Example(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.paint)
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter(self)
            qp.setBrush(QColor(200, 200, 0))
            for i in range(4):
                qp.drawEllipse(randint(1, 200), randint(1, 200), randint(1, 100), randint(1, 100))
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
