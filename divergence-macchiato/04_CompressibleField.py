from manim import *
from math import sin, cos, exp
import sympy as sp
import numpy as np


class Compressible(Scene):
    def construct(self):
        vecScale = 1.0

        t = ValueTracker(0.0)

        rhoFunc = (
            lambda x: 1
            + 10 * exp(-25.0 * (x[0] + 1.75) ** 2)
            + 10 * exp(-25.0 * (x[0] + 4.75) ** 2)
            # sin((x[0] + 7) * PI / 7) ** 2
            # + 1.0  # cos((x[1] + 3) * PI / 6) ** 2
        )

        divFrFunc = (
            lambda x: (
                -10 * (-50 * x[0] - 250) * exp(-25 * (x[0] + 5) ** 2)
                - 10 * (-50 * x[0] - 100) * exp(-25 * (x[0] + 2) ** 2)
            )
            * cos(2 * x[1])
            / (1 + 10 * exp(-25 * (x[0] + 5) ** 2) + 10 * exp(-25 * (x[0] + 2) ** 2))
            ** 2
        )

        weirdField = ArrowVectorField(
            lambda pos: np.array([cos(2 * pos[1]), sin(2 * pos[0]), 0.0]) * vecScale,
            x_range=[-7, 0, 0.25],
            y_range=[-3, 3, 0.25],
        )

        def vecFieldFunc(pos):
            return (
                np.array([cos(2 * pos[1]), sin(2 * pos[0]), 0.0])
                # np.array([5.0, 0.0])
                * vecScale
                / (1.0 * (1 - t.get_value()) + t.get_value() * rhoFunc(pos))
            )

        dx = 0.25

        compressibleField = ArrowVectorField(
            vecFieldFunc, x_range=[-7, 0, dx], y_range=[-3, 3, dx]
        )

        compressibleField.add_updater(
            lambda x: x.become(
                ArrowVectorField(
                    vecFieldFunc,
                    x_range=[-7, 0, dx],
                    y_range=[-3, 3, dx],
                )
            )
        )

        X = np.linspace(0, PI, 100)
        Y = np.linspace(0, PI, 100)

        X, Y = np.meshgrid(X, Y)

        Xs = np.linspace(0.5, 7.5, 100)
        Ys = np.linspace(-3, 3, 100)

        ctr = 4 * RIGHT

        rho = np.uint(
            # ((np.sin(X) ** 2 + 0.0 * np.sin(Y) ** 2))
            (255 * np.exp(-25 * (X - (PI / 4.0)) ** 2))
            + (255 * np.exp(-25 * (X - (3 * PI / 4.0)) ** 2))
            # * np.exp(-0.5 * np.sqrt((Xs - ctr[0]) ** 2 + (Ys - ctr[1]) ** 2))
        )

        # xsp, ysp = sp.symbols("xsp ysp")

        # fSp = np.array([sp.cos(2 * ysp), sp.sin(2 * xsp)])
        # rhoSp = (
        #     1 + 10 * sp.exp(-25 * (xsp + 2) ** 2) + 10 * sp.exp(-25 * (xsp + 5) ** 2)
        # )

        # frSp = fSp / rhoSp

        # frDiv = sp.diff(frSp, xsp) + sp.diff(frSp, ysp)

        rhoImg = ImageMobject(rho).move_to(ctr)
        # rhoImg = ImageMobject(np.uint8([[0, 100, 30, 200], [255, 0, 5, 33]]))
        rhoImg.width = 7
        rhoImg.height = 6

        r = 0.25

        cl = ValueTracker(1.5)
        cu = ValueTracker(0.0)

        ctr = cl.get_value() * LEFT + cu.get_value() * UP

        circleOnField = Circle(r, stroke_width=DEFAULT_STROKE_WIDTH / 2).move_to(ctr)

        circleOnField.add_updater(
            lambda x: x.become(
                Circle(r, stroke_width=DEFAULT_STROKE_WIDTH / 2).move_to(
                    cl.get_value() * LEFT + cu.get_value() * UP
                )
            )
        )

        divText = MathTex(
            "\\nabla\\cdot u = {}".format(
                round(divFrFunc(cl.get_value() * LEFT + cu.get_value() * UP))
            )
            # "\\nabla\\cdot u = {}".format(round(rhoFunc(circleOnField.get_center())))
        )

        divText.add_updater(
            lambda x: x.become(
                MathTex(
                    "\\nabla\\cdot u = {}".format(
                        round(divFrFunc(circleOnField.get_center()))
                    )
                    # "\\nabla\\cdot u = {}".format(
                    #     round(rhoFunc(circleOnField.get_center()))
                    # )
                )
            )
        )

        self.play(FadeIn(compressibleField))
        self.wait(2)

        # config.disable_caching = True

        self.play(FadeIn(rhoImg))
        self.wait(2)

        self.play(t.animate.set_value(1.0), run_time=2)

        self.play(Create(circleOnField))

        self.play(Write(divText))

        # self.play(FadeOut(weirdField))
        # self.play(FadeIn(compressibleField))
        self.wait(2)

        self.play(cl.animate.set_value(7), run_time=15)
