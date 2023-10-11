from manim import *
from math import sin, cos


class VectorField2D(Scene):
    def construct(self):
        divergingField = ArrowVectorField(lambda pos: (pos - LEFT * 4), x_range=[-7, 0])
        convergingField = ArrowVectorField(
            lambda pos: -(pos - LEFT * 4), x_range=[-7, 0]
        )
        weirdField = ArrowVectorField(
            lambda pos: [cos(2 * pos[1]), sin(pos[0]), 0.0],
            x_range=[-7, 0, 0.25],
        )

        circleOnField = Circle(1, stroke_width=DEFAULT_STROKE_WIDTH / 2).shift(2 * LEFT)

        t = ValueTracker(PI / 2)

        xArrow = -2.0 + cos(t.get_value())
        yArrow = sin(t.get_value())

        arrowCircle = Arrow(
            start=np.array([xArrow, yArrow, 0.0]),
            end=np.array([xArrow, yArrow, 0.0])
            + np.array([cos(2 * yArrow), sin(xArrow), 0.0]) / 2.0,
            buff=0,
        )

        def arrowUpdater(x):
            xArrow = -2.0 + cos(t.get_value())
            yArrow = sin(t.get_value())

            arrowCircle_ = Arrow(
                start=np.array([xArrow, yArrow, 0.0]),
                end=np.array([xArrow, yArrow, 0.0])
                + np.array([cos(2 * yArrow), sin(xArrow), 0.0]) / 2.0,
                buff=0,
            )

            x.become(arrowCircle_)

        arrowCircle.add_updater(arrowUpdater)

        divergingText = MathTex("\\nabla\\cdot u > 0").shift(3 * RIGHT + 2 * UP)
        convergingText = MathTex("\\nabla\\cdot u < 0").shift(3 * RIGHT + 2 * UP)
        NavierStokes = MathTex("\\rho(\\nabla u)u - \\Delta u + \\nabla p = f").shift(
            3 * RIGHT + 2 * UP
        )
        incompressibleText = MathTex("\\nabla\\cdot u = 0").shift(3 * RIGHT + 1 * UP)

        self.play(FadeIn(divergingField))
        self.play(Write(divergingText))
        self.wait(2)

        self.play(Unwrite(divergingText))
        self.play(FadeOut(divergingField))
        self.play(FadeIn(convergingField))
        self.play(Write(convergingText))
        self.wait(2)

        self.play(Unwrite(convergingText))
        self.play(FadeOut(convergingField))
        self.play(FadeIn(weirdField))
        self.play(Write(incompressibleText))
        self.play(Create(circleOnField))
        self.play(Create(arrowCircle))

        self.play(
            t.animate.set_value(-3 * PI / 2),
            run_time=10,
            # rate_func=rate_functions.linear,
        )

        self.play(Write(NavierStokes))

        self.wait(2)
