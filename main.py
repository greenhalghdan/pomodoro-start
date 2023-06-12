from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
reps = 1
ticks = ""
timer = NONE

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 1
    title.config(text="Timer", fg=GREEN, font=(FONT_NAME,35, "bold"), bg=YELLOW)
    canvas.itemconfig(timer_text, text=f"00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title.config(text="long break", fg=RED)
        count_down(long_break_sec)
        reps += 1
    elif reps % 2 == 0:
        title.config(text="short break", fg=PINK)
        count_down(short_break_sec)
        reps += 1
    else:
        title.config(text="Working", fg=GREEN)
        count_down(work_sec)
        reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    global ticks, timer

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            ticks += "✔"
            check_marks.config(text=ticks)
# ---------------------------- UI SETUP ------------------------------- #
#set up the window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# set up the canvas

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME,35, "bold"))
canvas.grid(column=2, row=2)

# label

title = Label(text="Timer", fg=GREEN, font=(FONT_NAME,35, "bold"), bg=YELLOW)
title.grid(column=2, row=1)

# Buttons

start = Button(text="Start", highlightthickness=0, command=start_timer)
reset = Button(text="Reset", highlightthickness=0, command=reset_timer)

start.grid(column=1, row=3)
reset.grid(column=3, row=3)

check_marks = Label(text=ticks,bg=YELLOW , fg=GREEN, font=(FONT_NAME))
check_marks.grid(column=2, row=3)

window.mainloop()

