from tkinter import *
import math
#--------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#009933"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.1
reps = 0
tick = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_time():
    global reps
    reps = 0
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    tick_label.config()
    canvas.itemconfig(timer_text, text=f"00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_time():
    global reps
    reps+=1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", bg=YELLOW, fg=RED, font=(FONT_NAME, 40))

    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", bg=YELLOW, fg=PINK, font=(FONT_NAME, 40))

    else:
        timer_label.config(text="Work", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40))
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

#count in seconds
def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)

    else:
        global tick
        start_time()
        if reps % 2 == 0:
            total_tick = int(reps / 2)
            tick += "✔"
            tick_label.config(text=tick)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
bg_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=bg_img)
timer_text = canvas.create_text(105, 130, text="00:00", fill='white', font=(FONT_NAME, 33, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text='start', highlightbackground=YELLOW, command=start_time)
start_button.grid(column=0, row=2)

reset_button = Button(text="reset")
reset_button.configure(bg=YELLOW, highlightbackground=YELLOW, command=reset_time)
reset_button.grid(column=2, row=2)

tick_label = Label(bg=YELLOW, fg=GREEN)
tick_label.grid(column=1, row=3)


window.mainloop()