from manim import *

class TwoD(Scene):
    def construct(self):
        def get_label(p, t, s, d):
            return VGroup(p.scale(0.5), Tex(t).scale(s).next_to(p, direction=d))
        
        def display(lines, texs, colors):
            self.play(FadeIn(texs[1]))
            for l, t, c in zip(lines, VGroup(texs[0], texs[2]), colors):
                self.play(l.animate.set_color(c))
                self.wait(0.3)
                self.play(TransformFromCopy(l, t.set_color(c)))

        #dots and lines
        a = [-0.5, 1.5, 0]
        b = [-4, -1.5, 0]
        c = [1.5, -1.5, 0]
        dot_a = get_label(Dot(a), r'$A$', 0.7, UR)
        dot_b = get_label(Dot(b), r'$B$', 0.7, DL)
        dot_c = get_label(Dot(c), r'$C$', 0.7, DR)

        tri = Polygon(a, b, c).set_color(WHITE)
        coord = (b+RIGHT*3, a+UP*1.5+LEFT*1)
        line = Line(*coord)
        extend = DashedLine(a, a+UP*4.5+LEFT*3, dashed_ratio=0.5)
        d = line_intersection(coord, (b, c))
        e = line_intersection(coord, (a, b))
        f = line_intersection(coord, (a, coord[1]))
        dot_d = get_label(Dot(d), r'$D$', 0.7, DOWN)
        dot_e = get_label(Dot(e), r'$E$', 0.7, LEFT)
        dot_f = get_label(Dot(f), r'$F$', 0.7, LEFT)

        self.play(Create(tri))
        for i in VGroup(dot_a, dot_b, dot_c):
            self.play(FadeIn(i))
        self.wait(0.5)
        self.play(Create(extend))
        self.wait(0.5)
        self.play(Create(line))
        self.wait(0.5)
        for i in VGroup(dot_d, dot_e, dot_f):
            self.play(FadeIn(i))
        
        #transform and write
        cf = VGroup(Line(c, f), DashedLine(a, f, dashed_ratio=0.5) )
        ab = VGroup(Line(a, e), Line(e, b))
        bc = VGroup(Line(b, d), Line(d, c))  
        tex0 = MathTex(r"{CF", r"\over", r"AF}")
        tex1 = MathTex(r"{AE", r"\over", r"EB}")
        tex2 = MathTex(r"{BD", r"\over", r"DC}")
        texs = VGroup(
            tex0,
            Tex(r"$\times$"),
            tex1,
            Tex(r"$\times$"),
            tex2,
            Tex(r"$=1$")
        ).scale(0.6).arrange(RIGHT).next_to(tri, RIGHT*3)
        tex3 = Tex(r"Menelaus's theorem states that${:}$ ").scale(0.7).next_to(texs, UP*1.8)


        self.wait()
        self.play(Write(tex3))
        self.wait()
        for l, t in zip(VGroup(cf, ab, bc), VGroup(tex0, tex1, tex2)):
            display(l, t, (PURE_GREEN, PURE_BLUE))
        for i in range(1, 6, 2):
            self.play(Write(texs[i]))
        self.wait()
        
        #reverse
        tex2 = VGroup(
            Tex(r"The converse of Menelaus' theorem is also true${:}$"),
            Tex(r"Suppose three points ${D, E, F}$ are on sides \\(or extension) ${AB, BC, AC}$ respectively,"),
            Tex(r"such that ${1}$ or ${3}$ of them are in the \\extensions of the sides."),
            Tex(r"Then points ${D, E, F}$ are collinear if and only if:"),
        ).scale(0.6).arrange(DOWN)
        tex2.next_to(tex1, UP)
        tex4 = Text("How can we prove it?").next_to(tri, DOWN*4)

        self.play(FadeOut(tex3))
        self.wait()
        for i in (dot_d, dot_e, dot_f):
            self.play(i.animate.set_color(YELLOW_C))
            self.wait(0.5)
        for i in tex2:
            self.play(Write(i, run_time = 3))
            self.wait(2)
        self.wait(2)
        self.play(FadeIn(tex4))
        self.wait(3)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.wait(3)

