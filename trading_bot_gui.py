import tkinter as tk
from tkinter import ttk
from trading_bot import Alpaca_Trade
from keys import API_KEY, SECRET_KEY

def display_orders():
    # Function to display orders
    # Create an instance of the Alpaca_Trade class
    alpaca = Alpaca_Trade(API_KEY, SECRET_KEY, 'AAPL')

    # Fetch and display orders
    orders = alpaca.get_orders()
    for i, order in enumerate(orders, start=1):
        order_id = order.id
        symbol = order.symbol
        qty = order.qty
        order_type = order.type
        side = order.side
        status = order.status
        

        if order_type == 'limit':
                price = order.limit_price
        elif order_type == 'market':
            price = order.filled_avg_price
        else:
            price = "N/A"  # Handle other order types as needed

        # Insert order details into the Treeview widget
        tree.insert("", "end", values=(i, order_id, symbol, qty, order_type, side, status, price))

def buy_shares(quantity):
    # Function to buy shares
    alpaca = Alpaca_Trade(API_KEY, SECRET_KEY, 'AAPL')
    alpaca.buy_shares(quantity)
    display_orders()

def sell_shares(quantity):
    # Function to sell shares
    alpaca = Alpaca_Trade(API_KEY, SECRET_KEY, 'AAPL')
    alpaca.sell_shares(quantity)
    display_orders()

# Create the main application window
root = tk.Tk()
root.title("Alpaca Trading Bot GUI")

# Create a treeview widget to display the orders
tree = ttk.Treeview(root, columns=("Order ID", "Symbol", "Quantity", "Order Type", "Side", "Status", "Price"))
tree.heading("#1", text="Order ID")
tree.heading("#2", text="Symbol")
tree.heading("#3", text="Quantity")
tree.heading("#4", text="Order Type")
tree.heading("#5", text="Side")
tree.heading("#6", text="Status")
tree.heading("#7", text="Price")

tree.pack()

# Create buttons for actions
buy_button = tk.Button(root, text="Buy", command=lambda: buy_shares(20))  # Example: Buying 20 shares
buy_button.pack()

sell_button = tk.Button(root, text="Sell", command=lambda: sell_shares(10))  # Example: Selling 10 shares
sell_button.pack()

refresh_button = tk.Button(root, text="Refresh Orders", command=display_orders)
refresh_button.pack()

# Run the Tkinter main loop
root.mainloop()
