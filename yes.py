from manim import *

class CreateCircle(Scene):
    def construct(self):
        graph = ComplexPlane().add_coordinates()

        dott = Dot(graph.n2p(0))
        dott2 = Dot(graph.n2p(3+2j))

        dott2_label = MathTex("3+2j").next_to(dott2, UR, 0.1)

        self.play(Create(graph), run_time=2)
        self.play(FadeIn(dott), FadeIn(dott2))
        self.play(FadeIn(dott2_label))

        path = Line(dott, dott2)
        self.play(Create(path))

        pathlabel = Tex("?").next_to(path.get_center(), UL, 0.1)
        pathlabel.add_updater(lambda d: d.next_to(path.get_center(), UL, 0.1))
        self.play(FadeIn(pathlabel))
        
        self.play(FadeOut(graph), FadeOut(dott), FadeOut(dott2), FadeOut(dott2_label))
        self.play(path.animate.move_to(0))

        realpart = MathTex("5").next_to(path, DOWN, 0.1)
        imagpart = MathTex("2j").next_to(path, RIGHT, 0.1)
        newpart = MathTex("2")
        solvedpart = MathTex("5.39")
        self.play(FadeIn(realpart), FadeIn(imagpart))
        self.wait()

        #Make Triangle
        self.play(FadeOut(path))
        tri_verts = Polygon(2*LEFT+DOWN, 2*RIGHT+DOWN, 2*RIGHT+UP, color=WHITE)
        self.play(Create(tri_verts))
        self.play(realpart.animate.next_to(tri_verts, DOWN, 0.1), imagpart.animate.next_to(tri_verts, RIGHT, 0.1))
        self.wait()
        newpart.move_to(imagpart)
        self.play(Transform(imagpart, newpart))

        #Move triangle to do math
        pathlabel.clear_updaters()
        self.play(tri_verts.animate.shift(2*UP), realpart.animate.shift(2*UP), imagpart.animate.shift(2*UP), pathlabel.animate.shift(2*UP))

        #Do Math
        magnitude = MathTex("\sqrt{5^2 + 2^2 = ?}").move_to(DOWN)
        magnitude2 = MathTex("5.39 = ?").move_to(magnitude)
        magnitude3 = MathTex("5.39 = A").move_to(ORIGIN)

        self.play(Create(magnitude), run_time=2)
        self.wait()
        self.play(Transform(magnitude, magnitude2))
        self.wait()
        solvedpart.move_to(pathlabel)
        self.play(Transform(pathlabel, solvedpart))
        self.wait()
        self.clear()
        self.wait()



        




        