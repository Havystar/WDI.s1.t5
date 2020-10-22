import tkinter as tk
from functools import partial

window = tk.Tk()
window.geometry('400x100')
window.title('Temperature Converter')
window.grid_columnconfigure(1, weight=1)

fromWhat = "Celsius"
inputNumber = tk.DoubleVar()
default = tk.StringVar()


def changeType(set_temp):
    global fromWhat
    fromWhat = set_temp


def convert(output, inputn):
    temp = inputn.get()
    if fromWhat == 'Celsius':
        fahrenheit = float((float(temp) * 9 / 5) + 32)
        output.config(text="%.1f Fahrenheit" % fahrenheit)
    if fromWhat == 'Fahrenheit':
        celsius = float((float(temp) - 32) * 5 / 9)
        output.config(text="%.1f Celsius" % celsius)
    return


inputDescription = tk.Label(window, text="Wpisz temperaturę")
inputTemperature = tk.Entry(window, textvariable=inputNumber)
inputDescription.grid(row=1)
inputTemperature.grid(row=1, column=1)
output = tk.Label(window)
output.grid(row=3, columnspan=4)

dropDownList = ["Celsius", "Fahrenheit"]
drop_down = tk.OptionMenu(window, default, *dropDownList, command=changeType)
default.set(dropDownList[0])
drop_down.grid(row=1, column=2)

convert = partial(convert, output, inputNumber)
submit = tk.Button(window, text="Convert", command=convert)
submit.grid(row=2, columnspan=1)

window.mainloop()
