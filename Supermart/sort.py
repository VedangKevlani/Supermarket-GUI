import tkinter as tk
import menu
from add import orderlist,quantitylist,pricelist

def sort_customer_order(mwindow):
    mwindow.destroy()
    sort_window = tk.Toplevel()
    # Set the title of the new window
    sort_window.title("GF Sort Customer Order")
    #Set dimensions for new window
    sort_window.minsize(500, 500)
    sort_window.maxsize(1200, 1200)
    sort_window.geometry("300x200+50+50")
    # Add some widgets to the new window
    tk.Label(sort_window, text="Sort current customer orders!").pack(padx=10, pady=10)
    sort_button = tk.Button(sort_window, text="Back to Main Menu", command=menu.create_new_window)
    sort_button.pack()
    return sort_window