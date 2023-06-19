from manim import *

class Introduction(Scene):
    def construct(self):
        text=MathTex(
            "A = \\begin{bmatrix} a_{11} & a_{12} \\\\ a_{21} & a_{22} \\end{bmatrix}"
        ).shift(2*UP)
        self.play(Write(text))
        
        eigen = MathTex("Ax = \\lambda x").next_to(text, DOWN)

        eigen1 = MathTex("Ae_1 = \\lambda_1v_1").next_to(eigen, DOWN)
        eigen2 = MathTex("Ae_2 = \\lambda_2v_2").next_to(eigen1, DOWN)

        anyVec = MathTex("x = c_1v_1 + c_2v_2").next_to(eigen2, DOWN)
        
        self.play(Write(eigen))
        self.play(Write(eigen1))
        self.play(Write(eigen2))
        self.play(Write(anyVec))
