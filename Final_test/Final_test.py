import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk  

class VendingMachine:
    def __init__(self):
        self.history = []
        self.total_income = 0.0
        self.snacks = {
            'salmon': {'price': 30, 'stock': 10, 'image': 'salmon.png'},
            'tuna': {'price': 25, 'stock': 15, 'image': 'tuna.png'},
            'chicken': {'price': 35, 'stock': 8, 'image': 'chicken.png'}
        }
        self.inserted_money = 0.0

    def buy_snack(self, snack_name, quantity):
        if snack_name in self.snacks:
            snack = self.snacks[snack_name]
            if snack['stock'] >= quantity:
                total_price = snack['price'] * quantity
                if self.inserted_money >= total_price:
                    snack['stock'] -= quantity
                    self.total_income += total_price
                    self.inserted_money -= total_price
                    self.history.append({'snack': snack_name, 'price': total_price, 'quantity': quantity})
                    return f"You bought {quantity} {snack_name}(s) for {total_price} Baht"
                else:
                    return f"Not enough money! Please insert at least {total_price} Baht."
            else:
                return f"Sorry, only {snack['stock']} {snack_name}(s) are in stock!"
        else:
            return f"{snack_name} is not available."

    def insert_money(self, amount):
        self.inserted_money += amount
        return f"You inserted {amount} Baht. Total: {self.inserted_money} Baht."

    def refund(self):
        refund_amount = self.inserted_money
        self.inserted_money = 0
        return f"Refunded {refund_amount} Baht."

