# gui.py

import tkinter as tk
from tkinter import font
from backend import calculate_roi, check_luck


class EpicSevenTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Epic Seven ROI Tracker")
        self.root.geometry("600x550")
        self.root.configure(bg="#1e1e1e")

        header_font = font.Font(size=14, weight='bold')
        label_font = font.Font(size=12)

        self.start_skystone = tk.IntVar()
        self.end_skystone = tk.IntVar()
        self.regular_pulls = tk.IntVar(value=0)
        self.mystic_pulls = tk.IntVar(value=0)

        entry_bg = "#2d2d2d"
        entry_fg = "#ffffff"
        label_fg = "#dddddd"
        button_bg = "#3a3a3a"
        button_fg = "#ffffff"

        tk.Label(root, text="Start Skystone:", font=label_font, fg=label_fg, bg="#1e1e1e").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        tk.Entry(root, textvariable=self.start_skystone, font=label_font, width=10, bg=entry_bg, fg=entry_fg, insertbackground="white").grid(row=0, column=1)

        tk.Label(root, text="End Skystone:", font=label_font, fg=label_fg, bg="#1e1e1e").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        tk.Entry(root, textvariable=self.end_skystone, font=label_font, width=10, bg=entry_bg, fg=entry_fg, insertbackground="white").grid(row=1, column=1)

        tk.Label(root, text="Regular Pulls:", font=label_font, fg=label_fg, bg="#1e1e1e").grid(row=2, column=0, sticky="e")
        tk.Label(root, textvariable=self.regular_pulls, font=label_font, fg=entry_fg, bg="#1e1e1e").grid(row=2, column=1)
        tk.Button(root, text="+", font=label_font, width=3, bg=button_bg, fg=button_fg, command=self.increase_regular).grid(row=2, column=2)
        tk.Button(root, text="-", font=label_font, width=3, bg=button_bg, fg=button_fg, command=self.decrease_regular).grid(row=2, column=3)

        tk.Label(root, text="Mystic Pulls:", font=label_font, fg=label_fg, bg="#1e1e1e").grid(row=3, column=0, sticky="e")
        tk.Label(root, textvariable=self.mystic_pulls, font=label_font, fg=entry_fg, bg="#1e1e1e").grid(row=3, column=1)
        tk.Button(root, text="+", font=label_font, width=3, bg=button_bg, fg=button_fg, command=self.increase_mystic).grid(row=3, column=2)
        tk.Button(root, text="-", font=label_font, width=3, bg=button_bg, fg=button_fg, command=self.decrease_mystic).grid(row=3, column=3)

        self.output = tk.Label(root, text="Enter values and press 'Calculate ROI'", font=label_font, fg="#00ff99", bg="#1e1e1e", justify="left", anchor="nw", width=70, height=12, wraplength=580)
        self.output.grid(row=4, column=0, columnspan=4, pady=20, sticky="w")

        tk.Button(root, text="Calculate ROI", font=header_font, bg="#007acc", fg="white", command=self.calculate_roi).grid(row=5, column=0, columnspan=4, pady=10)
        tk.Button(root, text="Check Luck", font=header_font, bg="#5555aa", fg="white", command=self.check_luck).grid(row=6, column=0, columnspan=4, pady=5)

    def increase_regular(self):
        self.regular_pulls.set(self.regular_pulls.get() + 1)

    def decrease_regular(self):
        if self.regular_pulls.get() > 0:
            self.regular_pulls.set(self.regular_pulls.get() - 1)

    def increase_mystic(self):
        self.mystic_pulls.set(self.mystic_pulls.get() + 1)

    def decrease_mystic(self):
        if self.mystic_pulls.get() > 0:
            self.mystic_pulls.set(self.mystic_pulls.get() - 1)

    def calculate_roi(self):
        try:
            result_text = calculate_roi(
                self.start_skystone.get(),
                self.end_skystone.get(),
                self.regular_pulls.get(),
                self.mystic_pulls.get()
            )
            self.output.config(text=result_text)
        except Exception:
            self.output.config(text="Error in input values")

    def check_luck(self):
        try:
            result_text = check_luck(
                self.start_skystone.get(),
                self.end_skystone.get(),
                self.regular_pulls.get(),
                self.mystic_pulls.get()
            )
            self.output.config(text=result_text)
        except Exception as e:
            self.output.config(text=f"❌ Error occurred: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = EpicSevenTracker(root)
    root.mainloop()
