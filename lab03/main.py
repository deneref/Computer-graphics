import sys
from interface import *
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
        self.ui.draw_line_button.clicked.connect(self.draw_line)
        self.ui.clear_all_button.clicked.connect(self.Clear_Scene)
        self.ui.choose_color_button.clicked.connect(self.color_choose)
        self.ui.back_color.clicked.connect(self.back_color_set)

        # Здеть тогл
        self.ui.line_comparison_check.toggled.connect(self.switch)
        self.ui.line_draw_check.toggle()

        #длина лучей солнца
        self.len = 100

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
       #оси
        ox = QtCore.QLineF(self.scene_width//2, 0,\
                           self.scene_width//2, self.scene_height)
        self.scene.addLine(ox)
        self.scene.addLine(0, self.scene_height//2,\
                           self.scene_width, self.scene_height//2)
        #стрелочки
        self.scene.addLine(self.scene_width//2 , 0,\
                           self.scene_width//2 + 10, 20)
        self.scene.addLine(self.scene_width//2 , 0,\
                           self.scene_width//2 - 10, 20)
        self.scene.addLine(self.scene_width, self.scene_height//2,\
                           self.scene_width - 20, self.scene_height//2 - 10)
        self.scene.addLine(self.scene_width, self.scene_height//2,\
                           self.scene_width - 20, self.scene_height//2 + 10)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.scene.addText("y", font).setPos(self.scene_width//2 - 30, 0)
        self.scene.addText("x", font).setPos(self.scene_width - 30, self.scene_height//2 + 10)
        for i in range(0, self.scene_width, 50):
            self.scene.addLine(i, self.scene_height//2 - 7,
                               i, self.scene_height//2 + 7)
        for i in range(50, self.scene_height+50, 50):
            self.scene.addLine(self.scene_width//2 - 7, i,
                               self.scene_width//2 + 7, i)

    def draw_bible_line(self, xn, yn, xk, yk):
        self.scene.addLine(xn+self.scene_width//2, self.scene_height//2 - yn,\
                           xk+self.scene_width//2, self.scene_height//2 - yk,\
                           self.pen)

    def draw_cda_line(self, xn, yn, xk, yk):
        if (xn == xk and yn == yk):
            self.scene.addLine(xn+self.scene_width//2,self.scene_height//2 - yn,\
                               xn+self.scene_width//2,self.scene_height//2 - yn, self.pen)
            return 0
        else:
            if abs(xk - xn) > abs(yk - yn):
                length = abs(xk - xn)
            else:
                length = abs(yk - yn)

            dx = (xk - xn)/length
            dy = (yk - yn)/length
            #print(dx, dy)
            x = xn; y = xn
            #изменить
            while abs(x - xk) > 1 or abs(y - yk) > 1:
                self.scene.addLine(x+self.scene_width//2,self.scene_height//2 - y,\
                               x+self.scene_width//2, self.scene_height//2 - y, self.pen)
                x += dx
                y += dy

    def sign(self, x):
        if x <= 0:
            return -1
        else:
            return 1
    def draw_brez_float_line(self, xn,yn,xk, yk):
        if(xn == xk and yn == yk):
            
            self.scene.addLine(xn+self.scene_width//2,self.scene_height//2 - yn,\
                               xn+self.scene_width//2,self.scene_height//2 - yn, self.pen)
            return 0
        dx = xk-xn
        dy = yk-yn
        sx = self.sign(dx)
        sy = self.sign(dy)
        dx = abs(dx); dy = abs(dy)
        m = dy/dx
        flag = 0
        if m >= 1:
            dx, dy = dy, dx
            m = 1/m
            flag = 1
        else:
            flag = 0
        f = m-0.5
        x = xn; y = yn
        while abs(x - xk) > 1 or abs(y - yk) > 1:
            self.scene.addLine(x+self.scene_width//2,self.scene_height//2 - y,\
                                x+self.scene_width//2,self.scene_height//2 - y, self.pen)

            if f>0:
                if flag == 1:
                    x += sx
                else:
                    y += sy
                f = f-1
            else:
                if flag == 1:
                    y += sy
                else:
                    x += sx
                f=f+m
        

    def draw_brez_int_line(self, xn, yn, xk, yk):
        if(xn == xk and yn == yk):
            self.scene.addLine(xn+self.scene_width//2,self.scene_height//2 - yn,\
                               xn+self.scene_width//2,self.scene_height//2 - yn, self.pen)
            return 0
        x = xn
        y = yn
        dx = abs(xk - xn)
        dy = abs(yk - yn)
        sx = self.sign(xk - xn)
        sy = self.sign(yk - yn)
        flag = 0
        if dy > dx:
            dy, dx = dx, dy
            flag = 1
        e = 2 * dy - dx
        while abs(x - xk) > 1 or abs(y - yk) > 1:
            self.scene.addLine(x+self.scene_width//2,self.scene_height//2 - y,\
                                x+self.scene_width//2,self.scene_height//2 - y, self.pen)
            while (e>=0):
                if flag:
                    x += sx
                else:
                    y += sy
                e = e - 2*dx
            if flag:
                y += sy
            else:
                x += sx
            e = e + 2*dy

    def DrawPoint(self, flag, x, y, e):
        Curr_pen = QtGui.QPen(self.color.lighter(100+(50 - e)))
##        if flag:
##            x, y = y, x
        #print(e)
        self.scene.addLine(x+self.scene_width//2, self.scene_height//2 - y,\
                            x+self.scene_width//2, self.scene_height//2 - y, Curr_pen)

    def draw_brez_no_stup_line(self, xn, yn, xk, yk):
        I = 50
        if(xn == xk and yn == yk):
            self.scene.addLine(xn+self.scene_width//2,self.scene_height//2 - yn,\
                               xn+self.scene_width//2,self.scene_height//2 - yn, self.pen)
            return 0
        dx = xk - xn
        dy = yk - yn
        sx = self.sign(dx)
        sy = self.sign(dy)
        dx = abs(dx)
        dy = abs(dy)
        flag = 0
        if (dy > dx):
            dx, dy = dy, dx
            flag = 1
        m = dy / dx
        e = I / 2
        xt = xn
        yt = yn
        m *= I
        W = I - m
        alpha = 50
        while abs(xt - xk) > 1 or abs(yt - yk) > 1:
            #print(alpha, e)
            self.DrawPoint(flag, xt, yt, alpha)
            alpha = e
            if (e<=W):
                if flag:
                    yt += sy
                else:
                    xt += sx
                e = e+m
            else:
                xt += sx
                yt += sy
                e = e-W
        
    def comp_bible_line(self, xc,yc,angle):
        angle = radians(angle)
        count = 2*pi // angle #сколько линий построится
        dfi = 2*pi / count
        while angle < 2*pi+dfi:
            self.draw_bible_line(xc,yc,\
                            xc+self.len*cos(angle), yc+self.len*sin(angle))
            angle += dfi
    def comp_cda_line(self, xc,yc,angle):
        angle = radians(angle)
        count = 2*pi // angle #сколько линий построится
        dfi = 2*pi / count
        while angle < 2*pi+dfi:
            self.draw_cda_line(xc,yc,\
                            int(xc+self.len*cos(angle)), int(yc+self.len*sin(angle)))
            angle += dfi

    def comp_brez_float_line(self, xc, yc, angle):
        angle = radians(angle)
        count = 2*pi // angle #сколько линий построится
        dfi = 2*pi / count
        while angle < 2*pi+dfi:
            self.draw_brez_float_line(xc,yc,\
                        xc+self.len*cos(angle), yc+self.len*sin(angle))
            angle += dfi

    def comp_brez_int_line(self, xc, yc, angle):
        angle = radians(angle)
        count = 2*pi // angle #сколько линий построится
        dfi = 2*pi / count
        while angle < 2*pi+dfi:
            self.draw_brez_int_line(xc,yc,\
                            xc+self.len*cos(angle), yc+self.len*sin(angle))
            angle += dfi

    def comp_brez_no_stup_line(self, xc, yc, angle):
        angle = radians(angle)
        count = 2*pi // angle #сколько линий построится
        dfi = 2*pi / count
        while angle < 2*pi+dfi:
            self.draw_brez_no_stup_line(xc,yc,\
                            xc+self.len*cos(angle), yc+self.len*sin(angle))
            angle += dfi
            
        
    def draw_line(self):
        if self.ui.line_draw_check.isChecked():
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
        
    def switch(self):
        if self.ui.line_comparison_check.isChecked():
            self.ui.label.hide()
            self.ui.label_9.hide()
            self.ui.Xn_entry.hide()
            self.ui.Xk_entry.hide()
            self.ui.Yn_entry.hide()
            self.ui.Yk_entry.hide()

            self.ui.Xc_entry.show()
            self.ui.Yc_entry.show()
            self.ui.angle_entry.show()
            self.ui.center_label.show()
            self.ui.label_6.setText("Xc:")
            self.ui.label_7.setText("Yc:")
            self.ui.label_2.setText("Средний угол")
            self.ui.label_8.setText("φ°")
            
        else:
            self.ui.label.show()
            self.ui.label_9.show()
            self.ui.Xn_entry.show()
            self.ui.Xk_entry.show()
            self.ui.Yn_entry.show()
            self.ui.Yk_entry.show()

            self.ui.Xc_entry.hide()
            self.ui.Yc_entry.hide()
            self.ui.angle_entry.hide()
            self.ui.center_label.hide()
            self.ui.label_6.setText("Xn:")
            self.ui.label_7.setText("Yn:")
            self.ui.label_2.setText("Конец отрезка")
            self.ui.label_8.setText("Xk")
            
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