class VendingMachineGUI:
    def __init__(self, root):
        self.machine = VendingMachine()
        self.root = root
        self.root.title("Vending Machine")
        self.root.geometry("400x600")
        self.root.configure(bg="#f7f7f7")

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Vending Machine", font=("Arial", 24, "bold"), bg="#f7f7f7", fg="#5a5a5a")
        self.title_label.pack(pady=10)

        # Display the snacks in a Treeview with columns
        columns = ("Snack", "Price", "Stock")
        self.snack_tree = ttk.Treeview(self.root, columns=columns, show="headings", height=5)
        self.snack_tree.heading("Snack", text="Snack")
        self.snack_tree.heading("Price", text="Price (Baht)")
        self.snack_tree.heading("Stock", text="Stock")

        self.update_snack_tree()
        self.snack_tree.pack(pady=10)

        # Bind selection event to show snack image
        self.snack_tree.bind('<<TreeviewSelect>>', self.show_snack_image)

        # Image display area
        self.image_label = tk.Label(self.root, bg="#f7f7f7")
        self.image_label.pack(pady=10)

        # Label for Insert Money Entry
        self.insert_money_label = tk.Label(self.root, text="Insert Money (Baht):", font=("Arial", 14), bg="#f7f7f7", fg="#5a5a5a")
        self.insert_money_label.pack(pady=5)

        # Entry for inserting money
        self.insert_money_entry = tk.Entry(self.root, font=("Arial", 14), width=15)
        self.insert_money_entry.pack(pady=5)

        self.insert_button = tk.Button(self.root, text="Insert Money", command=self.insert_money, font=("Arial", 14), bg="#4CAF50", fg="#fff", padx=10, pady=5)
        self.insert_button.pack(pady=5)

        # Label for Quantity Entry
        self.quantity_label = tk.Label(self.root, text="Enter Quantity:", font=("Arial", 14), bg="#f7f7f7", fg="#5a5a5a")
        self.quantity_label.pack(pady=5)

        # Entry for selecting quantity
        self.quantity_entry = tk.Entry(self.root, font=("Arial", 14), width=10)
        self.quantity_entry.pack(pady=5)
        self.quantity_entry.insert(0, "1")

        self.buy_button = tk.Button(self.root, text="Buy", command=self.buy_snack, font=("Arial", 14), bg="#2196F3", fg="#fff", padx=10, pady=5)
        self.buy_button.pack(pady=5)

        self.refund_button = tk.Button(self.root, text="Refund", command=self.refund_money, font=("Arial", 14), bg="#F44336", fg="#fff", padx=10, pady=5)
        self.refund_button.pack(pady=5)

        self.total_income_label = tk.Label(self.root, text=f"Total income: {self.machine.total_income} Baht", font=("Arial", 16), bg="#f7f7f7", fg="#5a5a5a")
        self.total_income_label.pack(pady=10)

        self.inserted_money_label = tk.Label(self.root, text=f"Inserted money: {self.machine.inserted_money} Baht", font=("Arial", 16), bg="#f7f7f7", fg="#5a5a5a")
        self.inserted_money_label.pack(pady=10)

        self.status_label = tk.Label(self.root, text="Welcome! Insert money to start.", font=("Arial", 12, "italic"), bg="#f7f7f7", fg="#5a5a5a")
        self.status_label.pack(pady=10)

        self.history_button = tk.Button(self.root, text="Show Purchase History", command=self.show_history, font=("Arial", 14), bg="#FFC107", fg="#fff", padx=10, pady=5)
        self.history_button.pack(pady=5)

        self.footer_label = tk.Label(self.root, text="Thank you for using our vending machine!", font=("Arial", 10), bg="#f7f7f7", fg="#5a5a5a")
        self.footer_label.pack(side=tk.BOTTOM, pady=10)

    def update_snack_tree(self):
        for snack in self.snack_tree.get_children():
            self.snack_tree.delete(snack)
        for snack, details in self.machine.snacks.items():
            self.snack_tree.insert('', 'end', values=(snack, details['price'], details['stock']))

    def show_snack_image(self, event):
        selected_item = self.snack_tree.selection()
        if selected_item:
            snack_name = self.snack_tree.item(selected_item)['values'][0]
            snack_image_path = self.machine.snacks[snack_name]['image']
            try:
                # Load and display the image
                img = Image.open(snack_image_path)
                img = img.resize((150, 150), Image.ANTIALIAS)  # Resize the image
                self.photo = ImageTk.PhotoImage(img)  # Create a PhotoImage
                self.image_label.config(image=self.photo)  # Update the label to show the image
                self.image_label.image = self.photo  # Keep a reference to avoid garbage collection
            except Exception as e:
                print(f"Error loading image: {snack_image_path} - {e}")  # Debugging line
                self.image_label.config(text="Image not found.")

    def insert_money(self):
        try:
            amount = float(self.insert_money_entry.get())
            if amount > 0:
                message = self.machine.insert_money(amount)
                self.status_label.config(text=message)
                self.insert_money_entry.delete(0, tk.END)
                self.inserted_money_label.config(text=f"Inserted money: {self.machine.inserted_money} Baht")
            else:
                self.status_label.config(text="Please insert a positive amount.")
        except ValueError:
            self.status_label.config(text="Invalid input. Please enter a valid number.")

    def buy_snack(self):
        selected_item = self.snack_tree.selection()
        if selected_item:
            snack_name = self.snack_tree.item(selected_item)['values'][0]
            try:
                quantity = int(self.quantity_entry.get())
                if quantity > 0:
                    message = self.machine.buy_snack(snack_name, quantity)
                    self.status_label.config(text=message)
                    self.update_snack_tree()
                    self.total_income_label.config(text=f"Total income: {self.machine.total_income} Baht")
                    self.inserted_money_label.config(text=f"Inserted money: {self.machine.inserted_money} Baht")
                else:
                    self.status_label.config(text="Please enter a positive quantity.")
            except ValueError:
                self.status_label.config(text="Invalid quantity. Please enter a valid number.")
        else:
            self.status_label.config(text="Please select a snack to buy.")

    def refund_money(self):
        message = self.machine.refund()
        self.status_label.config(text=message)
        self.inserted_money_label.config(text=f"Inserted money: {self.machine.inserted_money} Baht")

    def show_history(self):
        if self.machine.history:
            history_text = "\n".join(f"{purchase['quantity']} x {purchase['snack']} - {purchase['price']} Baht" for purchase in self.machine.history)
            self.status_label.config(text=history_text)
        else:
            self.status_label.config(text="No purchase history available.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VendingMachineGUI(root)
    root.mainloop()
