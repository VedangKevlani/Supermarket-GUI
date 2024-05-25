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
    showtable = tk.Button(view_window, text="Show Order", command=lambda: create_order_table(view_window))
    showtable.pack()

    calculate_final_price()
    view_button = tk.Button(view_window, text="Back to Main Menu", command=menu.create_new_window)
    view_button.pack()
    return view_window

def create_order_table(add_window):
    # Create a frame to hold the table elements
    table_frame = tk.Frame(add_window, borderwidth=1, relief="groove")
    table_frame.pack(padx=10, pady=10)

    # Define column headers
    tk.Label(table_frame, text="No.", width=5).grid(row=0, column=0, padx=5, pady=5)
    tk.Label(table_frame, text="Item", width=20).grid(row=0, column=1, padx=5, pady=5)
    tk.Label(table_frame, text="Quantity", width=10).grid(row=0, column=2, padx=5, pady=5)
    tk.Label(table_frame, text="Total (JMD)", width=15).grid(row=0, column=3, padx=5, pady=5)

    # Display order details in rows
    for i, (item, quantity, price) in enumerate(zip(orderlist, quantitylist, pricelist), start=1):
        total_price = quantity * price  # Calculate total price for each item

        tk.Label(table_frame, text=str(i)).grid(row=i, column=0, padx=5, pady=5)
        tk.Label(table_frame, text=item).grid(row=i, column=1, padx=5, pady=5)
        tk.Label(table_frame, text=f"{quantity:.1f}").grid(row=i, column=2, padx=5, pady=5)
        tk.Label(table_frame, text=f"{total_price:.2f}").grid(row=i, column=3, padx=5, pady=5)  # Format total price to 2 decimal places

def calculate_final_price():
    for i in range(0, len(orderlist)):
        finalprice = float(quantitylist[i]) * float(pricelist[i]) #fix this error tomorrow
        finalpricelist.append(finalprice)
    