from math import *
from tkinter import *
from tkinter.messagebox import *
import copy
canvas_width = 700 // 2
canvas_height = 700 // 2

class cat():
    def __init__(self, head_size = 50):

        self.head_radius = head_size #размер головы
        
        self.corpus_center = [0,0] #центр эллипса
        self.corpus_hw = [(4.6/3)*self.head_radius,\
                             (7/3)*self.head_radius] #полуоси эллипса [rx, ry]
        self.head_shift = [0, self.corpus_hw[1]+self.head_radius] #смещение относительно начала координат головы
        
        self.eyes_radius = int((1/5)*self.head_radius) #радиус глаз
        self.eyes_shift = [0.5*self.head_radius + self.head_shift[0],\
                           0.5*self.head_radius + self.head_shift[1]]
        
        self.must_shift = [0, \
                               self.head_shift[1]] #смещение усов
        self.must_len = self.head_radius #длина усов
        
        self.corpus = copy.deepcopy(self.create_ellipse(self.corpus_hw[0], self.corpus_hw[1], \
                                                       self.corpus_center[0], self.corpus_center[1]))
        self.head = copy.deepcopy(self.create_ellipse(self.head_radius, self.head_radius,\
                                                     self.head_shift[0],self.head_shift[1]))
        self.right_eye = copy.deepcopy(self.create_ellipse(self.eyes_radius, self.eyes_radius,\
                                                          self.eyes_shift[0], self.eyes_shift[1]))
        self.left_eye = copy.deepcopy(self.create_ellipse(self.eyes_radius, self.eyes_radius,\
                                                          -1*self.eyes_shift[0], self.eyes_shift[1]))
        #усы
        self.right_must = []
        self.left_must = []
        self.create_must(self.must_shift[0], self.must_shift[1])
        
        #ухи
        self.right_ear = []
        self.left_ear = []
        self.create_ears()
        
        #self.draw_cat()

    def draw_coord(self):
        c.create_line(0, canvas_height,\
                           canvas_width*2, canvas_height)
        c.create_line(canvas_width, 0,\
                      canvas_width, canvas_height*2)

    def create_ellipse(self, rx, ry, shift_x, shift_y):
        coord1 = [0, ry]
        ellipse = []
        
        pl = ry**2 - rx**2 * ry + (1/4)*(rx**2)
        x = 0
        y = ry
        while (2*(ry**2) * x < 2*(rx**2)*y):
           if pl < 0:
               x += 1
               coord = [x, y]
               pl = pl + 2* (ry**2) * x + ry**2
               ellipse.append(coord)
           else:
               x += 1
               y -= 1
               pl = pl + 2*(ry**2)*x - 2*(rx**2)*y + ry**2
               coord = [x,y]
               ellipse.append(coord)

        p2 = (ry**2)*(x + 1/2)**2 + (rx**2) * (y - 1)**2 - (rx**2) * (ry**2)
        while (y > 0):
            if p2 > 0:
               y = y - 1
               coord = [x, y]
               p2 = p2 - 2*(rx**2)*(y) + (rx**2)
               ellipse.append(coord)
            else:
                x += 1
                y -= 1
                p2 = p2 + 2*(ry**2)*x - 2*(rx**2)*y + (rx**2)
                coord = [x, y]
                ellipse.append(coord)

        for i in range(len(ellipse)-1, 1, -1):
            coord = [ellipse[i][0], -1*ellipse[i][1]]
            ellipse.append(coord)
        for i in range(len(ellipse) -1 , 1, -1):
            coord = [-1*ellipse[i][0], ellipse[i][1]]
            ellipse.append(coord)
        ellipse.append([ellipse[0][0], ellipse[0][1]])

        for i in range(len(ellipse)):
            ellipse[i][0] += shift_x
            ellipse[i][1] -= shift_y
        
        return ellipse
    
    def create_must(self, shift_x, shift_y):
        self.right_must.append([1/3*self.head_radius,\
                                self.head_radius//4])
        angle = 0.785
        for i in range(3):
            self.right_must.append([self.right_must[0][0]+self.must_len*cos(angle),\
                               self.right_must[0][1]+self.must_len*sin(angle)])
            angle -= 0.785

        for i in range(len(self.right_must)):
            self.left_must.append([-1*self.right_must[i][0], \
                                   self.right_must[i][1]])
            
        for i in range(len(self.right_must)):
            self.right_must[i][0] += shift_x
            self.right_must[i][1] -= shift_y
            self.left_must[i][0] += shift_x
            self.left_must[i][1] -= shift_y


    def create_ears(self):
        angle = -0.2
        for i in range(3):
            self.right_ear.append([self.head_shift[0]+self.head_radius*cos(angle),\
                               -1*self.head_shift[1]+self.head_radius*sin(angle)])
            angle -= 0.35

        self.right_ear[1][0] += (2/3)* self.head_radius
        self.right_ear[1][1] -= (2/3) * self.head_radius

        for i in range(len(self.right_ear)):
            self.left_ear.append([-1*self.right_ear[i][0],\
                                 self.right_ear[i][1]])
        
    def draw_cat(self):
        self.draw_coord()
        #рисуются голова, тело и глаза
        for i in range(len(self.corpus)-1):
            c.create_line(self.corpus[i][0] + canvas_width,\
                          self.corpus[i][1] + canvas_height,\
                          self.corpus[i+1][0] + canvas_width,\
                          self.corpus[i+1][1] + canvas_height)
        for i in range(len(self.head)-1):
            c.create_line(self.head[i][0] + canvas_width,\
                          self.head[i][1] + canvas_height,\
                          self.head[i+1][0] + canvas_width,\
                          self.head[i+1][1] + canvas_height)
        for i in range(len(self.right_eye)-1):
             c.create_line(self.right_eye[i][0] + canvas_width,\
                          self.right_eye[i][1] + canvas_height,\
                          self.right_eye[i+1][0] + canvas_width,\
                          self.right_eye[i+1][1] + canvas_height)
             c.create_line(self.left_eye[i][0] + canvas_width,\
                          self.left_eye[i][1] + canvas_height,\
                          self.left_eye[i+1][0] + canvas_width,\
                          self.left_eye[i+1][1] + canvas_height)
        #рисуются масташи
        for i in range (1, len(self.right_must)):
            c.create_line(self.right_must[0][0]+ canvas_width,\
                          self.right_must[0][1] + canvas_height,\
                          self.right_must[i][0] + canvas_width,\
                          self.right_must[i][1] + canvas_height)
        
            c.create_line(self.left_must[0][0] + canvas_width,\
                          self.left_must[0][1] + canvas_height,\
                          self.left_must[i][0] + canvas_width,\
                          self.left_must[i][1] + canvas_height) 


        for i in range(len(self.right_ear)-1):
            c.create_line(self.right_ear[i][0] + canvas_width, \
                          self.right_ear[i][1] + canvas_height,\
                          self.right_ear[i+1][0] + canvas_width,\
                          self.right_ear[i+1][1] + canvas_height)

            c.create_line(self.left_ear[i][0] + canvas_width, \
                          self.left_ear[i][1] + canvas_height,\
                          self.left_ear[i+1][0] + canvas_width,\
                          self.left_ear[i+1][1] + canvas_height)


    def move_cat(self, dx, dy):
        for i in range(len(self.corpus)):
            self.corpus[i][0] += dx
            self.corpus[i][1] -= dy
            

        for i in range(len(self.head)):
            self.head[i][0] += dx
            self.head[i][1] -= dy

        for i in range(len(self.right_eye)):
            self.right_eye[i][0] += dx
            self.right_eye[i][1] -= dy
            self.left_eye[i][0] += dx
            self.left_eye[i][1] -= dy

        for i in range(len(self.right_must)):
            self.right_must[i][0] += dx
            self.right_must[i][1] -= dy
            self.left_must[i][0] += dx
            self.left_must[i][1] -= dy
            
        for i in range(len(self.right_ear)):
            self.right_ear[i][0] += dx
            self.right_ear[i][1] -= dy
            self.left_ear[i][0] += dx
            self.left_ear[i][1] -= dy
        c.delete('all')
        self.draw_cat()

    def rotate_cat(self, xc, yc, angle):
        angle = radians(angle)
        for i in range(len(self.corpus)):
            self.corpus[i][0], self.corpus[i][1] =\
                               xc + (self.corpus[i][0] - xc)*cos(angle) +\
                               (self.corpus[i][1]-yc)*sin(angle)*canvas_width/canvas_height,\
                               yc + (self.corpus[i][1] - yc)*cos(angle) -\
                               (self.corpus[i][0]-xc)*sin(angle)*canvas_height/canvas_width
            
                                     
        for i in range(len(self.head)):
            self.head[i][0], self.head[i][1] =\
                               xc + (self.head[i][0] - xc)*cos(angle) +\
                               (self.head[i][1]-yc)*sin(angle)*canvas_width/canvas_height,\
                               yc + (self.head[i][1] - yc)*cos(angle) -\
                               (self.head[i][0]-xc)*sin(angle)*canvas_height/canvas_width

        for i in range(len(self.right_eye)):
            self.right_eye[i][0], self.right_eye[i][1] =\
                               xc + (self.right_eye[i][0] - xc)*cos(angle) +\
                               (self.right_eye[i][1]-yc)*sin(angle)*canvas_width/canvas_height,\
                               yc + (self.right_eye[i][1] - yc)*cos(angle) -\
                               (self.right_eye[i][0]-xc)*sin(angle)*canvas_height/canvas_width
            self.left_eye[i][0], self.left_eye[i][1] =\
                               xc + (self.left_eye[i][0] - xc)*cos(angle) +\
                               (self.left_eye[i][1]-yc)*sin(angle)*canvas_width/canvas_height,\
                               yc + (self.left_eye[i][1] - yc)*cos(angle) -\
                               (self.left_eye[i][0]-xc)*sin(angle)*canvas_height/canvas_width

        for i in range(len(self.right_must)):
            self.right_must[i][0], self.right_must[i][1] =\
                               xc + (self.right_must[i][0] - xc)*cos(angle) +\
                               (self.right_must[i][1]-yc)*sin(angle)*canvas_width/canvas_height,\
                               yc + (self.right_must[i][1] - yc)*cos(angle) -\
                               (self.right_must[i][0]-xc)*sin(angle)*canvas_height/canvas_width
            self.left_must[i][0], self.left_must[i][1] =\
                               xc + (self.left_must[i][0] - xc)*cos(angle) +\
                               (self.left_must[i][1]-yc)*sin(angle)*canvas_width/canvas_height,\
                               yc + (self.left_must[i][1] - yc)*cos(angle) -\
                               (self.left_must[i][0]-xc)*sin(angle)*canvas_height/canvas_width
        for i in range(len(self.right_ear)):
            self.right_ear[i][0], self.right_ear[i][1] =\
                               xc + (self.right_ear[i][0] - xc)*cos(angle) +\
                               (self.right_ear[i][1]-yc)*sin(angle)*canvas_width/canvas_height,\
                               yc + (self.right_ear[i][1] - yc)*cos(angle) -\
                               (self.right_ear[i][0]-xc)*sin(angle)*canvas_height/canvas_width
            self.left_ear[i][0], self.left_ear[i][1] =\
                               xc + (self.left_ear[i][0] - xc)*cos(angle) +\
                               (self.left_ear[i][1]-yc)*sin(angle)*canvas_width/canvas_height,\
                               yc + (self.left_ear[i][1] - yc)*cos(angle) -\
                               (self.left_ear[i][0]-xc)*sin(angle)*canvas_height/canvas_width

        c.delete('all')
        self.draw_cat()
                               
    def scale_cat(self, xm, ym, kx, ky):
        for i in range(len(self.corpus)):
            self.corpus[i][0], self.corpus[i][1] = \
                   self.corpus[i][0]*kx+(1-kx)*xm,\
                   self.corpus[i][1]*ky+(1-ky)*ym
            
        for i in range(len(self.head)):
            self.head[i][0], self.head[i][1] = \
                   self.head[i][0]*kx+(1-kx)*xm,\
                   self.head[i][1]*ky+(1-ky)*ym

        for i in range(len(self.right_eye)):
            self.right_eye[i][0], self.right_eye[i][1] = \
                   self.right_eye[i][0]*kx+(1-kx)*xm,\
                   self.right_eye[i][1]*ky+(1-ky)*ym
            self.left_eye[i][0], self.left_eye[i][1] = \
                   self.left_eye[i][0]*kx+(1-kx)*xm,\
                   self.left_eye[i][1]*ky+(1-ky)*ym

        for i in range(len(self.right_must)):
            self.right_must[i][0], self.right_must[i][1] = \
                   self.right_must[i][0]*kx+(1-kx)*xm,\
                   self.right_must[i][1]*ky+(1-ky)*ym
            self.left_must[i][0], self.left_must[i][1] = \
                   self.left_must[i][0]*kx+(1-kx)*xm,\
                   self.left_must[i][1]*ky+(1-ky)*ym

        for i in range(len(self.right_ear)):
            self.right_ear[i][0], self.right_ear[i][1] = \
                   self.right_ear[i][0]*kx+(1-kx)*xm,\
                   self.right_ear[i][1]*ky+(1-ky)*ym
            self.left_ear[i][0], self.left_ear[i][1] = \
                   self.left_ear[i][0]*kx+(1-kx)*xm,\
                   self.left_ear[i][1]*ky+(1-ky)*ym

        c.delete('all')
        self.draw_cat()

    def copycat(self, copied):
        self.corpus = copy.deepcopy(copied.corpus)
        self.head = copy.deepcopy(copied.head)
        self.right_eye = copy.deepcopy(copied.right_eye)
        self.left_eye = copy.deepcopy(copied.left_eye)
        self.right_must = copy.deepcopy(copied.right_must)
        self.left_must = copy.deepcopy(copied.left_must)
        self.right_ear = copy.deepcopy(copied.right_ear)
        self.left_ear = copy.deepcopy(copied.left_ear)

        

def move():
    global gato_curr
    global gato_prev
    try:
        dx = int(dx_move_entry.get())
        dy = int(dy_move_entry.get())
    except:
        showerror('Ошибка ввода','Для перемещения введите\nцелые значения')
        return 0

    gato_prev.copycat(gato_curr)
    gato_curr.move_cat(dx, dy)

def rotate():
    global gato_curr
    global gato_prev

    try:
        xc = int(dx_rotate_entry.get())
        yc = int(dy_rotate_entry.get())
        angle = float(angle_rotate_entry.get())
    except:
        showerror('Ошибка ввода',\
                  'Для поворота введите целые значения в поля xc и xy\nи дробное или целое для угла поворота')
        return 0

    gato_prev.copycat(gato_curr)
    gato_curr.rotate_cat(xc, yc, angle)

def scale():
    global gato_curr
    global gato_prev
    try:
        kx = float(kx_scale_entry.get())
        ky = float(ky_scale_entry.get())
        xm = float(Xm_scale_entry.get())
        ym = float(Ym_scale_entry.get())
    except:
        showerror('Ошибка ввода',\
                  'Для масштабирования введите\
                  целые значения в поля Xm и Ym - центр масштабирования\
                  и дробное или целое для полей xk и yk - коэффициенты масштабирования\n')
    
    gato_prev.copycat(gato_curr)
    gato_curr.scale_cat(xm, ym, kx, ky)


def reset():
    global gato_curr
    global gato_prev
    
    gato_prev.copycat(gato_curr)
    gato_curr = cat()
    c.delete('all')
    gato_curr.draw_cat()
    

def back():
    global gato_curr
    global gato_prev
    gato_curr.copycat(gato_prev)
    c.delete('all')
    gato_curr.draw_cat()



root = Tk()

root.title('Компьютерная графика. Лабораторная работа №2')
c = Canvas(root,\
           width = canvas_width*2,\
           height = canvas_height*2,\
           bg = 'white')
c.grid(row = 0, column = 0, rowspan = 40)
gato_curr = cat()
gato_curr.draw_cat()
gato_prev = cat()
#кнопки для функций
move_button = Button(text = 'Переместить',font=("Helvetica", 16),\
                   width = 20, command = lambda : move())
move_button.grid(row = 10, column = 1, columnspan = 4)

scale_button = Button(text = 'Масштабировать',font=("Helvetica", 16),\
                     width = 20, command = lambda : scale())
scale_button.grid(row = 22 ,column = 1, columnspan = 4)

rotate_button = Button(text = 'Вращать',font=("Helvetica", 16),\
                      width = 20, command = lambda : rotate())
rotate_button.grid(row = 38, column = 1, columnspan = 4)
#кнопки назад и возврата
back_button = Button(text = "back", width = 10, height = 3,\
                     font=("Helvetica", 16), command = lambda : back())
back_button.grid(row = 39, column = 1, columnspan = 2)

reset_button = Button(text = 'reset', width = 10, height = 3,\
                      font=("Helvetica", 16), command = lambda : reset())
reset_button.grid(row = 39, column = 3, columnspan = 2)

#Энтри и лейблы для перемещения
move_info_label_1 = Label(text = "по оси Ox",\
                        font=("Helvetica", 14))
move_info_label_1.grid(row = 0, column = 1, columnspan = 4, rowspan = 3)

move_info_label_2 = Label(text = "по оси Oy",\
                        font=("Helvetica", 14))
move_info_label_2.grid(row = 5, column = 1, columnspan = 4, rowspan = 1)

dx_move_label = Label(text = "dx",font=("Helvetica", 16))
dx_move_label.grid(row = 4, column = 1, columnspan = 1)

dx_move_entry = Entry(width = 15)
dx_move_entry.grid(row = 4, column = 2, columnspan = 2)

dy_move_label = Label(text = "dy",font=("Helvetica", 16))
dy_move_label.grid(row = 6, column = 1, columnspan = 1)

dy_move_entry = Entry(width = 15)
dy_move_entry.grid(row = 6, column = 2, columnspan = 2)

#Энтри и лейблы для масштабирования
scale_info_label_1= Label(text = "Центр масштабирования", \
                         font = ("Halvetica", 14))
scale_info_label_1.grid(row = 13, column = 1, columnspan = 4)

scale_info_label_2= Label(text = "Коэффициент масштабирования", \
                         font = ("Halvetica", 14))
scale_info_label_2.grid(row = 17, column = 1, columnspan = 4) 

Xm_scale_label = Label(text = "Xm",font=("Helvetica", 16))
Xm_scale_label.grid(row = 14, column = 1, columnspan = 1)

Xm_scale_entry = Entry(width = 15)
Xm_scale_entry.grid(row = 14, column = 2, columnspan = 2)

Ym_scale_label = Label(text = "Ym",font=("Helvetica", 16))
Ym_scale_label.grid(row = 16, column = 1, columnspan = 1)

Ym_scale_entry = Entry(width = 15)
Ym_scale_entry.grid(row = 16, column = 2, columnspan = 2)

kx_scale_label = Label(text = "kx",font=("Helvetica", 16))
kx_scale_label.grid(row = 18, column = 1, columnspan = 1)

kx_scale_entry = Entry(width = 15)
kx_scale_entry.grid(row = 18, column = 2, columnspan = 2)

ky_scale_label = Label(text = "ky",font=("Helvetica", 16))
ky_scale_label.grid(row = 20, column = 1, columnspan = 1)

ky_scale_entry = Entry(width = 15)
ky_scale_entry.grid(row = 20, column = 2, columnspan = 2)

#Энтри и лейблы для поворота

rotate_label_info = Label(text = 'Центр поворота',font = ("Halvetica", 14))
rotate_label_info.grid(row = 25, column = 1, columnspan = 4)

dx_rotate_label = Label(text = "Xc",font=("Helvetica", 16))
dx_rotate_label.grid(row = 26, column = 1, columnspan = 1)

dx_rotate_entry = Entry(width = 15)
dx_rotate_entry.grid(row = 26, column = 2, columnspan = 2)

dy_rotate_label = Label(text = "Yc",font=("Helvetica", 16))
dy_rotate_label.grid(row = 28, column = 1, columnspan = 1)

dy_rotate_entry = Entry(width = 15)
dy_rotate_entry.grid(row = 28, column = 2, columnspan = 2)

angle_rotate_label = Label(text = "Угол",font=("Helvetica", 16))
angle_rotate_label.grid(row = 32, column = 1, columnspan = 1)

angle_rotate_entry = Entry(width = 15)
angle_rotate_entry.grid(row = 32, column = 2, columnspan = 2)

root.mainloop()
    

