from tkinter import *

janela = Tk()

lb1 = Label(janela, text="Login: ")
lb2 = Label(janela, text="Senha: ")

ed1 = Entry(janela,)
ed2 = Entry(janela,)

bt = Button(janela, text="confirmar")

lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0)
ed1.grid(row=0, column=1)
ed2.grid(row=1, column=1)
bt.grid(row=2, column=1)


janela.geometry("200x200+200+200")
janela.mainloop()