from manim import *

class Seq(Scene):
    def construct(self):
        def make_seq(m, n, bool):
            seq = VGroup()
            for i in range(n):
                num_u = VGroup().add(Text('1').scale(0.7))
                for b in range(2, m+1):
                    num_u.add(Text(f'{b}').scale(0.7).next_to(num_u[b-2], UR))
                if bool == True:
                    num_u[m-1] = Text('m').scale(0.7).next_to(num_u[m-2], UR)
                else:
                    pass
                seq.add(num_u)

                num_d = VGroup().add(Text(f'{m-1}').scale(0.7).next_to(num_u[m-1], DR))
                count = 0
                for a in range(2, m-1)[::-1]:
                    num_d.add(Text(f'{a}').scale(0.7).next_to(num_d[count], DR))
                    count +=1
                seq.add(num_d)
            
            seq.arrange(RIGHT)
            seq.add(Text('1').scale(0.7).next_to(seq[2*n-1], DR))
            return seq

        
        def display_sum(x, y):
            self.wait()
            self.play(Write(x[0]), Write(x[1]))
            self.wait(0.5)
            for i in range(0, 9, 2):
                self.play(y[i].animate.set_color(PURE_GREEN))
            self.wait(0.5)
            self.play(Write(x[2]))
            self.wait(0.5)
            self.play(Write(x[3]))
            for i in range(1, 10, 2):
                self.play(y[i].animate.set_color(PURE_BLUE))
            self.wait(0.5)
            self.play(Write(x[4]))
            self.wait(0.5)
            self.play(Write(x[5]))
            
        title0 = Tex(r"Suppose that ${m}$, ${n}$ are positive integer with ${m\geq2}$").scale(0.7).shift(UP*3)
        title1 = Tex(r"a ${(m, n)}$-sawtooth sequence starts with 1 and has ${n}$ teeth,\\ each tooth goes up to ${m}$ and back down to 1.}").scale(0.7).next_to(title0, DOWN)
        
        seq0 = make_seq(4, 5, False).scale(0.7).next_to(title1, DOWN*1.8)
        seq1 = make_seq(4, 5, True).scale(0.7).move_to(seq0)
        br0 = Brace(seq1, sharpness=1.0).scale(0.7)
        t0 = Tex(r"${n}$ teeth").next_to(br0, DOWN).scale(0.6)

        tex0 = Tex(r"a (4, 5)-sawtooth sequence includes 31 terms and an average of ${\frac{76}{31}}$").scale(0.5).next_to(seq0, DOWN*1.8)
        q1 = Tex(r"How to find the sum of the terms in a ${(m, n)}$-sawtooth sequence?").scale(0.7).next_to(tex0, DOWN*2)

        tex1 = Tex(r"$Sum$", r"$=$", r"$(1+2+3+4)\cdot5$", r"$+$", r"$(2+3)\cdot5$", r"$+1=76$").scale(0.7).next_to(tex0, DOWN*2)
        tex1[2].set_color(PURE_GREEN), tex1[4].set_color(PURE_BLUE)

        tex2 = Tex(r"$Sum$", r"$=$", r"$(1+2+\cdots +m)\cdot n$", r"$+$", r"$(2+\cdots +m-1)\cdot n$", r"$+1$").scale(0.7).next_to(tex0, DOWN*2)
        tex2[2].set_color(PURE_GREEN), tex2[4].set_color(PURE_BLUE)

        br1 = VGroup(Brace(tex2[2], sharpness=1.0).scale(0.7), Brace(tex2[4], sharpness=1.0).scale(0.7))
        t1 = Text("arithmetic sequence").next_to(tex2[3], DOWN*2).scale(0.6)
        t2 = Tex(r"$S_{n}=\frac{a_{1}+ a_{n}}{2}\cdot n$").scale(0.7).move_to(t1) 

        tex3 = Tex(r"$=$", r"$(\frac{1+m}{2}\cdot m)\cdot n$", r"$+$", r"$(\frac{2+m-1}{2}\cdot (m-2))\cdot n$", r"$+1$").scale(0.7).next_to(tex2, DOWN*1.8).align_to(tex2[1], LEFT)
        tex3[1].set_color(PURE_GREEN), tex3[3].set_color(PURE_BLUE)

        tex4 = Tex(r"Sum=$(m^{2}-1)\cdot n+1$").scale(0.7).next_to(tex3, DOWN*1.8).align_to(tex2[1], LEFT)
        
        q2 = Tex(r"Prove that for all pairs of positive integers ${(m, n)}$ with ${m\geq2}$, \\ the", r"average", r"of the terms in the ${(m, n)}$-sawtooth sequence is not an integer").scale(0.5).move_to(title0)

        tex5 = Tex(r"$Average$", r"$=$", r"$\frac{Sum}{Nterms}$").scale(0.5).move_to(tex2).align_to(tex2, LEFT)

        tex6 = Tex(r"$Nterms$", r"$=$", r"$m\cdot n$", r"$+$", r"$(m-2)\cdot n$", r"$+1$").scale(0.5).next_to(tex5, DOWN).align_to(tex5, LEFT)
        tex6[2].set_color(PURE_GREEN), tex6[4].set_color(PURE_BLUE)

        tex7 = Tex(r"$\frac {(m^{2}-1)\cdot n+1}{m\cdot n+(m-2)\cdot n+1}$").scale(0.7).move_to(tex5[2]).align_to(tex5[2], LEFT)

        q3 = Tex(r"If an expression can be written as ${a + \frac{b}{c}}$, it can not be an integer").scale(0.5).next_to(q2, DOWN)

        q4 = Tex(r"Since the expression can be written as ${\frac{1}{2}\times}$ another fraction, it's not an integer").scale(0.7).move_to(q3).set_color(YELLOW_C)

        tex8 = Tex(r"after Simplfy: ${ \frac{1}{2}(m+1+\frac{1-m}{2mn-2n+1}) }$").scale(0.5).next_to(tex7, DOWN)

        tex9 = Tex(r"Since ${(2mn-2n+1)-(1-m)>0}$").scale(0.5).next_to(tex8, DOWN)

        tex10 = Tex(r"${\frac{1-m}{2mn-2n+1}}$ is a proper fraction, ${(m+1+\frac{1-m}{2mn-2n+1})}$ is also a fraction").scale(0.5).next_to(tex9, DOWN).align_to(tex8, LEFT)

        

        
        #title and q1
        self.play(Write(title0))
        self.wait()
        self.play(Write(title1, run_time = 4))
        self.wait()
        self.play(Write(seq0, run_time = 4))
        self.wait(0.5)
        self.play(FadeIn(tex0))
        self.wait()
        self.play(Write(q1, run_time = 2))
        self.wait(3)
        self.play(FadeOut(q1))     

        #(3,4)sawtooth
        display_sum(tex1, seq0)
        self.wait(3)
        self.play(FadeOut(tex0), FadeOut(tex1))
        self.wait()

        #(m,n)sawtooth
        self.play(ReplacementTransform(seq0, seq1))
        self.wait(0.5)
        self.play(Create(br0))
        self.play(Create(t0))
        self.wait()
        display_sum(tex2, seq1)
        self.wait(3)

        #sum
        self.play(Create(br1))
        self.wait()
        self.play(Create(t1))
        self.wait()
        self.play(FadeTransform(t1, t2))
        self.play(FadeOut(br1))
        self.wait()
        self.play(t2.animate.next_to(tex2, LEFT))
        self.wait()
        self.play(FadeIn(tex3))
        self.wait(3)
        self.play(FadeIn(tex4))
        self.wait(3)
        self.play(
            FadeOut(VGroup(title0, title1, t2, tex2, tex3))
        )
        self.play(seq1.animate.set_color(WHITE))

        #q2
        self.wait(2)
        self.play(FadeIn(q2))
        self.wait()
        self.play(Write(tex5))
        self.wait()
        display_sum(tex6, seq1)
        self.wait(3)
        self.play(ReplacementTransform(tex5[2], tex7))
        self.play(FadeOut(tex6), FadeOut(tex4))
        self.play(FadeIn(q3))
        self.wait()
        self.play(FadeIn(tex8))
        self.wait()
        self.play(FadeIn(tex9))
        self.wait()
        self.play(FadeIn(tex10))
        self.wait(3)
        self.play(FadeTransform(q3, q4))
        self.wait(3)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )