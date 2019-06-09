from tkinter import *

janela = Tk()

lb1 = Label(janela, text= "label 1", bg= "blue")
lb2 = Label(janela, text= "label 2", bg= "yellow")
lb3 = Label(janela, text= "label 3", bg="red")
lb4 = Label(janela, text= "label 4", bg="brown")

lb1.pack(side=TOP)
lb2.pack(side=LEFT)
lb3.pack(side=RIGHT)
lb4.pack(side=BOTTOM)


janela.geometry("400x400+200+200")
janela.mainloop()


