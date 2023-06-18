from manim import *

class OptimizationAnalogue(Scene):
    def construct(self):
        quadForm = MathTex("f(\mathbf{x}) = \\frac{1}{2}\mathbf{x}^\\top \mathbf{Ax} - \mathbf{b}^\\top \mathbf{x}").shift(2*UP)

        wrapbmatrix = lambda x : "\\begin{bmatrix}" + x + "\\end{bmatrix}"

        quadExpanded = MathTex("f\left({}\\right) = {}{}{} + {}{}".format(
            wrapbmatrix("x \\\\ y"),
            "\\frac{1}{2}" + wrapbmatrix("x & y"),
            wrapbmatrix("a_{11} & a_{12} \\\\ a_{21} & a_{22}"),
            wrapbmatrix("x \\\\ y"),
            wrapbmatrix("b_1 & b_2"),
            wrapbmatrix("x \\\\ y"),
        )).next_to(quadForm, DOWN)

        quadxy = MathTex("f(\mathbf{x}) = \\frac{1}{2}\left[a_{11}x^2 + (a_{12} + a_{21})xy + a_{22}y^2\\right] + b_1x + b_2y").next_to(quadExpanded, DOWN )

        grad0 = MathTex("\\frac{df}{d\mathbf{x}} = " + wrapbmatrix("\\frac{\partial f}{\partial x} & \\frac{\partial f}{\partial y}") + "^\\top = \mathbf{0}").next_to(quadExpanded, 3*DOWN)

        axb = MathTex("\mathbf{Ax} = \mathbf{b}").next_to(grad0, 2*DOWN)

        axbRect = SurroundingRectangle(axb)

        self.play(Create(quadForm))
        self.wait(2)
        self.play(Create(quadExpanded))
        self.wait(2)
        self.play(Create(quadxy))
        self.wait(2)
        self.play(Uncreate(quadExpanded))
        self.wait(2)
        self.play(quadxy.animate.shift(UP))
        self.wait(2)
        self.play(Create(grad0))
        self.wait(2)
        self.play(Create(axb))
        self.play(Create(axbRect))
        self.wait(2)
