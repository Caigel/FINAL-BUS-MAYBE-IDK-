
import tkinter as tk
from tkinter import ttk

class TimeApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1000x1000')
        self.root.title("Canvas")
        self.root.configure(bg='black')

        self.time = 0

        # Create the initial button
        self.start_button = ttk.Button(root, text="Press me to begin", command=self.start_button)
        self.start_button.pack(pady=10)

    def start_button(self):
        # Forget the start button
        self.start_button.pack_forget()

        # Show instructions and create the "BIG AND WOW" button
        self.instruction_label = tk.Label(self.root, text="Please select your current bus stop", bg='black', fg='white')
        self.instruction_label.pack(pady=10)

        self.big_and_wow_button = ttk.Button(self.root, text="BIG AND WOW", command=self.on_big_and_wow_button_press)
        self.big_and_wow_button.pack(pady=10)

    def on_big_and_wow_button_press(self):
        # Hide the "BIG AND WOW" button
        self.big_and_wow_button.pack_forget()
        # Increment total_time by 1
        self.increment_total_time(1)
        self.instruction_label.pack_forget()
        instruction_label_2 = tk.Label(self.root, text="Please select the bus stop where you wish to go", bg='black', fg='white')
        instruction_label_2.pack(pady=10)

        
    def increment_total_time(self, value):
        # Increment total_time by specified value and print the updated value
        self.time += value
        print(f"Total Time: {self.time}")

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()

    # Create an instance of the TimeApp class
    app = TimeApp(root)

    # Start the main event loop
    root.mainloop()
