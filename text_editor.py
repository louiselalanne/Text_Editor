from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog
import os

root = Tk()
root.minsize(650,650)
root.maxsize(650,650)
root.configure(background= "LightSteelBlue1")

open_img = ImageTk.PhotoImage(Image.open("open.png"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))
exit_img = ImageTk.PhotoImage(Image.open("exit.jpg"))

label_nomeArquivo = Label(root, text="Nome do Arquivo", background= "LightSteelBlue1", fg="gray30")
label_nomeArquivo.place(relx= 0.28, rely= 0.03, anchor= CENTER)

input_nomeArquivo = Entry(root, background="gray99")
input_nomeArquivo.place(relx= 0.46, rely= 0.03, anchor= CENTER)

my_text = Text(root, height= 35, width= 80, background="gray99")
my_text.place(relx= 0.5, rely= 0.55, anchor= CENTER)

name = ""
def openFile():
    global name
    my_text.delete(1.0, END)
    input_nomeArquivo.delete(0, END)
    text_file = filedialog.askopenfilename(title="Open Text File", filetypes=(("Text Files", "*.txt"),))

    name = os.path.basename(text_file)
    formated_name = name.split('.')[0]
    input_nomeArquivo.insert(END, formated_name)
    root.title(formated_name)
    text_file = open(name, 'r')
    paragrafo = text_file.read()
    my_text.insert(END, paragrafo)
    text_file.close()

open_btn = Button(root, image=open_img, text="Open File", command=openFile)
open_btn.place(relx=0.05, rely=0.03, anchor= CENTER)

def save():
    input_nome = input_nomeArquivo.get()
    file = open(input_nome + ".txt", "w")
    data = my_text.get("1.0", END)
    print(data)
    file.write(data)
    messagebox.showinfo("Atualizado", "Success! :D")

save_btn = Button(root, image=save_img, text="Save File", command=save)
save_btn.place(relx=0.11, rely=0.03, anchor=CENTER)

def close():
    root.destroy()

exit_btn = Button(root, image=exit_img, text="Exit File", command=close)
exit_btn.place(relx=0.17, rely=0.03, anchor=CENTER)

root.mainloop()