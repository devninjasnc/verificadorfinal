
import tkinter
import customtkinter
from PIL import ImageTk,Image
import tkinter.messagebox as MessageBox

customtkinter.set_appearance_mode("Dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green,white


app = customtkinter.CTk()  #creating cutstom tkinter window
app.geometry("600x440")
app.title('URL CHECKER')



def verificar_():
    nome=entry1.get()
    if nome == 'www.amazon.com.br':
        resposta=customtkinter.CTkLabel(master=frame,text_color='green',text='Seu site é SEGURO').place(x=100,y=250)
        img4=ImageTk.PhotoImage(file='imagens\mazon2.png')
        l4=customtkinter.CTkLabel(master=frame,image=img4)
        l4.place(x=20, y=300)
    elif 'www.americanas.com.br' == nome:
        resposta=customtkinter.CTkLabel(master=frame,text_color='green',text='Seu site é SEGURO').place(x=100,y=250)
        img3=ImageTk.PhotoImage(file='imagens\mericanas.png')
        l3=customtkinter.CTkLabel(master=frame,image=img3)
        l3.place(x=20, y=300)
    elif 'www.magazineluiza.com.br' == nome:
        resposta=customtkinter.CTkLabel(master=frame,text_color='green',text='Seu site é SEGURO').place(x=100,y=250)
        img5=ImageTk.PhotoImage(file='imagens\magalu.png')
        l5=customtkinter.CTkLabel(master=frame,image=img5)
        l5.place(x=20, y=300)
    else:
        resposta2=customtkinter.CTkLabel(master=frame,text_color='red',text='SITE FALSO').place(x=70,y=300)


    


img1=ImageTk.PhotoImage(Image.open("pattern.png"))
l1=customtkinter.CTkLabel(master=app,image=img1)
l1.pack()
#CRIANDO O FRAME
frame=customtkinter.CTkFrame(master=l1, width=320, height=370, corner_radius=15,fg_color='White')
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

img2=ImageTk.PhotoImage(file='imagens\LogoUrl.png')
l2=customtkinter.CTkLabel(master=frame,image=img2)
l2.place(x=110, y=10)

entry1=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='INSIRA A URL')
entry1.place(x=50, y=140)



#CRIAÇÂO DO BOTAO
button1 = customtkinter.CTkButton(master=frame, width=220, text="VERIFICAR", command=verificar_, corner_radius=6)
button1.place(x=50, y=170)
button2 = customtkinter.CTkButton(master=frame, width=220, text="LIMPAR", corner_radius=6)
button2.place(x=50, y=200)

app.mainloop()
