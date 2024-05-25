import tkinter as tk
import menu
from add import orderlist,quantitylist,pricelist

def delete_customer_order(mwindow):
    mwindow.destroy()
    delete_window = tk.Toplevel()
    # Set the title of the new window
    delete_window.title("GF Delete Customer Order")
    #Set dimensions for new window
    delete_window.minsize(500, 500)
    delete_window.maxsize(1200, 1200)
    delete_window.geometry("300x200+50+50")
    # Add some widgets to the new window
    tk.Label(delete_window, text="Delete current customer order!").pack(padx=10, pady=10)
    delete_button = tk.Button(delete_window, text="Back to Main Menu", command=menu.create_new_window)
    delete_button.pack()
    return delete_window