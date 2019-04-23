from math import *
from defs import *
from tkinter import *

file_name = 'test_1.txt';
x =[]; 
y =[];
result_x = []
result_y = []
global canvas_width; canvas_width = 700
global canvas_height; canvas_height = 500

def print_points(x, y):
    n = 2
    for i in range(len(x)):
        c.create_oval(x[i]-n, canvas_width - y[i] - n, \
                      x[i] + n, canvas_width - y[i] + n,\
                      fill = 'green')

def enter_from_file():
    file_name = file_entry.get()
    x, y = read_points(file_name)
    print_points(x,y)
    result_x, result_y = prosses(x, y)
'''
def draw_coord():
    c.create_line(25, 25, 25, canvas_height)
    c.create_line(25, canvas_height, canvas_width, canvas_height)
    #стрелочки
    c.create_line(25, 25, 15, 40)
    c.create_line(25, 25, 35, 40)

    c.create_line(canvas_width, canvas_height,\
                  canvas_width - 15, canvas_height - 10)
    c.create_line(canvas_width, canvas_height,\
                  canvas_width - 15, canvas_height + 10)

    for i in range(0, 14):
        shift = 50
        c.create_line(25 + (shift*i), canvas_height - 5,\
                      25 + (shift*i), canvas_height + 5)
        c.create_text(25+(shift*i), canvas_height + 15,\
                      text = shift*i)

    for i in range(0, 10):
        shift = 50
        c.create_line(25 - 5, canvas_height - (shift*i),\
                      25 + 5, canvas_height - (shift*i))
        c.create_text(10, canvas_height - (shift*i),\
                      text = shift*i)

'''        
root = Tk()
root.title('Компьютерная графика. Лабораторная работа №1')
c = Canvas(root,width = canvas_width + 30,height = canvas_height + 20,\
           bg = 'white')
c.grid(row = 0, column = 0, rowspan = 30)
#ввод из файла
Label(text = "Ввести точки из файла").grid(row = 2, column = 2, columnspan = 4)
file_entry = Entry(width = 20)
file_entry.grid(row = 3, column = 2, columnspan = 4)

file_insert = Button(text = "Enter", width = 10, height = 2,\
                     command = lambda : enter_from_file())
file_insert.grid(row = 4, column = 2, columnspan = 4)

#ввод для отдельных точек
Label(text = "x: ").grid(row = 7, column = 2)
x_entry = Entry(width = 10)
x_entry.grid(row = 7, column = 3)

Label(text = "y: ").grid(row = 7, column = 4)
y_entry = Entry(width = 10)
y_entry.grid(row = 7, column = 5, columnspan = 1)

point_enter = Button(text = "Ввести точку", width = 10, height = 2)
point_enter.grid(row = 9, column = 2, columnspan = 4)

Label(text = "Введеные точки:").grid(row = 10, column = 2, columnspan = 4)
entered_points = Label(text = "")
entered_points.grid(row = 11, column = 2, columnspan = 4)

draw_coord()
root.mainloop();

