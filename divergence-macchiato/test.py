from manim import *
import numpy as np

class RadialDensitySwamp(Scene):
    def construct(self):
        n_particles = 500
        r_base = 1.0       # base radius
        r_scale = 1.0      # how much the density scales radius

        # Density function as a function of angle
        def density(theta):
            return np.exp(0.8 * np.cos(5 * theta))

        # Normalize density
        thetas = np.linspace(0, 2*np.pi, n_particles)
        densities = density(thetas)
        max_density = np.max(densities)

        # Place points
        points = []

        
        for theta in thetas:
            rho = density(theta) / max_density  # normalize to [0,1]
            r = r_base + r_scale * rho
            x = r * np.cos(theta)
            y = r * np.sin(theta)
            points.append([x, y, 0])

        # Create dots
        dots = VGroup(*[Dot(point=pt, radius=0.03, color=BLUE) for pt in points])

        # Add axes (optional)
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": GREY},
        )

        self.add(axes)
        self.play(FadeIn(dots, lag_ratio=0.01), run_time=3)
        self.wait()
