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
        self.color = QtGui.QColor("#110058")
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
        self.ui.draw_line_button.clicked.connect(self.draw)
        self.ui.clear_all_button.clicked.connect(self.Clear_Scene)
        self.ui.choose_color_button.clicked.connect(self.color_choose)
        self.ui.back_color.clicked.connect(self.back_color_set)
        self.ui.info_button.clicked.connect(self.show_info)

    def draw_round_kanonich(self, xc, yc, r):
        #print(r, xc, yc)
        x = 0
        y = r
        while x < r+1:
##            print(x, r, y)
            y = int(sqrt(abs(r ** 2 - x ** 2)))
            self.scene.addLine(xc+x, yc+y, xc+x, yc+y, self.pen)
            self.scene.addLine(xc+x, yc-y, xc+x, yc-y, self.pen)
            self.scene.addLine(xc-x, yc+y, xc-x, yc+y, self.pen)
            self.scene.addLine(xc-x, yc-y, xc-x, yc-y, self.pen)
            x+=1
            
        for y in range(0, r+1,1):
            x = int(sqrt(abs(r ** 2 - y ** 2)))
            self.scene.addLine(xc+x, yc+y, xc+x, yc+y, self.pen)
            self.scene.addLine(xc+x, yc-y, xc+x, yc-y, self.pen)
            self.scene.addLine(xc-x, yc+y, xc-x, yc+y, self.pen)
            self.scene.addLine(xc-x, yc-y, xc-x, yc-y, self.pen)

    def draw_round_param(self, xc, yc, r):
        l = int(pi * r / 2)
        for i in range(0, l+1, 1):
            x = int(r * cos(i / r))
            y = int(r * sin(i / r))
            self.scene.addLine(xc + x, yc + y,
                               xc + x, yc + y, self.pen)
            self.scene.addLine(xc - x, yc + y,
                               xc - x, yc + y, self.pen)
            self.scene.addLine(xc + x, yc - y,
                               xc + x, yc - y, self.pen)
            self.scene.addLine(xc - x, yc - y,
                               xc - x, yc - y, self.pen)
            
            
    def draw_round_brez(self, xc, yc, r):
        x = 0
        y = r
        D = 2*(1-r)
        while (y >= 0):
            self.scene.addLine(xc + x, yc - y,
                               xc + x, yc - y, self.pen)

            self.scene.addLine(xc - x, yc - y,
                               xc - x, yc - y, self.pen)

            self.scene.addLine(xc - x, yc + y,
                               xc - x, yc + y, self.pen)

            self.scene.addLine(xc + x, yc + y,
                               xc + x, yc + y, self.pen)

            if D < 0:
                D1=2*D+2*y-1
                x+=1
                
                if D1 <= 0: #горизонт
