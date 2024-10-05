import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Input and Button GUI")
root.geometry("300x150")  # Set the window size

# Function to be called when the button is clicked
def buttoncall():
    address = entry.get()  # Get text from the entry box
    organize_file( address)

# Label for entry
label = tk.Label(root, text="Enter something:")
label.pack(pady=10)  # Add padding around the label

# Entry (input block) where user can type text
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Button to trigger the function show_input
button = tk.Button(root, text="Submit", command=buttoncall)
button.pack(pady=10)

# Start the GUI event loop
root.mainloop()