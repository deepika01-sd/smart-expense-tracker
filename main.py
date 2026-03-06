import tkinter as tk
from expense_manager import add_expense, get_total_expense
def add():
    amount = amount_entry.get()
    category = category_entry.get()
    description = description_entry.get()

    add_expense(amount, category, description)

    result_label.config(text="Expense Added!")

def show_total():
    total = get_total_expense()
    result_label.config(text=f"Total Expense: ₹{total}")

root = tk.Tk()
root.title("Smart Expense Tracker")
root.geometry("400x350")

tk.Label(root, text="Amount").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="Category").pack()
category_entry = tk.Entry(root)
category_entry.pack()

tk.Label(root, text="Description").pack()
description_entry = tk.Entry(root)
description_entry.pack()

tk.Button(root, text="Add Expense", command=add).pack(pady=10)
tk.Button(root, text="Show Total Expense", command=show_total).pack()

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()