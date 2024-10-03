from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card={}
to_learn={}


try:
    data=pd.read_csv("words_to_learn.csv")# Change from total word to words_to_learn
except FileNotFoundError:
    original_data=pd.read_csv("french_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")


def next_card():
    '''Generating the random or next card from the Data'''
    global current_card,flip_timer
    window.after_cancel(flip_timer)

    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card['French'],fill="black")
    canvas.itemconfig(canvas_image,image=card_front_img)

    flip_timer=window.after(3000,func=flip_card)   #3000 mili seconds delay

def flip_card():
    '''Flip the card to 'English' '''
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(canvas_image,image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    data=pd.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv",index=False)
    next_card()

#Create a main window
window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,func=flip_card)



'''Creating a Canvas For front side'''
canvas=Canvas(width=800,height=526)
card_front_img=PhotoImage(file="card_front.png") 
card_back_img=PhotoImage(file='card_back.png')

canvas_image=canvas.create_image(400,263,image=card_front_img)# 400,263 to align image at the centre

card_title=canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
card_word=canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)






'''Creating 'Left' and 'Right' button '''
cross_img=PhotoImage(file="wrong.png")
wrong_button=Button(image=cross_img,command=next_card)
wrong_button.config(bg=BACKGROUND_COLOR,highlightthickness=0)
wrong_button.grid(row=1,column=0)

right_img=PhotoImage(file="right.png")
right_button=Button(image=right_img,command=is_known)
right_button.config(bg=BACKGROUND_COLOR,highlightthickness=0)
right_button.grid(row=1,column=1)
canvas.grid(row=0,column=0)


next_card()
window.mainloop()