from PyQt5 import QtWidgets, QtCore


def show_pop_up(title, message, type_of_message):
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(message)
    msg.setIcon(type_of_message)
    msg.setStandardButtons(QtWidgets.QMessageBox.Cancel |
                           QtWidgets.QMessageBox.Ok)
    info = msg.exec_()
    
def show_message(message):
    box = QtWidgets.QMessageBox()
    box.setIcon(QtWidgets.QMessageBox.Information)
    box.setWindowTitle("Informacion")
    box.setText(message)
    
    timer = QtCore.QTimer()
    timer.timeout.connect(box.accept)
    timer.start(3000)
    
    box.exec_()


def validate_items(*args):
    for var in args:
        if var == "":
            return False

    return True
