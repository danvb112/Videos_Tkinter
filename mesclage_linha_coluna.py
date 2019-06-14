from tkinter import *

janela = Tk()

lb1 = Label(janela, width=15, bg="blue" )
lb2 = Label(janela, width=15, bg="yellow")
lb3 = Label(janela, width=15,  bg="red")
lb4 = Label(janela, width=15, bg="black")
lb5 = Label(janela, width=15,  bg="green")
lb6 = Label(janela, width=15, bg="pink")

lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0)
lb3.grid(row=0, column=1)
lb4.grid(row=1, column=1)

lb5.grid(row=2, column=0, columnspan=2, sticky=W+E)
lb6.grid(row=0, column=2, rowspan=2, sticky=N+S)


janela.geometry("400x400+200+200")
janela.mainloop()