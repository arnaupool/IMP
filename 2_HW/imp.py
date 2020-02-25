def func(tr, h_z0):
    n_vertex = 0
    vertex = []
    for v in tr.v:
        if (v[2] == h_z0):
            n_vertex = n_vertex + 1
            vertex.append(v)
    operations[str(n_vertex)](tr, vertex, h_z0)

def no_int_or_seg(tr, vertex, h_z0):
    s_1 = point2vector(tr.v[0], tr.v[1])
    s_2 = point2vector(tr.v[1], tr.v[2])
    s_3 = point2vector(tr.v[2], tr.v[0])
    print("no intersection")

def point_f(triangle, vertex, h_z0):
    print("one point intersection: " + str(vertex))
    pass

def segment_f(triangle, vertex, h_z0):
    print("segment intersection: " + str(point2vector(vertex[0], vertex[1])))
    pass

def plane_f(triangle, vertex, h_z0):
    print("triangle intersection: " + str(vertex))
    pass

def point2vector(p1, p2):
    p1 = [float(i) for i in p1]
    p2 = [float(i) for i in p2]
    return [p1[0] - p2[0], p1[1] - p2[1], p1[2] - p2[2]]

def parse(v):
    v = str(v).split()
    return v

operations = {
    '0': no_int_or_seg, '1': point_f, '2': segment_f, '3': plane_f
    }

class trigon:
    def __init__(self, f, s, t, h):
        self.v = [f, s, t]
        self.h_z0 = h

if __name__ == '__main__':

    f_v = parse(input("Enter the data\n"))
    s_v = parse(input(""))
    t_v = parse(input(""))
    h_z0 = input("")

    func(trigon(f_v, s_v, t_v, h_z0), h_z0)

    #print(str(f_v) + " // " + str(s_v) + " // " + str(t_v) + " // " + h_z0)

    quit()

""" This second homework, due to Feb 29th, requires you to write a piece of code that takes as input the
    3D coordinates of the vertices of a triangle, as three lines of text, containing each one three decimal
    numbers (x,y,z) separated by a tab or blank space. 

    The fourth input line contains another decimal number indicating the height (z0) of the cutting plane (Z=z0).

    Your program will calculate and print out the intersection of the given triangle with the horizontal plane,
    four cases are possible:

        1. null intersection  (output)--> "no intersection"

        2. one point intersection --> coordinates of the point

        3. intersection is a segment --> coordinates of the segment

        4. intersection is a triangle --> coordinates of the three vertices of the triangle 

    Sample input:

    -2.57295 6.23664 2
    0.959991 5.78899 2
    0.954239 6.4008 2
    3.2

    Output:

    no intersection """