class ThreeD(ThreeDScene):
    def construct(self):
        def get_label(p, t, x, a, d):
            return VGroup(p.scale(0.5), Tex(t).scale(0.7).rotate(x, axis = a).next_to(p, direction=d))
        
        def trans(lines, texs, colors):
            for l, t in zip(lines, texs):
                self.play(l.animate.set_color(colors))
                self.wait(0.3)
                self.play(FadeIn(t.set_color(colors)))
        
        def display(lines, texs, colors):
            n = 0
            for i in range(1, 6, 2):
                if i == 3:
                    self.play(FadeIn(texs[i]))
                else:
                    self.play(FadeIn(texs[i]))
                    trans((lines[int((i-1)/2)], lines[int((i+1)/2)]), (texs[i-1], texs[i+1]), colors[n])
                    n += 1
        
        #2d texts
        tex0 = MathTex(r"{JC", r"\over", r"BK}", r"=", r"{CD", r"\over", r"BD}")
        tex1 = MathTex(r"{JC", r"\over", r"AL}", r"=", r"{CF", r"\over", r"AF}")
        tex2 = Tex(r"$\frac{CF}{AF} \times \frac{AE}{EB} \times \frac{BD}{DC} =1$")
        tex3 = Tex(r"$\frac{JC}{AL} \times \frac{AE}{EB} \times \frac{BK}{JC} =1$")
        tex5 = Tex(r"Therefore${:}$")
        tex6 = MathTex(r"{AL", r"\over", r"BK}", r"=", r"{AE", r"\over", r"EB}")
        tex7 = Tex(r"${L, E, K}$;", r"${J, D, K}$;", r"${J, L, F}$", r"${;}$are collinear")
        tex4 = Tex(r"$\frac{JC}{AL} \times \frac{AL}{BK} \times \frac{BK}{JC} =1$")
        texs = VGroup(
            Tex(r"If it's known that: $\frac{CF}{AF} \times \frac{AE}{EB} \times \frac{BD}{DC} =1$"),
            Tex(r"How to prove points ${D, E, F}$ are collinear?"),
            Tex(r"Construct three lines perpendicular to ${xy}$-plane"),
            Tex(r"Find points ${J, L, K}$ so that:"),
            tex0, tex1, tex2, tex3, tex5, tex6, tex7, tex4
        ).scale(0.6).arrange(DOWN).to_corner(UR)
        texs2 = VGroup(
            Tex(r"Notice points ${D, E, F}$ are all locating on \\the line of intersection between plane ${LJK}$ and ${ABC}$"),
            Tex(r"Thus points ${D, E, F}$ are collinear")
        ).scale(0.6).arrange(DOWN).to_corner(UL)

        tex4.move_to(tex3)
        self.add_fixed_in_frame_mobjects(texs)
        self.add_fixed_in_frame_mobjects(texs2)
        self.play(FadeOut(texs), FadeOut(texs2))

        #setup axes and camera
        ax = ThreeDAxes(
            x_range=[-5, 5, 1],
            y_range=[-7, 7, 1],
            z_range=[-7, 7, 1],
            x_length=8,
            y_length=6,
            z_length=6,
        ).shift(LEFT).set_color(GREY_D)

        self.move_camera(phi=60* DEGREES, theta=-120* DEGREES)
        self.play(FadeIn(ax))
        self.wait()

        #display triangle + cross line on xy-plane
        a = ax.c2p(0.5, 1.5, 0)
        b = ax.c2p(-3, -1.5, 0)
        c = ax.c2p(1.5, -1.5, 0)
        dot_a = get_label(Dot(a), r'$A$', 0, RIGHT, UR)
        dot_b = get_label(Dot(b), r'$B$', 0, RIGHT, DL)
        dot_c = get_label(Dot(c), r'$C$', 0, RIGHT, DR)

        d = ax.c2p(0, -1.5, 0)
        e = ax.c2p(-0.2, 0.9, 0)
        f = ax.c2p(-0.5, 4.5, 0)
        dot_d = get_label(Dot(d), r'$D$', 0, RIGHT, DL)
        dot_e = get_label(Dot(e), r'$E$', 0, RIGHT, UL)
        dot_f = get_label(Dot(f), r'$F$', 0, RIGHT, LEFT)

        tri = Polygon(a, b, c, color=WHITE)
        extend = DashedLine(a, ax.c2p(-1, 6, 0), dashed_ratio=0.5)
        
        self.play(Create(tri))
        for i in VGroup(dot_a, dot_b, dot_c):
            self.play(FadeIn(i))
        self.wait(0.5)
        self.play(Create(extend))
        self.wait(0.5)
        self.play(Create(Line(d, f)))
        self.wait(0.5)
        for i in VGroup(dot_d, dot_e, dot_f):
            self.play(FadeIn(i))
        
        
        #question
        self.wait()
        self.play(Write(texs[0]))
        self.wait()
        self.play(Write(texs[1]))
        self.wait(2)
        
        #display 3d
        l = ax.c2p(0.5, 1.5, 1.6)
        k = ax.c2p(-3, -1.5, -6.3)
        j = ax.c2p(1.5, -1.5, 3.15)
        dot_l = get_label(Dot3D(l), r'$L$', PI/2, RIGHT, UR)
        dot_k = get_label(Dot3D(k), r'$K$', PI/2, RIGHT, UR)
        dot_j = get_label(Dot3D(j), r'$J$', PI/2, RIGHT, UR)
        
        slines = VGroup(
            Line3D(start=a, end=ax.c2p(0.5, 1.5, 7), color=GREY_C),
            Line3D(start=b, end=ax.c2p(-3, -1.5, -7), color=GREY_C),
            Line3D(start=c, end=ax.c2p(1.5, -1.5, 7), color=GREY_C)
        )

        cj = Line3D(start=c, end=j)
        la = Line3D(start=a, end=l)
        kb = Line3D(start=b, end=k)
        lines = VGroup(cj, la, kb)
        lineg1 = VGroup(cj, kb, Line(c, d), Line(b, d))
        lineg2 = VGroup(cj, la, Line(c, f), Line(a, f))
        lineg3 = VGroup(la, kb, Line(a, e), Line(e, b))
        
        self.play(Write(texs[2]))
        self.wait(0.5)
        self.play(Create(slines))
        self.wait()
        for i in VGroup(dot_j, dot_l, dot_k):
            self.play(FadeIn(i))
        self.wait(0.5)
        self.play(FadeIn(lines))
        self.play(FadeOut(slines))
        self.play(Write(texs[3]))
        self.wait()
        display(lineg1, tex0, (BLUE_C, GREEN_C))
        self.wait()
        display(lineg2, tex1, (RED_C, YELLOW_C))

        #conclution
        self.wait(3)
        self.play(FadeIn(tex2))
        self.wait(2)
        self.play(TransformFromCopy(tex2, tex3))
        self.wait(2)
        self.play(FadeOut(tex3), FadeIn(tex4))
        self.wait(2)
        self.play(Write(tex5))
        self.wait()
        display(lineg3, tex6, (PURPLE_C, MAROON_C))
        self.wait(3)

        #display 3d polygons and lines
        lek = Line3D(l, k)
        jdk = Line3D(j, k)
        jlf = Line3D(j, f)

        pg1 = VGroup(Polygon(k, d, b, color=TEAL_C, fill_color=TEAL_C, fill_opacity=0.5), Polygon(j, c, d, color=TEAL_C, fill_color=TEAL_C, fill_opacity=0.5))
        pg2 = VGroup(Polygon(k, e, b, color=LIGHT_PINK, fill_color=LIGHT_PINK, fill_opacity=0.5), Polygon(l, e, a, color=LIGHT_PINK, fill_color=LIGHT_PINK, fill_opacity=0.5))
        pg3 = VGroup(Polygon(l, f, a, color=GOLD_C, fill_color=GOLD_C, fill_opacity=0.5), Polygon(j, f, c, color=GOLD_C, fill_color=GOLD_C, fill_opacity=0.5))

        for i in (pg1, pg2, pg3):
            self.play(FadeIn(i))
            self.wait()
        self.wait(2)
        for i in tex7:
            self.play(Write(i))
        self.wait(3)

        #clean
        self.play(FadeOut(VGroup(pg1, pg2, pg3)))
        self.wait(2)
        for i in (lek, jdk, jlf):
            self.play(Create(i))
        self.wait(2)
        self.play(VGroup(lineg1, lineg2, lineg3).animate.set_color(WHITE))

        #final conclution
        jlk = Polygon(j, l, k, color=PURE_GREEN, fill_color=PURE_GREEN, fill_opacity=0.3)
        jfk = Polygon(j, f, k, color=PURE_GREEN, fill_color=PURE_GREEN, fill_opacity=0.3)
        
        self.wait(2)
        self.play(tri.animate.set_color(PURE_BLUE).set_opacity(0.3))
        self.wait()
        self.play(FadeIn(jlk))
        self.wait(2)
        self.play(Line(d, e).animate.set_color(YELLOW_C))
        for i in (dot_d, dot_e):
            self.play(i.animate.set_color(YELLOW_C))
            self.wait(0.5)
        self.wait(0.5)
        self.play(Transform(jlk, jfk))
        self.wait()
        self.play(FadeIn(dot_f.set_color(YELLOW_C)))
        self.wait(3)
        self.play(Write(texs2[0]))
        self.wait(3)
        self.play(Write(texs2[1]))
        self.wait(3)
        
        

        
        