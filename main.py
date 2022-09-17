from tkinter import *
from tkinter import ttk

import math
################# cores ###############
co1 = "#feffff"  # white/branca
co2 = "#6f9fbd"  # blue/azul
co3 = "#38576b"  # valor

fundo = "#e8e6e6"
co10 ="#363434"
cor11 ="#424345"

cor1='#FFAB40'
cor2='#ff333a'
cor3='#6bd66f'
cor4="#ab8918"

janela = Tk()
janela.title('')
janela.geometry('235x289')
janela.configure(bg=co1)


style = ttk.Style(janela)
style.theme_use("clam")

################# Frames ####################

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=280)

frame_score = Frame(janela, width=300, height=56,bg=co3, pady=0, padx=0, relief="flat",)
frame_score.grid(row=1, column=0, sticky=NW)

frame_cientifica = Frame(janela, width=300, height=86,bg=co3, pady=0, padx=0, relief="flat",)
frame_cientifica.grid(row=2, column=0, sticky=NW)

frame_quadros = Frame(janela, width=300, height=340,bg=fundo, pady=0, padx=0, relief="flat",)
frame_quadros.grid(row=3, column=0, sticky=NW)


################# Funções ####################

def entering_values(event):
	global all_values
	all_values = all_values + str(event)
	value_text.set(all_values)

def calculate():
	global all_values
 
	global texto

	texto = all_values

	modulos =['math.tan','math.sin','math.cos','math.sqrt','math.log','math.log10','math.e','math.pow','math.pi','math.radian']

	for i in modulos:
		if i=='math.tan':
			texto = texto.replace("tan", i)
			
		if i=='math.sin':
			texto = texto.replace("sin", i)
			
		if i=='math.cos':
			texto = texto.replace("cos", i)
			
		if i=='math.sqrt':
			texto = texto.replace("sqrt", i)
			
		# ------------------------------------
		
		if i=='math.log':
			texto = texto.replace("log", i)
			
		if i=='math.log10':
			texto = texto.replace("log10", i)
			
		if i=='math.e':
			texto = texto.replace("e", i)
			
		if i=='math.pow':
			texto = texto.replace("pow", i)
			
		# ------------------------------------
			
		if i=='math.radians':
			texto = texto.replace("rad", i)
			
		if i=='math.pi':
			texto = texto.replace("pi", i)
   
	result = str(eval(texto))
	
	print(result)
	print(texto)
	
	value_text.set(result)
	all_values = ""

def scream_clear(): 
    global all_values
    all_values = "" 
    value_text.set("")

#for storing all the expressions that will be evalueted
all_values = "" 

# for single value entering
value_text = StringVar()

################# Label ####################

app_scream = Label(frame_score,width=16,height=2,textvariable = value_text , padx=7, relief="flat", anchor="e",bd=0, justify=RIGHT, font=('Ivy 18 '), bg='#37474F', fg=co1)
app_scream.place(x=0, y=0)

################# Buttons ####################

b_tan = Button(frame_cientifica, text="tan", width=6, height=1, bg=co10, fg=fundo,font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values('tan'))
b_tan.place(x=0, y=1)
b_sin = Button(frame_cientifica, text="sin", width=6, height=1, bg=co10, fg=fundo,font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values('sin'))
b_sin.place(x=59, y=1)
b_cos = Button(frame_cientifica, text="cos", width=6, height=1, bg=co10, fg=fundo,font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values('cos'))
b_cos.place(x=118, y=1)
b_sqrt = Button(frame_cientifica, text="sqrt", width=6, height=1, bg=co10, fg=co1,font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values('sqrt'))
b_sqrt.place(x=177, y=1)

