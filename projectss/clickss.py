import tkinter as tk
from tkinter import messagebox
import random

class ClickTheButtonGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Click the Button Game")
        self.root.geometry("300x200")

        self.score = 0
        self.time_left = 10  # 10 seconds to play

        self.score_label = tk.Label(root, text=f"Score: {self.score}", font=("Arial", 16))
        self.score_label.pack(pady=10)

        self.timer_label = tk.Label(root, text=f"Time left: {self.time_left}", font=("Arial", 16))
        self.timer_label.pack(pady=10)

        # Colorful "Click Me!" button
        self.click_button = tk.Button(
            root,
            text="Click Me!",
            font=("Arial", 14),
            bg="lightblue",  # Background color
            fg="darkblue",   # Text color
            activebackground="yellow",  # Background color when clicked
            activeforeground="red",     # Text color when clicked
            command=self.increment_score
        )
        self.click_button.pack(pady=20)

        self.update_timer()

    def increment_score(self):
        self.score += 1
        self.score_label.config(text=f"Score: {self.score}")

        # Move the button to a random position
        new_x = random.randint(0, 250)
        new_y = random.randint(0, 150)
        self.click_button.place(x=new_x, y=new_y)

        # Change button color dynamically
        colors = ["lightgreen", "lightcoral", "lightpink", "lightyellow", "lavender"]
        self.click_button.config(bg=random.choice(colors))

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time left: {self.time_left}")
            self.root.after(1000, self.update_timer)
        else:
            self.click_button.config(state=tk.DISABLED)
            messagebox.showinfo("Game Over", f"Time's up! Your final score is {self.score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = ClickTheButtonGame(root)
    root.mainloop()