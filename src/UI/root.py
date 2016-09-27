# -*-coding:UTF-8-*

from .__init__ import *
from .buttons import *

# **********************************************
# Dans cette classe Root on gere tout ce qui   *
# est relatif a la fenetre de la calculatrice  *
# **********************************************


class Root:
    def __init__(self):
        self.dimx = 300
        self.dimy = 310
        self.window = Tk()
        self.canvas = Canvas(self.window, width=self.dimx * 2, height=self.dimy, bg="#edd")
        self.window.focus_set()
        self.window.bind("<KeyPress>", self.keyboard_event)
        self.window.title("Pycalc - Basic Mode")
        self.window.resizable(False, False)
        self.center(self)
        self.zone_saisieop = self.zone_result = ""
        self.analyseur = Analyseur()
        self.putzones("")
        self.buttons = Buttons(self)
        self.buttons.buttons_basic(self)
        self.canvas.create_window(25, 135, window=self.buttons.button_modescience)

    # *********************
    # Centrer la fenetre  *
    # *********************
    @staticmethod
    def center(root):
        w_ = root.window.winfo_screenwidth()
        h = root.window.winfo_screenheight()
        x = w_ / 2 - root.dimx / 2
        y = h / 2 - root.dimy / 2
        root.window.geometry("%dx%d+%d+%d" % ((root.dimx, root.dimy) + (x, y)))

    # *****************************************************
    # Gestion de la saisie et des zones                   *
    # d'affichages de la calculatrice.                    *                                       *
    # *****************************************************
    def putzones(self, text):
        self.analyseur.eval_expression(self, text)
        self.zone_result = Button(self.window, command="", width=140, relief="flat", bg="#edd",
                                  text=self.analyseur.operation,
                                  font="../font/myfont 13 bold", activebackground="#edd")
        self.zone_saisieop = Button(self.window, command="", width=120, relief="flat", bg="#fff",
                                    text=self.analyseur.expression, font="../font.myfont 15",
                                    activebackground="#fff")
        self.canvas.create_window(5 * len(self.analyseur.operation), 15, window=self.zone_result)
        self.canvas.create_window((self.dimx - 20) - 6 * self.analyseur.lenght_expression, 95,
                                  window=self.zone_saisieop)
        self.analyseur.lenght_expression += 1
        self.canvas.pack()

    # ******************************************
    # Redimensionnement de la fenetre          *
    # suivant le mode basique ou scientifique  *
    # ******************************************
    def changerootmode(self, dimx, title, button_mode):
        self.canvas.delete("all")
        self.dimx = dimx
        self.center(self)
        self.window.title(title)
        if button_mode == "Basic":
            self.canvas.create_window(25, 135, window=self.buttons.button_modescience)
            self.buttons.buttons_basic(self)
        elif button_mode == "Scientific":
            self.canvas.create_window(25, 135, window=self.buttons.button_modebasic)
            self.buttons.buttons_science(self)

    # ***********************************
    # Gestion des evenements            *
    # du clavier                        *
    # ***********************************
    def keyboard_event(self, event):
        key = str()
        number = "1234567890"
        alpha = "abcdefghijklmnopqrstuvwxyz"
        operateurs = ('plus', 'minus', 'asterisk', 'slash', 'parenleft', 'parenright', 'percent',
                      'asciicircum', 'greater')
        operateurs_sign = ('+', '-', '*', '/', '(', ')', '%', '^', '.')
        if operateurs.__contains__(event.keysym):
            key = operateurs_sign[operateurs.index(event.keysym)]
        if number.__contains__(event.keysym):
            key = number[number.find(event.keysym)]
        if alpha.__contains__(event.keysym):
            key = alpha[alpha.find(event.keysym)]
        if event.keysym == "Return":
            key = '='
        if event.keysym == "BackSpace":
            key = 'R'
        if key != str():
            self.putzones(key)
