import math 

def classify_triangle(a,b,c):
    arr = list()
    arr.extend((a,b,c))
    arr.sort() 
    a = arr[0]
    b = arr[1]
    c = arr[2]
    #For equalateral
    if (a == b) and (b == c):
        return ("It is an equilateral triangle")
    #Isoceles
    if (b == c) and (b != a):
        return ("It is an isoceles triangle")
    elif (a == b) and (c != b):
        return ("It is an isoceles triangle")

    #Right
    temp = math.sqrt(a*a+b*b)
    if ( c == temp):
        if (a == b):
            return ("It is a isoceles right triangle")
        else:
            return ("It is a scalene right triangle")
    #Scalene
    if (a != b) and (b != c):
        return ("It is a scalene triangle")



    

print (classify_triangle(3,4,5))