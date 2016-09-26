try:
    from Tkinter import Tk, Canvas, Button
except ImportError:
    from tkinter import Tk, Canvas, Button
finally:
    from src.Analyseur.analyseur import Analyseur
