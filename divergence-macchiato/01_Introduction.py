from manim import *


class Introduction(Scene):
    def construct(self):
        # func = lambda pos: np.sin(pos[1] / 2) * RIGHT + np.cos(pos[0] / 2) * UP
        # vector_field = ArrowVectorField(
        #     func, x_range=[-7, 7, 1], y_range=[-4, 4, 1], length_func=lambda x: x / 2
        # )
        # self.play(FadeIn(vector_field))
        
        title = Tex("Conservation of Mass").to_corner(LEFT + UP)

        self.play(Create(title))

        domain = Rectangle(width=2)

        self.play(Create(domain))

        enterArrows = [
            ArrowVectorField(
                lambda x: RIGHT / 2,
                x_range=[-3, -1.5, 0.5],
                y_range=[-0.75, 0.75, 0.5],
                length_func=lambda x: x,
            ),
            ArrowVectorField(
                lambda x: LEFT / 2,
                x_range=[1.5, 3, 0.5],
                y_range=[-0.75, 0.75, 0.5],
                length_func=lambda x: x,
            ),
            ArrowVectorField(
                lambda x: DOWN / 2,
                x_range=[-0.75, 0.75, 0.5],
                y_range=[1.5, 3, 0.5],
                length_func=lambda x: x,
            ),
            ArrowVectorField(
                lambda x: UP / 2,
                x_range=[-0.75, 0.75, 0.5],
                y_range=[-3, -1.5, 0.5],
                length_func=lambda x: x,
            ),
        ]

        self.play(*[Create(x) for x in enterArrows])

        m = MathTex("m").shift(4 * LEFT)
        self.play(Create(m))

        V = MathTex("V")
        self.play(Create(V))

        self.play(*[Rotate(x, PI) for x in enterArrows])

        S = MathTex("S").shift(1.25 * (RIGHT + UP))
        self.play(Create(S))

        massSurf = MathTex("\int_{S}\quad ", "\dot{m}", "\quad\  dS", " = 0").shift(
            3 * RIGHT + 1.75 * DOWN
        )
        self.play(Create(massSurf[0:-1]))
        self.play(Create(massSurf[-1]))

        self.play(
            massSurf[1].animate.become(
                MathTex("(\\rho \mathbf{u})\cdot\mathbf{\hat{n}}").move_to(
                    massSurf[1].get_center()
                )
            )
        )

        massVol = MathTex("\int_V \\nabla\cdot(\\rho\mathbf{u})\ dV = 0").move_to(
            massSurf.get_center()
        )

        self.play(ReplacementTransform(massSurf, massVol))

        self.play(
            massVol.animate.become(
                MathTex("\\nabla\cdot(\\rho\mathbf{u}) = 0").move_to(
                    massSurf.get_center()
                )
            )
        )
        self.wait(4)

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
        self.wait(2)
