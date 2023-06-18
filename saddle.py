from manim import *


class ThreeDSurfacePlot(ThreeDScene):
    def construct(self):
        resolution_fa = 40
        self.set_camera_orientation(phi=60 * DEGREES, theta=30 * DEGREES)

        def param_gauss(u, v):
            x = u
            y = v
            z = 0.1*x**2 + 0.5*x * y + 0.2*y
            return np.array([x, y, z])

        gauss_plane = Surface(
            param_gauss,
            resolution=(resolution_fa, resolution_fa),
            v_range=[-2, +2],
            u_range=[-2, +2]
        )

        gauss_plane.scale(2, about_point=ORIGIN)
        gauss_plane.set_style(fill_opacity=1,stroke_color=GREEN)
        gauss_plane.set_fill_by_checkerboard(ORANGE, BLUE, opacity=0.5)
        axes = ThreeDAxes()
        self.add(axes,gauss_plane)

        self.wait(4)
        self.begin_ambient_camera_rotation(rate=0.25)
        self.wait(10)
        # self.stop_ambient_camera_rotation()
        # self.move_camera(phi=0 * DEGREES, theta=0 * DEGREES)
        # self.wait()
        