#!/usr/bin/env python3

import argparse


class Painter():
    def __init__(self, figure, width, height):
        if figure == 'C':
            self.canvas_width = width
            self.canvas_height = height
            self.matrix = [[' ' for j in range(self.canvas_height)] for i in range(self.canvas_width)]
        else:
            raise TypeError("Necessary to create canvas first")
    
    def __call__(self, figure, *args):
        self.check_coordinates(*args)
        try:
            Painter.FIGURE_FUNC_DICT[figure](self, *args)
        except KeyError:
            raise KeyError('Not support "{}" figure or function'.format(figure))

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
            if isinstance(x,int) and x <= 0:
                raise IndexError("Coordinates must be more than 0")

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

    FIGURE_FUNC_DICT = {
            'L': draw_line, 
            'R': draw_rectangle, 
            'B': bucket_fill, 
            }


def draw(input_file=None, figure=None):
    if input_file and not figure:
        with open(input_file) as input:
            for line in input:
                fig, *args = line.split()
                args = args_to_int(*args)
                if fig == 'C':
                    output_figure = Painter(fig, *args)
                else:
                    try:
                        output_figure(fig, *args)            
                    except UnboundLocalError:
                        raise TypeError("Need to create convas first") 
            return output_figure
    elif input_file and figure:
        with open(input_file) as input:
            for line in input:
                fig, *args = line.split()
                args = args_to_int(*args)
                try:
                    figure(fig, *args)            
                except UnboundLocalError:
                    raise TypeError("Need to create convas first") 
            return figure
    else:
        raise AttributeError("No command for drawing. Try to add input file.")


def args_to_int(*args):
    arglist = []
    for x in args:
        if x.isdigit():
            arglist.append(int(x))
        else:
            arglist.append(x)
    return tuple(arglist)


def main(input_file, output_file):
    output_figure = draw(input_file = input_file)

    with open(output_file, 'w') as output:
        print(output_figure, file=output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-in', '--input', help="Input file from which painter\
            take the figures coordinates and colors.", default="input.txt")
    parser.add_argument('-out', '--output', help="To which file output figurel.",
            default="output.txt")
    args = parser.parse_args()

    if args.input[-3:] == '.in' and args.output == "output.txt":
        args.output = args.input.replace('.in', '.out') 
        args.output = args.output.replace('input_case', 'output_case') 

    main(input_file=args.input, output_file=args.output)

