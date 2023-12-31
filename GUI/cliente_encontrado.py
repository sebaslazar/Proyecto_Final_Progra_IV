# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cliente_encontrado.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Controller import bill_controler
import locale

try:
    locale.setlocale(locale.LC_ALL, 'es_CO.UTF-8')
except:
    current_info = locale.getdefaultlocale()
    current_info = f"{current_info[0]}.UTF-8"
    locale.setlocale(locale.LC_ALL, current_info)



class Ui_Client_Found(object):

    def back_main_menu(self, Client_Found, Search_Client, Main_Menu):
        Main_Menu.show()
        Search_Client.close()
        Client_Found.close()

    def setupUi(self, Client_Found, Search_Client, Main_Menu, client):
        Client_Found.setObjectName("Client_Found")
        Client_Found.resize(800, 600)
        self.Background = QtWidgets.QWidget(Client_Found)
        self.Background.setStyleSheet("QWidget{\n"
                                      "    background-color: rgb(236, 236, 236)\n"
                                      "}")
        self.Background.setObjectName("Background")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Background)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.Background)
        self.frame.setStyleSheet("QLineEdit{\n"
                                 "    font-size: 20px;\n"
                                 "    background-color: white\n"
                                 "}\n"
                                 "\n"
                                 "QLabel{\n"
                                 "    font-size: 20px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton{\n"
                                 "    font-size: 20px;\n"
                                 "    border: 2px solid black;\n"
                                 "    border-radius: 10px;\n"
                                 "    padding: 10px\n"
                                 "}\n"
                                 "\n"
                                 "#Antibiotics{\n"
                                 "    background: rgb(255, 170, 0);\n"
                                 "}\n"
                                 "\n"
                                 "#Antibiotics::Hover{\n"
                                 "    background-color: rgb(250, 198, 95);\n"
                                 "}\n"
                                 "\n"
                                 "#Antibiotics::Pressed{\n"
                                 "    background-color: rgb(102, 71, 9);\n"
                                 "    color: white\n"
                                 "}\n"
                                 "\n"
                                 "#Fertilizers{\n"
                                 "    background-color: rgb(0, 170, 255)\n"
                                 "}\n"
                                 "\n"
                                 "#Fertilizers::Hover{\n"
                                 "    background-color: rgb(188, 250, 255)\n"
                                 "}\n"
                                 "\n"
                                 "#Fertilizers::Pressed{\n"
                                 "    background-color: rgb(0, 0, 108);\n"
                                 "    color: white\n"
                                 "}\n"
                                 "\n"
                                 "#Pest_Control{\n"
                                 "    background: rgb(0, 170, 0);\n"
                                 "}\n"
                                 "\n"
                                 "#Pest_Control::Hover{\n"
                                 "    background-color: rgb(133, 222, 133);\n"
                                 "}\n"
                                 "\n"
                                 "#Pest_Control::Pressed{\n"
                                 "    background-color: rgb(0, 77, 0);\n"
                                 "    color: white\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox{\n"
                                 "    background-color: white;\n"
                                 "    font-size: 20px\n"
                                 "}\n"
                                 "\n"
                                 "#Quit_Button{\n"
                                 "    background-color: rgb(255, 0, 0);\n"
                                 "    color: black;\n"
                                 "}\n"
                                 "\n"
                                 "#Quit_Button::Hover{\n"
                                 "    background-color: rgb(232, 142, 142);\n"
                                 "    color: black;\n"
                                 "}\n"
                                 "\n"
                                 "#Quit_Button::Pressed{\n"
                                 "    background-color: rgb(150, 0, 0);\n"
                                 "    color: white;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QHeaderView::section{\n"
                                 "    width: 20px;\n"
                                 "    border: 2px solid black;\n"
                                 "    background-color: white;\n"
                                 "}\n"
                                 "\n"
                                 "QTableView{\n"
                                 "    gridline-color: black;\n"
                                 "}\n"
                                 "\n"
                                 "QTableView::item{\n"
                                 "    background-color: white;\n"
                                 "    border: 1px solid black\n"
                                 "}\n"
                                 "\n"
                                 "QTableView::item:selected{\n"
                                 "    background-color: rgb(94, 110, 255)\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(310, 160, 271, 28))
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setEditable(False)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox.setMinimumContentsLength(20)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.currentIndexChanged.connect(self.set_product_data)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(70, 200, 661, 81))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Antibiotics = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.Antibiotics.setFont(font)
        self.Antibiotics.setObjectName("Antibiotics")
        self.horizontalLayout.addWidget(self.Antibiotics)
        self.Fertilizers = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.Fertilizers.setFont(font)
        self.Fertilizers.setObjectName("Fertilizers")
        self.horizontalLayout.addWidget(self.Fertilizers)
        self.Pest_Control = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.Pest_Control.setFont(font)
        self.Pest_Control.setObjectName("Pest_Control")
        self.horizontalLayout.addWidget(self.Pest_Control)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(60, 500, 671, 81))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Total_Value = QtWidgets.QLabel(self.frame_3)
        self.Total_Value.setObjectName("Total_Value")
        self.horizontalLayout_2.addWidget(self.Total_Value)
        self.Quit_Button = QtWidgets.QPushButton(self.frame_3, clicked=lambda: self.back_main_menu(Client_Found, Search_Client, Main_Menu))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.Quit_Button.setFont(font)
        self.Quit_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Quit_Button.setObjectName("Quit_Button")
        self.horizontalLayout_2.addWidget(self.Quit_Button)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(110, 20, 561, 121))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(70, 300, 661, 191))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.Table_Antibiotics = QtWidgets.QTableWidget(self.frame_5)
        self.Table_Antibiotics.setGeometry(QtCore.QRect(0, 0, 651, 191))
        self.Table_Antibiotics.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Table_Antibiotics.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Table_Antibiotics.setProperty("showDropIndicator", False)
        self.Table_Antibiotics.setDragDropOverwriteMode(False)
        self.Table_Antibiotics.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.Table_Antibiotics.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.Table_Antibiotics.setShowGrid(True)
        self.Table_Antibiotics.setWordWrap(False)
        self.Table_Antibiotics.setObjectName("Table_Antibiotics")
        self.Table_Antibiotics.setColumnCount(4)
        self.Table_Antibiotics.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Antibiotics.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Antibiotics.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Antibiotics.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Antibiotics.setHorizontalHeaderItem(3, item)
        self.Table_Antibiotics.horizontalHeader().setDefaultSectionSize(160)
        self.Table_Antibiotics.horizontalHeader().setMinimumSectionSize(100)
        self.Table_Antibiotics.verticalHeader().setDefaultSectionSize(30)
        self.Table_Antibiotics.verticalHeader().setSortIndicatorShown(False)
        self.Table_Fertilizers = QtWidgets.QTableWidget(self.frame_5)
        self.Table_Fertilizers.setGeometry(QtCore.QRect(0, 0, 661, 191))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Table_Fertilizers.sizePolicy().hasHeightForWidth())
        self.Table_Fertilizers.setSizePolicy(sizePolicy)
        self.Table_Fertilizers.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Table_Fertilizers.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Table_Fertilizers.setProperty("showDropIndicator", False)
        self.Table_Fertilizers.setDragDropOverwriteMode(False)
        self.Table_Fertilizers.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.Table_Fertilizers.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.Table_Fertilizers.setShowGrid(True)
        self.Table_Fertilizers.setWordWrap(False)
        self.Table_Fertilizers.setObjectName("Table_Fertilizers")
        self.Table_Fertilizers.setColumnCount(5)
        self.Table_Fertilizers.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Fertilizers.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Fertilizers.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Fertilizers.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Fertilizers.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Fertilizers.setHorizontalHeaderItem(4, item)
        self.Table_Fertilizers.horizontalHeader().setDefaultSectionSize(130)
        self.Table_Fertilizers.horizontalHeader().setMinimumSectionSize(110)
        self.Table_Fertilizers.verticalHeader().setDefaultSectionSize(30)
        self.Table_Fertilizers.verticalHeader().setSortIndicatorShown(False)
        self.Table_Pests = QtWidgets.QTableWidget(self.frame_5)
        self.Table_Pests.setGeometry(QtCore.QRect(0, 0, 661, 191))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Table_Pests.sizePolicy().hasHeightForWidth())
        self.Table_Pests.setSizePolicy(sizePolicy)
        self.Table_Pests.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Table_Pests.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Table_Pests.setProperty("showDropIndicator", False)
        self.Table_Pests.setDragDropOverwriteMode(False)
        self.Table_Pests.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.Table_Pests.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.Table_Pests.setShowGrid(True)
        self.Table_Pests.setWordWrap(False)
        self.Table_Pests.setObjectName("Table_Fertilizers_2")
        self.Table_Pests.setColumnCount(5)
        self.Table_Pests.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Pests.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Pests.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Pests.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Pests.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Pests.setHorizontalHeaderItem(4, item)
        self.Table_Pests.horizontalHeader().setDefaultSectionSize(131)
        self.Table_Pests.horizontalHeader().setMinimumSectionSize(110)
        self.Table_Pests.verticalHeader().setDefaultSectionSize(30)
        self.Table_Pests.verticalHeader().setSortIndicatorShown(False)
        self.verticalLayout.addWidget(self.frame)
        Client_Found.setCentralWidget(self.Background)

        self.retranslateUi(Client_Found)
        self.Antibiotics.clicked.connect(self.Table_Antibiotics.show)  # type: ignore
        self.Fertilizers.clicked.connect(self.Table_Antibiotics.hide)  # type: ignore
        self.Pest_Control.clicked.connect(self.Table_Antibiotics.hide)  # type: ignore
        self.Antibiotics.clicked.connect(self.Table_Fertilizers.hide)  # type: ignore
        self.Fertilizers.clicked.connect(self.Table_Fertilizers.show)  # type: ignore
        self.Pest_Control.clicked.connect(self.Table_Fertilizers.hide)  # type: ignore
        self.Antibiotics.clicked.connect(self.Table_Pests.hide)  # type: ignore
        self.Fertilizers.clicked.connect(self.Table_Pests.hide)  # type: ignore
        self.Pest_Control.clicked.connect(self.Table_Pests.show)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Client_Found)
        self.client = client
        
        self.set_client_data(client)
        self.set_item_text_bill(client.bills)

        Search_Client.hide()

    def retranslateUi(self, Client_Found):
        _translate = QtCore.QCoreApplication.translate
        Client_Found.setWindowTitle(_translate("Client_Found", "Cliente Encontrado"))
        self.comboBox.setItemText(0, _translate("Client_Found", "FACTURAS"))
        self.Antibiotics.setText(_translate("Client_Found", "Antibióticos"))
        self.Fertilizers.setText(_translate("Client_Found", "Fertilizantes"))
        self.Pest_Control.setText(_translate("Client_Found", "Control de plagas"))
        self.Total_Value.setText(_translate("Client_Found", "VALOR TOTAL: "))
        self.Quit_Button.setText(_translate("Client_Found", "SALIR >>"))
        self.label_2.setText(_translate("Client_Found", "Nombre:"))
        self.label.setText(_translate("Client_Found", "Cédula:"))
        item = self.Table_Antibiotics.horizontalHeaderItem(0)
        item.setText(_translate("Client_Found", "NOMBRE"))
        item = self.Table_Antibiotics.horizontalHeaderItem(1)
        item.setText(_translate("Client_Found", "DOSIS"))
        item = self.Table_Antibiotics.horizontalHeaderItem(2)
        item.setText(_translate("Client_Found", "TIPO"))
        item = self.Table_Antibiotics.horizontalHeaderItem(3)
        item.setText(_translate("Client_Found", "COSTO"))
        
        item = self.Table_Fertilizers.horizontalHeaderItem(0)
        item.setText(_translate("Client_Found", "NOMBRE"))
        item = self.Table_Fertilizers.horizontalHeaderItem(1)
        item.setText(_translate("Client_Found", "ICA"))
        item = self.Table_Fertilizers.horizontalHeaderItem(2)
        item.setText(_translate("Client_Found", "FRECUENCIA"))
        item = self.Table_Fertilizers.horizontalHeaderItem(3)
        item.setText(_translate("Client_Found", "ÚLTIMA APLICACIÓN"))
        item = self.Table_Fertilizers.horizontalHeaderItem(4)
        item.setText(_translate("Client_Found", "COSTO"))
        
        item = self.Table_Pests.horizontalHeaderItem(0)
        item.setText(_translate("Client_Found", "NOMBRE"))
        item = self.Table_Pests.horizontalHeaderItem(1)
        item.setText(_translate("Client_Found", "ICA"))
        item = self.Table_Pests.horizontalHeaderItem(2)
        item.setText(_translate("Client_Found", "FRECUENCIA"))
        item = self.Table_Pests.horizontalHeaderItem(3)
        item.setText(_translate("Client_Found", "PERÍODO DE CARENCIA"))
        item = self.Table_Pests.horizontalHeaderItem(4)
        item.setText(_translate("Client_Found", "COSTO"))
        
        
    def set_product_data(self):
        self.clear_content()
        date = self.comboBox.currentText()
        bill = bill_controler.BillControler.search(date=date, bills=self.client.bills)
        if isinstance(bill, bool): return
        products = bill.products
        for product in products:
            variables = vars(product)
            _type = variables.get("type")
            table = f"self.Table_{_type}"
            last_row = eval(f"{table}.rowCount()")
            eval(f"{table}.insertRow(last_row)")
            for i, value in enumerate(list(variables.values())[1:]):
                item = QtWidgets.QTableWidgetItem(str(value))
                eval(f"{table}.setItem(last_row, i, item)")
                
        self.Total_Value.setText(f"VALOR TOTAL: {locale.currency(bill.total_value())}")
        
    def set_client_data(self, client):
        self.label_2.setText(f"Nombre: {client.name}")
        self.label.setText(f"Cedula: {client.dni}")
        
    def set_item_text_bill(self, bills):
        for bill in bills:
            self.comboBox.addItem(bill.date)
        
    def clear_content(self):
        self.Table_Antibiotics.clearContents()
        self.Table_Fertilizers.clearContents()
        self.Table_Pests.clearContents()
        
        self.Table_Antibiotics.setRowCount(0)
        self.Table_Fertilizers.setRowCount(0)
        self.Table_Pests.setRowCount(0)
        
        self.Total_Value.setText(f"VALOR TOTAL:")

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Client_Found = QtWidgets.QMainWindow()
    ui = Ui_Client_Found()
    ui.setupUi(Client_Found)
    Client_Found.show()
    sys.exit(app.exec_())
