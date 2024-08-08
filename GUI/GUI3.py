import tkinter as tk
from tkinter import messagebox

class VendingMachine:
    def __init__(self, root):
        self.root = root
        self.root.title("Vending Machine - Graphics Cards")
        self.cards = {
            "GTX 1650": {"price": 150, "details": "Entry-level card with 4GB VRAM."},
            "RTX 3060": {"price": 300, "details": "Mid-range card with 12GB VRAM, good for gaming."},
            "RTX 4080": {"price": 600, "details": "High-end card with 16GB VRAM, excellent for 4K gaming."}
        }
        self.selected_card = None
        self.balance = 0.0
        self.create_widgets()

    def create_widgets(self):
        # Frame for card buttons
        card_frame = tk.Frame(self.root)
        card_frame.pack(pady=10)

        # Create buttons for each graphics card
        for card, info in self.cards.items():
            tk.Button(card_frame, text=f"{card} - ${info['price']}",
                      command=lambda c=card: self.select_card(c)).pack(pady=5, fill=tk.X)

        # Frame for information and buttons
        info_frame = tk.Frame(self.root)
        info_frame.pack(pady=10)

        self.info_label = tk.Label(info_frame, text="Select a graphics card", font=("Helvetica", 12))
        self.info_label.pack(pady=10)

        self.purchase_button = tk.Button(info_frame, text="Purchase", command=self.purchase_card, bg="green", fg="white")
        self.purchase_button.pack(side=tk.LEFT, padx=5)

        self.reset_button = tk.Button(info_frame, text="Reset", command=self.reset_selection, bg="red", fg="white")
        self.reset_button.pack(side=tk.LEFT, padx=5)

        # Frame for balance and adding money
        balance_frame = tk.Frame(self.root)
        balance_frame.pack(pady=10)

        self.balance_label = tk.Label(balance_frame, text=f"Balance: ${self.balance:.2f}", font=("Helvetica", 12))
        self.balance_label.pack(pady=5)

        self.add_money_entry = tk.Entry(balance_frame)
        self.add_money_entry.pack(pady=5)

        self.add_money_button = tk.Button(balance_frame, text="Add Money", command=self.add_money)
        self.add_money_button.pack(pady=5)

    def select_card(self, card):
        self.selected_card = card
        price = self.cards[card]['price']
        self.info_label.config(text=f"Selected: {card} - ${price}\n{self.cards[card]['details']}")

    def purchase_card(self):
        if self.selected_card:
            price = self.cards[self.selected_card]['price']
            if self.balance >= price:
                self.balance -= price
                messagebox.showinfo("Purchase Confirmation", f"Purchased {self.selected_card} for ${price}")
                self.reset_selection()
            else:
                messagebox.showwarning("Insufficient Funds", "Not enough balance to purchase this item.")
        else:
            messagebox.showwarning("No Selection", "Please select a graphics card before purchasing.")
        self.update_balance_label()

    def add_money(self):
        try:
            amount = float(self.add_money_entry.get())
            if amount > 0:
                self.balance += amount
                self.add_money_entry.delete(0, tk.END)
                self.update_balance_label()
            else:
                messagebox.showwarning("Invalid Amount", "Please enter a positive amount.")
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")

    def update_balance_label(self):
        self.balance_label.config(text=f"Balance: ${self.balance:.2f}")

    def reset_selection(self):
        self.selected_card = None
        self.info_label.config(text="Select a graphics card")

if __name__ == "__main__":
    root = tk.Tk()
    app = VendingMachine(root)
    root.mainloop()
