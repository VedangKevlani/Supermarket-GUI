import tkinter as tk
from PIL import Image, ImageTk
import add
import view
import update
import delete
import search
import sort

def create_new_window():
    # Create a new window
    menu_window = tk.Toplevel()

    image = Image.open("generalfoodslogo.png")
    size = (100, 100)
    image = image.resize(size)
    # Convert the image to a Tkinter-compatible image
    photo = ImageTk.PhotoImage(image)

    window_img = tk.Label(menu_window, image=photo)
    window_img.image = photo  # Keep a reference to avoid garbage collection
    window_img.pack(side="top", anchor="n")
    
    menu_window.title("GF Main Menu")
    #Set dimensions for new window
    menu_window.minsize(500, 500)
    menu_window.maxsize(1200, 1200)
    menu_window.geometry("300x200+50+50")
    
    # Add some widgets to the new window
    tk.Label(menu_window, text="Welcome to the Main Menu!").pack(padx=10, pady=10)
    tk.Label(menu_window, text="Select an option to proceed.").pack(padx=10, pady=10)
    # Add feature
    add_label = tk.Label(menu_window, text="Add a new customer")
    add_label.pack()
    
    add_button = tk.Button(menu_window, text="Select", command=lambda: add.add_new_customer(menu_window))
    add_button.pack()
    # Search feature
    search_label = tk.Label(menu_window, text="Search for an existing customer")
    search_label.pack()
    
    search_button = tk.Button(menu_window, text="Select", command=lambda: search.search_customer_order(menu_window))
    search_button.pack()
    # View feature
    view_label = tk.Label(menu_window, text="View current customer's order")
    view_label.pack()
    
    view_button = tk.Button(menu_window, text="Select", command=lambda: view.view_customer_order(menu_window))
    view_button.pack()
    # Update feature
    update_label = tk.Label(menu_window, text="Update current customer's order")
    update_label.pack()
    
    update_button = tk.Button(menu_window, text="Select", command=lambda: update.update_customer_order(menu_window))
    update_button.pack()
    # Delete feature
    delete_label = tk.Label(menu_window, text="Delete current customer's order")
    delete_label.pack()
    
    delete_button = tk.Button(menu_window, text="Select", command=lambda: delete.delete_customer_order(menu_window))
    delete_button.pack()
    # Sort feature
    sort_label = tk.Label(menu_window, text="Sort current customer orders")
    sort_label.pack()
    
    sort_button = tk.Button(menu_window, text="Select", command=lambda: sort.sort_customer_order(menu_window))
    sort_button.pack(padx=10, pady=10)
    # Close feature
    tk.Button(menu_window, text="Close", command=menu_window.destroy).pack()
    return menu_window