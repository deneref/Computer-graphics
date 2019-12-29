from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class myScene(QGraphicsScene):
    def __init__(self, parent):
##        QtWidgets.QGraphicsScene.__init__(self, parent)
        super().__init__()
        self.parent = parent
        
    def mouseMoveEvent(self, event):
        parent = self.parent
        if not parent.get_pixel and not parent.new:
            parent.draw_figure()
        cord = event.scenePos()
        x = cord.x()
        y = cord.y()
        
        if parent.edges and not parent.new:
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
                parent.Bresenham(parent.edges[-1][0],\
                                parent.edges[-1][1],\
                                x, y, parent.color_bord.rgb())
            parent.repaint()

    def mouseReleaseEvent(self, event):
        parent = self.parent
        #parent.draw_figure()
        
        cord = event.scenePos()
        x = cord.x()
        y = cord.y()
        
##        if parent.ui.lines_draw.isChecked():
##            if parent.edges:
##                num = len(parent.edges[-1])
##                if parent.capslock and num:
##                    if y != parent.edges[-1][1]:
##                        t = ((x - parent.edges[-1][0])/\
##                             (y - parent.edges[-1][1]))
##                    else:
##                        t = 2
##                    if abs(t) <= 1:
##                        x = parent.edges[-1][0]
##                    else:
##                        y = parent.edges[-1][1]
##                if num > 0:
##                    parent.Bresenham(parent.edges[-1][0],\
##                                     parent.edges[-1][1],\
##                                     x,y)
##                    parent.add_point(x,y)
##        elif parent.ui.cutter.isChecked():
##            print(parent.cutter, x ,y)
##            parent.draw_cutter(x,y)
##            print(parent.cutter)
##        parent.repaint()

if __name__ == "main":
    pass