##                    x+=1
                    D+=2*x+1
                else:  #диагонал
                    y-=1
                    D+=2*(x-y+1)
            elif D == 0: #на окружности
                x+=1
                y-=1
                D+=2*(x-y+1)
            elif D > 0:
                D2 = 2*D-2*x-1
                y-=1
                if D2<0:
                    x+=1
                    D+=2*(x-y+1)
                else:
                    D=D-2*y+1
        
    def draw_round_bibl(self, xc, yc, r):
        self.scene.addEllipse(xc - r, yc - r,\
                              2*r, 2*r, self.pen)

    def draw_sr_toch(self, xc, yc, rx, ry):
        ellipse = []
        pl = ry**2 - rx**2 * ry + (1/4)*(rx**2)
        x = 0
        y = ry
        while (2*(ry**2) * x < 2*(rx**2)*y):
           if pl < 0:
               x += 1
               pl = pl + 2* (ry**2) * x + ry**2
               ellipse.append([x, y])
               self.scene.addLine(xc+x, -y+yc,\
                               xc+x ,-y+yc, self.pen)
           else:
               x += 1
               y -= 1
               pl = pl + 2*(ry**2)*x - 2*(rx**2)*y + ry**2
               ellipse.append([x,y])
               self.scene.addLine(xc+x, -y+yc,\
                               xc+x, -y+yc, self.pen)

        p2 = (ry**2)*(x + 1/2)**2 + (rx**2) * (y - 1)**2 - (rx**2) * (ry**2)
        while (y > 0):
            if p2 > 0:
               y = y - 1
               p2 = p2 - 2*(rx**2)*(y) + (rx**2)
               ellipse.append([x,y])
               self.scene.addLine(xc+x, -y+yc,\
                               xc+x, -y+yc, self.pen)
            else:
                x += 1
                y -= 1
                p2 = p2 + 2*(ry**2)*x - 2*(rx**2)*y + (rx**2)
                ellipse.append([x,y])
                self.scene.addLine(xc+x , -y+yc,\
                               xc+x, -y+yc, self.pen)

        for i in range(len(ellipse)-1, 1, -1):
            coord = [ellipse[i][0], -1*ellipse[i][1]]
            x = ellipse[i][0]
            y = ellipse[i][1] * (-1)
            ellipse.append(coord)
            self.scene.addLine(xc+x , -y+yc,\
                               xc+x , -y+yc, self.pen)
        for i in range(len(ellipse) -1 , 1, -1):
            #coord = [-1*ellipse[i][0], ellipse[i][1]]
            x = -1 * ellipse[i][0]
            y = ellipse[i][1]
            self.scene.addLine(xc+x , -y+yc,\
                               xc+x , -y+yc, self.pen)
        self.scene.addLine(xc+ellipse[0][0] ,\
                             - ellipse[0][1]+yc,\
                           xc+(-1)*ellipse[0][0] ,\
                             - ellipse[0][1]+yc, self.pen)
        
        self.scene.addLine(xc+ellipse[0][0] ,\
                             ellipse[0][1]+yc,\
                           xc+(-1)*ellipse[0][0] ,\
                            ellipse[0][1]+yc, self.pen)

    def draw_ellipse_param(self, xc, yc, a, b):
        m = max(a, b)
        l = int(pi * m / 2)
        for i in range(0, l+1, 1):
            x = int(a * cos(i / m))
            y = int(b * sin(i / m))
            self.scene.addLine(xc + x, yc - y,
                               xc + x, yc - y, self.pen)

            self.scene.addLine(xc - x, yc - y,
                               xc - x, yc - y, self.pen)

            self.scene.addLine(xc - x, yc + y,
                               xc - x, yc + y, self.pen)

            self.scene.addLine(xc + x, yc + y,
                               xc + x, yc + y, self.pen)  

    def draw_ellipse_kanonich(self, xc, yc, a, b):
        for x in range(0, a+1, 1):
            y = int(b * sqrt((1 - x**2/a**2)))
            self.scene.addLine(xc + x, yc - y,
                               xc + x, yc - y, self.pen)

            self.scene.addLine(xc - x, yc - y,
                               xc - x, yc - y, self.pen)

            self.scene.addLine(xc - x, yc + y,
                               xc - x, yc + y, self.pen)

            self.scene.addLine(xc + x, yc + y,
                               xc + x, yc + y, self.pen)         
