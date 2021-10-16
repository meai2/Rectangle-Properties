# lab3

def rectangle_point(l,w,x,y):
    """
    (float,float,float,float) -> [str, str]
    Input:  l, the x direction length of the rectangle, w, the y direction length of the rectangle, x, the x-coordinate of a point, and y, the y-coordinate of a point. 
    
    Output: A string representing the quadrant of the point as a Roman numeral between I and IV, and a string indicating if the point lies 'inside the rectangle' or 'outside the rectangle' of length l and width w centered at the origin.
    
    If the calculations determine that the length or width are less than or equal to zero, return 'invalid length' or 'invalid width' as the second string in the list.
    
    >>>rectangle_point (5,4,3,1)
    ['I', 'outside the rectangle']

    >>>rectangle_point (-5,4,3,1)
    ['I', 'invalid length']

    """
    #quadrant 1: ++
    if x > 0 and y > 0:
        quadrant = "I"
        #check dimensions
        if l < 0:
            error = "invalid length"
        elif w < 0:
            error = "invalid width"
        elif l <= 5 and w <= 5:
            error = "outside the rectangle"
        else:
            error = "inside the rectangle"   
            
    
    #quadrant 2: -+
    elif x < 0 and y > 0:
        quadrant = "II"
        #check dimensions
        if l < 0:
            error = "invalid length"
        elif w < 0:
            error = "invalid width"
        elif l <= 5 and w <= 5:
            error = "outside the rectangle"
        else:
            error = "inside the rectangle"
           
     
    #quadrant 3: - -
    elif x < 0 and y < 0:
        quadrant = "III"
        #check dimensions
        if l < 0:
            error = "invalid length"
        elif w < 0:
            error = "invalid width"
        elif l <= 5 and w <= 5:
            error = "outside the rectangle"
        else:
            error = "inside the rectangle"        
    
    #quadrant 4: +-
    elif x > 0 and y < 0:
        quadrant = "IV"
        #check dimensions
        if l < 0:
            error = "invalid length"
        elif w < 0:
            error = "invalid width"
        elif l <= 5 and w <= 5:
            error = "outside the rectangle"
        else:
            error = "inside the rectangle"        

    print("['"+quadrant+"', '"+error+"']")
    
l = int(input("length: "))
w = int(input("width: "))
x = int(input("x direction: "))
y = int(input("y direction: "))
rectangle_point(l,w,x,y)