b_log = Button(frame_cientifica, text="log", width=6, height=1, bg=co10, fg=fundo,font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values('log'))
b_log.place(x=0, y=30)
b_log10 = Button(frame_cientifica, text="log10", width=6, height=1, bg=co10, fg=fundo,font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values('log10'))
b_log10.place(x=59, y=30)
b_euler = Button(frame_cientifica, text="e", width=6, height=1, bg=co10, fg=fundo,font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values('e'))
b_euler.place(x=118, y=30)
b_pow = Button(frame_cientifica, text="pow", width=6, height=1, bg=co10, fg=co1,font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values('pow'))
b_pow.place(x=177, y=30)

b_12 = Button(frame_cientifica, text="pi", width=6, height=1, bg=co10, fg=fundo,font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values('pi'))
b_12.place(x=0, y=58)
b_13 = Button(frame_cientifica, text=",", width=6, height=1, bg=co10, fg=fundo,font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values(','))
b_13.place(x=59, y=58)
b_14 = Button(frame_cientifica, text="(", width=6, height=1, bg=co10, fg=fundo,font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values('('))
b_14.place(x=118, y=58)
b_15 = Button(frame_cientifica, text=")", width=6, height=1, bg=co10, fg=co1,font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values(')'))
b_15.place(x=177, y=58)


b_1 = Button(frame_quadros, text="C", width=14, height=1, bg=cor11, fg=fundo,font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: scream_clear())
b_1.place(x=0, y=0)
b_2 = Button(frame_quadros, text="%", width=6, height=1, bg=cor11, fg=fundo,font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values('%'))
b_2.place(x=118, y=0)
b_3 = Button(frame_quadros, text="/", width=6, height=1, bg=cor11, fg=co1,font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values('/'))
b_3.place(x=177, y=0)

b_4 = Button(frame_quadros, text="7", width=6, height=1, bg=co10, fg=fundo,font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values(7))
b_4.place(x=0, y=29)
b_5 = Button(frame_quadros, text="8", width=6, height=1, bg=co10, fg=fundo,font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values(8))
b_5.place(x=59, y=29)
b_6 = Button(frame_quadros, text="9", width=6, height=1, bg=co10, fg=fundo,font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values(9))
b_6.place(x=118, y=29)
b_7 = Button(frame_quadros, text="*", width=6, height=1, bg=cor11, fg=co1,font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values('*'))
b_7.place(x=177, y=29)

b_8 = Button(frame_quadros, text="4", width=6, height=1, bg=co10, fg=fundo,font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values(4))
b_8.place(x=0, y=58)
b_9 = Button(frame_quadros, text="5", width=6, height=1, bg=co10, fg=fundo,font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values(5))
b_9.place(x=59, y=58)
b_10 = Button(frame_quadros, text="6", width=6, height=1, bg=co10, fg=fundo,font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values(6))
b_10.place(x=118, y=58)
b_11 = Button(frame_quadros, text="-", width=6, height=1, bg=cor11, fg=co1,font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values('-'))
b_11.place(x=177, y=58)

b_12 = Button(frame_quadros, text="1", width=6, height=1, bg=co10, fg=fundo,font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values(1))
b_12.place(x=0, y=87)
b_13 = Button(frame_quadros, text="2", width=6, height=1, bg=co10, fg=fundo,font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values(2))
b_13.place(x=59, y=87)
b_14 = Button(frame_quadros, text="3", width=6, height=1, bg=co10, fg=fundo,font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values(3))
b_14.place(x=118, y=87)
b_15 = Button(frame_quadros, text="+", width=6, height=1, bg=cor11, fg=co1,font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values('+'))
b_15.place(x=177, y=87)

b_16 = Button(frame_quadros, text="0", width=14, height=1, bg=co10, fg=fundo,font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values(0))
b_16.place(x=0, y=116)
b_17 = Button(frame_quadros, text=".", width=6, height=1, bg=co10, fg=fundo,font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values('.'))
b_17.place(x=118, y=116)
b_18 = Button(frame_quadros, text="=", width=6, height=1, bg=cor11, fg=co1,font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: calculate())
b_18.place(x=177, y=116)



janela.mainloop()