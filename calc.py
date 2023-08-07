from tkinter import *
from tkinter import ttk

cor1 = "#feffff" #white/branca
cor2 = "#40E51F"
cor3 = "#691EE4"
cor4 = "#11C68B"

fundo = "#3b3b3b" #fundo/preto

janela = Tk()
janela.geometry("400x500")
janela.title("Calculadora")
janela.config(bg=cor4)
photo = PhotoImage(file="calculator.png")
janela.wm_iconphoto(False, photo)

#------------------------------------FRAMES---------------------------------------------------------------

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=280)

frame_tela = Frame(janela, width=400, height=56, bg=cor2, pady=0, padx=0, relief=FLAT)
frame_tela.grid(row=1, column=0, sticky=NW)

frame_quadros = Frame(janela, width=400, height=500, bg=cor2, pady=0, padx=0, relief=FLAT)
frame_quadros.grid(row=2, column=0, sticky=NW)

#------------------------------------------FUNÇOES---------------------------------------------------------

#Armazenar expressões que serão avaliadas
all_values = ""

text_value = StringVar()

#-----------------------------------------------FUNÇÕES-----------------------------------

def entrar_valor(event):
    global all_values

    all_values = all_values + str(event)

    #passar valores para a tela
    text_value.set(all_values)


def calcular():
    global all_values
    resultado = str(eval(all_values))
    text_value.set(resultado)
    all_values = " "

#------------função de limpar tela--------------------------

def limpar_tela():
    global all_values
    all_values = " "
    text_value.set("")

#-------------------------Labels-------------------------------------------------------

