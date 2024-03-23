
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
            raise TypeError(f'invalid data type: {type(x)}')

    def mi_to_km(self):
        #  ф-ция конвертирует милли в километры 
        mi = self._value*1.609344
        return mi

class View(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self['borderwidth'] = 1
        self['relief'] = SOLID
        self.pack(padx=2, pady=2, fill=BOTH, expand=True)

        # contant
        options = {'padx':2, 'pady':2, 'anchor': W}

        # CONVERT LABEL
        self.title_label = ttk.Label(self, text='Converter: miles to kilometers')
        self.title_label.pack(**options)

        # ENTRY
        self.type_entry = tk.StringVar(value=0) 
        self.entry = ttk.Entry(self, textvariable=self.type_entry)
        self.entry.pack(**options)

        # BUTTON
        self.button = ttk.Button(self, text='Click', command=self.click_button)
        self.button.pack(**options)

        # CONVERT LABEL
        self.convert_label = ttk.Label(self, text='1 миля = 1.609344 километров.')
        self.convert_label.pack(**options)

        # RESULT LABEL
        self.result_label = ttk.Label(self, text='Result')
        self.result_label.pack(**options)

        # set controller
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def click_button(self):
        if self.controller:
            try:
                entry_value = float(self.type_entry.get())
                self.controller.converter(entry_value)
            except Exception:
                self.show_error(error='ValueError:',  message='Некорректное значение!')

    def show_error(self, error, message):
        self.result_label['text'] = f'{error} {message}'
        self.result_label['foreground'] = 'red'
        self.entry['foreground'] = 'red'
   

    def show_result(self, message, x):
        self.convert_label['text'] = f'Convert: {x} mill to km'
        self.result_label['text'] = f'Result : {message} km'
        self.result_label['foreground'] = 'black'
        self.entry['foreground'] = 'black'
    

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view


    def converter(self, x):
        try:
            self.model.value = x
            res = self.model.mi_to_km()
            self.view.show_result(res, x)
        except TypeError as error:
            self.view.show_error('TypeError', error)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Hello world')
        self.geometry('400x300')
        # self.resizable(False, False)

        model = Model(10)
        view = View(self)

        controller = Controller(model, view)
        view.set_controller(controller)

if __name__ == '__main__':
    app = App()
    # view = View(app)
    app.mainloop()
