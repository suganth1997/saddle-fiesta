from manim import *
from math import sin, cos


class VectorField2D(Scene):
    def construct(self):
        divergingField = ArrowVectorField(
            lambda pos: (pos - LEFT * 4),
            x_range=[-7, 0, 0.5],
            y_range=[-3, 3, 0.5],
        )
        convergingField = ArrowVectorField(
            lambda pos: -(pos - LEFT * 4),
            x_range=[-7, 0, 0.5],
            y_range=[-3, 3, 0.5],
        )
        weirdField = ArrowVectorField(
            lambda pos: [cos(2 * pos[1]), sin(pos[0]), 0.0],
            x_range=[-7, 0, 0.5],
            y_range=[-3, 3, 0.5],
        )

        r = 0.5

        cl = ValueTracker(2.0)
        cu = ValueTracker(0.0)

        ctr = cl.get_value() * LEFT + cu.get_value() * UP

        circleOnField = Circle(r, stroke_width=DEFAULT_STROKE_WIDTH / 2).move_to(ctr)

        t = ValueTracker(PI / 2)

        xArrow = -2.0 + r * cos(t.get_value())
        yArrow = r * sin(t.get_value())

        arrowCircle = Arrow(
            start=np.array([xArrow, yArrow, 0.0]),
            end=np.array([xArrow, yArrow, 0.0])
            + np.array([cos(2 * yArrow), sin(xArrow), 0.0]) / 4.0,
            buff=0,
        )

        def arrowUpdater(x):
            xArrow = -2.0 + r * cos(t.get_value())
            yArrow = r * sin(t.get_value())

            arrowCircle_ = Arrow(
                start=np.array([xArrow, yArrow, 0.0]),
                end=np.array([xArrow, yArrow, 0.0])
                + np.array([cos(2 * yArrow), sin(xArrow), 0.0]) / 4.0,
                buff=0,
            )

            x.become(arrowCircle_)

        arrows = VGroup(
            *[
                Arrow(
                    start=ctr + np.array([r * cos(th), r * sin(th), 0.0]),
                    end=ctr
                    + np.array([r * cos(th), r * sin(th), 0.0])
                    + np.array(
                        [
                            cos(2 * (ctr[1] + r * sin(th))),
                            sin(ctr[0] + r * cos(th)),
                            0.0,
                        ]
                    )
                    / 4.0,
                    buff=0,
                )
                for th in list(np.linspace(PI / 2, -PI / 2, 10))
                + list(np.linspace(-PI / 2, -3 * PI / 2, 10))
            ]
        )

        circleOnField.add_updater(
            lambda x: x.become(
                Circle(r, stroke_width=DEFAULT_STROKE_WIDTH / 2).move_to(
                    cl.get_value() * LEFT + cu.get_value() * UP
                )
            )
        )

        def arrowsUpdater(x):
            ctr = cl.get_value() * LEFT + cu.get_value() * UP

            arrows_ = [
                Arrow(
                    start=ctr + np.array([r * cos(th), r * sin(th), 0.0]),
                    end=ctr
                    + np.array([r * cos(th), r * sin(th), 0.0])
                    + np.array(
                        [
                            cos(2 * (ctr[1] + r * sin(th))),
                            sin(ctr[0] + r * cos(th)),
                            0.0,
                        ]
                    )
                    / 4.0,
                    buff=0,
                )
                for th in list(np.linspace(PI / 2, -PI / 2, 10))
                + list(np.linspace(-PI / 2, -3 * PI / 2, 10))
            ]

            x.become(VGroup(*arrows_))

        arrows.add_updater(arrowsUpdater)

        # circleArrows.add_updater(circleArrowsUpdater)

        # arrowsCreate = [Create(x) for x in arrows]

        arrowCircle.add_updater(arrowUpdater)

        divergingText = MathTex("\\nabla\\cdot u > 0").shift(3 * RIGHT + 2 * UP)
        convergingText = MathTex("\\nabla\\cdot u < 0").shift(3 * RIGHT + 2 * UP)
        NavierStokes = MathTex("\\rho(\\nabla u)u - \\Delta u + \\nabla p = f").shift(
            3 * RIGHT + 2 * UP
        )
        incompressibleText = MathTex("\\nabla\\cdot u = 0").shift(3 * RIGHT + 1 * UP)
        compressibleText = MathTex("\\nabla\\cdot \\rho u = 0").shift(3 * RIGHT)

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

        self.play(Create(arrows))

        self.play(Write(NavierStokes), FadeOut(arrowCircle))

        self.play(cl.animate.set_value(5.0), cu.animate.set_value(1.0), run_time=3)

        self.play(cl.animate.set_value(1.5), cu.animate.set_value(2.75), run_time=2)

        # self.play(cl.animate.set_value(3.0), cu.animate.set_value(0.0), run_time=5)

        self.play(cl.animate.set_value(1.5), cu.animate.set_value(-2.75), run_time=3)

        self.play(cl.animate.set_value(2.75), cu.animate.set_value(-2.75), run_time=2)

        self.play(cl.animate.set_value(2.75), cu.animate.set_value(2.75), run_time=3)

        self.play(Create(compressibleText))

        self.wait(2)
