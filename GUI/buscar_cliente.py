# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buscar_cliente.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Search_Client(object):
    def setupUi(self, Search_Client):
        Search_Client.setObjectName("Search_Client")
        Search_Client.resize(799, 600)
        self.Background = QtWidgets.QWidget(Search_Client)
        self.Background.setStyleSheet("QWidget{\n"
                                      "    background-color: rgb(236, 236, 236)\n"
                                      "}")
        self.Background.setObjectName("Background")
        self.frame = QtWidgets.QFrame(self.Background)
        self.frame.setGeometry(QtCore.QRect(193, 0, 412, 600))
        self.frame.setStyleSheet("QLineEdit{\n"
                                 "    background-color: white;\n"
                                 "    font-size: 30px;\n"
                                 "}\n"
                                 "\n"
                                 "QLabel{\n"
                                 "    font-size: 30px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton{\n"
                                 "    font-size: 20px;\n"
                                 "    border: 2px solid;\n"
                                 "    border-radius: 6px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton::pressed{\n"
                                 "    color: rgb(225, 225, 225);\n"
                                 "    border-radius: 0;\n"
                                 "}\n"
                                 "\n"
                                 "#Search{\n"
                                 "    background-color: rgb(87, 255, 75);\n"
                                 "    border-color: rgb(0, 172, 0);\n"
                                 "}\n"
                                 "\n"
                                 "#Search::hover{\n"
                                 "    background-color: rgb(56, 247, 42);\n"
                                 "}\n"
                                 "\n"
                                 "#Search::pressed{\n"
                                 "    background-color: rgb(0, 172, 0);\n"
                                 "    border-color: rgb(87, 255, 75)\n"
                                 "}\n"
                                 "\n"
                                 "#Cancel{\n"
                                 "    background-color: rgb(242, 90, 90);\n"
                                 "    border-color: rgb(255, 0, 0)\n"
                                 "}\n"
                                 "\n"
                                 "#Cancel::hover{\n"
                                 "    background-color: rgb(237, 50, 50);\n"
                                 "    border-color: rgb(255, 0, 0)\n"
                                 "}\n"
                                 "\n"
                                 "#Cancel::pressed{\n"
                                 "    background-color: rgb(255, 0, 0);\n"
                                 "    border-color: rgb(255, 101, 101)\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.identification = QtWidgets.QFrame(self.frame)
        self.identification.setGeometry(QtCore.QRect(10, 150, 391, 151))
        self.identification.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.identification.setFrameShadow(QtWidgets.QFrame.Raised)
        self.identification.setObjectName("identification")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.identification)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Label = QtWidgets.QLabel(self.identification)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.Label.setFont(font)
        self.Label.setStyleSheet("QLabel{\n"
                                 "    margin-right: 25px;\n"
                                 "}")
        self.Label.setObjectName("Label")
        self.horizontalLayout_2.addWidget(self.Label)
        self.lineEdit = QtWidgets.QLineEdit(self.identification)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 340, 411, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Cancel.setObjectName("Cancel")
        self.horizontalLayout_3.addWidget(self.Cancel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.Search = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Search.setObjectName("Search")
        self.horizontalLayout_3.addWidget(self.Search)
        self.Introduction = QtWidgets.QLabel(self.frame)
        self.Introduction.setGeometry(QtCore.QRect(0, 40, 411, 101))
        self.Introduction.setObjectName("Introduction")
        Search_Client.setCentralWidget(self.Background)

        self.retranslateUi(Search_Client)
        QtCore.QMetaObject.connectSlotsByName(Search_Client)

    def retranslateUi(self, Search_Client):
        _translate = QtCore.QCoreApplication.translate
        Search_Client.setWindowTitle(_translate("Search_Client", "Buscar Cliente"))
        self.Label.setText(_translate("Search_Client", "Cédula"))
        self.Cancel.setText(_translate("Search_Client", "Cancelar"))
        self.Search.setText(_translate("Search_Client", "Buscar"))
        self.Introduction.setText(_translate("Search_Client",
                                             "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt;\">Ingrese la cédula que desea buscar en </span></p><p align=\"center\"><span style=\" font-size:15pt;\">el sistema, sin puntos, comas o guiones.</span></p></body></html>"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Search_Client = QtWidgets.QMainWindow()
    ui = Ui_Search_Client()
    ui.setupUi(Search_Client)
    Search_Client.show()
    sys.exit(app.exec_())
