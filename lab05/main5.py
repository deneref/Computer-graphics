import sys
from lab05_ui import *
from PyQt5 import *
from math import *

##class myScene(QtWidgets.QGraphicsScene):
##    def __init__(self, parent=None):
##        QtWidgets.QGraphicsScene.__init__(self, parent)
##        
##    def mousePressEvent(self, event):
##        x = event.scenePos().x()
##        y = event.scenePos().y()
##        myapp.add_point(x, y)
        
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
##        self.scene = myScene(self)
##        self.ui.c.setScene(self.scene)
##        self.image = QtGui.QImage(self.scene_width, self.scene_height, QtGui.QImage.Format_ARGB32_Premultiplied)
##        self.image.fill(self.bg_color)

##        self.show_image()
        self.scene = QtWidgets.QGraphicsScene(self)
        self.image = QtGui.QImage(self.scene_width,self.scene_height,QtGui.QImage.Format_RGB32)
        self.image.fill(self.bg_color)
        self.scene.addPixmap(QtGui.QPixmap.fromImage(self.image))
        self.ui.c.setScene(self.scene)
     
        # Здесь прописываем событие нажатия на кнопку                     
        self.ui.add_point.clicked.connect(self.add_point_bttn)
        self.ui.clear_all.clicked.connect(self.Clear_Scene)
        self.ui.delete_point.clicked.connect(self.get_pos_to_delete)
        self.ui.col_border_choose.clicked.connect(self.color_choose_border)
        self.ui.col_inside_shoose.clicked.connect(self.color_choose_inside)
        self.ui.fill.clicked.connect(self.fill)

        # Здеть тогл
        self.ui.no_stop.toggled.connect(self.switch)
        self.ui.no_stop.toggle()

        #точки и все такое
        self.points = []
        self.draw_coord()

        #лист бокс и друзья
        self.ui.list_point.itemDoubleClicked.connect(self.delete_point)
        self.ui.connect_check.setChecked(True)


    def Clear_Scene(self):
        self.image.fill(self.bg_color)
        self.points = []
        self.draw_coord()
        self.ui.list_point.clear()
        
    def show_image(self):
        self.pixmap = QtGui.QPixmap.fromImage(self.image)
        pixItem = QtWidgets.QGraphicsPixmapItem(self.pixmap)
        PixItem = self.scene.addItem(pixItem)

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
        self.points.append([x,y])
        self.draw_figure()
        self.ui.list_point.addItem("{} {}".format(x,y))

    def draw_figure(self):
        self.image.fill(self.bg_color)
        self.draw_coord()
        if len(self.points) > 1:
            self.draw_edges()

    def print_to_list(self):
        self.ui.list_point.clear()
        for i in range(len(self.points)):
            x = self.points[i][0]
            y = self.points[i][1]
            self.ui.list_point.addItem("{} {}".format(x,y))

    def draw_edges(self):
        p = QtGui.QPainter()
        p.begin(self.image)
        p.setPen(self.pen_bord)
        for i in range(len(self.points)-1):
            p.drawLine(self.points[i][0], self.points[i][1],
                               self.points[i+1][0], self.points[i+1][1])
##            self.draw_brez_line(self.points[i][0], self.points[i][1],
##                                self.points[i+1][0], self.points[i+1][1])
        if self.ui.connect_check.isChecked():
            p.drawLine(self.points[-1][0], self.points[-1][1],
                               self.points[0][0], self.points[0][1])
##            self.draw_brez_line(self.points[-1][0], self.points[-1][1],
##                                self.points[0][0], self.points[0][1])
        p.end()
##        self.show_image()

    def get_pos_to_delete(self):
        try:
            pos = int(self.ui.point_num_entry.text())
        except:
            return 0
        self.delete_point(pos)

    def delete_point(self, pos):
        try:
            del self.points[pos-1]
        except:
            return 0
        self.print_to_list()
        self.draw_figure()

    def switch(self):
