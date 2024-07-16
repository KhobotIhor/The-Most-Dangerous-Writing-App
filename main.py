import tkinter as tk
import time

countdown = 5


window = tk.Tk()
a = time.time()
window.title('The Most Dangerous Writing App')

label = tk.Label(text='Type, but do not stop for more than 5 sec.', font=('Calibri', 15, 'bold'))
label.grid(column=1, row=0)

text_area = tk.Text()

text_area.grid(column=1, row=1)
text_area.focus()


def count_down(count):
    label_count = tk.Label(text=f'Count: {count}')
    label_count.grid(column=1, row=2)


def start_timer(count):
    count_down(count)
    global countdown
    if count > 0:
        countdown = window.after(1000, start_timer, count - 1)
        print(count)
    else:
        text_area.delete('1.0', tk.END)

        print('End')


def is_writing(event):
    if event.char != '\x08' and event.char:
        global countdown
        window.after_cancel(countdown)
        start_timer(5)


text_area.bind('<Key>', is_writing)


window.mainloop()



