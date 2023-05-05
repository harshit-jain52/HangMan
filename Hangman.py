# Modules
from tkinter import *
from tkinter.font import Font
from PIL import ImageTk, Image
from Random_Word_Generator import letters  # Self-Defined

# Binding Fns
def game_start():
    # Gameplay Screen
    canv.delete("title") # <canvas_name>.delete(<tags>) deletes the object with the specified tags
    canv.delete('button')
    letters_list,changing_list = play()
    ebox = Entry(root, font=("Comic Sans MS",24),width=2, fg="black",bg="#A6A6A6",bd=0)
    canv.create_text(160,350,text="Enter Alphabet: ",font = font_comic20, anchor='nw',tags="instruction")
    canv.create_text(350,275,text=lw(changing_list), font = font_halv40, anchor='center',tags='blanks')
    canv.create_text(425,150,text="Type and Hit ENTER", font = font_halv30, anchor='center',tags="message")
    canv.create_image(25,35, image = hang_list[0], anchor = "nw",tags="hang_pic")

    def game_restart_prep():
        canv.delete("entrybox")
        canv.delete("instruction")
        
        def game_restart():
                canv.delete('blanks')
                canv.delete("message")
                canv.delete("hang_pic")
                game_start()

        restart = Button(root,
               text="Play Again",
               font= font_comic20,
               padx=10,
               bg="#A6A6A6",
               command=game_restart)
        button_win = canv.create_window(280,400,anchor="nw", window=restart, tags='button')

    def enter_click(e):
            l = ebox.get().upper()   # gets the value entered
            ebox.delete(0,END)       # deletes the entered value from text box
            
            if len(l) != 1:
                if len(l) > 1:
                    text = """
                Only One Alphabet
                At A Time, duh!"""
                else:
                    text = "No Blanks Please :)"
            elif not l.isalpha():
                text = "Only Alphabets!"
            else:
                if l in entered:
                    text = "Already Entered"
                elif l in letters_list:
                    text = "Correct Guess!"
                    for i in range(len(letters_list)):
                        if letters_list[i]==l:
                            changing_list[i]=l
                    canv.delete('blanks')
                    canv.create_text(350,275,text=lw(changing_list), font = font_halv40, anchor='center',tags='blanks')
                    entered.append(l)
                    if changing_list==letters_list:
                        text="Congrats!"
                        canv.delete('blanks')
                        canv.create_text(350,275,text=lw(letters_list), font = font_halv40,fill="green", anchor='center',tags='blanks')
                        game_restart_prep()
                else:
                    text = "Oops!"
                    entered.append(l)
                    wrong=0
                    for i in entered:
                        if i not in letters_list:
                            wrong+=1
                    canv.delete("hang_pic")
                    canv.create_image(25,35, image = hang_list[wrong], anchor = "nw",tags="hang_pic")
                    
                    if wrong == 10:
                        text='Better Luck Next Time :('
                        canv.delete('blanks')
                        canv.create_text(350,275,text=lw(letters_list), font = font_halv40,fill="red", anchor='center',tags='blanks')
                        game_restart_prep()

            canv.delete("message")
            canv.create_text(425,150,text=text, font = font_halv30, anchor='center',tags="message")


    entry_win = canv.create_window(370,350,anchor="nw", window=ebox, tags="entrybox")
    ebox.bind("<Return>",enter_click)
    entered=[]


# The Random Word
def play():
    letters_list = letters()
    changing_list=[]
    for i in range(len(letters_list)):
            changing_list.append("_")
    return letters_list,changing_list

def lw(blanks_letters):
    s=''
    for i in blanks_letters:
        s = s+i+" "
    return s

# Stage    
root = Tk()
root.title("Hangman")
root.geometry("700x500")
root.resizable(False, False)
root.iconbitmap('Images/icon.ico')

# Fonts
font_comic20 = Font(
    family="Comic Sans MS",
    size=20)
font_halv30 = Font(
    family="Halvetica",
    size=30)
font_halv40 = Font(
    family="Halvetica",
    size=40)

# Resources
bg = ImageTk.PhotoImage(file = "Images/chalkboard.jpg")
title = ImageTk.PhotoImage(file = "Images/title.png")
hang0 = ImageTk.PhotoImage(Image.open("Images/hang0.png").resize((200,200),Image.ANTIALIAS))
hang1 = ImageTk.PhotoImage(Image.open("Images/hang1.png").resize((200,200),Image.ANTIALIAS))
hang2 = ImageTk.PhotoImage(Image.open("Images/hang2.png").resize((200,200),Image.ANTIALIAS))
hang3 = ImageTk.PhotoImage(Image.open("Images/hang3.png").resize((200,200),Image.ANTIALIAS))
hang4 = ImageTk.PhotoImage(Image.open("Images/hang4.png").resize((200,200),Image.ANTIALIAS))
hang5 = ImageTk.PhotoImage(Image.open("Images/hang5.png").resize((200,200),Image.ANTIALIAS))
hang6 = ImageTk.PhotoImage(Image.open("Images/hang6.png").resize((200,200),Image.ANTIALIAS))
hang7 = ImageTk.PhotoImage(Image.open("Images/hang7.png").resize((200,200),Image.ANTIALIAS))
hang8 = ImageTk.PhotoImage(Image.open("Images/hang8.png").resize((200,200),Image.ANTIALIAS))
hang9 = ImageTk.PhotoImage(Image.open("Images/hang9.png").resize((200,200),Image.ANTIALIAS))
hang10 = ImageTk.PhotoImage(Image.open("Images/hang10.png").resize((200,200),Image.ANTIALIAS))
hang_list=[hang0,hang1,hang2,hang3,hang4,hang5,hang6,hang7,hang8,hang9,hang10]

# Display
canv = Canvas(root, width = 700,height = 500,bd=0,highlightthickness=0)
canv.place(x=0,y=0,relwidth=1,relheight=1)

# Title Screen
canv.create_image(0, 0, image = bg, anchor = "nw")
canv.create_image(75, 100, image = title, anchor = "nw",tags="title")

start = Button(root,
               text="Start",
               font= font_comic20,
               padx=10,
               bg="#A6A6A6",
               command=game_start)
button_win = canv.create_window(280,400,anchor="nw", window=start, tags='button')


root.mainloop()
