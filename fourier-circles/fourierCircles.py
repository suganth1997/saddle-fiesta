from manim import *
import numpy as np


class FourierCircles(Scene):
    def construct(self):
        data = np.loadtxt("fourierCoefficients.txt")
        c = data[0, :] + 1j * data[1, :]

        scale = 0.75

        n = int((len(c) - 1) / 2)

        arrows = []

        idx = np.array(
            [
                -10,
                -9,
                -8,
                -7,
                -6,
                -5,
                -4,
                -3,
                -2,
                -1,
                0,
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
            ]
        )

        t = Variable(0.0, label="t")

        c = c * np.exp(idx * 2 * np.pi * t.tracker.get_value() * 1j)

        def linesUpdater(l):
            c = data[0, :] + 1j * data[1, :]
            c = c * np.exp(idx * 2 * np.pi * t.tracker.get_value() * 1j)

            lines = [Line(start=ORIGIN, end=[c[n].real * scale, c[n].imag * scale, 0])]

            c_now = c[n].copy()

            for i in range(1, n + 1):
                lines.append(
                    Line(
                        start=[c_now.real * scale, c_now.imag * scale, 0],
                        end=[
                            c_now.real * scale + c[n + i].real * scale,
                            c_now.imag * scale + c[n + i].imag * scale,
                            0,
                        ],
                    )
                )

                c_now += c[n + i]

                # print(c_now)

                lines.append(
                    Line(
                        start=[c_now.real * scale, c_now.imag * scale, 0],
                        end=[
                            c_now.real * scale + c[n - i].real * scale,
                            c_now.imag * scale + c[n - i].imag * scale,
                            0,
                        ],
                    )
                )

                c_now += c[n - i]

                l.become(VGroup(*lines))

                # print(c_now)

        lines = [Line(start=ORIGIN, end=[c[n].real * scale, c[n].imag * scale, 0])]

        # arrows.append(Create(lines[0]))

        c_now = c[n].copy()

        # self.play(arrows[-1])

        for i in range(1, n + 1):
            lines.append(
                Line(
                    start=[c_now.real * scale, c_now.imag * scale, 0],
                    end=[
                        c_now.real * scale + c[n + i].real * scale,
                        c_now.imag * scale + c[n + i].imag * scale,
                        0,
                    ],
                )
            )

            c_now += c[n + i]

            print(c_now)

            lines.append(
                Line(
                    start=[c_now.real * scale, c_now.imag * scale, 0],
                    end=[
                        c_now.real * scale + c[n - i].real * scale,
                        c_now.imag * scale + c[n - i].imag * scale,
                        0,
                    ],
                )
            )

            c_now += c[n - i]

            print(c_now)

            # self.play(arrows[-2])
            # self.play(arrows[-1])

        linesGroup = VGroup(*lines)

        linesGroup.add_updater(linesUpdater)

        # lines_create = [Create(l) for l in lines]

        self.play(Create(linesGroup))

        self.play(t.tracker.animate.set_value(1.0), run_time=10)

        self.wait(2)
