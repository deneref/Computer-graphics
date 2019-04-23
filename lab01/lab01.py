from math import *
from defs import *
from tkinter import *
from tkinter import messagebox

canvas_width = 700
canvas_height = 700
real_width = 20 #10 единычных делений
real_height = 20 #по каждой оси

def print_points(x, y):
    n = 2
    global real_width; global real_height; global points_label_text
    global len_of_points_label
    points_label_text.set('')
    len_of_points_label = 0
    i = 0
    while i < len(x):
        k = canvas_width/real_width #на сколько надо сместиться на одно ед.деление
        #если выходим за пределы, то считаем новые пределы, все удаляем
        #и строим все точки по новой
        if abs(x[i]) >= real_width//2  + 1 or abs(y[i]) >= real_width//2 + 1:
            if abs(x[i]) >= real_width//2:
                real_width = 2*abs(x[i]) + abs(x[i])//10 
                real_height = 2*abs(x[i]) + abs(x[i])//10
                points_label_text.set('')
                len_of_points_label = 0
            elif abs(y[i]) > real_width//2:
                real_width = 2*abs(y[i]) + abs(y[i])//10
                real_height = 2*abs(y[i]) + abs(y[i])//10
                points_label_text.set('')
                len_of_points_label = 0
            c.delete('all')
            draw_coord()
            i = 0
        k = canvas_width/(real_width)
            
        #рисуем точки, n - что-то типо радиуса
        c.create_oval(k*x[i] + canvas_width//2 - n,\
                      k *(real_width/2 - y[i])+ n,\
                      k*(x[i])+ canvas_width//2 + n,\
                      k*(real_width/2 - y[i])- n,\
                      fill = 'green')
        
    #попытка печатать в лейбл
        if len_of_points_label < 21:
            s = points_label_text.get()
            s+=str(x[i])
            s+=' '
            s+=str(y[i])
            s+='\n'
            points_label_text.set(s)
            len_of_points_label += 1
            s = ''
        i+=1

def print_result_triangle(result):
##  в result
##  0 - иксы
##  1 - игрики
##  2 - медиана против первой вершины
##  3 - медиана против второй
##  4 - медиана против четвертой
    
    global real_width
    k = canvas_width//real_width
    #добавляем в конец первую точку чтобы треуг замкнулся
    result_x = result[0]
    result_y = result[1]
    result_x.append(result_x[0])
    result_y.append(result_y[0])
    #print('int canv\n',result)
    for i in range(len(result_x)-1):
        c.create_line((k*result_x[i] + canvas_width//2,\
                      k *(real_height - result_y[i]) - canvas_height//2,\
                      k*(result_x[i+1])+ canvas_width//2,\
                      k*(real_height - result_y[i+1])- canvas_height//2))
    #три медианы пунктиром
    for i in range(3):
        c.create_line((k*result_x[i] + canvas_width//2,\
                          k *(real_height - result_y[i]) - canvas_height//2,\
                          k*(result[i+2][0])+ canvas_width//2,\
                          k*(real_height - result[i+2][1])- canvas_height//2), dash = (4,2))
        
def input_from_file():
    global x; global y;
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
        x.append(x_new[j])
        y.append(y_new[j])
    #print(x, '\n', y)
    print_points(x,y)
    result = prosses(x, y)
    print_result_triangle(result)

def input_point():
    global x; global y
    global points_label_text
    result = []
    len_of_points_label = 0;
    try:
        x0 = int(x_entry.get())
        y0 = int(y_entry.get())
    except:
        messagebox.showerror("Ошибка ввода",\
                             "Точка должна иметь\nцелочисленные координаты")
    x.append(x0)
    y.append(y0)
    c.delete('all')
    draw_coord()
    print_points(x,y)
    
##    #попытка печатать в лейбл
##    if len_of_points_label < 15:
##        s = points_label_text.get()
##        s+=str(x0)
##        s+=' '
##        s+=str(y0)
##        s+='\n'
##        points_label_text.set(s)
    
    if len(x) >= 4:
        result = prosses(x, y)
        print_result_triangle(result)

    x_entry.delete(0, 'end')
    y_entry.delete(0, 'end')
    x_entry.focus()
    

def draw_coord():
    #рисуем координаты
    #можно подзапариться над делениями
    #они рисуются прямо перед мейнлупом
    c.create_line(0, canvas_height//2, canvas_width, canvas_height//2)
    c.create_line(canvas_width//2, 0, canvas_width//2, canvas_height)

def clear():
    global x; global y; global result;
    global len_of_points_label; 
##    чистим канвас
##    устанавливаем дефолтные настройки
    c.delete('all')
    draw_coord()
    x = [];
    y = [];
    result = [];
    real_width = 20;
    real_height = 20;
    len_of_points_label = 0
    points_label_text = ''

def enter_press(event):
    print(c.focus_get())
    if c.focus_get() == x_entry \
       or c.focus_get() == y_entry:
        input_point()
    elif c.focus_get() == file_entry:
        input_from_file()

        
x =[] 
y =[]
result = []    
root = Tk()
root.title('Компьютерная графика. Лабораторная работа №1')
c = Canvas(root,\
           width = canvas_width,\
           height = canvas_height,\
           bg = 'white')
c.grid(row = 0, column = 0, rowspan = 30)
#ввод из файла
Label(text = "Ввести точки из файла").grid(row = 2, column = 2, columnspan = 4)
file_entry = Entry(width = 20)
file_entry.grid(row = 3, column = 2, columnspan = 4)

file_insert = Button(text = "Enter", width = 10, height = 2,\
                     command = lambda : input_from_file())
file_insert.grid(row = 4, column = 2, columnspan = 4)

#ввод для отдельных точек
Label(text = "x: ").grid(row = 7, column = 2)
x_entry = Entry(width = 10)
x_entry.grid(row = 7, column = 3)

Label(text = "y: ").grid(row = 7, column = 4)
y_entry = Entry(width = 10)
y_entry.grid(row = 7, column = 5, columnspan = 1)

point_enter = Button(text = "Ввести точку", width = 10, height = 2,\
                     command = lambda : input_point())
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
                     command = lambda : clear())
clear_all.grid(row = 28, column = 2, columnspan = 4)

#bind на нажатие ентера
root.bind_class("Button","<Return>",enter_press)

#меню бар
menubar = Menu(root)
menubar.add_command(label="Задание",\
                    command = lambda: messagebox.showinfo("Задание",\
                                           "На плоскости дано множество точек.\nНайти такой треугольник с вершинами в этих точках,\nу которого разность максимального и минимального количества точек,\nпопавших в каждый из 6-ти треугольников,\nобразованных пересечением медиан, максимальна"))

root.config(menu=menubar)
draw_coord()
root.mainloop();

