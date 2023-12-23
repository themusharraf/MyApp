import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6 import QtGui


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(500, 700))
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setWindowTitle("My App")
        self.setStyleSheet('background-color: green;')

        button = QPushButton("hello world")
        font = QtGui.QFont()
        button.setFont(font)
        button.setFixedSize(QSize(70,40))
        button.setStyleSheet('background-color: yellow;')

        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

# https://pixabay.com/vectors/icon-summer-beach-sunset-5577198/
