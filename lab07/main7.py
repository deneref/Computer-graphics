import sys
from lab07_ui import *
from PyQt5 import *
from math import *
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPixmap
import time

class myScene(QtWidgets.QGraphicsScene):
    def __init__(self, parent=None):
        QtWidgets.QGraphicsScene.__init__(self, parent)
        self.parent = parent
        
##    def mousePressEvent(self, event):
##        x = event.scenePos().x()
##        y = event.scenePos().y()
##        if self.parent.ui.lines_draw.isChecked():
##            self.parent.add_point(x, y)
##        elif self.parent.ui.cutter.isChecked():
##            self.parent.draw_cutter(x,y)
##        self.parent.scene.update()
    def mouseMoveEvent(self, event):
        parent = self.parent
        parent.draw_figure()
        pen = QtGui.QPainter()
        pen.begin(parent.image)
        pen.setPen(parent.pen_line)
        if parent.ui.lines_draw.isChecked():
            x = event.scenePos().x()
            y = event.scenePos().y()
            if parent.edges:
                num = len(parent.edges[-1])
                if parent.capslock and num:
                    if y != parent.edges[-1][1]:
                        t = ((x - parent.edges[-1][0])/\
                             (y - parent.edges[-1][1]))
                    else:
                        t = 2
                    if abs(t) <= 1:
                        x = parent.edges[-1][0]
                    else:
                        y = parent.edges[-1][1]
                if num > 0:
                    parent.draw_figure()
                    pen.drawLine(parent.edges[-1][0],\
                                    parent.edges[-1][1],\
                                    x, y)
        pen.end()
            
        
class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        #устанавливает интерфейс
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #настройка размеров канваса
        self.scene_width = 720
        self.scene_height = 780
        self.ui.c.setGeometry(QtCore.QRect(10, 10,\
                                        10+self.scene_width, 10+self.scene_height))

        #установка текущего цвета
        self.color_line = QtGui.QColor("#fc6c2d")
        self.color_cut = QtGui.QColor("#170691")
        self.bg_color = QtGui.QColor("#ffffff")
        self.pen_line = QtGui.QPen(self.color_line)
        self.pen_cut = QtGui.QPen(self.color_cut)
        self.rect = QtCore.QRectF(QtCore.QPointF(10, 10), QtCore.QSizeF(30, 30))

        self.painter_line = QtGui.QPainter()
        self.painter_line.setPen(self.pen_line)

        self.painter_cut = QtGui.QPainter()
        self.painter_cut.setPen(self.pen_cut)

        #проверка цвета
        self.color_check_line = QtWidgets.QGraphicsScene()
        self.ui.c_col_line.setScene(self.color_check_line)

        self.color_check_cut = QtWidgets.QGraphicsScene()
        self.ui.c_col_cut.setScene(self.color_check_cut)
        self.change_color_check()
        
        #устанавливает сцену
        self.scene = myScene(self)
        
        self.image = QtGui.QImage(self.scene_width, self.scene_height, QtGui.QImage.Format_RGB32)
        self.image.fill(self.bg_color)
        self.scene.addPixmap(QPixmap.fromImage(self.image))

        self.ui.c.setStyleSheet("background-color: white")
        self.ui.c.setScene(self.scene)
     
        # Здесь прописываем событие нажатия на кнопку                     
        self.ui.add_point.clicked.connect(self.add_point_bttn)
        self.ui.clear_all.clicked.connect(self.Clear_Scene)
        self.ui.delete_point.clicked.connect(self.get_pos_to_delete)
        self.ui.col_line_choose.clicked.connect(self.color_choose_line)
        self.ui.col_cut_shoose.clicked.connect(self.color_choose_cut)
        self.ui.cut_button.clicked.connect(self.cut)

        # Здеть тогл
        self.ui.lines_draw.toggled.connect(self.switch)
        self.ui.lines_draw.toggle()

        #точки и все такое
        self.edges = [] #здесь храняться отрезки [x1,y1,x2,y2] - каждый отрезок
        self.cutter = [] #здесь коордиаты отсекателя
        self.new = True #отслеживание первого нажатия на канвас используется и для рисования отрезков, и для рисования отсекателя
        self.draw_coord()
        self.capslock = False

        #лист бокс и друзья
        self.ui.list_point.itemDoubleClicked.connect(self.delete_point)

    def Clear_Scene(self):
        self.image.fill(self.bg_color)
        self.edges = []
        self.draw_coord()
        self.ui.list_point.clear()
        self.new = True
        
    def show_image(self):
        pass

    def change_color_check(self):
        self.color_check.addRect(self.rect, self.pen)
        painter = QtGui.QPainter(self)
        painter.setPen(self.pen)
        painter.setBrush(self.brush)
        self.pen.setWidth(3)
        self.color_check.addRect(self.rect, self.pen)
        self.pen.setWidth(1)

    def draw_cutter(self, x, y):
        self.draw_figure()
        p = QtGui.QPainter()
        p.begin(self.image)
        p.setPen(self.pen_cut)
        if self.new:
            self.cutter = []
            self.cutter.append(x); self.cutter.append(y)
            self.new = False
        else:
            #self.draw_figure()
            self.cutter.append(x); self.cutter.append(y)
            #своп для того, чтобы рисовалось адекватно
            if self.cutter[0] > self.cutter[2]:
                self.cutter[0], self.cutter[2] = self.cutter[2],self.cutter[0]
            if self.cutter[1] > self.cutter[3]:
                self.cutter[1], self.cutter[3] = self.cutter[3], self.cutter[1]
            p.drawRect(self.cutter[0], self.cutter[1],\
                       abs(self.cutter[2] - self.cutter[0]), abs(self.cutter[3] - self.cutter[1]))
            self.new = True
        p.end()

    def add_point_bttn(self):
        try:
            x1 = int(self.ui.x1_entry.text())
            y1 = int(self.ui.y1_entry.text())
            x2 = int(self.ui.x2_entry.text())
            y2 = int(self.ui.y2_entry.text())
        except:
            return 0
        self.new = True
        self.add_point(x1,y1)
        self.add_point(x2,y2)

    def add_point(self, x, y):
        if self.ui.lines_draw.isChecked():
            if self.new:
                self.edges.append([x,y,x,y])
                self.new = False
            else:
                self.edges[-1][2] = x
                self.edges[-1][3] = y
                #self.edges.append([x,y, x, y])
                self.new = True
                self.print_to_list()
            if len(self.edges) > 0:
                self.draw_figure()
