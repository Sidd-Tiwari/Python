import tkinter as tk

# Function to handle button clicks and update the display
def button_click(number):
    current = display_var.get()
    display_var.set(current + str(number))

def clear_display():
    display_var.set("")

def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(result)
    except Exception:
        display_var.set("Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create a variable to store the display value
display_var = tk.StringVar()

# Create the display widget
display = tk.Entry(root, textvariable=display_var, font=("Helvetica", 16), bd=10, insertwidth=4, width=14, justify="right")
display.grid(row=0, column=0, columnspan=4)

# Define the calculator buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create and place the buttons
row_val, col_val = 1, 0
for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=("Helvetica", 16), command=lambda b=button: button_click(b) if b != "=" else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create and place the clear button
tk.Button(root, text="Clear", padx=20, pady=20, font=("Helvetica", 16), command=clear_display).grid(row=5, column=0, columnspan=4)

# Run the GUI
root.mainloop()
