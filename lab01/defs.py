def read_points(file_name):
    curr_x = 0; curr_y = 0;
    x= [];y=[];
    try:
        with open(file_name, 'r') as f:
            buff = f.readlines();
            for i in range(len(buff)):
                    try:
                        curr_x, curr_y = map(float, buff[i].split());
                        x.append(curr_x);
                        y.append(curr_y);
                    except ValueError:
                        print('Could not read all the given points');
    except:
        return [], []

    return x,y

def triangle_exists(x1, y1, x2, y2, x3, y3):
    if (y2 - y1)*(x3 - x1) != (y3 - y1)*(x2 - x1):
        return True
    else:
        return False

def find_centre_of_mediane_cross(x1_1, y1_1, x1_2, y1_2, x2_1, y2_1, x2_2, y2_2):
    #x1  точки первого отрезка, х2 - второго
    A1 = y1_1 - y1_2
    B1 = x1_2 - x1_1
    C1 = x1_1*y1_2 - x1_2*y1_1
    A2 = y2_1 - y2_2
    B2 = x2_2 - x2_1
    C2 = x2_1*y2_2 - x2_2*y2_1

    if B1*A2 - B2*A1 != 0:
        #Px, Py - точка пересечения
        try:
            Py = (C2*A1 - C1*A2) / (B1*A2 - B2*A1)
            Px = (-C1 - B1*Py) / A1
        except ZeroDivisionError:
            #print ("!");
            pass
    try:
        #plt.scatter(Px, Py, color = 'blue');
        return Px, Py
    except:
        #plt.scatter(x1_1, y1_1, color = 'red');
        #plt.scatter(x1_2, y1_2, color = 'red');
        return 1, 1
        

def is_in_triangle(x1, y1, x2, y2, x3, y3, x0, y0):
    k1 = (x1-x0)*(y2-y1)-(x2-x1)*(y1-y0)
    k2 = (x2-x0)*(y3-y2)-(x3-x2)*(y2-y0)
    k3 = (x3-x0)*(y1-y3)-(x1-x3)*(y3-y0)
    if (k1 > 0 and k2 > 0 and k3 > 0 ) \
       or (k1 < 0 and k2 < 0 and k3 < 0):
        return 1
    else:
        return 0
    
def prosses(x, y):
    max_diff = 0;
    max_point = 0;
    min_point = 0;
    points_in_triangle = [0]*6
    result_x = [0] * 3 #масс для вершин конечного треуг
    result_y = [0] * 3
    med_1 = [0]*2; med_2 = [0]*2; med_3 = [0]*2 #вершины для медиан [x1, y1]
    result = []
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            for k in range(j+1, len(x)):
                #перебор всех точек
                if triangle_exists(x[i], y[i], x[j], y[j], x[k], y[k]):
                    #если треугольник существует находим середины отрезков
#                   x_m_ij - координаты середины стороны соедин i и j вершины
                    x_m_ij = (x[i]+x[j]) / 2;
                    y_m_ij = (y[i]+y[j]) / 2;

                    x_m_ik = (x[i]+x[k]) / 2;
                    y_m_ik = (y[i]+y[k]) / 2;

                    x_m_jk = (x[j]+x[k]) / 2;
                    y_m_jk = (y[j]+y[k]) / 2;

                    #Px, Py - точка пересечения медиан
                    Px, Py = find_centre_of_mediane_cross(\
                        x_m_ij, y_m_ij, x[k], y[k], x_m_ik, y_m_ik, x[j], y[j]);


                    #перебор всех точек попадают ли они в каждый из 6-ти треугольников
                    for t in range(len(x)):
                        if is_in_triangle(x[i], y[i], Px, Py, x[j], y[j], x[t], y[t]):
                            points_in_triangle[0] += 1;

                        if is_in_triangle(x[i], y[i], Px, Py, x_m_ik, y_m_ik, x[t], y[t]):
                            points_in_triangle[1] += 1;

                        if is_in_triangle(x[k], y[k], Px, Py, x_m_ik, y_m_ik, x[t], y[t]):
                            points_in_triangle[2] += 1;

                        if is_in_triangle(x[k], y[k], Px, Py, x_m_jk, y_m_jk, x[t], y[t]):
                            points_in_triangle[3] += 1;

                        if is_in_triangle(x[j], y[j], Px, Py, x_m_jk, y_m_jk, x[t], y[t]):
                            points_in_triangle[4] += 1;

                        if is_in_triangle(x[j], y[j], Px, Py, x_m_ij, y_m_ij, x[t], y[t]):
                            points_in_triangle[5] += 1;

                    if (max(points_in_triangle) - min(points_in_triangle)) > max_diff:
                        max_diff = max(points_in_triangle) - min(points_in_triangle)
                        result_x[0], result_y[0] = x[i], y[i]
                        result_x[1], result_y[1] = x[j], y[j]
                        result_x[2], result_y[2] = x[k], y[k]

                        med_1[0], med_1[1] = x_m_jk, y_m_jk
                        med_2[0], med_2[1] = x_m_ik, y_m_ik
                        med_3[0], med_3[1] = x_m_ij, y_m_ij

                    #print(points_in_triangle)
                    
                    for r in range(len(points_in_triangle)):
                        points_in_triangle[r] = 0
                        
    result.append(result_x)
    result.append(result_y)
    result.append(med_1)
    result.append(med_2)
    result.append(med_3)
    
    return result

    
