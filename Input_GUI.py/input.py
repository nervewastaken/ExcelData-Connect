import tkinter as tk
from PIL import Image, ImageTk

# Create the main application window
root = tk.Tk()

# Set the window size to 1920x1080 pixels
root.config(width=1920,height=1080)

# Load the background image
background_image = Image.open("snew.png")  # Replace with your image file
background_photo = ImageTk.PhotoImage(background_image)

# Create a label to display the background image
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

# Add other widgets and functionality on top of the background

# Start the Tkinter main loop
root.mainloop()