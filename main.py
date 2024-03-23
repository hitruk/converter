
import tkinter as tk
from tkinter.constants import *
from tkinter import ttk


class Model:
    def __init__(self, value):
        # допустимые значения:
        # 0, float, int, отрицатеельные значения
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, x):
        if type(x) in [int, float]:
            self._value = x
        else:
            raise TypeError(f'invalid data type: {x}')

    def mi_to_km(self):
        #  ф-ция конвертирует милли в километры 
        mi = self._value*1.609344
        return mi


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Hello world')
        self.geometry('400x300')
        # self.resizable(False, False)



if __name__ == '__main__':
    app = App()
    app.mainloop()
