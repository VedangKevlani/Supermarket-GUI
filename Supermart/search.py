import tkinter as tk
import menu
from add import orderlist,quantitylist,pricelist

def search_customer_order(mwindow):
    mwindow.destroy()
    search_window = tk.Toplevel()
    # Set the title of the new window
    search_window.title("GF Search Customer Order")
    #Set dimensions for new window
    search_window.minsize(500, 500)
    search_window.maxsize(1200, 1200)
    search_window.geometry("300x200+50+50")
    # Add some widgets to the new window
    tk.Label(search_window, text="Search current customer order!").pack(padx=10, pady=10)
    search_button = tk.Button(search_window, text="Back to Main Menu", command=menu.create_new_window)
    search_button.pack()
    return search_window