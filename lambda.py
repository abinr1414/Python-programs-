#area of traingle rectangle square
print("PROGRAM TO FIND THE AREA OF TRIANGLE RECTANGLE SQUARE")

square=lambda a:a*a
rectangle=lambda l,b:l*b
triangle=lambda h,b:(1/2)*b*h

#square

a=int(input("enter the side:"))
sqr_area=square(a)
print("the area of square",sqr_area)
#rectangle
a=int(input("enter the breadth:"))
b=int(input("enter the lenght:"))

area_rectangle=rectangle(a,b)
print("the area of rectangle",area_rectangle)
#triangle
b=int(input("enter the base:"))
h=int(input("enter the height:"))

area_triangle=triangle(h,b)
print("the area of triangle",area_triangle)