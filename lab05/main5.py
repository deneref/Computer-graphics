import sys
from lab05_ui import *
from PyQt5 import *
from math import *

class myScene(QtWidgets.QGraphicsScene):
    def __init__(self, parent=None):
        QtWidgets.QGraphicsScene.__init__(self, parent)
##        self.setSceneRect(-100, -100, 200, 200)
    def mousePressEvent(self, event):
        x = event.scenePos().x()
        y = event.scenePos().y()
        myapp.add_point(x, y)
        
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
        self.pen_bord = QtGui.QPen(self.color_bord)
        self.pen_inside = QtGui.QPen(self.color_inside)
        self.rect = QtCore.QRectF(QtCore.QPointF(10, 10), QtCore.QSizeF(30, 30))

        #проверка цвета
        self.color_check_border = QtWidgets.QGraphicsScene()
        self.ui.c_col_border.setScene(self.color_check_border)

        self.color_check_inside = QtWidgets.QGraphicsScene()
        self.ui.c_col_inside.setScene(self.color_check_inside)
        self.change_color_check()
        
        #устанавливает сцену
        self.scene = myScene(self)
        self.ui.c.setScene(self.scene)
        self.image = QtGui.QImage(561, 581, QtGui.QImage.Format_ARGB32_Premultiplied)
        self.image.fill(QtGui.QColor(200,200,215,255))
        self.scene.addItem(self.image)
     
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
        self.scene.clear()
        self.points = []
        self.draw_coord()

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
        self.scene.clear()
        self.draw_coord()
        for i in range(len(self.points)-1):
            self.scene.addLine(self.points[i][0], self.points[i][1],
                               self.points[i+1][0], self.points[i+1][1], self.pen_bord)
        if self.ui.connect_check.isChecked():
            self.scene.addLine(self.points[-1][0], self.points[-1][1],
                               self.points[0][0], self.points[0][1], self.pen_bord)
        

    def print_to_list(self):
        self.ui.list_point.clear()
        for i in range(len(self.points)):
            x = self.points[i][0]
            y = self.points[i][1]
            self.ui.list_point.addItem("{} {}".format(x,y))

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
        if self.ui.with_stop.isChecked():
            self.ui.timer_label.show()
            self.ui.timer_entry.show()
        else:
            self.ui.timer_label.hide()
            self.ui.timer_entry.hide()

    def fill(self):
        pix = QtGui.QPixmap()
        p = QtGui.QPainter()
        
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
                
        print(xmin, xmax, ymin, ymax)
        cross = []
        y = ymin
        while y < ymax:
            x = xmin
            while x < xmax:
                #print(x)
                curr_col = QtGui.QColor(self.image.pixelColor(x,y))
                if curr_col == self.color_bord:
                    cross.append(x, y)
                x+=1
            y+=1
        cross.sort()
        print(cross)
            


    def color_choose_border(self):
        self.color_bord = QtWidgets.QColorDialog.getColor()
        self.pen_bord.setColor(self.color_bord)
        self.change_color_check()

    def color_choose_inside(self):
        self.color_inside = QtWidgets.QColorDialog.getColor()
        self.pen_inside.setColor(self.color_inside)
        self.change_color_check()
    
    def draw_coord(self):
        self.scene.addLine(0, 0,\
                           self.scene_width, 0)
        self.scene.addLine(0, 0,\
                           0, self.scene_height)
        
        self.scene.addLine(10 , self.scene_height - 20,\
                           0, self.scene_height)
##        self.scene.addLine(-10 , self.scene_height - 20,\
##                           0, self.scene_height)
        
##        self.scene.addLine(self.scene_width, 0,\
##                           self.scene_width - 20, 0 - 10)
        self.scene.addLine(self.scene_width, 0,\
                           self.scene_width - 20, 0 + 10)

    def change_color_check(self):
        pixmap = QtGui.QPixmap(40,40)
        pixmap.fill(self.color_bord)
        self.color_check_border.addPixmap(pixmap)
        
        pixmap = QtGui.QPixmap(40,40)
        pixmap.fill(self.color_inside)
        self.color_check_inside.addPixmap(pixmap)
        
        
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