app_label = Label(frame_tela, text='123456789', width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18 bold'))
app_label.place(x=15, y=9)



#----------------------------------BOTÕES-----------------------------------------------------------

#Primeira Linha
b_1 = Button(frame_quadros, text="C", width=19, height=4, bg=cor3, fg=cor1, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_quadros, text="%", width=9, height=4, bg=cor3, fg=cor1, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_2.place(x=200, y=0)

b_3 = Button(frame_quadros, text="/", width=9, height=4, bg=cor4, fg=fundo, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_3.place(x=300, y=0)

#Segunda Linha
b_4 = Button(frame_quadros, text="7", width=9, height=4, bg=cor3, fg=cor1, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_4.place(x=0, y=90)

b_5 = Button(frame_quadros, text="8", width=9, height=4, bg=cor3, fg=cor1, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_5.place(x=100, y=90)

b_6 = Button(frame_quadros, text="9", width=9, height=4, bg=cor3, fg=cor1, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_6.place(x=200, y=90)

b_7 = Button(frame_quadros, text="*", width=9, height=4, bg=cor4, fg=fundo, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_7.place(x=300, y=90)

#Terceira Linha
b_8 = Button(frame_quadros, text="4", width=9, height=4, bg=cor3, fg=cor1, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_8.place(x=0, y=180)

b_9 = Button(frame_quadros, text="5", width=9, height=4, bg=cor3, fg=cor1, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_9.place(x=100, y=180)

b_10 = Button(frame_quadros, text="6", width=9, height=4, bg=cor3, fg=cor1, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_10.place(x=200, y=180)

b_11= Button(frame_quadros, text="-", width=9, height=4, bg=cor4, fg=fundo, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_11.place(x=300, y=180)

#Quarta Linha
b_12 = Button(frame_quadros, text="1", width=9, height=4, bg=cor3, fg=cor1, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_12.place(x=0, y=270)

b_13 = Button(frame_quadros, text="2", width=9, height=4, bg=cor3, fg=cor1, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_13.place(x=100, y=270)

b_14 = Button(frame_quadros, text="3", width=9, height=4, bg=cor3, fg=cor1, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_14.place(x=200, y=270)

b_15 = Button(frame_quadros, text="+", width=9, height=4, bg=cor4, fg=fundo, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_15.place(x=300, y=270)

#Quinta Linha
b_16 = Button(frame_quadros, text="0", width=19, height=4, bg=cor3, fg=cor1, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_16.place(x=0, y=360)

b_17= Button(frame_quadros, text=".", width=9, height=4, bg=cor3, fg=cor1, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_17.place(x=200, y=360)

b_18= Button(frame_quadros, text="=", width=9, height=4, bg=cor4, fg=fundo, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_18.place(x=300, y=360)

app_scream = Label(frame_tela,textvariable=text_value,width=28,height=2, padx=7, relief=FLAT, anchor='e', bd=0, justify=RIGHT,font=('Ivy 18'), bg="#37474F",fg=cor1)
app_scream.place(x=0,y=0)

# ----------------------------------------------- Copiar novamente usando lambda para cada botão para que todos funcionem de acordo com as funções apresentadas-----------------------------------
#Primeira Linha
b_1 = Button(frame_quadros,command= lambda: limpar_tela(), text="C", width=19, height=4, bg=cor3, fg=cor1, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_quadros,command=lambda: entrar_valor("%"),text="%", width=9, height=4, bg=cor3, fg=cor1, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_2.place(x=200, y=0)

b_3 = Button(frame_quadros,command=lambda: entrar_valor("/"), text="/", width=9, height=4, bg=cor4, fg=fundo, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_3.place(x=300, y=0)

#Segunda Linha
b_4 = Button(frame_quadros,command=lambda: entrar_valor("7"), text="7", width=9, height=4, bg=cor3, fg=cor1, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_4.place(x=0, y=90)

b_5 = Button(frame_quadros,command=lambda: entrar_valor("8"), text="8", width=9, height=4, bg=cor3, fg=cor1, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_5.place(x=100, y=90)

b_6 = Button(frame_quadros,command=lambda: entrar_valor("9"), text="9", width=9, height=4, bg=cor3, fg=cor1, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_6.place(x=200, y=90)

b_7 = Button(frame_quadros,command=lambda: entrar_valor("*"), text="*", width=9, height=4, bg=cor4, fg=fundo, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_7.place(x=300, y=90)

#Terceira Linha
b_8 = Button(frame_quadros,command=lambda: entrar_valor("4"), text="4", width=9, height=4, bg=cor3, fg=cor1, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_8.place(x=0, y=180)

b_9 = Button(frame_quadros,command=lambda: entrar_valor("5"), text="5", width=9, height=4, bg=cor3, fg=cor1, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_9.place(x=100, y=180)

b_10 = Button(frame_quadros,command=lambda: entrar_valor("6"), text="6", width=9, height=4, bg=cor3, fg=cor1, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_10.place(x=200, y=180)

b_11= Button(frame_quadros,command=lambda: entrar_valor("-"), text="-", width=9, height=4, bg=cor4, fg=fundo, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_11.place(x=300, y=180)

#Quarta Linha
b_12 = Button(frame_quadros,command=lambda: entrar_valor("1"), text="1", width=9, height=4, bg=cor3, fg=cor1, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_12.place(x=0, y=270)

b_13 = Button(frame_quadros,command=lambda: entrar_valor("2"), text="2", width=9, height=4, bg=cor3, fg=cor1, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_13.place(x=100, y=270)

b_14 = Button(frame_quadros,command=lambda: entrar_valor("3"), text="3", width=9, height=4, bg=cor3, fg=cor1, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_14.place(x=200, y=270)

b_15 = Button(frame_quadros,command=lambda: entrar_valor("+"), text="+", width=9, height=4, bg=cor4, fg=fundo, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_15.place(x=300, y=270)

#Quinta Linha
b_16 = Button(frame_quadros,command=lambda: entrar_valor("0"), text="0", width=19, height=4, bg=cor3, fg=cor1, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_16.place(x=0, y=360)

b_17= Button(frame_quadros,command=lambda: entrar_valor("."), text=".", width=9, height=4, bg=cor3, fg=cor1, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_17.place(x=200, y=360)

b_18= Button(frame_quadros,command=lambda: entrar_valor("="), text="=", width=9, height=4, bg=cor4, fg=fundo, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_18.place(x=300, y=360)

#Função calcular e limpar:

b_18 = Button(frame_quadros, command=lambda: calcular(),text="=", width=9, height=4, bg=cor4, fg=fundo, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_18.place(x=300, y=360)

b_1 = Button(frame_quadros,command= lambda: limpar_tela(), text="C", width=19, height=4, bg=cor3, fg=cor1, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)

janela.mainloop()