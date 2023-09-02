from tkinter import *
from PIL import Image, ImageTk
import pygame
from pygame import mixer
import os

#cores ..

co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#3fb5a3"  # verde
co3 = "#2e2d2c"  # preto
co4 = "#403d3d"  # letra
co5 = "#4a88e8"  # Azul 



janela = Tk ()
janela.title ("")
janela.geometry('352x255')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)



frame_esquerda = Frame(janela, width=150, height=150, bg=co3)
frame_esquerda.grid(row=0, column=0, pady=1, padx=1, sticky=NSEW)

frame_direita = Frame(janela, width=250, height=150, bg=co3)
frame_direita.grid(row=0, column=1, pady=1, padx=0, sticky=NSEW)

frame_baixo= Frame(janela, width=404, height=100, bg=co3)
frame_baixo.grid(row=1, column=0, columnspan=3, pady=1, padx=0, sticky=NSEW)


#frame esquerdo..
img_1 = Image.open(r'iconmu.png')
img_1 = img_1.resize((130,130))
img_1 = ImageTk.PhotoImage(img_1)

l_logo = Label(frame_esquerda, height=130, image=img_1, compound=LEFT, padx=10, anchor='nw', font=('ivy 16 bold'), bg=co3, fg=co3)
l_logo.place(x=16, y=7)

# funçoes...

#tocar musica

def play_musica():
        tocando = listbox.get(ACTIVE)
        l_display['text'] = tocando
        pygame.mixer.music.load(tocando)
        pygame.mixer.music.play()



#pausar musica

def pause_musica():
        pygame.mixer.music.pause()




#musica anterior

def voltar_musica():
    pygame.mixer.music.rewind
    tocando = l_display['text']
    index = musicas.index(tocando)

    novo_index = index - 1
    tocando = musicas[novo_index]

    mixer.music.load(tocando)
    mixer.music.play()

    listbox.delete(0,END)
    mostrar()
    listbox.select_set(novo_index)
    listbox.config(selectmode=SINGLE)
    l_display['text'] = tocando

#proxima musica

def prox_musica():
    tocando = l_display['text']
    index = musicas.index(tocando)

    novo_index = index + 1
    tocando = musicas[novo_index]

    mixer.music.load(tocando)
    mixer.music.play()

    listbox.delete(0,END)
    mostrar()
    listbox.select_set(novo_index)
    listbox.config(selectmode=SINGLE)
    l_display['text'] = tocando




def cont_musica():
        mixer.music.unpause()


def canc_musica():
    mixer.music.stop()

#direito...


listbox = Listbox(frame_direita, width=22, height=10, selectmode=SINGLE, font=('arial 9 bold'), bg=co3, fg=co1)
listbox.grid(row=0, column=0)

s = Scrollbar(frame_direita)
s.grid(row=0, column=1, sticky=NSEW)

listbox.configure(yscrollcommand=s.set)
s.configure(command=listbox.yview)



#BAIXO ....

l_display = Label(frame_baixo, text= 'Curte um som', width=44, justify=LEFT, anchor='nw', font=('ivy 10'), bg=co1, fg=co4)
l_display.place(x=0, y=1)

img_2 = Image.open('voltar2.png')
img_2 = img_2.resize((30,30))
img_2 = ImageTk.PhotoImage(img_2)

l_rewind = Button(frame_baixo, command=voltar_musica, image= img_2, width=40, height=40, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co3, fg=co4)
l_rewind.place(x=40, y=35)

img_3 = Image.open('play4.png')
img_3 = img_3.resize((30,30))
img_3 = ImageTk.PhotoImage(img_3)

l_play = Button(frame_baixo, command=play_musica, image= img_3, width=40, height=40, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co3, fg=co4)
l_play.place(x=85, y=35)

img_4 = Image.open('pause3.png')
img_4 = img_4.resize((30,30))
img_4 = ImageTk.PhotoImage(img_4)

l_pause = Button(frame_baixo, command=pause_musica, image= img_4, width=40, height=40, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co3, fg=co4)
l_pause.place(x=130, y=35)

img_5 = Image.open('avanco5.png')
img_5 = img_5.resize((30,30))
img_5 = ImageTk.PhotoImage(img_5)

l_fast = Button(frame_baixo, command=prox_musica, image= img_5, width=40, height=40, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co3, fg=co4)
l_fast.place(x=175, y=35)

img_6 = Image.open('frente6.png')
img_6 = img_6.resize((30,30))
img_6 = ImageTk.PhotoImage(img_6)

l_frente = Button(frame_baixo, command= cont_musica, image= img_6, width=40, height=40, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co3, fg=co4)
l_frente.place(x=218, y=35)

img_7 = Image.open('total7.png')
img_7 = img_7.resize((30,30))
img_7 = ImageTk.PhotoImage(img_7)

l_stop = Button(frame_baixo, command=canc_musica, image= img_7, width=40, height=40, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co3, fg=co4)
l_stop.place(x=263, y=35)

os.chdir ('audios')
musicas = os.listdir()


def mostrar():
    for i in musicas:
        listbox.insert(END,i)


mostrar()

mixer.init()


janela.mainloop()