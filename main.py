import tkinter as tk

# update the entry widget
def update_entry(entry, value):
    # get the current text in the entry widget
    current_text = entry.get()
    clear_entry(entry)
    # insert the current text followed by the new value into the entry widget
    entry.insert(0, current_text + value)

# evaluate the expression in the entry widget
def evaluate_entry(entry):
    try:
        print(eval(entry.get()))
        # takes the current text in the entry widget, evaluates it as a python expression, and stores the result in the result variable
        result = eval(entry.get())
        clear_entry(entry)
        # inserts the evaluated result as a string into the entry widget
        entry.insert(0, str(result))
    except Exception as e:
        clear_entry(entry)
        # insert "Error" into the entry widget to indicate that an error occurred
        entry.insert(0, "Error")
        
# clear the entry widget
def clear_entry(entry):
    entry.delete(0, tk.END)

root = tk.Tk()

# sets title to "Calculator" (most useful comment)
root.title("Calculator")

# creates entry for cool numbers
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# probably explained it duh
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=4, height=2, font=('Arial', 18),
                           command=lambda e=entry: evaluate_entry(e))
    elif text == 'C':
        button = tk.Button(root, text=text, width=4, height=2, font=('Arial', 18),
                           command=lambda e=entry: clear_entry(e))
    else:
        button = tk.Button(root, text=text, width=4, height=2, font=('Arial', 18),
                           command=lambda e=entry, val=text: update_entry(e, val))
    button.grid(row=row, column=col, padx=5, pady=5)

# run the application
root.mainloop()
