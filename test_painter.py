import unittest
import os


from painter import draw


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(BASE_DIR, 'input_case')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output_case')
IN_EXTENSION = '.in'
OUT_EXTENSION = '.out'


def get_input_path(filename):
    filename += IN_EXTENSION
    return os.path.join(INPUT_DIR, filename)


def get_output_path(filename):
    filename += OUT_EXTENSION
    return os.path.join(OUTPUT_DIR, filename)


def get_figure_from_output(filename):
    figure = ''
    with open(get_output_path(filename)) as output:
        for line in output: figure+= line
    figure = figure[:-1]  
    return figure


class TestPainter(unittest.TestCase):
    @staticmethod
    def create_default_canvas():
        filename = "create_canvas_square_10"
        canvas = draw(input_file=get_input_path(filename))
        return canvas

    def in_equal_out(self, filename):
        work_figure = draw(input_file=get_input_path(filename))
        self.assertEqual(work_figure.__str__(), get_figure_from_output(filename))

    def test_create_canvas_10x15(self):
        filename = "create_canvas_10x15" # так и не нашел как получить имя текущей фукции, чтобы брать имя файла из нее
        self.in_equal_out(filename)

    def test_create_canvas_20x10(self):
        filename = "create_canvas_20x10"
        self.in_equal_out(filename)

    def test_create_canvas_square_10(self):
        filename = "create_canvas_square_10"
        self.in_equal_out(filename)

    def test_miss_canvas(self):
        filename = "miss_canvas"
        with self.assertRaises(TypeError):
            work_figure = draw(input_file=get_input_path(filename))

    def test_draw_line_out_canvas_left_border(self):
        filename = "draw_line_out_canvas_left_border" 
        work_figure = self.create_default_canvas()
        with self.assertRaises(IndexError): 
            draw(input_file=get_input_path(filename), figure=work_figure)

    def test_draw_line_out_canvas_right_border(self):
        filename = "draw_line_out_canvas_right_border" 
        work_figure = self.create_default_canvas()
        with self.assertRaises(IndexError): 
            draw(input_file=get_input_path(filename), figure=work_figure)

    def test_create_line_1_v(self):
        filename = "create_line_1_v"
        self.in_equal_out(filename)

    def test_create_line_3_v(self):
        filename = "create_line_3_v"
        self.in_equal_out(filename)

    def test_create_line_10_v(self):
        filename = "create_line_10_v"
        self.in_equal_out(filename)

    def test_create_line_1_h(self):
        filename = "create_line_1_h"
        self.in_equal_out(filename)

    def test_create_line_3_h(self):
        filename = "create_line_3_h"
        self.in_equal_out(filename)

    def test_create_line_10_h(self):
        filename = "create_line_10_h"
        self.in_equal_out(filename)

    def test_create_lattice_15x10(self):
        filename = "create_lattice_15x10"
        self.in_equal_out(filename)

    def test_create_rectangle(self):
        filename = "create_rectangle"
        self.in_equal_out(filename)

    def test_create_3_rectangles(self):
        filename = "create_3_rectangles"
        self.in_equal_out(filename)

    def test_bucket_fill_1_cell(self):
        filename = "bucket_fill_1_cell"
        self.in_equal_out(filename)

    def test_bucket_fill_2_cell(self):
        filename = "bucket_fill_2_cell"
        self.in_equal_out(filename)

    def test_bucket_fill_3_cell(self):
        filename = "bucket_fill_3_cell"
        self.in_equal_out(filename)

    def test_bucket_fill_4_cell(self):
        filename = "bucket_fill_4_cell"
        self.in_equal_out(filename)

    def test_bucket_fill_5_cell(self):
        filename = "bucket_fill_5_cell"
        self.in_equal_out(filename)

    def test_bucket_fill_6_cell(self):
        filename = "bucket_fill_6_cell"
        self.in_equal_out(filename)

    def test_bucket_fill_7_cell(self):
        filename = "bucket_fill_7_cell"
        self.in_equal_out(filename)

    def test_bucket_fill_8_cell(self):
        filename = "bucket_fill_8_cell"
        self.in_equal_out(filename)

    def test_bucket_fill_9_cell(self):
        filename = "bucket_fill_9_cell"
        self.in_equal_out(filename)

    def test_bucket_fill_10_cell(self):
        filename = "bucket_fill_10_cell"
        self.in_equal_out(filename)

    def test_bucket_fill_leaked(self):
        filename = "bucket_fill_leaked" 
        self.in_equal_out(filename)


if __name__ == "__main__":
    unittest.main()