##        if self.ui.with_stop.isChecked():
##            self.ui.timer_label.show()
##            self.ui.timer_entry.show()
##        else:
##            self.ui.timer_label.hide()
##            self.ui.timer_entry.hide()
        pass

    def go_delay(self):
        #print("delay on")
        self.repaint()
        self.repaint()
        self.update()

    def fill(self):
        pix = QtGui.QPixmap()
        p = QtGui.QPainter()
        try:
            if self.ui.with_stop.isChecked():
                delay = int(self.ui.timer_entry.text())
            else:
                delay = 0
        except:
            delay = 0
        
        xmin = xmax = self.points[0][0]; ymin = ymax = self.points[0][1]
        for i in range(1, len(self.points)):
            if self.points[i][0] > xmax:
                xmax = self.points[i][0]
            elif self.points[i][0] < xmin:
                xmin = self.points[i][0]
            if self.points[i][1] > ymax:
                ymax = self.points[i][1]
            elif self.points[i][1] < ymin:
                ymin = self.points[i][1]
                
        #print(xmin, xmax, ymin, ymax)
        cross = []
        y = ymin
        while y < ymax:
            x = xmin
            while x < xmax:
                #print(x)
                curr_col = QtGui.QColor(self.image.pixelColor(x,y))
                curr_col_next = QtGui.QColor(self.image.pixelColor(x+1, y))
                if (curr_col != self.bg_color) and (curr_col_next == self.bg_color):
                    cross.append([y, x])
                x+=1
            y+=1
        cross.sort()
##        print(cross)
        p = QtGui.QPainter()
        p.begin(self.image)
        p.setPen(self.pen_inside)
        lines = []
        y = ymin
        i = 0
        while y < ymax and i < len(cross):
            if cross[i][0] != y:
                y+1
                continue
            if cross[i][0] == cross[i+1][0]\
               and cross[i][1] != cross[i+1][1]:
                print([cross[i], cross[i+1]], y,i)
                lines.append([cross[i], cross[i+1]])
                i+2
            else:
                y+=1
                i+=1
        count = 0
        print(lines)
        for j in range(10):
            for i in range(count,count + len(cross) // 10, 2):
##                print(cross[i], cross[i+1])
##                print(count)
                p.drawLine(cross[i][1], cross[i][0],\
                            cross[i+1][1], cross[i+1][0])
            count += len(cross)//10
            if self.ui.with_stop.isChecked():
                self.go_delay()
        p.end()
##        self.show_image()

        
    def color_choose_border(self):
        self.color_bord = QtWidgets.QColorDialog.getColor()
        self.pen_bord.setColor(self.color_bord)
        self.change_color_check()

    def color_choose_inside(self):
        self.color_inside = QtWidgets.QColorDialog.getColor()
        self.pen_inside.setColor(self.color_inside)
        self.change_color_check()
    
    def draw_coord(self):
        p = QtGui.QPainter()
        p.begin(self.image)
        p.drawLine(0, 0,\
                           self.scene_width, 0)
        p.drawLine(0, 0,\
                           0, self.scene_height)
        
        p.drawLine(10 , self.scene_height - 20,\
                           0, self.scene_height)

        p.drawLine(self.scene_width, 0,\
                           self.scene_width - 20, 0 + 10)
        self.show_image()
        p.end()

    def change_color_check(self):
        pixmap = QtGui.QPixmap(40,40)
        pixmap.fill(self.color_bord)
        self.color_check_border.addPixmap(pixmap)
        
        pixmap = QtGui.QPixmap(40,40)
        pixmap.fill(self.color_inside)
        self.color_check_inside.addPixmap(pixmap)

    def mousePressEvent(self, QMouseEvent):
        coord = QMouseEvent.pos()
        y = coord.y()
        x = coord.x()
        if (x >= 15 and y >= 15 and y <= self.scene_height and x <= self.scene_width):
            x-=15
            y-=15
        self.add_point(x,y)

    def sign(self, x):
        if x > 0:
            return 1
        else:
            return -1

    def draw_brez_line(self, x1, y1, x2, y2):
        print('here')
        dx = int(x2 - x1)
        dy = int(y2 - y1)
        sx = sign(dx)
        sy = sign(dy)
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
            
        for i in range(int(dx+1)):
            print(x,y)
            self.image.setPixel(x,y,self.color_bord.rgb())
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
