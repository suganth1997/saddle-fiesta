from manim import *
from math import sin, cos, exp, sqrt


class RhoField(ThreeDScene):
    def construct(self):
        resolution_fa = 48
        plane_range = 3.5
        self.set_camera_orientation(phi=0.0 * DEGREES, theta=0.0 * DEGREES)

        surfaceFn = lambda x: np.exp(-(np.linalg.norm(x) ** 2))
        surfaceGrad = lambda x: np.exp(-(np.linalg.norm(x) ** 2)) * 2 * x

        def param_gauss(u, v):
            x = u
            y = v
            sigma, mu = 1.0 / sqrt(2), [0.0, 0.0]
            d = np.linalg.norm(np.array([x - mu[0], y - mu[1]]))
            z = np.exp(-(d**2 / (2.0 * sigma**2)))
            return np.array([x, y, z])

        planeOp = ValueTracker(1.0)
        gauss_plane = Surface(
            param_gauss,
            resolution=(resolution_fa, resolution_fa),
            v_range=[-plane_range, +plane_range],
            u_range=[-plane_range, +plane_range],
            fill_opacity=planeOp.get_value(),
            stroke_width=0.0,
        )

        axes = ThreeDAxes()

        gauss_plane.set_fill_by_value(
            axes=axes, colorscale=[(BLACK, 0), (WHITE, 1.0)], axis=2
        )

        def gauss_plane_updater(x):
            gplanes = Surface(
                param_gauss,
                resolution=(resolution_fa, resolution_fa),
                v_range=[-plane_range, +plane_range],
                u_range=[-plane_range, +plane_range],
                fill_opacity=planeOp.get_value(),
                stroke_width=0.0,
            )

            axes = ThreeDAxes()

            gplanes.set_fill_by_value(
                axes=axes, colorscale=[(BLACK, 0), (WHITE, 1.0)], axis=2
            )

            x.become(gplanes)

        gauss_plane.add_updater(gauss_plane_updater)

        # gauss_plane.scale(1, about_point=ORIGIN)
        # gauss_plane.set_style(fill_opacity=1, stroke_color=GREEN)
        # gauss_plane.set_fill_by_checkerboard(ORANGE, BLUE, opacity=0.5)

        vecScale = 1.0

        t = ValueTracker(0.0)

        rhoFunc = (
            lambda x: 1
            + 10 * exp(-1.0 * (x[0] ** 2 + x[1] ** 2))
            # sin((x[0] + 7) * PI / 7) ** 2
            # + 1.0  # cos((x[1] + 3) * PI / 6) ** 2
        )

        def vecFieldFunc(pos):
            return (
                np.array([cos(2 * pos[1]), sin(2 * pos[0]), 0.0])
                # np.array([5.0, 0.0])
                * vecScale
                / (1.0 * (1 - t.get_value()) + t.get_value() * rhoFunc(pos))
            )

        dx = 0.25

        fieldOpacity = ValueTracker(1.0)

        compressibleField = ArrowVectorField(
            vecFieldFunc,
            x_range=[-3, 3, dx],
            y_range=[-3, 3, dx],
            opacity=fieldOpacity.get_value(),
        )

        compressibleField.add_updater(
            lambda x: x.become(
                ArrowVectorField(
                    vecFieldFunc,
                    x_range=[-3, 3, dx],
                    y_range=[-3, 3, dx],
                    opacity=fieldOpacity.get_value(),
                )
            )
        )

        divuText = MathTex("\\nabla\\cdot\\rho u = 0").to_corner(UR)

        divuChain = (
            MathTex("\\rho\\nabla\\cdot u + \\nabla\\rho\\cdot u = 0")
            .next_to(divuText, DOWN)
            .shift(0.5 * LEFT)
        )

        divuChainRes = MathTex(
            "\\nabla\\cdot u = -\\frac{\\nabla\\rho}{\\rho}\\cdot u"
        ).next_to(divuChain, DOWN)

        dxArrow = ValueTracker(0.0)
        dyArrow = ValueTracker(0.0)

        xArrow = 0.0 + dxArrow.get_value()
        yArrow = -0.5 + dyArrow.get_value()
        gradArrow = Arrow3D(
            start=[xArrow, yArrow, surfaceFn(np.array([xArrow, yArrow]))],
            end=list(
                np.array([xArrow, yArrow]) + surfaceGrad(np.array([xArrow, yArrow]))
            )
            + [surfaceFn(np.array([xArrow, yArrow]))],
            color=BLUE,
        )

        def gradArrowUpdater(x):
            xArrow = 0.0 + dxArrow.get_value()
            yArrow = -0.5 + dyArrow.get_value()
            gradArrow = Arrow3D(
                start=[xArrow, yArrow, surfaceFn(np.array([xArrow, yArrow]))],
                end=list(
                    np.array([xArrow, yArrow]) + surfaceGrad(np.array([xArrow, yArrow]))
                )
                + [surfaceFn(np.array([xArrow, yArrow]))],
                color=BLUE,
            )

            x.become(gradArrow)

        gradArrow.add_updater(gradArrowUpdater)

        theta = ValueTracker(0.0)

        centerDot = Dot([5, 0, 0], radius=DEFAULT_DOT_RADIUS * 1.5)
        gradRhoArrow = Arrow(start=[5, 0, 0], end=[4, -1, 0], buff=0)
        uArrow = Arrow(
            start=[5, 0, 0],
            end=np.array([5, 0, 0])
            + sqrt(2) * np.array([cos(theta.get_value()), sin(theta.get_value()), 0]),
            buff=0,
        )

        uArrow.add_updater(
            lambda x: x.become(
                Arrow(
                    start=[5, 0, 0],
                    end=np.array([5, 0, 0])
                    + sqrt(2)
                    * np.array([cos(theta.get_value()), sin(theta.get_value()), 0]),
                    buff=0,
                )
            )
        )

        gradRhodotu = MathTex(
            "\\frac{\\nabla\\cdot\\rho}{\\rho}\\cdot u = ",
            "{:.2f}".format(
                np.dot(
                    np.array([-1, -1]) / sqrt(2),
                    np.array([cos(theta.get_value()), sin(theta.get_value())]),
                )
            ),
        ).next_to(gradRhoArrow, RIGHT + 2 * DOWN)

        gradRhodotu.add_updater(
            lambda x: x.become(
                MathTex(
                    "\\frac{\\nabla\\cdot\\rho}{\\rho}\\cdot u = ",
                    "{:.2f}".format(
                        np.dot(
                            np.array([-1, -1]) / sqrt(2),
                            np.array([cos(theta.get_value()), sin(theta.get_value())]),
                        )
                    ),
                ).next_to(gradRhoArrow, RIGHT + 2 * DOWN)
            )
        )

        # self.set_camera_orientation(
        #     75 * DEGREES, -30 * DEGREES, frame_center=[1.0, 0.0, 0.0]
        # )
        # self.add(axes, gauss_plane)
        # self.add(gradArrow)

        # self.add_fixed_in_frame_mobjects(gradRhoArrow, uArrow, centerDot)

        # return

        self.add(axes, gauss_plane)
        self.add(axes, compressibleField)

        # self.add(divuText)

        # self.begin_3dillusion_camera_rotation(rate=2)

        self.wait(PI / 2)

        self.play(t.animate.set_value(1.0), run_time=PI / 2)

        self.wait(PI / 2)

        self.play(planeOp.animate.set_value(1.0), run_time=PI / 2)

        self.wait(PI / 2)

        self.move_camera(75 * DEGREES, -30 * DEGREES, frame_center=[1.0, 0.0, 0.0])

        self.wait(PI / 2)

        self.add_fixed_in_frame_mobjects(divuText)
        self.play(Write(divuText))

        self.add_fixed_in_frame_mobjects(divuChain)
        self.play(Write(divuChain))

        # self.play(FadeOut(compressibleField))
        self.play(fieldOpacity.animate.set_value(0.0), run_time=2)

        self.play(Create(gradArrow))

        self.wait(PI / 2)

        self.play(dxArrow.animate.set_value(0.5), run_time=2)
        self.play(dyArrow.animate.set_value(0.5), run_time=2)

        self.add_fixed_in_frame_mobjects(gradRhoArrow, uArrow, centerDot)
        self.play(Create(gradRhoArrow), Create(uArrow), Create(centerDot))

        self.add_fixed_in_frame_mobjects(gradRhodotu)
        self.play(Create(gradRhodotu))

        self.wait(PI / 2)

        self.play(theta.animate.set_value(PI), run_time=2.0)
        self.play(theta.animate.set_value(2 * PI), run_time=2.0)

        # self.add_fixed_in_frame_mobjects(divuChainRes)
        # self.play(ReplacementTransform(divuChain, divuChainRes))

        # self.stop_3dillusion_camera_rotation()
