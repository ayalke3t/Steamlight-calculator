import tkinter as tk
import math

# Color scheme
BG_COLOR = "#2A2F3B"
ENTRY_COLOR = "#1E232E"
BTN_NUM_COLOR = "#4A90E2"
BTN_OP_COLOR = "#9B59B6"
BTN_SCI_COLOR = "#2ECC71"
BTN_EQ_COLOR = "#E67E22"
BTN_CLR_COLOR = "#E74C3C"
TEXT_COLOR = "white"

# Button click logic
def button_click(char):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(char))

def clear_entry():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate_result():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Scientific functions
def scientific_function(func):
    try:
        val = float(entry.get())
        if func == "sqrt":
            result = math.sqrt(val)
        elif func == "log":
            result = math.log10(val)
        elif func == "ln":
            result = math.log(val)
        elif func == "exp":
            result = math.exp(val)
        elif func == "sin":
            result = math.sin(math.radians(val))
        elif func == "cos":
            result = math.cos(math.radians(val))
        elif func == "tan":
            result = math.tan(math.radians(val))
        elif func == "asin":
            result = math.degrees(math.asin(val))
        elif func == "acos":
            result = math.degrees(math.acos(val))
        elif func == "atan":
            result = math.degrees(math.atan(val))
        elif func == "sinh":
            result = math.sinh(val)
        elif func == "cosh":
            result = math.cosh(val)
        elif func == "tanh":
            result = math.tanh(val)
        elif func == "square":
            result = val ** 2
        elif func == "cube":
            result = val ** 3
        elif func == "reciprocal":
            result = 1 / val
        elif func == "factorial":
            if val.is_integer() and val >= 0:
                result = math.factorial(int(val))
            else:
                raise ValueError
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Window setup
window = tk.Tk()
window.title("AYALKBET Scientific Calculator")
window.attributes('-fullscreen', True)
window.configure(bg=BG_COLOR)
window.bind('<Escape>', lambda e: window.attributes('-fullscreen', False))

# Title label
title_label = tk.Label(window, text="AYALKBET SCI", font=("Arial", 24, "bold"), 
                      bg=BG_COLOR, fg=TEXT_COLOR, pady=10)
title_label.pack(fill=tk.X)

# Entry field
entry = tk.Entry(window, font=("Arial", 28), bg=ENTRY_COLOR, fg=TEXT_COLOR,
                insertbackground=TEXT_COLOR, bd=10, justify='right')
entry.pack(pady=20, padx=10, fill=tk.X)

# Button styling functions
def create_button(parent, text, color, command):
    btn = tk.Button(parent, text=text, font=("Arial", 14, "bold"),
                   bg=color, fg=TEXT_COLOR, activebackground=color,
                   activeforeground=TEXT_COLOR, relief="flat",
                   command=command, padx=10, pady=10)
    
    # Hover effects
    btn.bind("<Enter>", lambda e: btn.config(relief="sunken"))
    btn.bind("<Leave>", lambda e: btn.config(relief="flat"))
    return btn

# Main button frame
btn_frame = tk.Frame(window, bg=BG_COLOR)
btn_frame.pack(fill=tk.BOTH, expand=True, padx=10)

# Calculator buttons (added backspace ⌫ at top-left)
buttons = [
    ('⌫', 0, 0), ('^', 0, 1), ('%', 0, 2), ('π', 0, 3),
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('/', 4, 3),
]

for text, row, col in buttons:
    if text == 'π':
        action = lambda v=str(math.pi): button_click(v)
        color = BTN_SCI_COLOR
    elif text == 'e':
        action = lambda v=str(math.e): button_click(v)
        color = BTN_SCI_COLOR
    elif text == '^':
        action = lambda: button_click('**')
        color = BTN_OP_COLOR
    elif text == '%':
        action = lambda: button_click('%')
        color = BTN_OP_COLOR
    elif text == '⌫':
        action = backspace
        color = BTN_CLR_COLOR
    elif text == '=':
        action = calculate_result
        color = BTN_EQ_COLOR
    else:
        color = BTN_NUM_COLOR if text.isdigit() or text == '.' else BTN_OP_COLOR
        action = lambda ch=text: button_click(ch)

    btn = create_button(btn_frame, text, color, action)
    btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

# Scientific buttons frame
sci_frame = tk.Frame(window, bg=BG_COLOR)
sci_frame.pack(fill=tk.X, pady=10, padx=10)

sci_buttons = [
    ('√', 'sqrt'), ('log10', 'log'), ('ln', 'ln'), ('exp', 'exp'),
    ('sin', 'sin'), ('cos', 'cos'), ('tan', 'tan'),
    ('sin⁻¹', 'asin'), ('cos⁻¹', 'acos'), ('tan⁻¹', 'atan'),
    ('sinh', 'sinh'), ('cosh', 'cosh'), ('tanh', 'tanh'),
    ('x²', 'square'), ('x³', 'cube'), ('1/x', 'reciprocal'),
    ('n!', 'factorial'),
]

for i, (label, func) in enumerate(sci_buttons):
    btn = create_button(sci_frame, label, BTN_SCI_COLOR, 
                       lambda f=func: scientific_function(f))
    btn.grid(row=i//4, column=i%4, sticky="nsew", padx=2, pady=2)

# Clear button
clear_btn = create_button(window, 'CLEAR', BTN_CLR_COLOR, clear_entry)
clear_btn.pack(fill=tk.X, padx=10, pady=10)

# Configure grid weights
for i in range(5):
    btn_frame.rowconfigure(i, weight=1)
for j in range(4):
    btn_frame.columnconfigure(j, weight=1)

for i in range(4):
    sci_frame.columnconfigure(i, weight=1)

window.mainloop()