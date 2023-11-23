import GUI
from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])

if __name__ == '__main__':
    login = uic.loadUi(agregar_cliente)
    login.show()
    app.exec()
