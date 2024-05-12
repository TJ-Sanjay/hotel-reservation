from pathlib import Path
import tkinter as tk
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Button, PhotoImage, ttk, Label
from tkcalendar import Calendar
from subprocess import call

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"table_2_assets\frame0")


def input_page():
    window.destroy()
    call(["python", "input.py"])


def get_selected_date():
    def print_date():
        selected_date = date_picker.get_date()
        label = Label(text=selected_date, font=20, bg="#D9D9D9")
        label.place(x=390, y=375)
        return selected_date

    top = tk.Toplevel(window)
    top.title("Select Date")

    # Date picker
    date_picker = Calendar(top, date_pattern="dd/mm/yyyy", width=12, background='#00FF00',
                           foreground='white', borderwidth=2)
    date_picker.pack(padx=10, pady=10)

    # Button to print selected date
    submit_button = ttk.Button(top, text="Submit", command=print_date)
    submit_button.pack(pady=10)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1280x832")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=832,
    width=1280,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    640.0,
    52.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=936.0,
    y=31.0,
    width=85.0,
    height=42.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=821.0,
    y=31.0,
    width=85.0,
    height=42.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=1051.0,
    y=31.0,
    width=121.0,
    height=42.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    209.5,
    52.5,
    image=entry_image_1
)

cal_image_1 = PhotoImage(
    file=relative_to_assets("image_5.png"))

entry_1 = Button(window,
                 image=cal_image_1,
                 command=get_selected_date,
                 font=20,
                 bd=0,
                 bg="#D9D9D9",
                 fg="#000000",
                 highlightthickness=0
                 )
entry_1.place(
    x=950,
    y=373.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    640.0,
    468.0,
    image=image_image_2
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=24.0,
    y=543.0,
    width=163.0,
    height=66.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    255.0,
    198.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    140.0,
    402.0,
    image=image_image_4
)
image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))

back_button = Button(
    image=image_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: input_page(),
    relief="flat"
)
back_button.place(x=50, y=700)
window.resizable(False, False)
window.mainloop()
