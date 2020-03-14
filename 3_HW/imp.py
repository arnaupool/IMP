vertex_list = []
filename = None
down_tr =  0
total_tr = 0

def initialize():             #Figuring out z0
    global filename
    aux : float = 999999
    with open(filename, 'r') as f:
        for elem in f.readlines():
            elem = str(elem).strip().split(' ')
            if (str(elem[0]) == "vertex"):
                if (float(elem[3]) < float(aux)):
                    aux = elem[3]
    f.close()
    return aux

def create_output_file():     #Creating and populating output file
    global vertex_list
    f = open("out.stl", 'w')
    f.write("solid OpenSCAD_Model\n")
    for elem in vertex_list:
        f.write(str(elem[0]))
        f.write("\touter loop\n")
        for inv in elem[1]:
            f.write(inv)
        f.write("\tendloop\n")
        f.write("  endfacet\n")
    f.write("endsolid OpenSCAD_Model")
    f.close()
    pass

def overhang_calc(z0):        #Calculation of number of total triangles and number of triangles facing down without being from the base
    global filename
    global down_tr
    global vertex_list
    global total_tr
    with open(filename, 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            line = lines[i]
            elem = str(line).strip().split(' ')
            if (str(elem[0]) == "facet"):
                total_tr = total_tr + 1
                if (0 >= float(elem[4])):
                    list = lines[i+2:i+5]
                    if (base_triangles(z0, list)):
                        vertex_list.append([line, list])
                        down_tr = down_tr + 1
    f.close()

def base_triangles(z0, v_list):
    #v_list_split = str(v_list).strip().split(' ')
    for elem in v_list:
        elem = str(elem).replace('vertex', '').replace('\n', '').strip().split(' ')
        if (elem[2] == z0):
            return False
    return True

if __name__ == '__main__':
    filename = input("Enter the name of the file and its extension:\n")
    try:
        f = open(filename, 'r')
    except FileNotFoundError:
        print("Error 404 - File not found")
        quit() 
    f.close()
    try:
        overhang_calc(initialize())
        #bottom_face_vertex(initialize())
        create_output_file()
        print(down_tr)
        print(total_tr)
        print("Overhangs = " + str(format(float((down_tr/total_tr) * 100), '.2f')) + " %")
        #do everything
        pass
    except UnicodeDecodeError:
        print("File is not in ASCII format")
    f.close()
    quit()

"""
You have to write a program that:
    
    1. Will read an STL file (either from a file or from the standard filename) (you already did that in HW#1!)
    2. Calculate de total area (also done in HW#1)
    3. Calculate the area of the triangles that represent an overhang (those facing somehow down, excluding
    those of the base of the part)
    4. Print to the standard error the message "Overhangs=xx.xx %", where xx.xx represents the percentage of the
    overhang area with respect to the total area
    5. Print to the standard output the list of triangles representing the overhangs (using ASCII STL format for that)

Please note that we consider the base of the object is a horizontal plane (Z=z0) where z0 is lowest
values for the z coordinates of all the vertices.  A triangle belongs to the base if it has at less
one vertex on the base plane. The picture above shows how the spheres have some parts on its bottom
exclude from the overhang count as these triangles touch the base of the object. The gray zone represents
the overhang triangles of the spheres. (Spheres are seen somehow from the bottom).

If you are doing it right, you can do something like this:

    $ cat 3spheres.stl |java Ex3 >out.stl

and you should see:

    Overhangs=49,11 %

plus file out.stl should contain the triangles shown in gray in the picture above.
You can use Meshlab or Netfabb software to view these STL files.
(Please note out.stl file may be flagged as a defective STL file as it will contain holes in the mesh).

If you do the same with cube.stl  file:

$ cat cube.stl |java Ex3 >out.stl

the output should be 

Overhangs=0,00 %

And out.stl now should be empty (as the only triangles facing down are resting on the base and therefore do not
count as overhangs).
"""