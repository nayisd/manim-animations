from manim import *

class Trigdisplay(Scene):
    def construct(self):
        #display basic function
        text1 = Text('Find the least positive integer n such that',font_size=30)
        tex1 = Tex(r'$\frac{1}{sin45^\circ sin46^\circ}+\frac{1}{sin47^\circ sin48^\circ}+\cdots+\frac{1}{sin133^\circ sin134^\circ}=\frac{1}{sin(n^\circ)}$',font_size=35)
        tex2 = Tex(r'$\frac{1}{sin45^\circ sin46^\circ}+\frac{1}{sin46^\circ sin47^\circ}+\frac{1}{sin47^\circ sin48^\circ}+\cdots+\frac{1}{sin89^\circ sin90^\circ}=\frac{1}{sin(n^\circ)}$',font_size=35)
        self.play(Write(text1))
        self.wait()
        self.play(text1.animate.next_to(tex1, UP, buff=0.5))
        self.play(FadeIn(tex1))
        self.wait()
        self.play(FadeOut(text1))
        self.play(tex1.animate.shift(UP*3))
        
        #geometry
        self.wait()
        axes = Axes(
            x_length=4, y_length=4,
            tips=False,
        )
        circle = Circle()
        ang1 = Sector(
            start_angle=0,
            angle= 133 / 360 * TAU,
            outer_radius=1,
            color=BLUE,
            fill_opacity = 0.5,
        )
        a1 = Tex(r'$133^\circ$', color=BLUE, font_size=30)
        ang2 = Sector(
            start_angle=PI,
            angle= -47 / 360 * TAU,
            outer_radius=1,
            color=GREEN,
            fill_opacity = 0.5,
        )
        a2 = Tex(r'$47^\circ$', color=GREEN, font_size=30)
        text2 = Text('every angle >90 can be transformed into its reference angle',font_size=30)
        geo = VGroup()
        geo.add(axes, circle, a1, ang1, a2, ang2, text2)
        self.add(axes)
        self.play(Write(circle))
        self.play(Create(ang1))
        self.play(Create(ang2))
        self.play(a1.animate.next_to(ang1, RIGHT))
        self.play(a2.animate.next_to(ang2, LEFT))
        self.wait()
        self.play(text2.animate.next_to(axes, DOWN))
        self.wait()
        self.play(*[FadeOut(mob) for mob in geo])
        self.play(Transform(tex1, tex2))
        self.wait()
        self.play(tex1.animate.shift(UP*3))
        self.wait()

        form1 = Tex(r'$\frac{1}{sin45^\circ sin46^\circ}$')
        form1.shift(UP*2)
        form2 = Tex(r'$sin(A\pm B)=sinAcosB\pm cosAsinB$')
        form4 = Tex(r'$sin(n+1-n)=sin(n+1)cos(n)-cos(n+1)sin(n)$')
        form3 = Tex(r'$\frac{1}{sin(n) sin(n+1)}$')
        form5 = Tex(r'$\frac{sin1^\circ}{sin(n) sin(n+1)}\cdot \frac{1}{sin1^\circ}$')
        form7 = Tex(r'$\frac{sin(n+1-n)}{sin(n) sin(n+1)}\cdot \frac{1}{sin1^\circ}$')
        form9 = Tex(r'$\frac{sin(n+1)cos(n)-cos(n+1)sin(n)}{sin(n) sin(n+1)}\cdot \frac{1}{sin1^\circ}$')
        form11 = Tex(r'$(\frac{cos(n)}{sin(n)}-\frac{cos(n+1)}{sin(n+1)})\cdot \frac{1}{sin1^\circ}$')
        formulas = [form3, form5, form7, form9, form11]
        self.play(FadeIn(form1))
        self.play(FadeIn(form2))
        self.wait()
        self.play(FadeTransform(form2, form4))
        self.wait()
        self.play(FadeOut(form4))
        for i in formulas:
            self.play(i.animate.next_to(form1, DOWN, buff = formulas.index(i)+1))
            self.wait()

        self.play(FadeOut(form1))
        for i in formulas:
            self.play(FadeOut(i))

        #final
        tex3 = Tex(r'$(\frac{cos45^\circ}{sin45^\circ}-\frac{cos46^\circ}{sin46^\circ})\cdot \frac{1}{sin1^\circ} \newline +(\frac{cos46^\circ}{sin46^\circ}-\frac{cos47^\circ}{sin47^\circ})\cdot \frac{1}{sin1^\circ} \newline +\cdots \newline +(\frac{cos89^\circ}{sin89^\circ}-\frac{cos90^\circ}{sin90^\circ})\cdot \frac{1}{sin1^\circ}$')
        tex3.shift(UP*1)
        tex4 = Tex(r'$(\frac{cos45}{sin45}-\frac{cos90}{sin90})\cdot \frac{1}{sin1^\circ}$')
        tex5 = Tex(r'$(1-0)\cdot\frac{1}{sin1^\circ}$')
        tex6 = Tex(r'$\frac{1}{sin1^\circ}$')
        text3 = Text('Apply it to every fraction, we have',font_size=30)
        text5 = Text('x = 1')

        texs = [tex4, tex5, tex6]
        
        self.play(Write(text3))
        self.wait()
        self.play(FadeOut(text3))
        self.play(FadeOut(tex1))
        self.wait()
        self.play(FadeIn(tex3))
        self.wait()
        for i in texs:
            self.play(i.animate.next_to(tex3, DOWN, buff = texs.index(i)+1))
            self.wait()
        self.play(FadeOut(tex3))
        for i in texs:
            self.play(FadeOut(i))
        self.wait()
        self.play(Write(text5))
        self.wait(3)

