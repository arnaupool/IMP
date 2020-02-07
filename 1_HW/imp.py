import math

def triangle_calculation(input):
    n_triangle = 0
    for elem in input.readlines():
        elem = str(elem).strip().split(' ')
        if elem[0] == str("outer"):
            n_triangle = n_triangle + 1
    
    print("The total number of triangles of the provided file is: " + str(n_triangle))

def cross(v1, v2):
    v1 = [float(i) for i in v1]
    v2 = [float(i) for i in v2] 
    s1 = v1[1] * v2[2] - v1[2] * v2[1]
    s2 = v1[2] * v2[0] - v1[0] * v2[2]
    s3 = v1[0] * v2[1] - v1[1] * v2[0]
    return math.sqrt(math.pow(s1,2) + math.pow(s2,2) + math.pow(s3,2))

def point2vector(p1, p2):
    p1 = [float(i) for i in p1]
    p2 = [float(i) for i in p2]
    return [p1[0] - p2[0], p1[1] - p2[1], p1[2] - p2[2]]

def surface_calculation(input):
    area = 0
    vertex_list = []
    for elem in input.readlines():
        elem = elem.split()
        if (elem[0] == str("vertex")):
            elem.remove(elem[0])
            vertex_list.append(elem)
    for pos in range(0, len(vertex_list), 3):
        triangle = vertex_list[pos:pos+3]
        v1 = point2vector(triangle[0], triangle[1])
        v2 = point2vector(triangle[0], triangle[2])
        area =+ area + cross(list(v1), list(v2))/2
    print("The total area of the surface of the provided file is: " + str(round(area, 2)))

def shell_calculation(input):
    """ n_shell = 0
    for elem in input.readlines():
        elem = elem.split(' ')

        if elem[0] == str("solid"):
            n_shell = n_shell + 1 """
    
    #print("The total number of shells of the provided file is: " + str(n_shell))
    print("This operation has not yet been implemented")


operations = {'1': triangle_calculation, '2': surface_calculation, '3': shell_calculation}

if __name__ == '__main__':
    filename = input("Enter the name of the file\n")
    try:
        userinput = open(filename, 'r')
    except FileNotFoundError:
        print("Error 404 - File not found")
        quit()

    print("What operation do you want to do?\n1. Number of triangles\n2. Total surface of the 3D object(s)\n3. Number of shells\n\n")
    option = input("Select a number to continue\n")
    #operations[option](userinput)
    try:
        operations[option](userinput)
    except UnicodeDecodeError:
        print("File is not in ASCII format")
    except KeyError:
        print("That value is not within the range")
    
    
""" You have to write some code for reading an STL file and printing out:

The total number of triangles it contains
The total surface of the 3D object(s)
Extra credit: The number of 3D shells within the STL file (for example if your STL file contains 3 non-intersecting spheres the answer here would be 3).

Your code will need to read ASCII STL files only and it cannot use any library to read the STL file. 

Submit your code to Dropbox folder (Espacio Compartido) in PoliformaT server before February 16th.  """


    

    