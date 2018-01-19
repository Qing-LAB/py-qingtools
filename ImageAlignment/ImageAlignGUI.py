import sys
from PyQt5 import QtWidgets, QtGui


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    l1 = QtWidgets.QLabel(w)
    l2 = QtWidgets.QLabel(w)

    l1.setText('this is a test')
    l2.setPixmap(QtGui.QPixmap('../resources/lab-badge.png'))

    w.setWindowTitle('ImageAlign')
    w.setGeometry(100, 100, 300, 300)
    l1.move(100, 20)
    l2.move(10, 90)
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
