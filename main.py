from tkinter import *

FONT_NAME = "Courier"
YELLOW = "#f7f5dd"

window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title('The Pomodoro Technique')

image_background = Canvas(width=200, height=230, bg=YELLOW, highlightthickness=0)
image_tomato = PhotoImage(file='tomato.png')
image_background.create_image(100, 115, image=image_tomato)
image_background.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
image_background.pack()









window.mainloop()