##            self.ui.list_point.addItem("{} {}".format(x,y))

    def draw_figure(self):
        self.image.fill(self.bg_color)
        self.draw_coord()
        self.draw_edges()

    def print_to_list(self):
        self.ui.list_point.clear()
        self.ui.list_point.addItem("{}      {}        {}        {}".format("X1", "Y1", "X2", "Y2"))
        for i in range(len(self.edges)):
            x1 = self.edges[i][0]; x2 = self.edges[i][2]
            y1 = self.edges[i][1]; y2 = self.edges[i][3]
            self.ui.list_point.addItem("{}   {}   {}   {}".format(x1,y1, x2, y2))

    def draw_edges(self):
        p = QtGui.QPainter()
        p.begin(self.image)
        p.setPen(self.pen_line)
        for e in self.edges:
            #p.drawEllipse(e[0]-2,e[1]-2,4,4)
            #p.drawEllipse(e[2]-2,e[3]-2,4,4)
            p.drawLine(e[0], e[1],
                               e[2], e[3])
        p.end()

    def log_prod(self, code1, code2):
        p = 0
        for i in range(4):
            p += code1[i] & code2[i]
        return p

    def get_code(self, point):
        #point[0] = [x1,y1]
        #point[1] = [x2, y2]
        code = [0,0,0,0]
        if point[0] < self.cutter[0]:
            code[0] = 1
        if point[0] > self.cutter[1]:
            code[1] = 1
        if point[1] < self.cutter[2]:
            code[2] = 1
        if point[1] > self.cutter[3]:
            code[3] = 1
        return code

    def is_visible(self, line):
        #0 - невидимый
        #1 - видимый
        #2 - частично видимый
        s1 = sum(self.get_code(line[0]))
        s2 = sum(self.get_code(line[1]))

        visible = 2
        if not s1 and not s2:
            visible = 1
        else:
            l = self.log_prod(self.get_code(line[0]), self.get_code(line[1]))
            if l != 0:
                visible = 0
        return visible
        
        
    def cut(self):
        if len(self.edges) < 1 or len(self.cutter) < 4:
            return 0
        self.cutter[1],self.cutter[2] = self.cutter[2],self.cutter[1]

        for line in self.edges:
            print(line)
            self.cohen_sutherland([[line[0], line[1]],[line[2],line[3]]])

    def cohen_sutherland(self,line):
        p = QtGui.QPainter()
        p.begin(self.image)
        p.setPen(self.pen_cut)
        flag = 1
        t = 1
        #проверка на вертикальность и горизонтальность
        if line[1][0] - line[0][0] == 0:
            flag = -1 #отрезок вертикальный
        else:
            t = (line[1][1] - line[0][1]) / (line[1][0] - line[0][0])
            if t == 0:
                flag = 0 #горизонтальный отрезок
        for i in range(4):
            vis = self.is_visible(line)
            if vis == 1:
                p.drawLine(line[0][0], line[0][1], line[1][0],line[1][1])
                return 0
            elif not vis:
                return 0
            code1 = self.get_code(line[0])
            code2 = self.get_code(line[1])

            if code1[i] == code2[i]:
                continue

            if not code1[i]:
                line[0], line[1] = line[1], line[0]

            if flag != -1:
                if i<2:
                    line[0][1] = t * (self.cutter[i] - line[0][0]) + line[0][1]
                    line[0][0] = self.cutter[i]
                    continue
                else:
                    line[0][0] = (1/t) * (self.cutter[i] - line[0][1]) + line[0][0]

            line[0][1] = self.cutter[i]
        p.drawLine(line[0][0], line[0][1], line[1][0], line[1][1])
                    
                
        p.end()
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
        self.new = True
        
    def color_choose_line(self):
        self.color_line = QtWidgets.QColorDialog.getColor()
        self.pen_line.setColor(self.line)
        self.change_color_check()

    def color_choose_cut(self):
        self.color_cut = QtWidgets.QColorDialog.getColor()
        self.pen_cut.setColor(self.color_cut)
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
        pixmap.fill(self.color_line)
        self.color_check_line.addPixmap(pixmap)
        
        pixmap = QtGui.QPixmap(40,40)
        pixmap.fill(self.color_cut)
        self.color_check_cut.addPixmap(pixmap)
        
    def paintEvent(self, e):
        self.scene.clear()
        self.scene.addPixmap(QPixmap.fromImage(self.image))

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == 16777252:
            self.capslock = not self.capslock

    def mousePressEvent(self, QMouseEvent):
        coord = QMouseEvent.pos()
        y = coord.y()
        x = coord.x()
        if x >= 10 and y>=10 and\
           y<=self.scene_height and x<= self.scene_width:
            x -= 15
            y -= 15
        if self.ui.lines_draw.isChecked():
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
        elif self.ui.cutter.isChecked():
            self.draw_cutter(x,y)
        self.scene.update()
        
      
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
