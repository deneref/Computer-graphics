# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lab03.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1119, 666)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        
        self.centralwidget.setObjectName("centralwidget")
        
        self.c = QtWidgets.QGraphicsView(self.centralwidget)
        self.c.setGeometry(QtCore.QRect(20, 20, 511, 591))
        self.c.setObjectName("c")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(560, 80, 161, 61))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.center_label = QtWidgets.QLabel(self.centralwidget)
        self.center_label.setGeometry(QtCore.QRect(560, 80, 160, 61))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.center_label.setFont(font)
        self.center_label.setObjectName("center_label")
        self.center_label.hide()

        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(560, 130, 151, 61))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(730, 80, 41, 61))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(890, 80, 41, 61))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(730, 130, 41, 61))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(890, 130, 41, 61))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        
        self.Xn_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.Xn_entry.setGeometry(QtCore.QRect(770, 100, 113, 22))
        self.Xn_entry.setObjectName("Xn_entry")

        self.Xc_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.Xc_entry.setGeometry(QtCore.QRect(770, 100, 113, 22))
        self.Xc_entry.setObjectName("Xc_entry")
        self.Xc_entry.hide()
        
        self.Xk_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.Xk_entry.setGeometry(QtCore.QRect(770, 150, 113, 22))
        self.Xk_entry.setObjectName("Xk_entry")

        self.angle_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.angle_entry.setGeometry(QtCore.QRect(770, 150, 113, 22))
        self.angle_entry.setObjectName("angle_entry")
        self.angle_entry.hide()

        self.Yk_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.Yk_entry.setGeometry(QtCore.QRect(940, 150, 113, 22))
        self.Yk_entry.setObjectName("Yk_entry")
        
        self.Yn_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.Yn_entry.setGeometry(QtCore.QRect(940, 100, 113, 22))
        self.Yn_entry.setObjectName("Yn_entry")

        self.Yc_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.Yc_entry.setGeometry(QtCore.QRect(940, 100, 113, 22))
        self.Yc_entry.setObjectName("Yc_entry")
        self.Yc_entry.hide()
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(710, 210, 201, 61))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(780, 460, 61, 61))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.draw_line_button = QtWidgets.QPushButton(self.centralwidget)
        self.draw_line_button.setGeometry(QtCore.QRect(710, 180, 191, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.draw_line_button.setFont(font)
        self.draw_line_button.setObjectName("draw_line_button")
        self.choose_color_button = QtWidgets.QPushButton(self.centralwidget)
        self.choose_color_button.setGeometry(QtCore.QRect(680, 510, 251, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.choose_color_button.setFont(font)
        self.choose_color_button.setObjectName("choose_color_button")

        
        self.clear_all_button = QtWidgets.QPushButton(self.centralwidget)
        #700 560 221 51
        self.clear_all_button.setGeometry(QtCore.QRect(700, 590, 211, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.clear_all_button.setFont(font)
        self.clear_all_button.setObjectName("clear_all_button")

        self.back_color = QtWidgets.QPushButton(self.centralwidget)
        #700 560 221 51
        self.back_color.setGeometry(QtCore.QRect(690, 555, 231, 30))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.back_color.setFont(font)
        self.back_color.setObjectName("back_color")
        
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(540, 10, 551, 80))
        self.groupBox.setObjectName("groupBox")
        self.line_draw_check = QtWidgets.QRadioButton(self.groupBox)
        self.line_draw_check.setGeometry(QtCore.QRect(10, 20, 231, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.line_draw_check.setFont(font)
        self.line_draw_check.setObjectName("line_draw_check")
        self.line_comparison_check = QtWidgets.QRadioButton(self.groupBox)
        self.line_comparison_check.setGeometry(QtCore.QRect(250, 20, 301, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.line_comparison_check.setFont(font)
        self.line_comparison_check.setObjectName("line_comparison_check")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(540, 250, 551, 231))
        self.groupBox_2.setObjectName("groupBox_2")
        self.CDA_check = QtWidgets.QRadioButton(self.groupBox_2)
        self.CDA_check.setGeometry(QtCore.QRect(10, 20, 241, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.CDA_check.setFont(font)
        self.CDA_check.setObjectName("CDA_check")
        self.brez_float_check = QtWidgets.QRadioButton(self.groupBox_2)
        self.brez_float_check.setGeometry(QtCore.QRect(10, 60, 421, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.brez_float_check.setFont(font)
        self.brez_float_check.setObjectName("brez_float_check")
        self.brez_int_check = QtWidgets.QRadioButton(self.groupBox_2)
        self.brez_int_check.setGeometry(QtCore.QRect(10, 100, 341, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.brez_int_check.setFont(font)
        self.brez_int_check.setObjectName("brez_int_check")
        self.brez_no_stup_check = QtWidgets.QRadioButton(self.groupBox_2)
        self.brez_no_stup_check.setGeometry(QtCore.QRect(10, 140, 451, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.brez_no_stup_check.setFont(font)
        self.brez_no_stup_check.setObjectName("brez_no_stup_check")
        self.bibl_check = QtWidgets.QRadioButton(self.groupBox_2)
        self.bibl_check.setGeometry(QtCore.QRect(10, 180, 291, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.bibl_check.setFont(font)
        self.bibl_check.setObjectName("bibl_check")
        self.current_color = QtWidgets.QGraphicsView(self.centralwidget)
        self.current_color.setGeometry(QtCore.QRect(620, 510, 41, 41))
        self.current_color.setObjectName("current_color")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1119, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Компьютерная графика. Лабораторная Работа №3"))
        self.label.setText(_translate("MainWindow", "Начало отрезка"))
        self.center_label.setText(_translate("MainWindow", "Центр"))
        self.label_2.setText(_translate("MainWindow", "Конец отрезка"))
        self.label_6.setText(_translate("MainWindow", "Xn:"))
        self.label_7.setText(_translate("MainWindow", "Yn:"))
        self.label_8.setText(_translate("MainWindow", "Xk:"))
        self.label_9.setText(_translate("MainWindow", "Yk:"))
        self.label_3.setText(_translate("MainWindow", "Выбор алгоритма"))
        self.label_4.setText(_translate("MainWindow", "Цвет"))
        self.draw_line_button.setText(_translate("MainWindow", "Построить"))
        self.choose_color_button.setText(_translate("MainWindow", "Выбрать цвет"))
        self.clear_all_button.setText(_translate("MainWindow", "Очистить"))
        self.back_color.setText(_translate("MainWindow", "Установить цвет фона"))
        self.groupBox.setTitle(_translate("MainWindow", "Режим"))
        self.line_draw_check.setText(_translate("MainWindow", "Построение отрезков"))
        self.line_comparison_check.setText(_translate("MainWindow", "Визуальные характеристики"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Доступные алгоритмы"))
        self.CDA_check.setText(_translate("MainWindow", "ЦДА"))
        self.brez_float_check.setText(_translate("MainWindow", "Брезенхейма с действительным числами"))
        self.brez_int_check.setText(_translate("MainWindow", "Брезенхейма с целыми числами"))
        self.brez_no_stup_check.setText(_translate("MainWindow", "Брезенхейма с устранением ступенчатости"))
        self.bibl_check.setText(_translate("MainWindow", "Библиотечный алгоритм"))

