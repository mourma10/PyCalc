# -*-coding:UTF-8-*
try:
    from Tkinter import Button
except ImportError:
    from tkinter import Button

# **************************************
# Les Boutons sont encapsulés dans     *
# une classe a part                    *
# **************************************


class Buttons:
    def __init__(self, root):
        self.button_7 = Button(root.window, text="7", width=4, command=lambda: root.putzones("7"),
                               relief="flat", font="../font/myfont 9 bold", bg="#fff")
        self.button_8 = Button(root.window, text="8", width=4, command=lambda: root.putzones("8"),
                               relief="flat", font="../font/myfont 9 bold", bg="#fff")
        self.button_9 = Button(root.window, text="9", width=4, command=lambda: root.putzones("9"),
                               relief="flat", font="../font/myfont 9 bold", bg="#fff")
        self.button_4 = Button(root.window, text="4", width=4, command=lambda: root.putzones("4"),
                               relief="flat", font="../font/myfont 9 bold", bg="#fff")
        self.button_5 = Button(root.window, text="5", width=4, command=lambda: root.putzones("5"),
                               relief="flat", font="../font/myfont 9 bold", bg="#fff")
        self.button_6 = Button(root.window, text="6", width=4, command=lambda: root.putzones("6"),
                               relief="flat", font="../font/myfont 9 bold", bg="#fff")
        self.button_1 = Button(root.window, text="1", width=4, command=lambda: root.putzones("1"),
                               relief="flat", font="../font/myfont 9 bold", bg="#fff")
        self.button_2 = Button(root.window, text="2", width=4, command=lambda: root.putzones("2"),
                               relief="flat", font="../font/myfont 9 bold", bg="#fff")
        self.button_3 = Button(root.window, text="3", width=4, command=lambda: root.putzones("3"),
                               relief="flat", font="../font/myfont 9 bold", bg="#fff")
        self.button_0 = Button(root.window, text="0", width=4, command=lambda: root.putzones("0"),
                               relief="flat", font="../font/myfont 9 bold", bg="#fff")
        self.button_dot = Button(root.window, text=".", width=4,
                                 command=lambda: root.putzones("."), relief="flat",
                                 font="../font/myfont 9 bold", bg="#fff")
        self.button_per = Button(root.window, text="%", width=4,
                                 command=lambda: root.putzones("%"), relief="flat",
                                 font="../font/myfont 9 bold", bg="#fff")
        self.button_div = Button(root.window, text="/", width=4,
                                 command=lambda: root.putzones("/"), relief="flat",
                                 font="../font/myfont 9 bold", bg="#fff")
        self.button_c = Button(root.window, text="C", width=4, command=lambda: root.putzones("C"),
                               relief="flat", font="../font/myfont 9 bold", bg="#fff")
        self.button_r = Button(root.window, text="R", width=4, command=lambda: root.putzones("R"),
                               relief="flat", font="../font/myfont 9 bold", bg="#fff")
        self.button_mul = Button(root.window, text="*", width=4,
                                 command=lambda: root.putzones("*"), relief="flat",
                                 font="../font/myfont 9 bold", bg="#fff")
        self.button_paro = Button(root.window, text="(", width=4,
                                  command=lambda: root.putzones("("), relief="flat",
                                  font="../font/myfont 9 bold", bg="#fff")
        self.button_parf = Button(root.window, text=")", width=4,
                                  command=lambda: root.putzones(")"), relief="flat",
                                  font="../font/myfont 9 bold", bg="#fff")
        self.button_moins = Button(root.window, text="-", width=4,
                                   command=lambda: root.putzones("-"), relief="flat",
                                   font="../font/myfont 9 bold", bg="#fff")
        self.button_pow = Button(root.window, text="x^", width=4,
                                 command=lambda: root.putzones("^"), relief="flat",
                                 font="../font/myfont 9 bold", bg="#fff")
        self.button_sqrt = Button(root.window, text="Rac", width=4, command="", relief="flat",
                                  font="../font/myfont 9 bold", bg="#fff")
        self.button_plus = Button(root.window, text="+", width=4,
                                  command=lambda: root.putzones("+"), relief="flat",
                                  font="../font/myfont 9 bold", bg="#fff")
        self.button_egal = Button(root.window, text="=", width=9,
                                  command=lambda: root.putzones("="), relief="flat",
                                  font="../font/myfont 9 bold", bg="#fff")
        self.button_modebasic = Button(root.window, text="Bc", width=4,
                                       command=lambda: root.putzones("Bc"), relief="flat",
                                       font="../font/myfont 9 bold", bg="#fff")
        self.button_modescience = Button(root.window, text="Sc", width=4,
                                         command=lambda: root.putzones("Sc"), relief="flat",
                                         font="../font/myfont 9 bold", bg="#fff")
        self.button_cos = Button(root.window, text="cos", width=4,
                                 command=lambda: root.putzones("cos"), relief="flat",
                                 font="../font/myfont 9 bold", bg="#fff")
        self.button_sin = Button(root.window, text="sin", width=4,
                                 command=lambda: root.putzones("sin"), relief="flat",
                                 font="../font/myfont 9 bold", bg="#fff")
        self.button_tan = Button(root.window, text="tan", width=9,
                                 command=lambda: root.putzones("tan"), relief="flat",
                                 font="../font/myfont 9 bold", bg="#fff")
        self.button_acos = Button(root.window, text="acos", width=4,
                                  command=lambda: root.putzones("acos"), relief="flat",
                                  font="../font/myfont 9 bold", bg="#fff")
        self.button_asin = Button(root.window, text="asin", width=4,
                                  command=lambda: root.putzones("asin"), relief="flat",
                                  font="../font/myfont 9 bold", bg="#fff")
        self.button_atan = Button(root.window, text="atan", width=9,
                                  command=lambda: root.putzones("atan"), relief="flat",
                                  font="../font/myfont 9 bold", bg="#fff")
        self.button_cosh = Button(root.window, text="cosh", width=4,
                                  command=lambda: root.putzones("cosh"), relief="flat",
                                  font="../font/myfont 9 bold", bg="#fff")
        self.button_sinh = Button(root.window, text="sinh", width=4,
                                  command=lambda: root.putzones("sinh"), relief="flat",
                                  font="../font/myfont 9 bold", bg="#fff")
        self.button_tanh = Button(root.window, text="tanh", width=4,
                                  command=lambda: root.putzones("tanh"), relief="flat",
                                  font="../font/myfont 9 bold", bg="#fff")
        self.button_exp = Button(root.window, text="exp", width=9,
                                 command=lambda: root.putzones("exp"), relief="flat",
                                 font="../font/myfont 9 bold", bg="#fff")
        self.button_log = Button(root.window, text="log", width=9,
                                 command=lambda: root.putzones("log"), relief="flat",
                                 font="../font/myfont 9 bold", bg="#fff")
        self.button_ln = Button(root.window, text="ln", width=4,
                                command=lambda: root.putzones("ln"), relief="flat",
                                font="../font/myfont 9 bold", bg="#fff")
        self.button_pi = Button(root.window, text="pi", width=9,
                                command=lambda: root.putzones("pi"), relief="flat",
                                font="../font/myfont 9 bold", bg="#fff")
        self.button_fact = Button(root.window, text="x!", width=9,
                                  command=lambda: root.putzones("!"), relief="flat",
                                  font="../font/myfont 9 bold", bg="#fff")
        self.button_abs = Button(root.window, text="|x|", width=9,
                                 command=lambda: root.putzones("abs"), relief="flat",
                                 font="../font/myfont 9 bold", bg="#fff")
        self.button_e = Button(root.window, text="e", width=9,
                               command=lambda: root.putzones("e"), relief="flat",
                               font="../font/myfont 9 bold", bg="#fff")

    # **********************************************
    # Boutons qui seront affiches en mode basique  *
    # **********************************************

    def buttons_basic(self, root):
        root.canvas.create_window(25, 170, window=self.button_7)
        root.canvas.create_window(75, 170, window=self.button_8)
        root.canvas.create_window(125, 170, window=self.button_9)
        root.canvas.create_window(175, 170, window=self.button_div)
        root.canvas.create_window(225, 170, window=self.button_c)
        root.canvas.create_window(275, 170, window=self.button_r)
        root.canvas.create_window(25, 210, window=self.button_4)
        root.canvas.create_window(75, 210, window=self.button_5)
        root.canvas.create_window(125, 210, window=self.button_6)
        root.canvas.create_window(175, 210, window=self.button_mul)
        root.canvas.create_window(225, 210, window=self.button_paro)
        root.canvas.create_window(275, 210, window=self.button_parf)
        root.canvas.create_window(25, 250, window=self.button_1)
        root.canvas.create_window(75, 250, window=self.button_2)
        root.canvas.create_window(125, 250, window=self.button_3)
        root.canvas.create_window(175, 250, window=self.button_moins)
        root.canvas.create_window(225, 250, window=self.button_pow)
        root.canvas.create_window(275, 250, window=self.button_sqrt)
        root.canvas.create_window(25, 290, window=self.button_0)
        root.canvas.create_window(75, 290, window=self.button_dot)
        root.canvas.create_window(125, 290, window=self.button_per)
        root.canvas.create_window(175, 290, window=self.button_plus)
        root.canvas.create_window(250, 290, window=self.button_egal)
        root.canvas.pack()

    # ***********************************************************
    # Boutons qui seront affiches en plus en mode scientifique  *
    # ***********************************************************

    def buttons_science(self, root):
        self.buttons_basic(root)
        root.canvas.create_window(325, 170, window=self.button_cos)
        root.canvas.create_window(375, 170, window=self.button_sin)
        root.canvas.create_window(450, 170, window=self.button_tan)
        root.canvas.create_window(325, 210, window=self.button_acos)
        root.canvas.create_window(375, 210, window=self.button_asin)
        root.canvas.create_window(450, 210, window=self.button_atan)
        root.canvas.create_window(325, 250, window=self.button_cosh)
        root.canvas.create_window(375, 250, window=self.button_sinh)
        root.canvas.create_window(425, 250, window=self.button_tanh)
        root.canvas.create_window(550, 210, window=self.button_exp)
        root.canvas.create_window(500, 250, window=self.button_log)
        root.canvas.create_window(575, 250, window=self.button_ln)
        root.canvas.create_window(450, 290, window=self.button_fact)
        root.canvas.create_window(550, 290, window=self.button_pi)
        root.canvas.create_window(550, 170, window=self.button_abs)
        root.canvas.create_window(350, 290, window=self.button_e)
        root.canvas.pack()
