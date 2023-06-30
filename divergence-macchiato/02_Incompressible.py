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

        # arrowChangeExtraField2 = ArrowVectorField(
        #     lambda x: arrowChange(x[0]) * RIGHT / 2,
        #     x_range=[1.6, 1.6, 1.6],
        #     y_range=[-0.75, 0.75, 0.5],
        #     length_func=lambda x: x,
        # ).scale(2)

        self.play(Create(domain))

        self.play(Create(arrowField))

        self.play(arrowField.animate.become(arrowChangeField))

        xDotDomain = np.linspace(-2, 2, 15)
        dotRep = [
            Dot([x, 0, 0], DEFAULT_DOT_RADIUS / 2)
            for x in -0.25 * (xDotDomain**2) + xDotDomain + 1
        ]

        dotRepCreate = [Create(x) for x in dotRep]
        dotRepUncreate = [Uncreate(x) for x in dotRep]

        # expandDot = Dot(0.75 * LEFT, DEFAULT_DOT_RADIUS / 2)
        # expandDot = Dot([1, 0, 0], DEFAULT_DOT_RADIUS / 2)

        expandPointer = ArcBetweenPoints([1, 0, 0], [3, 1, 0])

        duxdx = (
            MathTex("\\frac{\\partial u_x}{\\partial x} < 0")
            .scale(0.75)
            .move_to([3, 1.5, 0])
        )

        dudxDisc = MathTex("u_{front} < u_{behind}").scale(0.75).move_to([3.5, 1.5, 0])

        divComp = (
            MathTex("\\nabla\cdot u < 0 \\Rightarrow \\text{Compression}")
            .scale(0.75)
            .move_to([4.2, 1.5, 0])
        )

        divExp = (
            MathTex("\\nabla\cdot u > 0 \\Rightarrow \\text{Expansion}")
            .scale(0.75)
            .next_to(divComp, DOWN)
        )

        dotExp = [
            Dot([x, 0, 0], DEFAULT_DOT_RADIUS / 2)
            for x in 0.25 * (xDotDomain**2) + xDotDomain - 1
        ]

        dotExpCreate = [Create(x) for x in dotExp]
        dotExpUncreate = [Uncreate(x) for x in dotExp]

        arrowChangeExp = lambda x: 0.6 + x / 5
        arrowExpand = ArrowVectorField(
            lambda x: arrowChangeExp(x[0]) * RIGHT / 2,
            x_range=[-1, 0.5, 0.5],
            y_range=[-0.75, 0.75, 0.5],
            length_func=lambda x: x,
        ).scale(2)

        # REASONING WRONG, HAVE TO MAKE TWO FIELDS EXPANDING AND COMPRESSING

        self.play(Create(expandPointer))

        self.play(Write(duxdx))

        self.play(ReplacementTransform(duxdx, dudxDisc))

        self.play(*dotRepCreate)

        self.play(ReplacementTransform(dudxDisc, divComp))

        self.play(*dotRepUncreate, Uncreate(expandPointer))

        self.play(*dotExpCreate, arrowField.animate.become(arrowExpand))

        self.play(Write(divExp))

        self.play(*dotExpUncreate)

        self.wait(2)
