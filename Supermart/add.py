import tkinter as tk
import menu
orderlist = []
quantitylist = []
pricelist = []

def add_new_customer(mwindow):
    mwindow.destroy()
    add_window = tk.Toplevel()
    # Set the title of the new window
    add_window.title("GF Add a Customer")
    #Set dimensions for new window
    add_window.minsize(500, 500)
    add_window.maxsize(1200, 1200)
    add_window.geometry("300x200+50+50")
    # Add some widgets to the new window
    tk.Label(add_window, text="Add a new customer!").pack(padx=10, pady=10)
    tk.Label(add_window, text="Fill out the information as prompted.").pack(padx=10, pady=10)
    
    customer_namelabel = tk.Label(add_window, text="Enter customer name: ")
    customer_namelabel.pack(padx=10, pady=10)
    
    customer_namefield = tk.Entry(add_window)
    customer_namefield.pack()
    
    def customer_name_call():
        #Greet customer
        cname = customer_namefield.get()
        tk.Label(add_window, text="Hello " + cname).pack()
        customer_namelabel.pack_forget()
        customer_namefield.pack_forget()
        customer_button.pack_forget()
        order = order_details()
        
    def order_details():
        #First stage of add process - add item name
        customer_orderlabel = tk.Label(add_window, text="Place a single order. Enter the name of the item.")
        customer_orderlabel.pack(padx=10, pady=10)
        
        customer_orderfield = tk.Entry(add_window)
        customer_orderfield.pack()
        
        order_button = tk.Button(add_window, text="Enter", command=lambda: get_customerorder(customer_orderlabel, customer_orderfield, order_button))
        order_button.pack()
        
    def get_customerorder(corderlabel, corder, corderbutton):
        #Retreive customer order from textfield
        custorder = corder.get()
        orderlist.append(custorder)
        tk.Label(add_window, text="Current Catalog: {}".format(orderlist)).pack()
        corderlabel.pack_forget()
        corder.pack_forget()
        corderbutton.pack_forget()
        quantity_details()
        
        
    def another_order():
        #Add another order
        opt_orderlabel = tk.Label(add_window, text="Add another item? [y/n]")
        opt_orderlabel.pack()
        
        opt_orderfield = tk.Entry(add_window)
        opt_orderfield.pack()
        opt_orderbutton = tk.Button(add_window, text="Enter", command=lambda: get_optorder(opt_orderlabel, opt_orderfield, opt_orderbutton))
        opt_orderbutton.pack()
        
    def get_optorder(optlabel, optfield, optbutton):
        #Optional Customer order
        opt = optfield.get().lower()
        optlabel.pack_forget()
        optfield.pack_forget()
        optbutton.pack_forget()
        if(opt == 'y'):
            order_details()
        elif(opt == 'n'):
            tk.Label(add_window, text="Final Catalog: {}".format(orderlist)).pack()
            showtable = tk.Button(add_window, text="Show Order", command=lambda: create_order_table(add_window))
            showtable.pack()

            order_button = tk.Button(add_window, text="Finish Order", command=menu.create_new_window)
            order_button.pack()
        else:
            tk.Label(add_window, text="Invalid input. Please enter 'y' or 'n' only.").pack()
            repeat_order = tk.Button(add_window, text="Retry", command=another_order)
            repeat_order.pack()
    
    def quantity_details():
        #Second stage of add process - add quantity
        customer_quantitylabel = tk.Label(add_window, text="Enter a quantity in numbers [lb/kg]")
        customer_quantitylabel.pack()
        
        customer_quantityfield = tk.Entry(add_window)
        customer_quantityfield.pack()
        
        order_button = tk.Button(add_window, text="Enter", command=lambda: get_quantity(customer_quantitylabel, customer_quantityfield, order_button))
        order_button.pack()
        
    def get_quantity(cquantitylabel, cquantityfield, obutton):
        #Retreive customer quantity from textfield
        custquantity = float(cquantityfield.get())
        quantitylist.append(custquantity)
        cquantitylabel.pack_forget()
        cquantityfield.pack_forget()
        obutton.pack_forget()
        price_details()
        
    def price_details():
        #Third stage of add process - add price
        customer_pricelabel = tk.Label(add_window, text="Enter the unit price to charge [JMD]: ")
        customer_pricelabel.pack()
        
        customer_pricefield = tk.Entry(add_window)
        customer_pricefield.pack()
        
        order_button = tk.Button(add_window, text="Enter", command=lambda: get_price(customer_pricelabel, customer_pricefield, order_button))
        order_button.pack()
        
    def get_price(cpricelabel, cpricefield, obutton):
        #Retreive customer price from textfield
        custprice = float(cpricefield.get())
        pricelist.append(custprice)
        cpricelabel.pack_forget()
        cpricefield.pack_forget()
        obutton.pack_forget()
        another_order()
    
    customer_button = tk.Button(add_window, text="Enter", command=customer_name_call)
    customer_button.pack()

def create_order_table(add_window):
    # Create a frame to hold the table elements
    table_frame = tk.Frame(add_window, borderwidth=1, relief="groove")
    table_frame.pack(padx=10, pady=10)

    # Define column headers
    tk.Label(table_frame, text="No.", width=5).grid(row=0, column=0, padx=5, pady=5)
    tk.Label(table_frame, text="Item", width=20).grid(row=0, column=1, padx=5, pady=5)
    tk.Label(table_frame, text="Quantity", width=10).grid(row=0, column=2, padx=5, pady=5)
    tk.Label(table_frame, text="Unit Price (JMD)", width=15).grid(row=0, column=3, padx=5, pady=5)

    # Display order details in rows
    for i, (item, quantity, price) in enumerate(zip(orderlist, quantitylist, pricelist), start=1):
        tk.Label(table_frame, text=str(i)).grid(row=i, column=0, padx=5, pady=5)
        tk.Label(table_frame, text=item).grid(row=i, column=1, padx=5, pady=5)
        tk.Label(table_frame, text=str(quantity)).grid(row=i, column=2, padx=5, pady=5)
        tk.Label(table_frame, text=f"{price:.2f}").grid(row=i, column=3, padx=5, pady=5)  # Format price to 2 decimal places
    
    return add_window

