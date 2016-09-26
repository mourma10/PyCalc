try:
    from .__init__ import *
except ImportError:
    pass


class Analyseur:
    def __init__(self):
        self.operation = self.expression = self.res = str()
        self.lenght_expression = 0

    # ******************************
    # Analyse de l'expression      *
    # saisie par l'utilisateur     *
    # ******************************

    def eval_expression(self, root, text):
        self.expression += str(text)

        # ****************************
        # Passage en Mode Scientific *
        # ****************************
        if text == "Sc":
            self.expression = self.expression.replace("Sc", "")
            self.lenght_expression -= 2
            root.changerootmode(600, "PyCalc - Scientific Mode ", "Scientific")

        # **********************
        # Retour en Mode Basic *
        # **********************
        if text == "Bc":
            self.expression = self.expression.replace("Bc", "")
            root.changerootmode(300, "PyCalc - Basic Mode ", "Basic")

        # ***************************
        # Effacer la zone de saisie *
        # ***************************
        if text == "C":
            self.expression = ""
            self.lenght_expression = 0
            self.operation = ""

        # *******************
        # Retour en arriere *
        # *******************
        if text == "R":
            self.expression = self.expression[:len(self.expression) - 2]
            self.lenght_expression -= 2
            if self.expression == "":
                self.lenght_expression = 0

        # **********************************************
        # Si on appuie sur le bouton '=' ou sur        *
        # la touche'Entree'                            *
        # **********************************************
        if text == "=":
            try:
                self.expression = self.expression[:len(self.expression) - 1]
                textop = self.expression
                if self.expression != str():
                    trigo = ('cos', 'sin', 'tan')
                    if self.expression.__contains__('^'):
                        self.expression = self.expression.replace('^', '**')
                    for x in trigo:
                        if x in self.expression:
                            a = c = str()
                            if self.expression[self.expression.find(x, 1) - 1] != 'a':
                                self.expression = self.expression.replace(x, 'radians', 1)
                                ind = self.expression.find('radians(') + 8
                                a = 'radians('
                                while self.expression[ind] != ')':
                                    a += self.expression[ind]
                                    ind += 1
                                a += ')'
                                b = str(eval(a))
                                c = x + '(' + b + ')'
                            if self.expression[self.expression.find(x, 1) - 1] == 'a':
                                x = 'a' + x
                                ind = self.expression.find(x) + 5
                                a = x + '('
                                while self.expression[ind] != ')':
                                    a += self.expression[ind]
                                    ind += 1
                                a += ')'
                                b = str(eval(a))
                                c = 'degrees(' + b + ')'
                            self.expression = self.expression.replace(a, c)
                    self.res = self.calcul_expression()
                    self.operation = textop + " = " + self.res
                    self.expression = self.res
                    self.lenght_expression = len(self.expression)
                else:
                    self.lenght_expression = 0
            except TypeError:
                self.operation = "Erreur"

    # *******************************
    # Evaluation de l'expression    *
    # avec la fonction eval         *
    # *******************************

    def calcul_expression(self):
        try:
            return str(round(eval(self.expression), 7))
        except SyntaxError:
            self.operation = "Erreur"
        except ZeroDivisionError:
            self.operation = "Erreur"
        except NameError:
            self.operation = "Erreur"
