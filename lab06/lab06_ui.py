# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lab06_ui.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1593, 870)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.c = QtWidgets.QGraphicsView(self.centralwidget)
        self.c.setGeometry(QtCore.QRect(15, 11, 1201, 811))
        self.c.setObjectName("c")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(1220, 10, 351, 441))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 30, 321, 401))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.y_entry = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.y_entry.setObjectName("y_entry")
        self.gridLayout.addWidget(self.y_entry, 1, 2, 1, 1)
        self.add_point = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.add_point.setObjectName("add_point")
        self.gridLayout.addWidget(self.add_point, 2, 0, 1, 4)
        self.x_entry = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.x_entry.setObjectName("x_entry")
        self.gridLayout.addWidget(self.x_entry, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.point_num_entry = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.point_num_entry.setObjectName("point_num_entry")
        self.gridLayout.addWidget(self.point_num_entry, 3, 2, 1, 1)
        self.clear_all = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.clear_all.setObjectName("clear_all")
        self.gridLayout.addWidget(self.clear_all, 6, 0, 1, 3)
        self.delete_point = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.delete_point.setObjectName("delete_point")
        self.gridLayout.addWidget(self.delete_point, 3, 0, 1, 2)
        self.list_point = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.list_point.setObjectName("list_point")
        self.gridLayout.addWidget(self.list_point, 7, 0, 1, 4)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(1220, 449, 351, 101))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(9, 19, 331, 72))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.no_stop = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.no_stop.setFont(font)
        self.no_stop.setObjectName("no_stop")
        self.gridLayout_2.addWidget(self.no_stop, 0, 0, 1, 1)
        self.with_stop = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.with_stop.setFont(font)
        self.with_stop.setObjectName("with_stop")
        self.gridLayout_2.addWidget(self.with_stop, 2, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(1229, 549, 341, 191))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_3)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 20, 331, 176))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 0, 1, 1)
        self.col_inside_shoose = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.col_inside_shoose.setObjectName("col_inside_shoose")
        self.gridLayout_3.addWidget(self.col_inside_shoose, 3, 2, 1, 1)
        self.c_col_inside = QtWidgets.QGraphicsView(self.gridLayoutWidget_3)
        self.c_col_inside.setMaximumSize(QtCore.QSize(50, 50))
        self.c_col_inside.setObjectName("c_col_inside")
        self.gridLayout_3.addWidget(self.c_col_inside, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 1, 1, 2)
        self.c_col_border = QtWidgets.QGraphicsView(self.gridLayoutWidget_3)
        self.c_col_border.setMaximumSize(QtCore.QSize(50, 50))
        self.c_col_border.setObjectName("c_col_border")
        self.gridLayout_3.addWidget(self.c_col_border, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 2, 1, 1, 2)
        self.col_border_choose = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.col_border_choose.setObjectName("col_border_choose")
        self.gridLayout_3.addWidget(self.col_border_choose, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 4, 2, 1, 1)
        self.fill = QtWidgets.QPushButton(self.centralwidget)
        self.fill.setGeometry(QtCore.QRect(1230, 777, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fill.setFont(font)
        self.fill.setObjectName("fill")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(1230, 740, 341, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.zetr_pix_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.zetr_pix_button.setObjectName("zetr_pix_button")
        self.horizontalLayout.addWidget(self.zetr_pix_button)
        spacerItem4 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.zamkn_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.zamkn_button.setObjectName("zamkn_button")
        self.horizontalLayout.addWidget(self.zamkn_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1593, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Добавление и редактирование точек"))
        self.label.setText(_translate("MainWindow", "Координата Х"))
        self.label_2.setText(_translate("MainWindow", "Координата Y"))
        self.add_point.setText(_translate("MainWindow", "Добавить точку"))
        self.clear_all.setText(_translate("MainWindow", "Очистить все поля"))
        self.delete_point.setText(_translate("MainWindow", "Удалить вершину номер"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Режим"))
        self.no_stop.setText(_translate("MainWindow", "Без прерывания"))
        self.with_stop.setText(_translate("MainWindow", "С прерыванием"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Выбор цвета"))
        self.col_inside_shoose.setText(_translate("MainWindow", "Выбрать цвет"))
        self.label_4.setText(_translate("MainWindow", "                    Цвет границы"))
        self.label_6.setText(_translate("MainWindow", "                    Цвет закраски"))
        self.col_border_choose.setText(_translate("MainWindow", "Выбрать цвет"))
        self.fill.setText(_translate("MainWindow", "Закрасить"))
        self.zetr_pix_button.setText(_translate("MainWindow", "Добавить затравку"))
        self.zamkn_button.setText(_translate("MainWindow", "Замкнуть линию"))


