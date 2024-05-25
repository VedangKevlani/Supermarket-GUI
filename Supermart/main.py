import datetime
import tkinter as tk
import os
from PIL import Image, ImageTk
import menu

window = tk.Tk()
window.title("GF User Login")

# Set the window size
window.minsize(500, 500)
window.maxsize(1200, 1200)
window.geometry("300x200+50+50")

image = Image.open("generalfoodslogo.png")
size = (100, 100)
image = image.resize(size)
# Convert the image to a Tkinter-compatible image
photo = ImageTk.PhotoImage(image)

window_img = tk.Label(window, image=photo)
window_img.image = photo  # Keep a reference to avoid garbage collection
window_img.pack(side="top", anchor="n")

current_date = datetime.datetime.now()
date_string = current_date.strftime("%B %d, %Y")

greeting = tk.Label(window, text="Welcome, user! Today's Date is: " + date_string)
greeting.pack()

username_label = tk.Label(window, text="Enter username: ")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

password_label = tk.Label(window, text="Enter password: ")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

def toggle_password_visibility():
    if password_entry["show"] == "*":
        password_entry.config(show="")
        show_button.config(text="Hide password")
    else:
        password_entry.config(show="*")
        show_button.config(text="Show password")

show_button = tk.Button(window, text="Show password", command=toggle_password_visibility)
show_button.pack(padx=10, pady=10)

def check_file():
    print("Checking file...")
    username_input = username_entry.get()
    password_input = password_entry.get()
    # print("Username input:", username_input)
    # print("Password input:", password_input)
    filename = "Supermart/cred.txt"
    print("Current working directory:", os.getcwd())
    if os.path.isfile(filename):
        # print("File found")
        with open(filename, "r") as credfile:
            numlines = credfile.readlines()
            for l in range(0, len(numlines)-1, 2):
                if username_input == numlines[l].strip() and password_input == numlines[l+1].strip():
                    print("Login successful")
                    new_window = menu.create_new_window()
                    window.withdraw()  # Hide the old window
                    new_window.mainloop()  # Show the new window
                    return  # Exit the function after successful login
            # If no match is found, display error
            error_label.config(text="Incorrect entry details. Please try again.")
            print("Incorrect entry details")
    else:
        error_label.config(text="Credentials file not found.")
        print("Credentials file not found")

error_label = tk.Label(window, text="")
error_label.pack()  
enter = tk.Button(window, text="Enter", command=check_file)
enter.pack()

# Start the event loop
window.mainloop()
