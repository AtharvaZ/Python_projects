from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser

root = Tk()
root.title('Text Editor')
root.geometry('700x560')

global open_status_name
open_status_name = False

global selected
selected = False

def new_file():
    my_text.delete("1.0", END)
    root.title('New File')
    status_bar.config(text="New File    ")

    global open_status_name
    open_status_name = False

def open_file():
    my_text.delete("1.0", END)\

    file = filedialog.askopenfilename(initialdir = '''Enter your directory''', title="Open File", filetypes=(("Text Files","*.txt"), ("PDF Files", "*.pdf"), ("All Files","*.*")))

    if file:
        global open_status_name
        open_status_name = file

    name = file
    status_bar.config(text=name)
    name = name.replace('''Enter your directory''',"")
    root.title(f'{name}')

    file = open(file, 'r')
    data = file.read()

    my_text.insert(END, data)
    file.close()

def save_file():
    global open_status_name
    if open_status_name:
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()
        status_bar.config(text=f'Saved: {open_status_name}          ')
    else:
        save_as_file()
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir='''Enter your directory''', titel="Save File", filetypes=(("All Files"), ("*.*")))
    if text_file:
        name = text_file
        status_bar.config(text=f'Saved: {name}          ')
        name = name.replace('''Enter your directory''',"")
        root.title(f'{name}')

        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0,END))

        text_file.close()
def cut_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    if my_text.selection_get():
        selected = my_text.selection_get()
        my_text.delete("sel.first", "sel.last")
        root.clipboard_clear()
        root.clipboard_append(selected)
def copy_text(e):
    global selected
    if e:
        selected = root.clipboard_get()

    if my_text.selection_get():
        selected = my_text.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)
def paste_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position, root.clipboard_get())

def bold_text():
    bold_font = font.Font(my_text, my_text.cget("font"))
    bold_font.configure(weight="bold")

    my_text.tag_configure("bold", font=bold_font)

    current_tags = my_text.tag_names("sel.first")

    if "bold" in current_tags:
        my_text.tag_remove("bold", "sel.first", "sel.last")
    else:
        my_text.tag_add("bold", "sel.first", "sel.last")



def italic_text():
    italic_font = font.Font(my_text, my_text.cget("font"))
    italic_font.configure(slant="italic")

    my_text.tag_configure("italic", font=italic_font)

    current_tags = my_text.tag_names("sel.first")

    if "italic" in current_tags:
        my_text.tag_remove("italic", "sel.first", "sel.last")
    else:
        my_text.tag_add("italic", "sel.first", "sel.last")


def text_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:

        color_font = font.Font(my_text, my_text.cget("font"))

        my_text.tag_configure("colored", font=color_font, foreground = my_color)

        current_tags = my_text.tag_names("sel.first")

        if "colored" in current_tags:
            my_text.tag_remove("colored", "sel.first", "sel.last")
        else:
            my_text.tag_add("colored", "sel.first", "sel.last")


def bg_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(background=my_color)


def all_text_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(foreground=my_color)


def select_all_text(e):
    my_text.tag_add('sel', '1.0','end')

def clear_all_text():
    my_text.delete(1.0, END)


toolbar_frame = Frame(root)
toolbar_frame.pack(side=TOP, fill=X)

my_frame = Frame(root)
my_frame.pack(pady=5)

text_scroll_up = Scrollbar(my_frame, orient=VERTICAL)
text_scroll_up.pack(side=RIGHT, fill=Y)

text_scroll_side = Scrollbar(my_frame, orient=HORIZONTAL)
text_scroll_side.pack(side=BOTTOM, fill=X)

my_text = Text(my_frame, width=97, height=25, font=('Helvetica', 16), selectbackground="cyan", selectforeground="black", background="WHITE", foreground="BLACK", undo=True, yscrollcommand=text_scroll_up.set, xscrollcommand=text_scroll_side.set, wrap="none")
my_text.configure(insertbackground='black')
my_text.pack()

my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label="New", command = new_file)
file_menu.add_command(label="Open", command = open_file)
file_menu.add_command(label="Save", command = save_file)
file_menu.add_command(label="Save As", command = save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label="Cut               (Ctrl+x)", command=lambda: cut_text(False),)
edit_menu.add_command(label="Copy            (Ctrl+c)", command=lambda: copy_text(False))
edit_menu.add_command(label="Paste           (Ctrl+v)", command=lambda: paste_text(False))
edit_menu.add_command(label="Undo            (Ctrl+z)", command=my_text.edit_undo)
edit_menu.add_command(label="Redo            (Ctrl+y)", command=my_text.edit_redo)
edit_menu.add_command(label="Select all     (Ctrl+a)", command=lambda: select_all_text(True))
edit_menu.add_command(label="Clear all", command=clear_all_text)


color_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Colors', menu=color_menu)
color_menu.add_command(label="Change Selected text", command=text_color)
color_menu.add_command(label="All text", command = all_text_color)
color_menu.add_command(label="Background color", command=bg_color)




text_scroll_up.config(command=my_text.yview)
text_scroll_side.config(command=my_text.xview)

status_bar = Label(root, text='Ready        ', anchor=E)
status_bar.pack(side=BOTTOM, fill=X, ipady=5)

root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)
root.bind('<Control-a>', select_all_text)

bold_button = Button(toolbar_frame, text="Bold", command = bold_text)
bold_button.grid(row=0, column=0, sticky=W, padx=5)

italic_button = Button(toolbar_frame, text="Italics", command = italic_text)
italic_button.grid(row=0, column=1, padx=5)

undo_button = Button(toolbar_frame, text="Undo", command = my_text.edit_undo)
undo_button.grid(row=0, column=2, padx=5)

redo_button = Button(toolbar_frame, text="Redo", command = my_text.edit_redo)
redo_button.grid(row=0, column=3, padx=5)

color_text_button = Button(toolbar_frame,text = "Text Color", command = text_color)
color_text_button.grid(row=0, column=4, padx=5)

root.mainloop()
