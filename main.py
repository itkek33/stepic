#импорты библиотек
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow
)

from PyQt5.uic import loadUi

import sys

from PyQt5.QtGui import QPixmap, QIcon

#главный класс(окно)
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("mainwindow.ui", self)

#запуск приложения

app = QApplication(sys.argv)

welcome = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)

#грузим иконку

icon = QIcon()
icon.addPixmap(QPixmap("logo.png"), QIcon.Normal, QIcon.Off)
widget.setWindowIcon(icon)
widget.show()

#запуск кода 

try:
    sys.exit(app.exec_())
except:
    print("exiting")