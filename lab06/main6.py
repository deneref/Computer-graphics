import sys
from lab06_ui import *
from PyQt5 import *
from math import *
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPixmap
from MScene import *
import time
        
class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        #устанавливает интерфейс
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #настройка размеров канваса
        self.scene_width = 1200
        self.scene_height = 800
        self.ui.c.setGeometry(QtCore.QRect(10, 10,\
                                        10+self.scene_width, 10+self.scene_height))

        #установка текущего цвета
        self.color_bord = QtGui.QColor("#fc6c2d")
        self.color_inside = QtGui.QColor("#fffaaf")
        self.bg_color = QtGui.QColor("#ffffff")
        self.pen_bord = QtGui.QPen(self.color_bord)
        self.pen_inside = QtGui.QPen(self.color_inside)
        self.rect = QtCore.QRectF(QtCore.QPointF(10, 10), QtCore.QSizeF(30, 30))

        self.painter_bord = QtGui.QPainter()
        self.painter_bord.setPen(self.pen_bord)

        self.painter_inside = QtGui.QPainter()
        self.painter_inside.setPen(self.pen_inside)

        #проверка цвета
        self.color_check_border = QtWidgets.QGraphicsScene()
        self.ui.c_col_border.setScene(self.color_check_border)

        self.color_check_inside = QtWidgets.QGraphicsScene()
        self.ui.c_col_inside.setScene(self.color_check_inside)
        self.change_color_check()
        
        #устанавливает сцену
        self.scene = myScene(self)
        
        self.image = QtGui.QImage(self.scene_width, self.scene_height, QtGui.QImage.Format_RGB32)
        self.image.fill(self.bg_color)
        self.scene.addPixmap(QPixmap.fromImage(self.image))

        self.ui.c.setStyleSheet("background-color: white")
        self.ui.c.setScene(self.scene)
        self.ui.c.setMouseTracking(True)
     
        # Здесь прописываем событие нажатия на кнопку                     
        self.ui.add_point.clicked.connect(self.add_point_bttn)
        self.ui.clear_all.clicked.connect(self.Clear_Scene)
        self.ui.delete_point.clicked.connect(self.get_pos_to_delete)
        self.ui.col_border_choose.clicked.connect(self.color_choose_border)
        self.ui.col_inside_shoose.clicked.connect(self.color_choose_inside)
        self.ui.fill.clicked.connect(self.fill)
        self.ui.zetr_pix_button.clicked.connect(self.add_pixel)
        self.ui.zamkn_button.clicked.connect(self.zamkn)

        # Здеть тогл
