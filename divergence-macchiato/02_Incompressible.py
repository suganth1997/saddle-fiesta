from manim import *


class Incompressible(Scene):
    def construct(self):
        diverge = MathTex("\\nabla\\cdot\left(\\rho\mathbf{u}\\right) = 0").shift(UP)

        self.play(Create(diverge))
        self.wait(2)

        rhoZero = MathTex("\\rho = 0").next_to(diverge, 2 * DOWN)

        self.play(Create(rhoZero))
        self.wait(2)

        incomp = MathTex("\\nabla\\cdot\mathbf{u} = 0").shift(UP)
        self.play(ReplacementTransform(Group(diverge, rhoZero), incomp))
        self.wait(2)

        divexp = MathTex(
            "\\frac{\partial u_x}{\partial x} + \\frac{\partial u_y}{\partial y} = 0"
        ).next_to(incomp, DOWN)

        self.play(Create(divexp))

        self.play(divexp.animate.move_to(UP * 3), Uncreate(incomp))

        self.wait(2)

        domain = Rectangle(width=2).scale(2)

        arrowField = ArrowVectorField(
            lambda x: RIGHT / 2,
            x_range=[-1, 0.5, 0.5],
            y_range=[-0.75, 0.75, 0.5],
            length_func=lambda x: x,
        ).scale(2)

        arrowChange = lambda x: 0.6 - x / 5
        arrowChangeField = ArrowVectorField(
            lambda x: arrowChange(x[0]) * RIGHT / 2,
            x_range=[-1, 0.5, 0.5],
            y_range=[-0.75, 0.75, 0.5],
            length_func=lambda x: x,
        ).scale(2)

        arrowChangeExtraField1 = ArrowVectorField(
            lambda x: arrowChange(x[0]) * RIGHT / 2,
            x_range=[0.8, 0.8, 0.8],
            y_range=[-0.75, 0.75, 0.5],
            length_func=lambda x: x,
        ).scale(2)

        # arrowChangeExtraField2 = ArrowVectorField(
        #     lambda x: arrowChange(x[0]) * RIGHT / 2,
        #     x_range=[1.6, 1.6, 1.6],
        #     y_range=[-0.75, 0.75, 0.5],
        #     length_func=lambda x: x,
        # ).scale(2)

        self.play(Create(domain))

        self.play(Create(arrowField))

        self.play(arrowField.animate.become(arrowChangeField))

        self.play(Create(arrowChangeExtraField1))

        # expandDot = Dot(0.75 * LEFT, DEFAULT_DOT_RADIUS / 2)
        expandDot = Dot([-1, 0, 0], DEFAULT_DOT_RADIUS / 2)

        expantPointer = CurvedArrow([-1, 0, 0], [-3, 1, 0])

        # REASONING WRONG, HAVE TO MAKE TWO FIELDS EXPANDING AND COMPRESSING

        self.play(Create(expandDot))

        self.play(Create(expantPointer))

        self.wait(2)
