

class Canvas():
    def __init__(self):
        self.shapes = []

    def render(self):
        canvas = [['.' for x in range(10)] for y in range(10)]
        for rect in self.shapes:
            rect.render(canvas)
        
        for row in canvas:
            print(' '.join(row))

    def add_shape(self, rect):
        self.shapes.append(rect)

    def clear_all_shapes(self):
        for i in range(len(self.shapes)):
            for j in range(len(self.shapes[0])):
                self.shapes[i][j] = ' '
    
    
class Rectangle():

    @classmethod
    def is_valid(pos):
        if pos < 0 or pos > 9:
            return False
        return True


    def __init__(self, start_x, start_y, end_x, end_y, fill_char):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.fill_char = fill_char
    
    def change_fill_char(self,new_fill_char):
        self.fill_char = new_fill_char


    def translate(self, axis, num):
        if axis == 'x':
            self.start_x += num
            self.end_x  += num
        else:
            self.start_y += num
            self.end_y += num
    
    def render(self, canvas):
        for i in range(self.start_x, self.end_x+1):
            for j in range(self.start_y, self.end_y+1):
                canvas[i][j] = self.fill_char



a = Canvas()
rect1 = Rectangle(1,1,3,3,'X')
rect1.translate('y', 4)
a.add_shape(rect1)
rect2 = Rectangle(1,2,3,4,'O')
a.add_shape(rect2)
a.render()

