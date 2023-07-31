from manim import *

class ALG(Scene):
    def construct(self):
        #intro
        
        title = Text('ALG Inequality')
        title1 = Text('Arithmetic-Logarithmic-Geometric Mean').move_to(title)
        ineq = Tex(r'$b>\frac{a+b}{2}>\frac{b-a}{\ln b-\ln a}>\sqrt{ab}>\frac{2}{\frac{1}{a} + \frac{1}{b}}>ab>a>0$')

        self.play(Write(title))
        self.wait()
        self.play(Transform(title, title1))
        self.wait(3)
        self.play(FadeOut(title))
        self.play(FadeIn(ineq))
        self.wait()
        self.play(FadeOut(ineq))
        self.wait()
        
        a = ValueTracker(1)
        b = ValueTracker(4)
        
        def get_label(x, l, z):
            return VGroup(x.scale(0.5), Tex(l).scale(0.5).next_to(x, direction=z))
        
        def graph_vertical_line(ax, function, x, l):
            result = VGroup()
            line = DashedLine(
                start= ax.c2p(x, function.underlying_function(x)),
                end= ax.c2p(x, 0),
            )
            dot = get_label(Dot(ax.c2p(x, function.underlying_function(x))), l, UR*0.5)
            result.add(line, dot)
            return result
        
        def graph_horizontal_line(ax, function, x, l1, l2):
            result = VGroup()
            line = DashedLine(
                start= ax.c2p(a.get_value(), function.underlying_function(x)),
                end= ax.c2p(b.get_value(), function.underlying_function(x)),
            )
            dot1 = get_label(Dot(ax.c2p(a.get_value(), function.underlying_function(x))), l1, LEFT)
            dot2 = get_label(Dot(ax.c2p(b.get_value(), function.underlying_function(x))), l2, RIGHT)
            result.add(line, dot1, dot2)
            return result
        
        def graph_line(ax, function, x1, x2):
            return DashedLine(
                start= ax.c2p(x1, function.underlying_function(x1)),
                end= ax.c2p(x2, function.underlying_function(x2)),
            )
        
        def period():
            self.play(b.animate.set_value(2), run_time = 3)
            self.play(b.animate.set_value(4), run_time = 3)
        
        #set up axes and graph
        ax = Axes(
            x_range=[-0.5, 5, 0.5],
            y_range=[-0.5, 1.5, 0.5],
            x_length= 7,
            y_length= 7,
            axis_config={"include_numbers": False,"include_ticks": True},
        ).shift(LEFT*3)
        graph = ax.plot(lambda x: 1/x, x_range=[0.7, 4.5], use_smoothing=False)
        
        #basic dots and updator
        dot_a = always_redraw(lambda:
        get_label(Dot(ax.c2p(a.get_value(), 0)), r'$a$', DOWN)
        )
        dot_b = always_redraw(lambda:
        get_label(Dot(ax.c2p(b.get_value(), 0)), r'$b$', DOWN)
        )
        dot_ab = always_redraw(lambda:
        get_label(Dot(ax.c2p(np.sqrt(a.get_value()*b.get_value()), 0)), r'$\sqrt{ab}$', DOWN)
        )
        dot_fab = always_redraw(lambda:
        get_label(Dot(ax.c2p((a.get_value()+b.get_value())/2, 0)), r'$\frac{a+b}{2}$', DOWN)
        )
        dot_y = always_redraw(lambda:
        get_label(Dot(ax.c2p(b.get_value(), 1)), r'$Y$', UR)
        )                    
        
        #vertical line
        l_ap = always_redraw(lambda:
        graph_vertical_line(ax, graph, a.get_value(), r"$P$")
        )
        l_bq= always_redraw(lambda:
        graph_vertical_line(ax, graph, b.get_value(), r"$Q$")
        )
        l_abt= always_redraw(lambda:
        graph_vertical_line(ax, graph, np.sqrt(a.get_value()*b.get_value()), r"$T$")
        )
        l_fabk= always_redraw(lambda:
        graph_vertical_line(ax, graph, (a.get_value()+b.get_value())/2, r"$K$")
        )
        l_yb =always_redraw(lambda:
        DashedLine(ax.c2p(b.get_value(), 1), ax.c2p(b.get_value(), 0))                    
        )
        l_pt =always_redraw(lambda:
        graph_line(ax, graph, a.get_value(), np.sqrt(a.get_value()*b.get_value()))                    
        )
        l_pq =always_redraw(lambda:
        graph_line(ax, graph, a.get_value(), b.get_value())                    
        )
        
        
        
        #horizontal line
        l_cd = always_redraw(lambda:
        graph_horizontal_line(ax, graph, np.sqrt(a.get_value()*b.get_value()), r"$D$", r"$C$")
        )
        l_mn = always_redraw(lambda:
        graph_horizontal_line(ax, graph, (a.get_value()+b.get_value())/2, r"$M$", r"$N$")
        )
        l_yp =always_redraw(lambda:
        DashedLine(ax.c2p(b.get_value(), 1), ax.c2p(a.get_value(), 1))                    
        )
        l_qx = always_redraw(lambda:
        graph_horizontal_line(ax, graph, b.get_value(), r"$X$", r"$Q$")
        )
        
        #tangent line
        line1 = always_redraw(lambda:
        ax.plot(lambda x: (-4/(a.get_value()+b.get_value())**2)*x + 4/(a.get_value()+b.get_value()),
                x_range=[0.5, b.get_value()+0.5], use_smoothing=False)
        )
       
        dot_e= always_redraw(lambda:
        ax.get_graph_label(graph=line1, label=Tex(r"$E$").scale(0.7), x_val= a.get_value(), dot=True, direction=UL)
        )
        dot_f= always_redraw(lambda:
        ax.get_graph_label(graph=line1, label=Tex(r"$F$").scale(0.7), x_val= b.get_value(), dot=True, direction=DR)
        )  
        
        #area
        A_abqp_c = always_redraw(lambda:
        ax.get_area(graph,
            x_range=(a.get_value(),b.get_value()),
            color=(BLUE_C),
            opacity=0.5,
        )                   
        )
        A_abfe = always_redraw(lambda:
        ax.get_area(line1,
            x_range=(a.get_value(),b.get_value()),
            color=(GREEN_C),
            opacity=0.5,
        )                   
        )
        A_autp_c = always_redraw(lambda:
        ax.get_area(graph,
            x_range=(a.get_value(),np.sqrt(a.get_value()*b.get_value())),
            color=(RED_C),
            opacity=0.5,
        )                   
        )
        
        A_autp = always_redraw(lambda:
        Polygon(
            ax.c2p(a.get_value(), 0),
            ax.c2p(a.get_value(), graph.underlying_function(a.get_value())),
            ax.c2p(np.sqrt(a.get_value()*b.get_value()), graph.underlying_function(np.sqrt(a.get_value()*b.get_value()))),
            ax.c2p(np.sqrt(a.get_value()*b.get_value()), 0),
            color = TEAL_D,
            fill_color = TEAL_D,
            fill_opacity=0.5
        )
        )

        A_abcd = always_redraw(lambda:
        Polygon(
            ax.c2p(a.get_value(), 0),
            ax.c2p(b.get_value(), 0),
            ax.c2p(b.get_value(), graph.underlying_function(np.sqrt(a.get_value()*b.get_value()))),
            ax.c2p(a.get_value(), graph.underlying_function(np.sqrt(a.get_value()*b.get_value()))),
            color = PURPLE_C,
            fill_color = PURPLE_C,
            fill_opacity=0.5
        )
        )
        A_abqx = always_redraw(lambda:
        Polygon(
            ax.c2p(a.get_value(), 0),
            ax.c2p(b.get_value(), 0),
            ax.c2p(b.get_value(), graph.underlying_function(b.get_value())),
            ax.c2p(a.get_value(), graph.underlying_function(b.get_value())),
            color = MAROON_C,
            fill_color = MAROON_C,
            fill_opacity=0.5
        )
        )
        A_abqp = always_redraw(lambda:
        Polygon(
            ax.c2p(a.get_value(), 0),
            ax.c2p(b.get_value(), 0),
            ax.c2p(b.get_value(), graph.underlying_function(b.get_value())),
            ax.c2p(a.get_value(), graph.underlying_function(a.get_value())),
            color = GOLD_C,
            fill_color = GOLD_C,
            fill_opacity=0.5
        )
        )
        A_abyp = always_redraw(lambda:
        Polygon(
            ax.c2p(a.get_value(), 0),
            ax.c2p(b.get_value(), 0),
            ax.c2p(b.get_value(), graph.underlying_function(a.get_value())),
            ax.c2p(a.get_value(), graph.underlying_function(a.get_value())),
            color = YELLOW_C,
            fill_color = YELLOW_C,
            fill_opacity=0.5
        )
        )
        A_abmn = always_redraw(lambda:
        Polygon(
            ax.c2p(a.get_value(), 0),
            ax.c2p(b.get_value(), 0),
            ax.c2p(b.get_value(), graph.underlying_function((a.get_value()+b.get_value())/2)),
            ax.c2p(a.get_value(), graph.underlying_function((a.get_value()+b.get_value())/2)),
            color = ORANGE,
            fill_color = ORANGE,
            fill_opacity=0.5
        )
        )

        #text
        tex1 = Tex(r'$A_{1}$', r'$>$', r'$A_{2}$').scale(0.7).shift(RIGHT * 3).to_edge(UP * 2)
        abfe = Tex(r'$\frac{2}{a+b}\cdot (b-a)$', color=GREEN_C).scale(0.7).move_to(tex1[2]).shift(0.9* RIGHT)
        abqp_c = VGroup(
            Tex(r'$\int_{a}^{b}\frac{1}{x}dx$', color= BLUE_C).scale(0.7).move_to(tex1[0]).shift(0.5 * LEFT),
            Tex(r'$\ln b-\ln a$', color= BLUE_C).scale(0.7).move_to(tex1[0]).shift(0.6 * LEFT)
        )

        tex2 = Tex(r'$A_{3}$', r'$=$', r'$\int_{a}^{\sqrt{ab}}\frac{1}{x}dx$').scale(0.7).next_to(tex1, DOWN * 1.8)
        tex2_1 = Tex(r'$\frac{1}{2}$', r'$A_{1}$').scale(0.7).next_to(tex1, DOWN * 2)
        autp_c = VGroup(
            Tex(r'$\ln\sqrt{ab}-\ln a$', color= RED_C).scale(0.7).move_to(tex2[2]).shift(0.5* RIGHT),
            Tex(r'$\frac{1}{2}\ln b-\ln a$', color= RED_C).scale(0.7).move_to(tex2[2]).shift(0.2* RIGHT)
        )
        
        tex3 = Tex(r'$A_{4}$', r'$=$', r'$\frac{1}{2}$', r'$A_{5}$').scale(0.7).next_to(tex2, DOWN * 1.8)
        autp = Tex(r'$\frac{1}{2}(\frac{1}{a}+\frac{1}{\sqrt{ab}})\sqrt{ab}-a$', color= TEAL_D).scale(0.7).shift(LEFT *2 + UP*3)
        autp_1 = Tex(r'$\frac{1}{2}\cdot$', r'$\frac{b-a}{\sqrt{ab}}$', color= TEAL_D).scale(0.7).move_to(autp)
        abcd = Tex(r'$\frac{b-a}{\sqrt{ab}}$', color= PURPLE_C).scale(0.7).next_to(autp, DOWN * 1.8)

        tex4 = Tex(r'$A_{3}$', r'$<$', r'$A_{4}$').scale(0.7).next_to(tex3, DOWN * 1.8)
        autp_2 = Tex(r'$\frac{b-a}{\sqrt{ab}}$', color=PURPLE_C).scale(0.7).move_to(tex4[2]).shift(0.2 * RIGHT)
        autp_c_1 = Tex(r'$\ln b-\ln a$', color= BLUE_C).scale(0.7).move_to(tex4[0]).shift(0.5 * LEFT)

        tex1[0].set_color(BLUE_C), tex1[2].set_color(GREEN_C)
        tex2[0].set_color(RED_C), tex2[2].set_color(RED_C)
        tex2_1[1].set_color(BLUE_C)
        tex3[0].set_color(TEAL_D), tex3[3].set_color(PURPLE_C),
        tex4[0].set_color(RED_C), tex4[2].set_color(TEAL_D)

        
        

        tex5 = Tex(r'$A_{6}$', r'$<$', r'$A_{1}$', r'$<$', r'$A_{7}$', r'$<$', r'$A_{8}$').scale(0.7).next_to(tex4, DOWN * 4)
        tex6 = Tex(r'$\frac{1}{b}(b-a)$', r'$<$', r'$\ln b-\ln a$', r'$<$', r'$\frac{1}{2}(\frac{1}{a}+\frac{1}{b})(b-a)$', r'$<$', r'$\frac{1}{a}(b-a)$').scale(0.7).next_to(tex5, DOWN * 3)
        tex5[0].set_color(MAROON_C), tex5[2].set_color(BLUE_C),
        tex5[4].set_color(GOLD_C), tex5[6].set_color(YELLOW_C),

        tex6[0].set_color(MAROON_C), tex6[2].set_color(BLUE_C),
        tex6[4].set_color(GOLD_C), tex6[6].set_color(YELLOW_C), 

        abmn = Tex(r'$\frac{2(b+a)}{a+b}$', color= ORANGE).scale(0.7).shift(LEFT *2 + UP*1)

        

        #animation
        self.wait()
        self.play(Create(ax), Create(graph))
        self.wait()
        self.play(Write(dot_a), Write(dot_b))
        self.play(Create(l_ap), Create(l_bq))
        self.wait()
        self.play(Write(dot_ab))
        self.play(Write(dot_fab))
        self.play(Create(l_abt), Create(l_fabk))
        self.wait()
        self.play(Create(line1))
        self.play(Write(dot_e), Write(dot_f))
        self.wait()
        self.play(Write(dot_y))
        self.play(Create(l_yb), Create(l_yp))
        self.wait()
        self.play(Create(l_cd), Create(l_mn), Create(l_qx))
        self.wait()
        self.play(Create(l_pt), Create(l_pq))
        
        #inequa 1
        self.wait()
        self.play(FadeIn(A_abqp_c))
        self.wait()
        self.play(TransformFromCopy(A_abqp_c, tex1[0]))
        self.wait()
        self.play(FadeIn(A_abfe))
        self.wait()
        self.play(TransformFromCopy(A_abfe, tex1[2]))
        period()
        self.wait(0.5)
        self.play(Write(tex1[1]))
        self.wait()
        self.play(Transform(tex1[0], abqp_c[0]), Transform(tex1[2], abfe))
        self.wait()
        self.play(Transform(tex1[0], abqp_c[1]))
        

        #autp_c and abqp
        self.wait()
        self.play(FadeIn(A_autp_c))
        self.wait()
        self.play(TransformFromCopy(A_autp_c, tex2[0]))
        self.wait()
        self.play(Write(tex2[1]), Write(tex2[2]))
        self.wait()
        self.play(Transform(tex2[2], autp_c[0]))
        self.wait()
        self.play(Transform(tex2[2], autp_c[1]))
        self.wait()
        self.play(Transform(tex2[2], tex2_1))

        #autp
        self.wait()
        self.play(FadeIn(A_autp))
        self.wait()
        self.play(TransformFromCopy(A_autp, tex3[0]))
        self.play(Write(autp))
        self.play(Transform(autp, autp_1))
        self.wait()
        self.play(FadeIn(A_abcd))
        self.wait()
        self.play(TransformFromCopy(A_abcd, abcd))
        self.wait()
        self.play(Write(tex3[1]), Write(tex3[2]), Write(tex3[3]))
        self.play(FadeOut(autp), FadeOut(abcd), FadeOut(A_abcd))

        #autp_c<autp => inb- ina <
        self.wait()
        self.play(TransformFromCopy(A_autp_c, tex4[0]))
        self.wait(0.5)
        self.play(TransformFromCopy(A_autp, tex4[2]))
        period()
        self.wait(0.5)
        self.play(Write(tex4[1]))
        self.wait()
        self.play(Transform(tex4[0], autp_c_1), Transform(tex4[2], autp_2))

        #abqx<abqp_c<abqp<abyp
        self.wait()
        self.play(FadeOut(A_abfe), FadeOut(A_abcd), FadeOut(A_abmn), FadeOut(A_autp), FadeOut(A_autp_c))
        self.play(FadeIn(A_abqx))
        self.wait()
        self.play(TransformFromCopy(A_abqx, tex5[0]))
        self.play(FadeIn(A_abqp_c))
        self.wait()
        self.play(TransformFromCopy(A_abqp_c, tex5[2]))
        self.play(FadeIn(A_abqp))
        self.wait()
        self.play(TransformFromCopy(A_abqp, tex5[4]))
        self.play(FadeIn(A_abyp))
        self.wait()
        self.play(TransformFromCopy(A_abyp, tex5[6]))
        self.play(FadeOut(A_abyp))
        
        period()
        self.wait()
        self.play(Write(tex5[1]), Write(tex5[3]), Write(tex5[5]))
        self.wait()
        self.play(TransformFromCopy(tex5, tex6))
        self.wait()
        self.play(FadeIn(A_abmn))
        self.play(TransformFromCopy(A_abmn, abmn))
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

        tex7 = Tex(r'$\frac{1}{b}(b-a)<\frac{2(b+a)}{a+b}<\ln b-\ln a<\frac{b-a}{\sqrt{ab}}<\frac{1}{2}(\frac{1}{a}+\frac{1}{b})(b-a)<\frac{1}{a}(b-a)$').scale(0.5).next_to(tex6, DOWN * 2.8)

       

        tex8 = Tex(r'$Divide by (b-a): \frac{1}{b}<\frac{2(b+a)}{(a+b)(b-a)}<\frac{b-a}{\ln b-\ln a}<\frac{1}{\sqrt{ab}}<\frac{1}{2}(\frac{1}{a}+\frac{1}{b})<\frac{1}{a}$').scale(0.5).next_to(tex7, DOWN * 1.8)



        tex9 = Tex(r'$b>\frac{a+b}{2}>\frac{b-a}{\ln b-\ln a}>\sqrt{ab}>\frac{2}{\frac{1}{a} + \frac{1}{b}}>ab>a>0$'
        ).scale(0.5).next_to(tex7, DOWN * 1.8)

        self.wait(2)
        self.play(Write(tex7.move_to(ORIGIN)))
        self.wait(3)
        self.play(Write(tex8.next_to(tex7, DOWN*1.8)))
        self.wait(3)
        self.play(Write(tex9.next_to(tex8, DOWN*1.8)))
        self.wait(3)