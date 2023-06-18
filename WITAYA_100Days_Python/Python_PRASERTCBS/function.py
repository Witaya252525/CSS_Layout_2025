
def rectangle(w,h):
    area = (w*h)
    return area

def triangle(w,h):
    area = 0.5*w*h
    return area

w = int(input("Please Enter Width = "))
h = int(input("Please Enter height = "))
print(rectangle(w, h))
print(triangle(w, h))




