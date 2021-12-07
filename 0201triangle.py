# area of a triangle is A=1/2*base*height
'''
l1: Take the input of the height and base
l2: put them into the formula
l3: print the result
'''


def area(height, base):
    # b = base
    # h = height
    area = (1/2)*height*base
    return area


height = int(input("Enter the height of th triangle: "))
base = int(input("Enter the base of the triangle: "))
Area = area(height, base)
print(Area)
