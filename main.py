from tkinter import *

FONT_NAME = "Courier"
GREEN = "#9bdeac"
yellow = "#f7f5dd"


def count_down(minutes=25, seconds=0):
    if seconds == 0:
        image_background.itemconfig(timer, text=f'{minutes}:00')
        seconds = 59
        window.after(1000, count_down, minutes-1, seconds)
    elif seconds < 10:
        image_background.itemconfig(timer, text=f'{minutes}:0{seconds}')
        window.after(1000, count_down, minutes, seconds-1)
    else:
        image_background.itemconfig(timer, text=f'{minutes}:{seconds}')
        window.after(1000, count_down, minutes, seconds-1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100, pady=50, bg=yellow)
window.title('The Pomodoro Technique')

image_background = Canvas(width=200, height=230, bg=yellow, highlightthickness=0)
image_tomato = PhotoImage(file='tomato.png')
image_background.create_image(100, 115, image=image_tomato)
timer = image_background.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
image_background.grid(row=2, column=2)

timer_label = Label(text='Timer', fg=GREEN, bg=yellow, font=(FONT_NAME, 50, 'bold'))
timer_label.grid(row=1, column=2)

check = '✓'
check_label = Label(text=check, fg=GREEN, bg=yellow, font=15)
check_label.grid(row=4, column=2)

start_button = Button(text='Start', command=count_down)
start_button.grid(row=3, column=1)

reset_button = Button(text='Reset')
reset_button.grid(row=3, column=3)



window.mainloop()
