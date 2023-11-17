from tkinter import *
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
repeat = 0


# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(time_in_seconds):
    minutes = floor(time_in_seconds / 60)
    seconds = time_in_seconds % 60
    if minutes < 10 and seconds < 10:
        image_background.itemconfig(timer, text=f'0{minutes}:0{seconds}')
    elif seconds == 0:
        image_background.itemconfig(timer, text=f'{minutes}:00')
    elif minutes < 10:
        image_background.itemconfig(timer, text=f'0{minutes}:{seconds}')
    elif seconds < 10:
        image_background.itemconfig(timer, text=f'{minutes}:0{seconds}')
    else:
        image_background.itemconfig(timer, text=f'{minutes}:{seconds}')

    window.after(1000, count_down, time_in_seconds - 1)
    if time_in_seconds == 0:
        minutes_to_seconds()


def minutes_to_seconds(minutes=WORK_MIN):
    global repeat
    repeat += 1
    print(repeat)
    if repeat == 8:
        whats_now_label.config(text='Long break', fg=GREEN, bg=YELLOW)
        count_down(LONG_BREAK_MIN*60)
    elif repeat % 2 != 0:
        whats_now_label.config(text='Work time', fg=PINK, bg=YELLOW)
        count_down(WORK_MIN*60)
    else:
        whats_now_label.config(text='Short break', fg=RED, bg=YELLOW)
        count_down(SHORT_BREAK_MIN*60)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title('The Pomodoro Technique')

image_background = Canvas(width=200, height=230, bg=YELLOW, highlightthickness=0)
image_tomato = PhotoImage(file='tomato.png')
image_background.create_image(100, 115, image=image_tomato)
timer = image_background.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
image_background.grid(row=3, column=2)

timer_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, 'bold'))
timer_label.grid(row=1, column=2)

whats_now_label = Label(text='', font=(FONT_NAME, 20, 'bold'))
whats_now_label.grid(row=2, column=2)

check = '✓'
check_label = Label(text=check, fg=GREEN, bg=YELLOW, font=15)
check_label.grid(row=5, column=2)

start_button = Button(text='Start', command=minutes_to_seconds)
start_button.grid(row=4, column=1)

reset_button = Button(text='Reset')
reset_button.grid(row=4, column=3)









window.mainloop()
