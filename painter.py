import sys


class Painter():
    def __init__(self, figure, width, height):
        if figure == 'C':
            self.canvas_width = width
            self.canvas_height = height
            self.matrix = []
            for i in range(self.canvas_width):
                self.matrix.append([])
                for j in range(self.canvas_height):
                    self.matrix[i].append(' ')
        else:
            raise TypeError("Necessary to create canvas first")


    def __call__(self, figure, *args):
        self.check_coordinates(*args)
        if figure == 'L': 
            self.draw_line(*args)
        elif figure == 'R':
            self.draw_rectangle(*args)
        elif figure == 'B':
            self.bucket_fill(*args)
        else:
            raise TypeError('Not support "{}" figure or function'.format(figure))


    def __str__(self):
        self._result = '-' * self.canvas_width + '--\n'
        for j in range(self.canvas_height):
            self._result += '|'
            for i in range(self.canvas_width):
                self._result += self.matrix[i][j]
            self._result += '|\n'
        self._result += '-' * self.canvas_width + '--\n'
        return self._result


    @staticmethod
    def check_coordinates(*args):
        for x in args:
            if x is int:
                if x <= 0:
                    raise AttributeError("Coordinates must be more than 0")

    @staticmethod
    def normalize_coordinates(*args): 
        return tuple(x-1 for x in args)


    def draw_line(self, x1, y1, x2, y2, fill='X'):
        x1, y1, x2, y2 = self.normalize_coordinates(x1, y1, x2, y2)
        if x1 == x2:
            for i in range(y1, y2+1):
                self.matrix[x1][i] = fill
        elif y1 == y2:
            for i in range(x1, x2+1):
                self.matrix[i][y1] = fill


    def draw_rectangle(self, x1, y1, x2, y2, fill='X'):
        x1, y1, x2, y2 = self.normalize_coordinates(x1, y1, x2, y2)
        for i in range(x1, x2+1):
            self.matrix[i][y1] = fill
            self.matrix[i][y2] = fill
        for j in range(y1, y2+1):
            self.matrix[x1][j] = fill
            self.matrix[x2][j] = fill


    def bucket_fill(self, x, y, color):
        x, y = self.normalize_coordinates(x, y)
        curr_color = self.matrix[x][y]
        def fill_around(self, x, y):
            self.matrix[x][y] = color
            for i in range(3):
                for j in range(3):
                    next_x = x - 1 + i
                    next_y = y - 1 + j
                    if next_x == -1 or next_y == -1:
                        continue
                    try:
                        point = self.matrix[next_x][next_y]
                    except IndexError:
                        continue
                    if point == curr_color:
                        self.matrix[next_x][next_y] = color
                        fill_around(self, x=next_x, y=next_y)
        fill_around(self, x, y)


def main(input_file, output_file):
    with open(input_file) as input:
        for line in input:
            fig, *args = line.split()
            arglist = []
            for x in args:
                if x.isdigit():
                    arglist.append(int(x))
                else:
                    arglist.append(x)
            args = tuple(arglist)
            if fig == 'C':
                output_figure = Painter(fig, *args)
            else:
                output_figure(fig, *arglist)            
    with open(output_file, 'w') as output:
        print(output_figure, file=output)


if __name__ == "__main__":
    args = sys.argv[1:]
    if '-in' in args:
        pos = args.index('-in')
        input_file = args[pos+1]
    elif '--input' in args:
        pos = args.index('--input')
        input_file = args[pos+1]
    else:
        raise AttributeError('No input params. Use "painter.py -in input.txt" or "painter.py --input input.txt"')

    if '-out' in args:
        pos = args.index('-out')
        output_file = args[pos+1]
    elif '--output' in args:
        pos = args.index('--output')
        output_file = args[pos+1]
    else:
        output_file = 'painter_output'

    main(input_file=input_file, output_file=output_file)
