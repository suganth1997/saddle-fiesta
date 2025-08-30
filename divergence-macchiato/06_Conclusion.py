from manim import *


class Conclusion(Scene):
    def construct(self):
        title = Tex("Conservation of Mass").to_corner(LEFT+UP)

        self.play(Create(title))

        rectangleShift = 3*LEFT + 0.125 * DOWN

        domain = Rectangle(width=2).shift(rectangleShift)

        self.play(Create(domain))

        enterArrows = [
            ArrowVectorField(
                lambda x: RIGHT / 2,
                x_range=[-3, -1.5, 0.5],
                y_range=[-0.75, 0.75, 0.5],
                length_func=lambda x: x,
            ).shift(rectangleShift),
            ArrowVectorField(
                lambda x: LEFT / 2,
                x_range=[1.5, 3, 0.5],
                y_range=[-0.75, 0.75, 0.5],
                length_func=lambda x: x,
            ).shift(rectangleShift),
            ArrowVectorField(
                lambda x: DOWN / 2,
                x_range=[-0.75, 0.75, 0.5],
                y_range=[1.5, 3, 0.5],
                length_func=lambda x: x,
            ).shift(rectangleShift),
            ArrowVectorField(
                lambda x: UP / 2,
                x_range=[-0.75, 0.75, 0.5],
                y_range=[-3, -1.5, 0.5],
                length_func=lambda x: x,
            ).shift(rectangleShift),
        ]

        self.play(*[Create(x) for x in enterArrows])

        m = MathTex("m").shift(4 * LEFT).shift(rectangleShift + 0.5 * RIGHT)
        V = MathTex("V").shift(rectangleShift)
        S = MathTex("S").shift(1.25 * (RIGHT + UP)).shift(rectangleShift)

        massSurf = MathTex("\int_{S}", "\dot{m}", "\ dS", " = 0").shift(
            3 * RIGHT + 1.75 * DOWN
        ).shift(rectangleShift)

        self.play(Create(m), Create(V), Create(S))
        self.wait(2)

        self.play(Create(massSurf[0:-1]))
        self.play(Create(massSurf[-1]))
        self.wait(2)
