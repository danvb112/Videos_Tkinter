from tkinter import *

janela = Tk()

lb1 = Label(janela, text="Label 1", bg="blue")
lb2 = Label(janela, text="Label 2", bg="yellow")
lb3 = Label(janela, text="Label 3", bg="brown")
lb4 = Label(janela, text="Label 4", bg="red")

lb1.pack(side=TOP, fill=BOTH, expand=1)
lb2.pack(side=TOP, fill=BOTH, expand=1)
lb3.pack(side=TOP, fill=BOTH, expand=1)
lb4.pack(side=TOP, fill=BOTH, expand=1)

janela.geometry("400x400+200+200")
janela.mainloop()