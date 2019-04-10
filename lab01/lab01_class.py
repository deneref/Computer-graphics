from math import *
from defs import *
from tkinter import *
from tkinter import messagebox


class triangle():
    def __init__(self):
        self.x =[]
        self.y = []
        self.result = []

        self.canvas_width = 700
        self.canvas_height = 700
        self.real_width = 20
        self.real_width = 20

        self.len_of_points = 0

        self.coordinates = []

    def print_points(self):
        n = 2
        points_label_text.set('')
        self.len_of_points_label = 0
        i = 0
        self.coord = []
        while i < len(self.x):
            k = self.canvas_width/self.real_width #на сколько надо сместиться на одно ед.деление
            #если выходим за пределы, то считаем новые пределы, все удаляем
            #и строим все точки по новой
            if abs(self.x[i]) >= self.real_width//2  + 1 \
               or abs(self.y[i]) >= self.real_width//2 + 1:
                if abs(self.x[i]) >= self.real_width//2:
                    self.real_width = 2*abs(self.x[i]) + abs(self.x[i])//10 
                    self.real_width = 2*abs(self.x[i]) + abs(self.x[i])//10
                    points_label_text.set('')
                    len_of_points_label = 0
                elif abs(self.y[i]) > self.real_width//2:
                    self.real_width = 2*abs(self.y[i]) + abs(self.y[i])//10
                    self.real_width = 2*abs(self.y[i]) + abs(self.y[i])//10
                    points_label_text.set('')
                    len_of_points_label = 0
                c.delete('all')
                self.draw_coord()
                i = 0
                self.coord = []
            k = self.canvas_width/(self.real_width)
                
            #рисуем точки, n - что-то типо радиуса
            p = c.create_oval(k*self.x[i] + self.canvas_width//2 - n,\
                          k *(self.real_width/2 - self.y[i])+ n,\
                          k*(self.x[i])+ self.canvas_width//2 + n,\
                          k*(self.real_width/2 - self.y[i])- n,\
                          fill = 'green')
            coord = [p, self.x[i], self.y[i]]
            self.coordinates.append(coord)
        
    #попытка печатать в лейбл
            if self.len_of_points_label < 21:
                s = points_label_text.get()
                s+=str(self.x[i])
                s+=' '
                s+=str(self.y[i])
                s+='\n'
                points_label_text.set(s)
                self.len_of_points_label += 1
                s = ''
            i+=1

    def print_result_triangle(self, result):
    ##  в result
    ##  0 - иксы
    ##  1 - игрики
    ##  2 - медиана против первой вершины
    ##  3 - медиана против второй
    ##  4 - медиана против четвертой
        print(self.result)
        k = self.canvas_width/self.real_width
        #добавляем в конец первую точку чтобы треуг замкнулся
        result_x = self.result[0]
        result_y = self.result[1]
        result_x.append(result_x[0])
        result_y.append(result_y[0])
        #print('int canv\n',result)
        for i in range(len(result_x)-1):
            c.create_line((k*result_x[i] + self.canvas_width//2,\
                          k *(self.real_width - result_y[i]) - self.canvas_height//2,\
                          k*(result_x[i+1])+ self.canvas_width//2,\
                          k*(self.real_width - result_y[i+1])- self.canvas_height//2))
        #три медианы пунктиром
        for i in range(3):
            c.create_line((k*result_x[i] + self.canvas_width//2,\
                              k *(self.real_width - result_y[i]) - self.canvas_height//2,\
                              k*(result[i+2][0])+ self.canvas_width//2,\
                              k*(self.real_width - result[i+2][1])- self.canvas_height//2), dash = (4,2))
            
        if (result_x[0] + result_y[0] + result_x[1] + result_y[1] + result_x[2] + result_y[2] == 0):
            messagebox.showinfo("Результат",\
                                "На данных точках нельзя построить такого треугольника, чтобы в него попала хоть одна другая")
        else:
            messagebox.showinfo("Результат",\
                               "На данном множестве точек в треугольнике\nс вершинами [{} {}],[{} {}],[{} {}] разница количества точек,\n попавших в каждый из шести треугольников\nобразованных медианами максимальна".\
                               format(result_x[0], result_y[0], result_x[1], result_y[1], result_x[2], result_y[2]))

    def input_point(self):
        c.delete('all')
        self.draw_coord()
        self.print_points()
            
##        if len(self.x) >= 4:
##            self.result = prosses(self.x, self.y)
##            self.print_result_triangle(self.result)

    def draw_coord(self):
        #рисуем координаты
        #можно подзапариться над делениями
        #они рисуются прямо перед мейнлупом
        c.create_line(0, self.canvas_height//2, self.canvas_width, self.canvas_height//2)
        c.create_line(self.canvas_width//2, 0, self.canvas_width//2, self.canvas_height)
        c.create_line(self.canvas_width//2 , 0,\
                      self.canvas_width//2 + 10, 20)
        c.create_line(self.canvas_width//2 , 0,\
                      self.canvas_width//2- 10, 20)
        c.create_line(self.canvas_width - 20, self.canvas_height//2 + 10,\
                      self.canvas_width, self.canvas_height//2 )
        c.create_line(self.canvas_width - 20, self.canvas_height//2 - 10,\
                      self.canvas_width, self.canvas_height//2)
        for i in range(0, self.canvas_width, 50):
            c.create_line(i, self.canvas_height//2 - 7,
                               i, self.canvas_height//2 + 7)
        for i in range(50, self.canvas_height+50, 50):
            c.create_line(self.canvas_width//2 - 7, i,
                               self.canvas_width//2 + 7, i)


    def add_point(self, x_new, y_new):
        self.x.append(x_new)
        self.y.append(y_new)

def clear_press():
    c.delete('all')
    points.x = [];
    points.y = [];
    points.result = [];
    points.real_width = 20;
    points.real_width = 20;
    points.len_of_points_label = 0
    points_label_text.set('')
    points.draw_coord()

def enter_file_press():
    file_name = file_entry.get()
    if file_name == '':
        messagebox.showerror("Ошибка ввода", "Не стоит оставлять\nэто поле пустым")
        return 0
            #если сначала были введены какие-то точки, а потом читается файл
            #читаем в новый массик, потом добавляем к уже имеющимся
    x_new, y_new = read_points(file_name)
    if(x_new == [] or y_new == []):
        messagebox.showerror("Ошибка ввода",\
                                     "Такого файла нет.\nНе получилось считать точки")
        return 0 
    for j in range(len(x_new)):
        points.add_point(x_new[j], y_new[j])
    points.input_point()

def input_point_press():
    try:
        x0 = float(x_entry.get())
        y0 = float(y_entry.get())
    except:
        messagebox.showerror("Ошибка ввода",\
                             "Точка должна иметь\nцелочисленные координаты")
    points.add_point(x0, y0)
    points.input_point()
    x_entry.delete(0, 'end')
    y_entry.delete(0, 'end')
    x_entry.focus()

def draw_coordinates(event, a, b):
    c.bind("<Motion>", lambda event, a = points.canvas_width,\
           b = points.canvas_height: draw_coordinates(event, a, b))

    x = (event.x - points.canvas_width)/2*2*points.real_width/points.canvas_height + points.real_width/2
    y = (event.y - points.canvas_width)/2*2*points.real_width/points.canvas_height * (-1) - points.real_width/2
    label_coords['text'] = '{:.4}, {:.4}'.format(x, y)


def leave_canvas(event):
    label_coords['text'] = '(-/-)'

def plot_button_press():
    if len(points.x) >= 3:
        points.result = prosses(points.x, points.y)
        points.print_result_triangle(points.result)
    
root = Tk()
root.title('Компьютерная графика. Лабораторная работа №1')
points = triangle()
c = Canvas(root,\
           width = points.canvas_width,\
           height = points.canvas_height,\
           bg = 'white')
c.grid(row = 0, column = 0, rowspan = 30)

#ввод из файла
Label(text = "Ввести точки из файла").grid(row = 2, column = 2, columnspan = 4)
file_entry = Entry(width = 20)
file_entry.grid(row = 3, column = 2, columnspan = 4)

file_insert = Button(text = "Enter", width = 10, height = 2,\
                     command = lambda : enter_file_press())
file_insert.grid(row = 4, column = 2, columnspan = 4)

#Кнопка построить
plot_button = Button(text = "Plot", width = 10, height = 2,\
                     command = lambda : plot_button_press())
plot_button.grid(row = 5, column = 2, columnspan = 4)

#ввод для отдельных точек
Label(text = "x: ").grid(row = 7, column = 2)
x_entry = Entry(width = 10)
x_entry.grid(row = 7, column = 3)

Label(text = "y: ").grid(row = 7, column = 4)
y_entry = Entry(width = 10)
y_entry.grid(row = 7, column = 5, columnspan = 1)

point_enter = Button(text = "Ввести точку", width = 10, height = 2,\
                     command = lambda : input_point_press())
point_enter.grid(row = 9, column = 2, columnspan = 4)

#Лейбл для уже введеных точек
Label(text = "Введеные точки:").grid(row = 10, column = 2, columnspan = 4)
points_label_text = StringVar()
points_label_text.set('')
entered_points = Label(textvariable = points_label_text)
entered_points.grid(row = 11, column = 2, columnspan = 4, rowspan = 20)
len_of_points_label = 0

#Кнопка очистить канвасик и все засетить на дефолт
clear_all = Button(text = "Очистить", width = 15, height = 2,\
                     command = lambda : clear_press())
clear_all.grid(row = 28, column = 2, columnspan = 4)

#меню бар
menubar = Menu(root)
menubar.add_command(label="Задание",\
                    command = lambda: messagebox.showinfo("Задание",\
                                           "На плоскости дано множество точек.\nНайти такой треугольник с вершинами в этих точках,\nу которого разность максимального и минимального количества точек,\nпопавших в каждый из 6-ти треугольников,\nобразованных пересечением медиан, максимальна"))

label_coords = Label(text = '(-, -)')
label_coords.grid(row = 8, column = 1, columnspan = 9)
c.bind("<Motion>", lambda event, a = points.canvas_width, b = points.canvas_height: draw_coordinates(event, a, b))
c.bind("<Leave>", leave_canvas)

root.config(menu=menubar)
points.draw_coord()
root.mainloop();

