import tkinter as tk
import menu
from add import orderlist, quantitylist, pricelist

def update_customer_order(mwindow):
    mwindow.destroy()
    update_window = tk.Toplevel()
    # Set the title of the new window
    update_window.title("GF Update Customer Order")
    #Set dimensions for new window
    update_window.minsize(500, 500)
    update_window.maxsize(1200, 1200)
    update_window.geometry("300x200+50+50")
    # Add some widgets to the new window
    tk.Label(update_window, text="Update current customer order!").pack(padx=10, pady=10)

    update_button = tk.Button(update_window, text="Back to Main Menu", command=menu.create_new_window)
    update_button.pack()
    update_window.pack()

    def update_item(add_window):
        item_updatelabel = tk.Label(update_window, text="Enter the name of the item you want to update.")
        item_updatelabel.pack(padx=10, pady=10)
        
        item_orderfield = tk.Entry(update_window)
        item_orderfield.pack()

    return update_window