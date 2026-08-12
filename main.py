import os
import customtkinter as ctk
from config import BUTTONS, BTN_BG, HOVER_C, TEXT_C
from logic import handle_press

app = ctk.CTk()
app.title('Calculator')
app.geometry('350x600') 
app.resizable(True, True)

if os.path.exists('logo.ico'):
    try:
        app.iconbitmap('logo.ico')
    except Exception:
        pass

app.configure(fg_color=("white", "black"))
ctk.set_appearance_mode('dark')

def toggle_theme():
    if ctk.get_appearance_mode() == 'Dark':
        ctk.set_appearance_mode('Light')
    else:
        ctk.set_appearance_mode('Dark')

top_frame = ctk.CTkFrame(app, fg_color="transparent")
top_frame.pack(fill="x", padx=10, pady=(10, 0))

theme_btn = ctk.CTkButton(
    top_frame, text="💡", width=40, height=40, 
    fg_color="transparent", hover_color=("#e0e0e0", "#1f1f1f"),
    text_color=("black", "white"), font=("Arial", 24),
    command=toggle_theme
)
theme_btn.pack(side="left")

history_display = ctk.CTkLabel(
    app, text='', font=('Arial', 18),
    anchor='e', text_color=("gray60", "gray50")
)
history_display.pack(padx=20, fill='x')

display = ctk.CTkLabel(
    app, text='0', font=('Arial Black', 48, 'bold'),
    anchor='e', text_color=("black", "white")
)
display.pack(pady=(0, 20), padx=20, fill='x')

frame = ctk.CTkFrame(app, fg_color=("white", "black"))
frame.pack(padx=10, pady=10, fill="both", expand=True)

for i in range(4):
    frame.columnconfigure(i, weight=1)
for i in range(6):
    frame.rowconfigure(i, weight=1)

def press_wrapper(symbol):
    handle_press(symbol, display, history_display)

def key_handler(event):
    key = event.char
    # Цифры и базовые операторы
    if key in '0123456789+-^%':
        press_wrapper(key)
    elif key == '*' or key.lower() == 'x':
        press_wrapper('x')
    elif key == '/':
        press_wrapper(':')
    elif key in ['.', ',']:
        press_wrapper('.')
    elif event.keysym == 'Return' or key == '=':
        press_wrapper('=')
    elif event.keysym == 'BackSpace':
        press_wrapper('⌫')  # Теперь logic.py правильно его обработает
    elif event.keysym == 'Escape':
        press_wrapper('C')


app.bind('<Key>', key_handler)


for row_index, row in enumerate(BUTTONS):
    for col_index, text in enumerate(row):
        btn = ctk.CTkButton(
            frame, text=text, corner_radius=10,
            command=lambda x=text: press_wrapper(x),
            fg_color=BTN_BG, hover_color=HOVER_C,
            text_color=TEXT_C, font=('Arial', 22, 'bold')
        )
        btn.grid(row=row_index, column=col_index, padx=5, pady=5, sticky="nsew")

app.mainloop()