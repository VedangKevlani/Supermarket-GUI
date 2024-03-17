import datetime
import tkinter as tk
import os
import menu

# Create a window
window = tk.Tk()

# Set the window title
window.title("GF User Login")

# Set the window size
window.minsize(500, 500)
window.maxsize(1200, 1200)
window.geometry("300x200+50+50")

current_date = datetime.datetime.now()
date_string = current_date.strftime("%B %d, %Y")
# Create a greeting
greeting = tk.Label(window, text="Welcome, user! Today's Date is: "+date_string)

#Create an image
window_image = tk.PhotoImage(file="generalfoodslogo.gif")
window_img = tk.Label(window, image=window_image)
window_img.pack()

#Add greeting label to window
greeting.pack()

#Create a label which says username and add it to the window
username_label = tk.Label(window, text="Enter username: ")
username_label.pack()

#Create a textfield and add it to the window
username_entry = tk.Entry(window)
username_entry.pack()

#Create a label which says password and add it to the window
password_label = tk.Label(window, text="Enter password: ")
password_label.pack()

#Create a textfield and add it to the window
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
    
def close_old_window():
    # Destroy the current (old) window
    window.destroy()
    
def check_file():
    print("Checking file...")
    username_input = username_entry.get()
    password_input = password_entry.get()
    #print(username_input)
    #print(password_input)
    filename = "cred.txt"
    if os.path.isfile(filename):
        with open(filename, "r") as credfile:
            numlines = credfile.readlines()
            for l in range(0, len(numlines)-1, 2):
                if username_input == numlines[l].strip() and password_input == numlines[l+1].strip():
                    new_window = menu.create_new_window()
                    window.withdraw()  # Hide the old window
                    new_window.mainloop()  # Show the new window
                    break
                else:
                    error = tk.Label(window, text="Incorrect entry details. Please try again.")
                    error.pack()
                    break

#Create a button to enter data    
enter = tk.Button(window, text="Enter", command=check_file)
enter.pack()

# Start the event loop
window.mainloop()
