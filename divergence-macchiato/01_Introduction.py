from manim import *

class Introduction(Scene):
    def construct(self):
        diverge = MathTex("\\nabla\\cdot\left(\\rho\mathbf{u}\\right) = 0")

        self.play(Create(diverge))
        self.wait(2)
        