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

        
        self.label_center = QtWidgets.QLabel(self.centralwidget)
        self.label_center.setGeometry(QtCore.QRect(560, 130, 151, 61))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.label_center.setFont(font)
        self.label_center.setObjectName("label_center")
        self.label_xc = QtWidgets.QLabel(self.centralwidget)
        self.label_xc.setGeometry(QtCore.QRect(730, 80, 41, 61))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.label_xc.setFont(font)
        self.label_xc.setObjectName("label_xc")
        self.label_yc = QtWidgets.QLabel(self.centralwidget)
        self.label_yc.setGeometry(QtCore.QRect(890, 80, 41, 61))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.label_yc.setFont(font)
        self.label_yc.setObjectName("label_yc")
        self.label_rad = QtWidgets.QLabel(self.centralwidget)
        self.label_rad.setGeometry(QtCore.QRect(730, 130, 41, 61))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.label_rad.setFont(font)
        self.label_rad.setObjectName("label_rad")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(890, 130, 41, 61))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        
        self.xc_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.xc_entry.setGeometry(QtCore.QRect(770, 100, 113, 22))
        self.xc_entry.setObjectName("xc_entry")

##        self.Xc_entry = QtWidgets.QLineEdit(self.centralwidget)
##        self.Xc_entry.setGeometry(QtCore.QRect(770, 100, 113, 22))
##        self.Xc_entry.setObjectName("Xc_entry")
##        self.Xc_entry.hide()
        
        self.r_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.r_entry.setGeometry(QtCore.QRect(770, 150, 113, 22))
        self.r_entry.setObjectName("r_entry")

        self.angle_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.angle_entry.setGeometry(QtCore.QRect(770, 150, 113, 22))
        self.angle_entry.setObjectName("angle_entry")
        self.angle_entry.hide()

        self.b_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.b_entry.setGeometry(QtCore.QRect(940, 150, 113, 22))
        self.b_entry.setObjectName("b_entry")
        self.b_entry.hide
        
        self.yc_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.yc_entry.setGeometry(QtCore.QRect(940, 100, 113, 22))
        self.yc_entry.setObjectName("yc_entry")

