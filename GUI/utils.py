from PyQt5 import QtWidgets

def show_pop_up(title, message, type_of_message):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(type_of_message)
        msg.setStandardButtons(QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Ok)
        info = msg.exec_()