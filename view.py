import tkinter as tk
import menu
from add import orderlist, quantitylist, pricelist

finalpricelist = []
def view_customer_order(mwindow):
    mwindow.destroy()
    view_window = tk.Toplevel()
    # Set the title of the new window
    view_window.title("GF View Customer Order")
    #Set dimensions for new window
    view_window.minsize(500, 500)
    view_window.maxsize(1200, 1200)
    view_window.geometry("300x200+50+50")
    # Add some widgets to the new window
    tk.Label(view_window, text="View current customer order!").pack(padx=10, pady=10)
    #tk.Label(view_window, text=cname + "'s Order:").pack(padx=10, pady=10)
    
    tk.Label(view_window, text="Order Catalog: {}".format(orderlist)).pack()
    tk.Label(view_window, text="Quantity Catalog: {}".format(quantitylist)).pack()
    tk.Label(view_window, text="Unit Catalog: {}".format(pricelist)).pack()
    calculate_final_price()
    tk.Label(view_window, text="Final Price Catalog: {}".format(finalpricelist)).pack()
    view_button = tk.Button(view_window, text="Back to Main Menu", command=menu.create_new_window)
    view_button.pack()
    return view_window

def calculate_final_price():
    for i in range(0, len(orderlist)):
        finalprice = float(quantitylist[i]) * float(pricelist[i]) #fix this error tomorrow
        finalpricelist.append(finalprice)
    