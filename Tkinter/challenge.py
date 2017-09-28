#write a gui app to create a simple calculator.
import tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Calculator")
mainWindow.geometry('640x480-8-200')
mainWindowPadding = 8
mainWindow['padx'] = mainWindowPadding

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)
mainWindow.columnconfigure(3, weight=1)
mainWindow.columnconfigure(4, weight=1)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=1)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=1)
mainWindow.rowconfigure(4, weight=1)
mainWindow.rowconfigure(5, weight=1)

result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky='nsew')

buttonConfig = [
    [('C', 1), ('CE', 1)],
    [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
    [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
    [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
    [('0', 1), ('=', 2), ('/', 1)]
]

keyPad = tkinter.Frame(mainWindow)
keyPad.grid(row=1, column=0, sticky='nsew')

keyPadding = 6

row = 0
for keyRow in buttonConfig:
    col = 0
    for buttonInfo in keyRow:
        label, columnSpan = buttonInfo
        button = tkinter.Button(keyPad, text=label, padx = keyPadding)
        button.grid(row=row, column=col, columnspan=columnSpan, sticky=tkinter.E + tkinter.W)
        col += columnSpan
    row += 1

mainWindow.update()

mainWindow.minsize(keyPad.winfo_width() + mainWindowPadding, result.winfo_height() + keyPad.winfo_height())
mainWindow.maxsize(keyPad.winfo_width() + 50 + mainWindowPadding, result.winfo_height() + 50 + keyPad.winfo_height())
mainWindow.mainloop()
