# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'comprar_producto.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(920, 643)
        self.Background = QtWidgets.QWidget(MainWindow)
        self.Background.setStyleSheet("QWidget{\n"
"    background-color: rgb(236, 236, 236)\n"
"}")
        self.Background.setObjectName("Background")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Background)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.Background)
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Type_Products = QtWidgets.QHBoxLayout()
        self.Type_Products.setObjectName("Type_Products")
        self.Antibiotics = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Antibiotics.setFont(font)
        self.Antibiotics.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Antibiotics.setStyleSheet("QPushButton{\n"
"    background-color: rgb(252, 104, 104);\n"
"    padding: 10px;\n"
"    border-radius: 10px;\n"
"    border: 1px solid black\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: rgb(245, 132, 132);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: rgb(150, 47, 47);\n"
"    color: white\n"
"}")
        self.Antibiotics.setObjectName("Antibiotics")
        self.Type_Products.addWidget(self.Antibiotics)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.Type_Products.addItem(spacerItem)
        self.Fertilizers = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Fertilizers.setFont(font)
        self.Fertilizers.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Fertilizers.setStyleSheet("QPushButton{\n"
"    background-color: rgb(72, 188, 250);\n"
"    padding: 10px;\n"
"    border-radius: 10px;\n"
"    border: 1px solid black\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: rgb(144, 210, 245);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: rgb(25, 90, 125);\n"
"    color: white\n"
"}")
        self.Fertilizers.setObjectName("Fertilizers")
        self.Type_Products.addWidget(self.Fertilizers)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.Type_Products.addItem(spacerItem1)
        self.Pest_Control = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Pest_Control.setFont(font)
        self.Pest_Control.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Pest_Control.setStyleSheet("QPushButton{\n"
"    background-color: rgb(70, 224, 87);\n"
"    padding: 10px;\n"
"    border-radius: 10px;\n"
"    border: 1px solid black\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: rgb(125, 227, 136);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: rgb(28, 120, 38);\n"
"    color: white\n"
"}")
        self.Pest_Control.setObjectName("Pest_Control")
        self.Type_Products.addWidget(self.Pest_Control)
        self.verticalLayout.addLayout(self.Type_Products)
        self.Purchase = QtWidgets.QFrame(self.frame)
        self.Purchase.setMinimumSize(QtCore.QSize(900, 400))
        self.Purchase.setStyleSheet("")
        self.Purchase.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Purchase.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Purchase.setObjectName("Purchase")
        self.frame_3 = QtWidgets.QFrame(self.Purchase)
        self.frame_3.setGeometry(QtCore.QRect(600, 0, 300, 400))
        self.frame_3.setMinimumSize(QtCore.QSize(231, 400))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Purchased_Products = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Purchased_Products.setFont(font)
        self.Purchased_Products.setStyleSheet("QLabel{\n"
"    background-color: rgb(255, 255, 127);\n"
"    border: 1px solid black\n"
"}")
        self.Purchased_Products.setScaledContents(False)
        self.Purchased_Products.setAlignment(QtCore.Qt.AlignCenter)
        self.Purchased_Products.setObjectName("Purchased_Products")
        self.verticalLayout_2.addWidget(self.Purchased_Products)
        self.List_Purchased_Products = QtWidgets.QListWidget(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.List_Purchased_Products.setFont(font)
        self.List_Purchased_Products.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.List_Purchased_Products.setStyleSheet("QListWidget{\n"
"    background-color: white\n"
"}\n"
"\n"
"QListWidget::item:hover{\n"
"    background-color: rgb(170, 255, 127);\n"
"}")
        self.List_Purchased_Products.setObjectName("List_Purchased_Products")
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.List_Purchased_Products.addItem(item)
        self.verticalLayout_2.addWidget(self.List_Purchased_Products)
        self.frame_4 = QtWidgets.QFrame(self.Purchase)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 610, 400))
        self.frame_4.setMinimumSize(QtCore.QSize(601, 400))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.Table_Antibiotics = QtWidgets.QTableWidget(self.frame_4)
        self.Table_Antibiotics.setGeometry(QtCore.QRect(10, 10, 471, 311))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Table_Antibiotics.sizePolicy().hasHeightForWidth())
        self.Table_Antibiotics.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Table_Antibiotics.setFont(font)
        self.Table_Antibiotics.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Table_Antibiotics.setStyleSheet("QHeaderView::section{\n"
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
        self.Table_Antibiotics.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Table_Antibiotics.setAutoScrollMargin(16)
        self.Table_Antibiotics.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.Table_Antibiotics.setProperty("showDropIndicator", False)
        self.Table_Antibiotics.setDragDropOverwriteMode(False)
        self.Table_Antibiotics.setAlternatingRowColors(False)
        self.Table_Antibiotics.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.Table_Antibiotics.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.Table_Antibiotics.setShowGrid(True)
        self.Table_Antibiotics.setGridStyle(QtCore.Qt.SolidLine)
        self.Table_Antibiotics.setWordWrap(False)
        self.Table_Antibiotics.setCornerButtonEnabled(True)
        self.Table_Antibiotics.setObjectName("Table_Antibiotics")
        self.Table_Antibiotics.setColumnCount(4)
        self.Table_Antibiotics.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.Table_Antibiotics.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.Table_Antibiotics.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.Table_Antibiotics.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.Table_Antibiotics.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.Table_Antibiotics.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.Table_Antibiotics.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.Table_Antibiotics.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Antibiotics.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Antibiotics.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Antibiotics.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Antibiotics.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Antibiotics.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Antibiotics.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Antibiotics.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Antibiotics.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Antibiotics.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Antibiotics.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Antibiotics.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Antibiotics.setItem(2, 3, item)
        self.Table_Antibiotics.horizontalHeader().setVisible(True)
        self.Table_Antibiotics.horizontalHeader().setCascadingSectionResizes(False)
        self.Table_Antibiotics.horizontalHeader().setDefaultSectionSize(110)
        self.Table_Antibiotics.horizontalHeader().setHighlightSections(True)
        self.Table_Antibiotics.horizontalHeader().setMinimumSectionSize(110)
        self.Table_Antibiotics.verticalHeader().setCascadingSectionResizes(True)
        self.Table_Pest_Control = QtWidgets.QTableWidget(self.frame_4)
        self.Table_Pest_Control.setGeometry(QtCore.QRect(10, 10, 591, 261))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Table_Pest_Control.sizePolicy().hasHeightForWidth())
        self.Table_Pest_Control.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Table_Pest_Control.setFont(font)
        self.Table_Pest_Control.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Table_Pest_Control.setStyleSheet("QHeaderView::section{\n"
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
        self.Table_Pest_Control.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Table_Pest_Control.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.Table_Pest_Control.setAutoScrollMargin(16)
        self.Table_Pest_Control.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.Table_Pest_Control.setProperty("showDropIndicator", False)
        self.Table_Pest_Control.setDragDropOverwriteMode(False)
        self.Table_Pest_Control.setAlternatingRowColors(False)
        self.Table_Pest_Control.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.Table_Pest_Control.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.Table_Pest_Control.setTextElideMode(QtCore.Qt.ElideRight)
        self.Table_Pest_Control.setShowGrid(True)
        self.Table_Pest_Control.setGridStyle(QtCore.Qt.SolidLine)
        self.Table_Pest_Control.setWordWrap(False)
        self.Table_Pest_Control.setCornerButtonEnabled(True)
        self.Table_Pest_Control.setObjectName("Table_Pest_Control")
        self.Table_Pest_Control.setColumnCount(5)
        self.Table_Pest_Control.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.Table_Pest_Control.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.Table_Pest_Control.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.Table_Pest_Control.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.Table_Pest_Control.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.Table_Pest_Control.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.Table_Pest_Control.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Pest_Control.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.Table_Pest_Control.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Pest_Control.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Pest_Control.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Pest_Control.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Pest_Control.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Pest_Control.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Pest_Control.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Pest_Control.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Pest_Control.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Pest_Control.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Pest_Control.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Pest_Control.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Pest_Control.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Pest_Control.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Pest_Control.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Pest_Control.setItem(2, 4, item)
        self.Table_Pest_Control.horizontalHeader().setVisible(True)
        self.Table_Pest_Control.horizontalHeader().setCascadingSectionResizes(False)
        self.Table_Pest_Control.horizontalHeader().setDefaultSectionSize(110)
        self.Table_Pest_Control.horizontalHeader().setHighlightSections(True)
        self.Table_Pest_Control.verticalHeader().setCascadingSectionResizes(True)
        self.Table_Fertilizers = QtWidgets.QTableWidget(self.frame_4)
        self.Table_Fertilizers.setGeometry(QtCore.QRect(10, 10, 581, 251))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Table_Fertilizers.sizePolicy().hasHeightForWidth())
        self.Table_Fertilizers.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Table_Fertilizers.setFont(font)
        self.Table_Fertilizers.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Table_Fertilizers.setStyleSheet("QHeaderView::section{\n"
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
        self.Table_Fertilizers.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Table_Fertilizers.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Table_Fertilizers.setAutoScrollMargin(16)
        self.Table_Fertilizers.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.Table_Fertilizers.setProperty("showDropIndicator", False)
        self.Table_Fertilizers.setDragDropOverwriteMode(False)
        self.Table_Fertilizers.setAlternatingRowColors(False)
        self.Table_Fertilizers.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.Table_Fertilizers.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.Table_Fertilizers.setTextElideMode(QtCore.Qt.ElideRight)
        self.Table_Fertilizers.setShowGrid(True)
        self.Table_Fertilizers.setGridStyle(QtCore.Qt.SolidLine)
        self.Table_Fertilizers.setWordWrap(False)
        self.Table_Fertilizers.setCornerButtonEnabled(True)
        self.Table_Fertilizers.setObjectName("Table_Fertilizers")
        self.Table_Fertilizers.setColumnCount(5)
        self.Table_Fertilizers.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.Table_Fertilizers.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.Table_Fertilizers.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.Table_Fertilizers.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.Table_Fertilizers.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.Table_Fertilizers.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.Table_Fertilizers.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Fertilizers.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.Table_Fertilizers.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Fertilizers.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Fertilizers.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Fertilizers.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Fertilizers.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Fertilizers.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Fertilizers.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Fertilizers.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Fertilizers.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Fertilizers.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Fertilizers.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Fertilizers.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Fertilizers.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Fertilizers.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Fertilizers.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.Table_Fertilizers.setItem(2, 4, item)
        self.Table_Fertilizers.horizontalHeader().setVisible(True)
        self.Table_Fertilizers.horizontalHeader().setCascadingSectionResizes(False)
        self.Table_Fertilizers.horizontalHeader().setDefaultSectionSize(110)
        self.Table_Fertilizers.horizontalHeader().setHighlightSections(True)
        self.Table_Fertilizers.horizontalHeader().setMinimumSectionSize(110)
        self.Table_Fertilizers.verticalHeader().setCascadingSectionResizes(True)
        self.verticalLayout.addWidget(self.Purchase)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(900, 90))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.Add_Products = QtWidgets.QPushButton(self.frame_2)
        self.Add_Products.setGeometry(QtCore.QRect(190, 20, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Add_Products.setFont(font)
        self.Add_Products.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Add_Products.setStyleSheet("QPushButton{\n"
"    background-color: rgb(170, 0, 0);\n"
"    color: white;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    border: 2px solid black\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: rgb(245, 175, 137);\n"
"    color: black\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: white\n"
"}")
        self.Add_Products.setObjectName("Add_Products")
        self.End_Purchase = QtWidgets.QPushButton(self.frame_2)
        self.End_Purchase.setGeometry(QtCore.QRect(500, 20, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.End_Purchase.setFont(font)
        self.End_Purchase.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.End_Purchase.setStyleSheet("QPushButton{\n"
"    background-color: rgb(170, 0, 0);\n"
"    color: white;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    border: 2px solid black\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: rgb(245, 175, 137);\n"
"    color: black\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: white\n"
"}")
        self.End_Purchase.setObjectName("End_Purchase")
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.Background)

        self.retranslateUi(MainWindow)
        self.Fertilizers.clicked.connect(self.Table_Antibiotics.hide) # type: ignore
        self.Pest_Control.clicked.connect(self.Table_Antibiotics.hide) # type: ignore
        self.Antibiotics.clicked.connect(self.Table_Antibiotics.show) # type: ignore
        self.Fertilizers.clicked.connect(self.Table_Fertilizers.show) # type: ignore
        self.Antibiotics.clicked.connect(self.Table_Fertilizers.hide) # type: ignore
        self.Pest_Control.clicked.connect(self.Table_Fertilizers.hide) # type: ignore
        self.Pest_Control.clicked.connect(self.Table_Pest_Control.show) # type: ignore
        self.Fertilizers.clicked.connect(self.Table_Pest_Control.hide) # type: ignore
        self.Antibiotics.clicked.connect(self.Table_Pest_Control.hide) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Inventario"))
        self.Antibiotics.setText(_translate("MainWindow", "Antibióticos"))
        self.Fertilizers.setText(_translate("MainWindow", "Fertilizantes"))
        self.Pest_Control.setText(_translate("MainWindow", "Control de plagas"))
        self.Purchased_Products.setText(_translate("MainWindow", "PRODUCTOS COMPRADOS"))
        __sortingEnabled = self.List_Purchased_Products.isSortingEnabled()
        self.List_Purchased_Products.setSortingEnabled(False)
        item = self.List_Purchased_Products.item(0)
        item.setText(_translate("MainWindow", "Texto de prueba"))
        self.List_Purchased_Products.setSortingEnabled(__sortingEnabled)
        self.Table_Antibiotics.setSortingEnabled(False)
        item = self.Table_Antibiotics.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.Table_Antibiotics.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.Table_Antibiotics.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.Table_Antibiotics.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "NOMBRE"))
        item = self.Table_Antibiotics.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "DOSIS"))
        item = self.Table_Antibiotics.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "TIPO"))
        item = self.Table_Antibiotics.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "COSTO"))
        __sortingEnabled = self.Table_Antibiotics.isSortingEnabled()
        self.Table_Antibiotics.setSortingEnabled(False)
        item = self.Table_Antibiotics.item(0, 0)
        item.setText(_translate("MainWindow", "Oxitrat"))
        item = self.Table_Antibiotics.item(0, 1)
        item.setText(_translate("MainWindow", "400ml"))
        item = self.Table_Antibiotics.item(0, 2)
        item.setText(_translate("MainWindow", "Bovino"))
        item = self.Table_Antibiotics.item(0, 3)
        item.setText(_translate("MainWindow", "114000"))
        item = self.Table_Antibiotics.item(1, 0)
        item.setText(_translate("MainWindow", "Edo Benpropen"))
        item = self.Table_Antibiotics.item(1, 1)
        item.setText(_translate("MainWindow", "550ml"))
        item = self.Table_Antibiotics.item(1, 2)
        item.setText(_translate("MainWindow", "Caprino"))
        item = self.Table_Antibiotics.item(1, 3)
        item.setText(_translate("MainWindow", "200000"))
        item = self.Table_Antibiotics.item(2, 0)
        item.setText(_translate("MainWindow", "Aurotilmicosin"))
        item = self.Table_Antibiotics.item(2, 1)
        item.setText(_translate("MainWindow", "500ml"))
        item = self.Table_Antibiotics.item(2, 2)
        item.setText(_translate("MainWindow", "Porcinos"))
        item = self.Table_Antibiotics.item(2, 3)
        item.setText(_translate("MainWindow", "150000"))
        self.Table_Antibiotics.setSortingEnabled(__sortingEnabled)
        self.Table_Pest_Control.setSortingEnabled(False)
        item = self.Table_Pest_Control.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.Table_Pest_Control.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.Table_Pest_Control.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.Table_Pest_Control.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "NOMBRE"))
        item = self.Table_Pest_Control.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ICA"))
        item = self.Table_Pest_Control.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "FRECUENCIA"))
        item = self.Table_Pest_Control.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "P. DE CARENCIA"))
        item = self.Table_Pest_Control.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "COSTO"))
        __sortingEnabled = self.Table_Pest_Control.isSortingEnabled()
        self.Table_Pest_Control.setSortingEnabled(False)
        item = self.Table_Pest_Control.item(0, 0)
        item.setText(_translate("MainWindow", "Curathane"))
        item = self.Table_Pest_Control.item(0, 1)
        item.setText(_translate("MainWindow", "LKJ4682"))
        item = self.Table_Pest_Control.item(0, 2)
        item.setText(_translate("MainWindow", "10 días"))
        item = self.Table_Pest_Control.item(0, 3)
        item.setText(_translate("MainWindow", "4"))
        item = self.Table_Pest_Control.item(0, 4)
        item.setText(_translate("MainWindow", "82000"))
        item = self.Table_Pest_Control.item(1, 0)
        item.setText(_translate("MainWindow", "Rovral FLO"))
        item = self.Table_Pest_Control.item(1, 1)
        item.setText(_translate("MainWindow", "HBV7591"))
        item = self.Table_Pest_Control.item(1, 2)
        item.setText(_translate("MainWindow", "8 días"))
        item = self.Table_Pest_Control.item(1, 3)
        item.setText(_translate("MainWindow", "3"))
        item = self.Table_Pest_Control.item(1, 4)
        item.setText(_translate("MainWindow", "458000"))
        item = self.Table_Pest_Control.item(2, 0)
        item.setText(_translate("MainWindow", "Sincosin"))
        item = self.Table_Pest_Control.item(2, 1)
        item.setText(_translate("MainWindow", "WQP8426"))
        item = self.Table_Pest_Control.item(2, 2)
        item.setText(_translate("MainWindow", "10 días"))
        item = self.Table_Pest_Control.item(2, 3)
        item.setText(_translate("MainWindow", "5"))
        item = self.Table_Pest_Control.item(2, 4)
        item.setText(_translate("MainWindow", "123000"))
        self.Table_Pest_Control.setSortingEnabled(__sortingEnabled)
        self.Table_Fertilizers.setSortingEnabled(False)
        item = self.Table_Fertilizers.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.Table_Fertilizers.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.Table_Fertilizers.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.Table_Fertilizers.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "NOMBRE"))
        item = self.Table_Fertilizers.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ICA"))
        item = self.Table_Fertilizers.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "FRECUENCIA"))
        item = self.Table_Fertilizers.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ÚLTIMA APLIC."))
        item = self.Table_Fertilizers.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "COSTO"))
        __sortingEnabled = self.Table_Fertilizers.isSortingEnabled()
        self.Table_Fertilizers.setSortingEnabled(False)
        item = self.Table_Fertilizers.item(0, 0)
        item.setText(_translate("MainWindow", "Sulfato amónico"))
        item = self.Table_Fertilizers.item(0, 1)
        item.setText(_translate("MainWindow", "AVH1239"))
        item = self.Table_Fertilizers.item(0, 2)
        item.setText(_translate("MainWindow", "15 días"))
        item = self.Table_Fertilizers.item(0, 3)
        item.setText(_translate("MainWindow", "19/10/2023"))
        item = self.Table_Fertilizers.item(0, 4)
        item.setText(_translate("MainWindow", "55000"))
        item = self.Table_Fertilizers.item(1, 0)
        item.setText(_translate("MainWindow", "Cloruro potásico"))
        item = self.Table_Fertilizers.item(1, 1)
        item.setText(_translate("MainWindow", "BZD6935"))
        item = self.Table_Fertilizers.item(1, 2)
        item.setText(_translate("MainWindow", "30 días"))
        item = self.Table_Fertilizers.item(1, 3)
        item.setText(_translate("MainWindow", "15/10/2023"))
        item = self.Table_Fertilizers.item(1, 4)
        item.setText(_translate("MainWindow", "70000"))
        item = self.Table_Fertilizers.item(2, 0)
        item.setText(_translate("MainWindow", "Superfosfato simple"))
        item = self.Table_Fertilizers.item(2, 1)
        item.setText(_translate("MainWindow", "PLT9531"))
        item = self.Table_Fertilizers.item(2, 2)
        item.setText(_translate("MainWindow", "7 días"))
        item = self.Table_Fertilizers.item(2, 3)
        item.setText(_translate("MainWindow", "12/10/2023"))
        item = self.Table_Fertilizers.item(2, 4)
        item.setText(_translate("MainWindow", "45000"))
        self.Table_Fertilizers.setSortingEnabled(__sortingEnabled)
        self.Add_Products.setText(_translate("MainWindow", "AGREGAR A CARRITO"))
        self.End_Purchase.setText(_translate("MainWindow", "FINALIZAR COMPRA  >>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())