##        self.ui.no_stop.toggled.connect(self.switch)
##        self.ui.no_stop.toggle()
        #self.with_delay = False

        #точки и все такое
        self.edges = []
        self.new = True
        self.get_pixel = False
        self.capslock = False
        self.with_delay = False
        self.draw_coord()
        self.last_point = 0
        self.pixel = []

        #лист бокс и друзья
        self.ui.list_point.itemDoubleClicked.connect(self.delete_point)

    def Clear_Scene(self):
        self.image.fill(self.bg_color)
        self.edges = []
        self.draw_coord()
        self.ui.list_point.clear()
        self.new = True
        self.last_point = 0

    def paintEvent(self, e):
        self.scene.clear()
        self.scene.addPixmap(QPixmap.fromImage(self.image))
        

    def zamkn(self):
        if not self.new:
            self.add_point(self.edges[self.last_point][0], self.edges[self.last_point][1])
            self.last_point = len(self.edges)
            self.new = True

    def add_pixel(self):
        self.get_pixel = True

    def change_color_check(self):
        self.color_check.addRect(self.rect, self.pen)
        painter = QtGui.QPainter(self)
        painter.setPen(self.pen)
        painter.setBrush(self.brush)
        self.pen.setWidth(3)
        self.color_check.addRect(self.rect, self.pen)
        self.pen.setWidth(1)

    def add_point_bttn(self):
        try:
            x = int(self.ui.x_entry.text())
            y = int(self.ui.y_entry.text())
        except:
            return 0
        self.add_point(x,y)

    def add_point(self, x, y):
        if self.get_pixel:
            self.pixel = [x,y] 
            self.get_pixel = False
        else:
            if self.new:
                self.edges.append([x,y,x,y])
                self.new = False
            else:
                self.edges[-1][2] = x
                self.edges[-1][3] = y
                self.edges.append([x,y, x, y])
            if len(self.edges) > 0:
                self.draw_figure()
            self.ui.list_point.addItem("{} {}".format(x,y))

    def draw_figure(self):
        self.image.fill(self.bg_color)
        self.draw_coord()
        self.draw_edges()

    def print_to_list(self):
        self.ui.list_point.clear()
        for i in range(len(self.edges)):
            x = self.edges[i][0]
            y = self.edges[i][1]
            self.ui.list_point.addItem("{} {}".format(x,y))

    def draw_edges(self):
        for e in self.edges:
            self.Bresenham(e[0], e[1], e[2], e[3], self.color_bord.rgb())

    def get_pos_to_delete(self):
        try:
            pos = int(self.ui.point_num_entry.text())
        except:
            return 0
        self.delete_point(pos)

    def delete_point(self, pos):
        try:
            self.edges[pos-2][2] = self.edges[pos-1][2]
            self.edges[pos-2][3] = self.edges[pos-1][3]
            del self.edges[pos-1]
        except:
            return 0
        self.print_to_list()
        self.draw_figure()

    def switch(self):
        pass

    def go_delay(self):
        #self.update()
        self.repaint()

    def fill(self):
        if (not self.pixel):
            return 0
        stack = []
        stack.append(self.pixel)
        while stack:
            if self.ui.with_stop.isChecked:
                QtWidgets.QApplication.processEvents()
            p = stack.pop()
            x = p[0]
            y = p[1]
            tx = p[0]
            self.image.setPixel(x,y,self.color_inside.rgb())
            x -= 1
            #Заполняем слева от затравки
            while self.image.pixel(x,y) != self.color_bord.rgb():
                self.image.setPixel(x,y,self.color_inside.rgb())
                x-=1

            if self.with_delay:
                self.go_delay()
            
            #сохраняет крайний слева пиксель
            xl = x+1
            x = tx
            x+=1
            #Заполняем справа от затравки
            while self.image.pixel(x,y) != self.color_bord.rgb():
                self.image.setPixel(x,y,self.color_inside.rgb())
                x+=1
            xr = x-1
            y +=1
            x = xl
            while x <= xr:
                fl = 0
                while self.image.pixel(x,y) != self.color_bord.rgb()and\
                     self.image.pixel(x,y) != self.color_inside.rgb() and x<=xr:
                    if fl == 0:
                        fl = 1
                    x += 1
                
                if fl == 1:
                    if x == xr and self.image.pixel(x,y) != self.color_inside.rgb() and\
                        self.image.pixel(x,y)!=self.color_bord.rgb():
                        stack.append([x,y])
                    else:
                        stack.append([x-1,y])
                    fl = 0
                tx = x
                while (self.image.pixel(x,y) == self.color_bord.rgb() or\
                        self.image.pixel(x,y) == self.color_inside.rgb()) and\
                        x < xr:
                    x+=1
                if x == tx:
                    x+=1
            y -= 2
            x = xl
            while x <= xr:
                fl = 0
                while self.image.pixel(x,y) != self.color_bord.rgb() and\
                        self.image.pixel(x,y) != self.color_inside.rgb() and\
                        x <= xr:
                    if fl == 0:
                        fl = 1
                    x +=1
                if fl == 1:
                    if x == xr and\
                        self.image.pixel(x,y) != self.color_inside.rgb() and\
                        self.image.pixel(x,y) != self.color_bord.rgb():
                        stack.append([x,y])
                    else:
                        stack.append([x-1,y])
                    fl = 0       
                xt = x
                while (self.image.pixel(x,y) == self.color_bord.rgb() or\
                        self.image.pixel(x,y) == self.color_inside.rgb()) and\
                        x < xr:
                    x+=1
                if x == xt:
                    x += 1
                
        
    def color_choose_border(self):
        self.color_bord = QtWidgets.QColorDialog.getColor()
        self.pen_bord.setColor(self.color_bord)
        self.change_color_check()

    def color_choose_inside(self):
        self.color_inside = QtWidgets.QColorDialog.getColor()
        self.pen_inside.setColor(self.color_inside)
        self.change_color_check()
    
    def draw_coord(self):
        self.Bresenham(0, 0,\
                           self.scene_width, 0)
        self.Bresenham(0, 0,\
                           0, self.scene_height)
        
        self.Bresenham(10 , self.scene_height - 20,\
                           0, self.scene_height)

        self.Bresenham(self.scene_width, 0,\
                           self.scene_width - 20, 0 + 10)

    def change_color_check(self):
        pixmap = QtGui.QPixmap(40,40)
        pixmap.fill(self.color_bord)
        self.color_check_border.addPixmap(pixmap)
        
        pixmap = QtGui.QPixmap(40,40)
        pixmap.fill(self.color_inside)
        self.color_check_inside.addPixmap(pixmap)

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == 16777252:
            self.capslock = not self.capslock
        elif QKeyEvent.key() == QtCore.Qt.Key_Return and\
             len(self.edges) > 2:
            self.zamkn()

    def mousePressEvent(self, QMouseEvent):
        if not self.get_pixel:
            self.draw_figure()
        coord = QMouseEvent.pos()
        y = coord.y()
        x = coord.x()
        if x >= 10 and y>=10 and\
           y<=self.scene_height and x<= self.scene_width:
            x -= 15
            y -= 15
        if self.edges:
            if self.capslock and len(self.edges[-1]):
                if y != self.edges[-1][1]:
                    t = ((x - self.edges[-1][0]) /\
                            (y - self.edges[-1][1]))
                else:
                    t = 2
                if abs(t) <= 1:
                    x = self.edges[-1][0]
                else:
                    y = self.edges[-1][1]
        self.add_point(x, y)
        self.scene.update()

    def sign(self, x):
        if x > 0:
            return 1
        else:
            return -1

    def Bresenham(self,x1,y1,x2,y2,color = QtGui.QColor(0,0,0).rgb(),t=False):
        dx = int(x2 - x1)
        dy = int(y2 - y1)
        sx = self.sign(dx)
        sy = self.sign(dy)
        dx = abs(dx)
        dy = abs(dy)    
        swap = False
        if (dy <= dx):
            swap = False
        else:
            swap = True
            dx,dy = dy,dx
        
    
        e = int(2*dy-dx)
        x = int(x1)
        y = int(y1)
            
        for i in range(dx+1):
            self.image.setPixel(x,y,color)
            if t:
                self.image.setPixel(x+1,y,color)
                self.image.setPixel(x-1,y,color)
                self.image.setPixel(x,y+1,color)
                self.image.setPixel(x,y-1,color)
            if (e>=0):
                if (swap):
                    x += sx
                else:
                    y +=sy
                e = e-2*dx
            if (e < 0): 
                if (swap):
                    y +=sy
                else:
                    x += sx
                e = e+2*dy

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
