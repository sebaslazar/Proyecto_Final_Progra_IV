# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nuevo_fertilizante.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Add_Fertilizer(object):
    def setupUi(self, Add_Fertilizer, Add_Product, Main_Menu):
        Add_Fertilizer.setObjectName("Add_Fertilizer")
        Add_Fertilizer.resize(799, 608)
        self.Background = QtWidgets.QWidget(Add_Fertilizer)
        self.Background.setStyleSheet("QWidget{\n"
                                      "    background-color: rgb(236, 236, 236)\n"
                                      "}")
        self.Background.setObjectName("Background")
        self.frame = QtWidgets.QFrame(self.Background)
        self.frame.setGeometry(QtCore.QRect(133, 0, 561, 601))
        self.frame.setStyleSheet("QLineEdit{\n"
                                 "    background-color: white;\n"
                                 "    font-size: 20px;\n"
                                 "}\n"
                                 "\n"
                                 "QLabel{\n"
                                 "    font-size: 20px;\n"
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
                                 "#Add{\n"
                                 "    background-color: rgb(87, 255, 75);\n"
                                 "    border-color: rgb(0, 172, 0);\n"
                                 "}\n"
                                 "\n"
                                 "#Add::hover{\n"
                                 "    background-color: rgb(56, 247, 42);\n"
                                 "}\n"
                                 "\n"
                                 "#Add::pressed{\n"
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
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.Introduction = QtWidgets.QLabel(self.frame)
        self.Introduction.setObjectName("Introduction")
        self.verticalLayout.addWidget(self.Introduction)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.Name = QtWidgets.QFrame(self.frame)
        self.Name.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Name.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Name.setObjectName("Name")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Name)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Label = QtWidgets.QLabel(self.Name)
        self.Label.setStyleSheet("QLabel{\n"
                                 "    margin-right: 88px;\n"
                                 "}")
        self.Label.setObjectName("Label")
        self.horizontalLayout_2.addWidget(self.Label)
        self.lineEdit = QtWidgets.QLineEdit(self.Name)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout.addWidget(self.Name)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.ICA = QtWidgets.QFrame(self.frame)
        self.ICA.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ICA.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ICA.setObjectName("ICA")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ICA)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Label_5 = QtWidgets.QLabel(self.ICA)
        self.Label_5.setStyleSheet("QLabel{\n"
                                   "    margin-right: 127px\n"
                                   "}")
        self.Label_5.setObjectName("Label_5")
        self.horizontalLayout.addWidget(self.Label_5)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.ICA)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.verticalLayout.addWidget(self.ICA)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.Frequency = QtWidgets.QFrame(self.frame)
        self.Frequency.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frequency.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frequency.setObjectName("Frequency")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Frequency)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Label_4 = QtWidgets.QLabel(self.Frequency)
        self.Label_4.setStyleSheet("QLabel{\n"
                                   "    margin-right: 63px\n"
                                   "}")
        self.Label_4.setObjectName("Label_4")
        self.horizontalLayout_4.addWidget(self.Label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.Frequency)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_4.addWidget(self.lineEdit_3)
        self.verticalLayout.addWidget(self.Frequency)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.Last_Application = QtWidgets.QFrame(self.frame)
        self.Last_Application.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Last_Application.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Last_Application.setObjectName("Last_Application")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.Last_Application)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Label_3 = QtWidgets.QLabel(self.Last_Application)
        self.Label_3.setStyleSheet("QLabel{\n"
                                   "    margin-right: 5\n"
                                   "}")
        self.Label_3.setObjectName("Label_3")
        self.horizontalLayout_6.addWidget(self.Label_3)
        self.dateEdit = QtWidgets.QDateEdit(self.Last_Application)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        self.dateEdit.setStyleSheet("QDateEdit{\n"
                                    "    background-color: white;\n"
                                    "}")
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate(2023, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_6.addWidget(self.dateEdit)
        self.verticalLayout.addWidget(self.Last_Application)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.Value = QtWidgets.QFrame(self.frame)
        self.Value.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Value.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Value.setObjectName("Value")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Value)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Label_2 = QtWidgets.QLabel(self.Value)
        self.Label_2.setStyleSheet("QLabel{\n"
                                   "    margin-right: 108px\n"
                                   "}")
        self.Label_2.setObjectName("Label_2")
        self.horizontalLayout_5.addWidget(self.Label_2)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.Value)
        self.lineEdit_4.setStyleSheet("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_5.addWidget(self.lineEdit_4)
        self.verticalLayout.addWidget(self.Value)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Cancel = QtWidgets.QPushButton(self.frame)
        self.Cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Cancel.setObjectName("Cancel")
        self.horizontalLayout_3.addWidget(self.Cancel)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.Add = QtWidgets.QPushButton(self.frame)
        self.Add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Add.setObjectName("Add")
        self.horizontalLayout_3.addWidget(self.Add)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        Add_Fertilizer.setCentralWidget(self.Background)

        Add_Product.hide()

        self.retranslateUi(Add_Fertilizer)
        QtCore.QMetaObject.connectSlotsByName(Add_Fertilizer)

    def retranslateUi(self, Add_Fertilizer):
        _translate = QtCore.QCoreApplication.translate
        Add_Fertilizer.setWindowTitle(_translate("Add_Fertilizer", "Agregar Fertilizante"))
        self.Introduction.setText(_translate("Add_Fertilizer",
                                             "<html><head/><body><p align=\"center\"><span style=\" "
                                             "font-size:15pt;\">Ingrese los datos del nuevo "
                                             "fertilizante</span></p></body></html>"))
        self.Label.setText(_translate("Add_Fertilizer", "Nombre"))
        self.Label_5.setText(_translate("Add_Fertilizer", "ICA"))
        self.Label_4.setText(_translate("Add_Fertilizer", "Frecuencia"))
        self.Label_3.setText(_translate("Add_Fertilizer", "Última Aplicación"))
        self.Label_2.setText(_translate("Add_Fertilizer", "Costo"))
        self.Cancel.setText(_translate("Add_Fertilizer", "Cancelar"))
        self.Add.setText(_translate("Add_Fertilizer", "Agregar"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Add_Fertilizer = QtWidgets.QMainWindow()
    ui = Ui_Add_Fertilizer()
    ui.setupUi(Add_Fertilizer)
    Add_Fertilizer.show()
    sys.exit(app.exec_())
