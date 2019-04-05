import sys
from interface4 import *
from PyQt5 import *
from math import *

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        #устанавливает интерфейс
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #настройка размеров канваса
        self.scene_width = 500
        self.scene_height = 600
        self.ui.c.setGeometry(QtCore.QRect(20, 20,\
                                        20+self.scene_width, 20+self.scene_height))

        #установка текущего цвета
        self.color = QtGui.QColor("#fc6c2d")
        self.pen = QtGui.QPen(self.color)
        self.brush = QtGui.QBrush(QtGui.QColor(200,200,215,255), QtCore.Qt.SolidPattern)
        self.rect = QtCore.QRectF(QtCore.QPointF(10, 10), QtCore.QSizeF(30, 30))
    
        self.color_check = QtWidgets.QGraphicsScene()
        self.ui.current_color.setScene(self.color_check)
        self.change_color_check()
        
        #устанавливает сцену
        self.scene = QtWidgets.QGraphicsScene()
        self.ui.c.setScene(self.scene)
        self.draw_coord()
     
        # Здесь прописываем событие нажатия на кнопку                     
##        self.ui.draw_line_button.clicked.connect(self.draw_line)
        self.ui.clear_all_button.clicked.connect(self.Clear_Scene)
        self.ui.choose_color_button.clicked.connect(self.color_choose)
        self.ui.back_color.clicked.connect(self.back_color_set)

    def Clear_Scene(self):
        self.scene.clear()
        self.draw_coord()

    def change_color_check(self):
        self.color_check.addRect(self.rect, self.pen)
        painter = QtGui.QPainter(self)
        painter.setPen(self.pen)
        painter.setBrush(self.brush)
        self.pen.setWidth(3)
        self.color_check.addRect(self.rect, self.pen)
        self.pen.setWidth(1)

    def draw_coord(self):
        ox = QtCore.QLineF(self.scene_width//2, 0,\
                           self.scene_width//2, self.scene_height)
        self.scene.addLine(ox)
        self.scene.addLine(0, self.scene_height//2,\
                           self.scene_width, self.scene_height//2)
        
    def draw_line(self):
        if self.ui.round_draw_check.isChecked():
            try:
                xn = int(self.ui.Xn_entry.text())
                yn = int(self.ui.Yn_entry.text())
                xk = int(self.ui.Xk_entry.text())
                yk = int(self.ui.Yk_entry.text())
            except:
                print("what")
                return 0
            if self.ui.CDA_check.isChecked():
                self.draw_cda_line(xn,yn,xk,yk)
            elif self.ui.bibl_check.isChecked():
                self.draw_bible_line(xn,yn,xk,yk)
            elif self.ui.brez_float_check.isChecked():
                self.draw_brez_float_line(xn, yn, xk, yk)
            elif self.ui.brez_int_check.isChecked():
                self.draw_brez_int_line(xn, yn, xk, yk)
            elif self.ui.brez_no_stup_check.isChecked():
                self.draw_brez_no_stup_line(xn, yn, xk, yk)
                
        elif self.ui.line_comparison_check.isChecked():
            try:
                xc = int(self.ui.Xc_entry.text())
                yc = int(self.ui.Yc_entry.text())
                angle = float(self.ui.angle_entry.text())
            except:
                print("err")
                return 0
            if self.ui.CDA_check.isChecked():
                self.comp_cda_line(xc,yc, angle)
                
            elif self.ui.bibl_check.isChecked():
                self.comp_bible_line(xc, yc, angle)
                
            elif self.ui.brez_float_check.isChecked():
                self.comp_brez_float_line(xc, yc, angle)
                
            elif self.ui.brez_int_check.isChecked():
                self.comp_brez_int_line(xc, yc, angle)
                
            elif self.ui.brez_no_stup_check.isChecked():
                self.comp_brez_no_stup_line(xc, yc, angle)

    def color_choose(self):
        self.color = QtWidgets.QColorDialog.getColor()
        self.pen.setColor(self.color)
        self.change_color_check()

    def back_color_set(self):
        self.color = QtGui.QColor(255,255,255)
        self.pen.setColor(self.color)
        self.change_color_check()
                
            
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
