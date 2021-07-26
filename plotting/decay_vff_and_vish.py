from collections import defaultdict
from manim import *


class DecayVFF(Scene):
    def construct(self):
        self.camera.background_color = "#ffffff"
        _range = range(-2, 4)
        for l, i in enumerate(_range):
            # horizonal
            line = Line(ORIGIN + i * UP + 3 * LEFT, ORIGIN + i * UP + (max(_range) + 1) * RIGHT).set_color(BLACK).set_opacity(.1)
            label = MathTex(f"j = {l}").next_to(line, direction=LEFT).set_color(BLACK)
            self.add(line, label)
        for l, i in enumerate(_range):
            line = Line(ORIGIN + 3 * DOWN + i * RIGHT, ORIGIN + (max(_range) + 1) * UP + i * RIGHT).set_color(BLACK).set_opacity(.1)
            label = MathTex(f"i = {l}").next_to(line, direction=DOWN).set_color(BLACK).rotate(45)
            self.add(line, label)
        for l1, i in enumerate(_range):
            for l2, j in enumerate(_range):
                square = Square(.7 * .8 ** l1 * .8 ** l2).set_color(ORANGE).set_opacity(.3).move_to(ORIGIN + i * RIGHT + j * UP)
                self.add(square)
        
        s = Square(side_length=4).set_fill(opacity=0).set_color(BLUE).shift(DOWN * .6 + LEFT * .6)
        self.add(s)


class DecayVISH(Scene):
    def construct(self):
        self.camera.background_color = "#ffffff"
        _range = range(-3, 3)
        for l, i in enumerate(_range):
            # horizonal
            line = Line(ORIGIN + i * DOWN + (l+1) * LEFT, ORIGIN + i * DOWN + (l + 1) * RIGHT).set_color(BLACK).set_opacity(.1).shift(RIGHT)
            label = MathTex(f"n = {l}").next_to(line, direction=LEFT).set_color(BLACK)
            self.add(line, label)
        # for l, i in enumerate(_range):
        #     line = Line(ORIGIN + 3 * DOWN + i * RIGHT, ORIGIN + (max(_range) + 1) * UP + i * RIGHT).set_color(BLACK).set_opacity(.1)
        #     label = MathTex(f"i = {l}").next_to(line, direction=DOWN).set_color(BLACK).rotate(45)
        #     self.add(line, label)

        squares = defaultdict(list)
        for nn, n in enumerate(_range):
            for jj, j in enumerate(range(2 * nn + 1)):
                square = Square(.7 * .75 ** nn).set_color(ORANGE).set_opacity(.3).move_to(ORIGIN + n * DOWN + jj * RIGHT - nn * RIGHT).shift(RIGHT)
                squares[nn].append(square)
                self.add(square)
            
        dot1 = Dot(ORIGIN + 3.8 * UP).shift(2 * RIGHT)
        dot3 = Dot(ORIGIN - 1.3 * UP + 5 * RIGHT).shift(2 * RIGHT)

        m = (dot1.get_center()[1] - dot3.get_center()[1]) / (dot1.get_center()[0] - dot3.get_center()[0])
        b = dot1.get_center()[1] - m * dot1.get_center()[0]

        for i in range(len(squares[5])):
            def calc_intersection(X, Y):
                return (
                    (X + m * Y - m*b) / (1+m**2),
                    (m * X + m**2 * Y + b) / (1+m**2),
                )

            s = squares[5][i].get_center() + .6 * LEFT + .6 * DOWN
            ex, ey = calc_intersection(s[0], s[1])
            line = Line(
                start=s,
                end=np.array([ex, ey, 0])
            ).set_color(BLACK).set_opacity(.1)
            label = MathTex(f"j = {i}").next_to(line, direction=LEFT + DOWN).set_color(BLACK).rotate(45).shift(.5 * RIGHT)
            self.add(line, label)
        
        dot1 = Dot(ORIGIN + 3.8 * UP).shift(RIGHT)
        dot2 = Dot(ORIGIN - 1.3 * UP + 5 * LEFT).shift(RIGHT)
        dot3 = Dot(ORIGIN - 1.3 * UP + 5 * RIGHT).shift(RIGHT)
        line1 = Line(dot1.get_center(), dot2.get_center()).set_color(BLUE)
        line2 = Line(dot2.get_center(), dot3.get_center()).set_color(BLUE)
        line3 = Line(dot1.get_center(), dot3.get_center()).set_color(BLUE)



        self.add(line1, line2, line3)

        # tr = RegularPolygon()
        # self.add(tr)
            # self.add(line.copy().shift(RIGHT))
        # s = Square(side_length=4).set_fill(opacity=0).set_color(BLUE).shift(DOWN * .6 + LEFT * .6)
        # self.add(s)