##        self.Yc_entry = QtWidgets.QLineEdit(self.centralwidget)
##        self.Yc_entry.setGeometry(QtCore.QRect(940, 100, 113, 22))
##        self.Yc_entry.setObjectName("Yc_entry")
##        self.Yc_entry.hide()
        
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
        self.groupBox.setGeometry(QtCore.QRect(540, 6, 225, 90))
        self.groupBox.setObjectName("groupBox")

        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(770, 6, 225, 90))
        self.groupBox_3.setObjectName("groupBox")

        self.info_button = QtWidgets.QPushButton(self.centralwidget)
        #700 560 221 51
        self.info_button.setGeometry(QtCore.QRect(1070, 10, 40, 40))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.info_button.setFont(font)
        self.info_button.setObjectName("info_button")


        #верхние чеки
        self.round_draw_check = QtWidgets.QRadioButton(self.groupBox)
        self.round_draw_check.setGeometry(QtCore.QRect(10, 10, 231, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.round_draw_check.setFont(font)
        self.round_draw_check.setObjectName("round_draw_check")

        self.ellipse_draw_check = QtWidgets.QRadioButton(self.groupBox)
        self.ellipse_draw_check.setGeometry(QtCore.QRect(10, 45, 231, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.ellipse_draw_check.setFont(font)
        self.ellipse_draw_check.setObjectName("ellipse_draw_check")
        
        self.draw_one_check = QtWidgets.QRadioButton(self.groupBox_3)
        self.draw_one_check.setGeometry(QtCore.QRect(10, 10, 231, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.draw_one_check.setFont(font)
        self.draw_one_check.setObjectName("draw_one_check")

        self.draw_mult_check = QtWidgets.QRadioButton(self.groupBox_3)
        self.draw_mult_check.setGeometry(QtCore.QRect(10, 45, 231, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.draw_mult_check.setFont(font)
        self.draw_mult_check.setObjectName("draw_one_check")
        
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(540, 250, 551, 231))
        self.groupBox_2.setObjectName("groupBox_2")
        self.kanonich_check = QtWidgets.QRadioButton(self.groupBox_2)
        self.kanonich_check.setGeometry(QtCore.QRect(10, 20, 270, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.kanonich_check.setFont(font)
        self.kanonich_check.setObjectName("kanonich_check")
        
        self.param_check = QtWidgets.QRadioButton(self.groupBox_2)
        self.param_check.setGeometry(QtCore.QRect(10, 60, 421, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.param_check.setFont(font)
        self.param_check.setObjectName("param_check")
        self.brez_check = QtWidgets.QRadioButton(self.groupBox_2)
        self.brez_check.setGeometry(QtCore.QRect(10, 100, 341, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.brez_check.setFont(font)
        self.brez_check.setObjectName("brez_check")
        self.sr_toch_check = QtWidgets.QRadioButton(self.groupBox_2)
        self.sr_toch_check.setGeometry(QtCore.QRect(10, 140, 451, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.sr_toch_check.setFont(font)
        self.sr_toch_check.setObjectName("sr_toch_check")
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

        #тоглы
        self.draw_one_check.toggled.connect(self.switch_draws)
        self.round_draw_check.toggled.connect(self.switch_figure)
        self.round_draw_check.toggle()
        self.draw_one_check.toggle()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Компьютерная графика. Лабораторная Работа №4"))
        self.label.setText(_translate("MainWindow", "Центр"))
        self.center_label.setText(_translate("MainWindow", "Центр"))
        self.label_center.setText(_translate("MainWindow", "Радиус"))
        self.label_xc.setText(_translate("MainWindow", "Xс:"))
        self.label_yc.setText(_translate("MainWindow", "Yс:"))
        self.label_rad.setText(_translate("MainWindow", "r:"))
        self.label_9.setText(_translate("MainWindow", "b:"))
        self.label_3.setText(_translate("MainWindow", "Выбор алгоритма"))
        self.label_4.setText(_translate("MainWindow", "Цвет"))
        self.draw_line_button.setText(_translate("MainWindow", "Построить"))
        self.choose_color_button.setText(_translate("MainWindow", "Выбрать цвет"))
        self.clear_all_button.setText(_translate("MainWindow", "Очистить"))
        self.back_color.setText(_translate("MainWindow", "Установить цвет фона"))
        self.groupBox.setTitle(_translate("MainWindow", "Что рисуем?"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Режим"))
        self.round_draw_check.setText(_translate("MainWindow", "Окружность"))
        self.ellipse_draw_check.setText(_translate("MainWindow", "Эллипс"))
        self.draw_one_check.setText(_translate("MainWindow", "Одна фигура"))
        self.draw_mult_check.setText(_translate("MainWindow", "Несколько"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Доступные алгоритмы"))
        self.kanonich_check.setText(_translate("MainWindow", "Каноническое уравнение"))
        self.param_check.setText(_translate("MainWindow", "Параметрическое уравнение"))
        self.brez_check.setText(_translate("MainWindow", "Брезенхейма"))
        self.sr_toch_check.setText(_translate("MainWindow", "Средней точки"))
        self.bibl_check.setText(_translate("MainWindow", "Библиотечный алгоритм"))
        self.info_button.setText(_translate("MainWindow", "?"))

    def switch_draws(self):
        if self.draw_one_check.isChecked():
            self.switch_figure()
        elif self.draw_mult_check.isChecked():
            self.label_9.show()
            self.label_9.setText("k:")
            self.b_entry.show()
            if self.ellipse_draw_check.isChecked():
                self.label_center.setText("Полуоси")
                self.label_rad.setText("a:")
            elif self.round_draw_check.isChecked():
                self.label_center.setText("Радиус")
                self.label_rad.setText("r:")
                self.label_9.show()
                self.label_9.setText("k:")
                self.b_entry.show()
    def switch_figure(self):
        if self.round_draw_check.isChecked():
            self.b_entry.hide()
            self.label_center.setText("Радиус")
            self.label_9.hide()
            self.label_rad.setText("r:")
        elif self.ellipse_draw_check.isChecked():
            self.b_entry.show()
            self.label_9.show()
            self.label_rad.setText("a:")
            self.label_center.setText("Полуоси")
            if self.draw_mult_check.isChecked():
                self.label_9.setText("k:")
            elif self.draw_one_check.isChecked():
                self.label_9.setText("b")

class Message_box():
    def __init__(self):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText("wtf")
        #self.msg.exec_()

    def wrong_input(self):
        self.msg.setIcon(QtWidgets.QMessageBox.Warning)
        self.msg.setText("Вы ввели в поля неподходящие значения")
        self.msg.setInformativeText("Кроме того, не стоит оставлять их пустыми")
        self.msg.setWindowTitle("Ошибка ввода!")
        self.msg.setDetailedText("Значения должны быть целыми числами")
        self.msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.msg.exec_()

    def show_info(self):
        self.msg.setIcon(QtWidgets.QMessageBox.Information)
        self.msg.setText("Программа позволяет построить окружности и эллипсы при помощи различных алгоритмов")
        self.msg.setInformativeText(("Все вводимые значения должны быть целыми.\n"+\
                                     "Для того чтобы построить окружность необходим центр и радиус.\n"+\
                                     "Для эллипса - центр и полуоси.\n"+\
                                     "Для того, чтобы построить концентрические окружности или эллипсы "+\
                                     "введите максимальный радиус и желаемое колличество фигур."))
        self.msg.setWindowTitle("Информация")
        self.msg.setDetailedText("Программу, кстати, сделал студент ИУ7-44 Мокеев Даниил")
        self.msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.msg.exec_()        


   