##        for y in range(0, b+1, 1):
##            x = int(a * sqrt(1 - y ** 2 / b ** 2))
##            self.scene.addLine(xc + x, yc - y,
##                               xc + x, yc - y, self.pen)
##
##            self.scene.addLine(xc - x, yc - y,
##                               xc - x, yc - y, self.pen)
##
##            self.scene.addLine(xc - x, yc + y,
##                               xc - x, yc + y, self.pen)
##
##            self.scene.addLine(xc + x, yc + y,
##                               xc + x, yc + y, self.pen)
        
    def draw_ellipse_brez(self, xc, yc, a, b):
        rx2 = a**2
        ry2 = b**2
        r2y2 = 2 * ry2
        r2x2 = 2 * rx2
        x = 0
        y = b
        d = rx2 + ry2 - r2x2 * y
        while y>=0:
            self.scene.addLine(xc + x, yc - y,
                               xc + x, yc - y, self.pen)

            self.scene.addLine(xc - x, yc - y,
                               xc - x, yc - y, self.pen)

            self.scene.addLine(xc - x, yc + y,
                               xc - x, yc + y, self.pen)

            self.scene.addLine(xc + x, yc + y,
                               xc + x, yc + y, self.pen)
            if (d<0):
                d1 = 2*d + r2x2*y - 1
                if d1 >0 :
                    y -= 1
                    x += 1
                    d += r2y2 * x + ry2 + rx2 - r2x2*y
                else:
                    x+=1
                    d+=r2y2*x+ry2
            elif d == 0:
                x += 1
                y -=1
                d += r2y2*x+ry2+rx2 - r2x2*y
            else:
                d2 = 2*d - r2y2 * x - 1
                if (d2 < 0):
                    y -= 1
                    x += 1
                    d += r2y2*x+ry2+rx2 - r2x2*y
                else:
                    y-=1
                    d += rx2 - r2x2*y
                

    def draw_ellipse_bibl(self, xc, yc, a, b):
        self.scene.addEllipse(xc - a , yc - b,\
                              2*a, 2*b, self.pen)

    def draw_round_param_comparison(self,xc, yc, r, k):
        h = r / k
        count = r // int(h)
        for i in range(int(count)):
            self.draw_round_param(xc, yc, int(r))
            r -= h

    def draw_round_kanonich_comparison(self,xc, yc, r, k):
        h = r / k
        count = r // int(h)
        for i in range(int(count)):
            self.draw_round_kanonich(xc, yc, int(r))
            r -= h
        
    def draw_round_brez_comparison(self,xc, yc, r, k):
        h = r / k
        count = r // int(h)
        for i in range(int(count)):
            self.draw_round_brez(xc, yc, int(r))
            r -= h

    def draw_sr_toch_round_comparison(self, xc, yc, r, k):
        h = r / k
        count = r // int(h)
        for i in range(int(count)):
            self.draw_sr_toch(xc, yc, int(r), int(r))
            r -= h

    def draw_round_bibl_comparison(self, xc, yc, r, k):
        h = r / k
        count = r // int(h)
        for i in range(int(count)):
            self.draw_round_bibl(xc, yc, int(r))
            r -= h

    def draw_ellipse_kanonich_comparison(self,xc, yc, a, k):
        h = a / k
        count = a // int(h)
        for i in range(int(count)):
            self.draw_ellipse_kanonich(xc, yc, int(a), int(a/2))
            a -= h

    def draw_ellipse_param_comparison(self,xc, yc, a, k):
        h = a / k
        count = a // int(h)
        for i in range(int(count)):
            self.draw_ellipse_param(xc, yc, int(a), int(a/2))
            a -= h
        
    def draw_ellipse_brez_comparison(self,xc, yc, a, k):
        h = a / k
        count = a // int(h)
        for i in range(int(count)):
            self.draw_ellipse_brez(xc, yc, int(a), int(a/2))
            a -= h

    def draw_sr_toch_ellipse_comparison(self, xc, yc, a, k):
        h = a / k
        count = a // int(h)
        for i in range(int(count)):
            self.draw_sr_toch(xc, yc, int(a), int(a/2))
            a -= h

    def draw_ellipse_bibl_comparison(self, xc, yc, a, k):
        h = a / k
        count = a // int(h)
        for i in range(int(count)):
            self.draw_ellipse_bibl(xc, yc, int(a), int(a/2))
            a -= h

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
        self.scene.addLine(0, 0,\
                           self.scene_width, 0)
        self.scene.addLine(0, 0,\
                           0, self.scene_height)
        
        self.scene.addLine(10 , self.scene_height - 20,\
                           0, self.scene_height)
        self.scene.addLine(-10 , self.scene_height - 20,\
                           0, self.scene_height)
        
        self.scene.addLine(self.scene_width, 0,\
                           self.scene_width - 20, 0 - 10)
        self.scene.addLine(self.scene_width, 0,\
                           self.scene_width - 20, 0 + 10)
        
    def draw(self):
        if self.ui.draw_one_check.isChecked():
            self.draw_one()
        elif self.ui.draw_mult_check.isChecked():
            self.draw_comparison()

    def draw_one(self):
        try:
            xc = int(self.ui.xc_entry.text())
            yc = int(self.ui.yc_entry.text())
        except:
            msge = Message_box().wrong_input()
            return 0
        if self.ui.round_draw_check.isChecked():
            try:
                r = int(self.ui.r_entry.text())
            except:
                msge = Message_box().wrong_input()
                return 0
            self.draw_one_round(xc, yc, r)
        if self.ui.ellipse_draw_check.isChecked():
            try:
                a = int(self.ui.r_entry.text())
                b = int(self.ui.b_entry.text())
            except:
                msge = Message_box().wrong_input()
                return 0
            self.draw_one_ellipse(xc, yc, a, b)

    def draw_comparison(self):
        try:
            xc = int(self.ui.xc_entry.text())
            yc = int(self.ui.yc_entry.text())
            k = int(self.ui.b_entry.text())
        except:
            msge = Message_box().wrong_input()
            return 0
        if self.ui.round_draw_check.isChecked():
            try:
                r = float(self.ui.r_entry.text())
            except:
                msge = Message_box().wrong_input()
                return 0
            self.draw_comparison_round(xc, yc, r, k)
        if self.ui.ellipse_draw_check.isChecked():
            try:
                a = int(self.ui.r_entry.text())
            except:
                msge = Message_box().wrong_input()
                return 0
            self.draw_comparison_ellipse(xc, yc, a, k)

    def draw_one_round(self, xc, yc, r):
        if self.ui.param_check.isChecked():
            self.draw_round_param(xc, yc, r)
        elif self.ui.kanonich_check.isChecked():
            self.draw_round_kanonich(xc, yc, r)
        elif self.ui.brez_check.isChecked():
            self.draw_round_brez(xc, yc, r)
        elif self.ui.sr_toch_check.isChecked():
            self.draw_sr_toch(xc, yc, r, r)
        elif self.ui.bibl_check.isChecked():
            self.draw_round_bibl(xc, yc, r)

    def draw_one_ellipse(self, xc, yc, a, b):
        if self.ui.param_check.isChecked():
            self.draw_ellipse_param(xc, yc, a, b)
        elif self.ui.kanonich_check.isChecked():
            self.draw_ellipse_kanonich(xc, yc, a, b)
        elif self.ui.brez_check.isChecked():
            self.draw_ellipse_brez(xc, yc, a, b)
        elif self.ui.sr_toch_check.isChecked():
            self.draw_sr_toch(xc, yc, a, b)
        elif self.ui.bibl_check.isChecked():
            self.draw_ellipse_bibl(xc, yc, a, b)

    def draw_comparison_round(self, xc, yc, r, k):
        if self.ui.param_check.isChecked():
            self.draw_round_param_comparison(xc, yc, r, k)
        elif self.ui.kanonich_check.isChecked():
            self.draw_round_kanonich_comparison(xc, yc, r, k)
        elif self.ui.brez_check.isChecked():
            self.draw_round_brez_comparison(xc, yc, r, k)
        elif self.ui.sr_toch_check.isChecked():
            self.draw_sr_toch_round_comparison(xc, yc, r, k)
        elif self.ui.bibl_check.isChecked():
            self.draw_round_bibl_comparison(xc, yc, r, k)

    def draw_comparison_ellipse(self, xc, yc, a, k):
        if self.ui.param_check.isChecked():
            self.draw_ellipse_param_comparison(xc, yc, a, k)
        elif self.ui.kanonich_check.isChecked():
            self.draw_ellipse_kanonich_comparison(xc, yc, a, k)
        elif self.ui.brez_check.isChecked():
            self.draw_ellipse_brez_comparison(xc, yc, a, k)
        elif self.ui.sr_toch_check.isChecked():
            self.draw_sr_toch_ellipse_comparison(xc, yc, a, k)
        elif self.ui.bibl_check.isChecked():
            self.draw_ellipse_bibl_comparison(xc, yc, a, k)

    def color_choose(self):
        self.color = QtWidgets.QColorDialog.getColor()
        self.pen.setColor(self.color)
        self.change_color_check()

    def back_color_set(self):
        self.color = QtGui.QColor(255,255,255)
        self.pen.setColor(self.color)
        self.change_color_check()

    def show_info(self):
        print("here")
        msge = Message_box().show_info()
                
            
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
