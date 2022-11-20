class Circle:
    ''' Class Circle has the variables related to the circles'''
    inner = 1
    outer = 2
    offset : int = 3  # Set according to the orientation of the circle.

class Boton:
    '''This Class takes care of the botons'''
    pressed = False
    notPressed = True
    def __init__(self, circle: int, scale_degree : int, state : bool = True):
        self.circle = circle
        self.scale_degree = scale_degree
        self.state = state

outer_circle_list = []
outer_circle_list.append(Boton(Circle.inner, 0))
outer_circle_list.append(Boton(Circle.inner, 7))
outer_circle_list.append(Boton(Circle.inner, 2))
outer_circle_list.append(Boton(Circle.inner, 9))
outer_circle_list.append(Boton(Circle.inner, 4))
outer_circle_list.append(Boton(Circle.inner, 11))
outer_circle_list.append(Boton(Circle.inner, 6))
outer_circle_list.append(Boton(Circle.inner, 1))
outer_circle_list.append(Boton(Circle.inner, 8))
outer_circle_list.append(Boton(Circle.inner, 3))
outer_circle_list.append(Boton(Circle.inner, 10))
outer_circle_list.append(Boton(Circle.inner, 5))

print(outer_circle_list[3].scale_degree)
print(outer_circle_list[3].state)