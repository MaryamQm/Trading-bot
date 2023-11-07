# import the necessary modules
import alpaca_trade_api as tradeapi # imports the alpaca python SDK for interacting with alpacas API
import argparse # to handle command-line arguments
import time
import pandas as pd
from keys import API_KEY, SECRET_KEY

class Alpaca_Trade():
    def __init__(self, API_KEY, SECRET_KEY, symbol):
        # Initialize the Alpaca API and other attributes
        self.key = API_KEY
        self.secret = SECRET_KEY
        self.alpaca_endpoint = 'https://paper-api.alpaca.markets'
        self.api = tradeapi.REST(self.key, self.secret, self.alpaca_endpoint, api_version='v2')
        self.symbol = symbol

    def get_orders(self):
        # Fetch and return a list of orders
        orders = self.api.list_orders(status='all')
        return orders

    def buy_shares(self, quantity):
        # Function to buy shares
        try:
            order = self.api.submit_order(
                symbol=self.symbol,
                qty=quantity,
                type='market',
                side='buy',
                time_in_force='day'
            )
            return order
        except Exception as e:
            print(f"Error placing buy order: {e}")
            return None

    def sell_shares(self, quantity):
        # Function to sell shares
        try:
            order = self.api.submit_order(
                symbol=self.symbol,
                qty=quantity,
                type='market',
                side='sell',
                time_in_force='day'
            )
            return order
        except Exception as e:
            print(f"Error placing sell order: {e}")
            return None

    def get_position(self): # get current position
        try:
            position = self.api.get_position(self.symbol)
            return position.qty
        except:
            return 0

    def submit_order(self, target): # buy and sell orders
        current_position = self.get_position()
        delta = target - current_position
        if delta == 0:
            return

        if delta > 0:
            buy_quantity = delta
            
            print(f'Buying {buy_quantity} {self.symbol} shares')
            
            self.order = self.api.submit_order(
                symbol=self.symbol,
                qty=buy_quantity,
                type='market',
                side='buy',
                time_in_force='day'
            )

        elif delta < 0:
            sell_quantity = abs(delta)
            print(f'Selling {sell_quantity} {self.symbol} shares')
            
            self.order = self.api.submit_order(
                symbol=self.symbol,
                qty=sell_quantity,
                type='market',
                side='sell',
                time_in_force='day'
            )
# to check if script is being run as main program and not imported as module (code wil execute if only run directly)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Alpaca Trading Bot')
    parser.add_argument('--buy', type=int, help='Number of shares to buy')
    parser.add_argument('--sell', type=int, help='Number of shares to sell')  
    parser.add_argument('--cancel', type=str, help='Order ID to cancel')  
    parser.add_argument('--show-position', action='store_true', help='Show current position')
    parser.add_argument('--show-orders', action='store_true', help='Show current orders')
    args = parser.parse_args()
    
    aapl = Alpaca_Trade(API_KEY, SECRET_KEY, 'AAPL') # creates instance of the 'alpaca_trade' class passing the necessary parameters to the constructor
    
    if args.show_position: # if included when running script then:
            # Add a delay to give time for position update
            time.sleep(5)  # Wait for 5 seconds
            current_position = aapl.get_position()
            print(f'Current position in {aapl.symbol}: {current_position} shares')
    elif args.buy is not None:
        aapl.submit_order(args.buy)
    elif args.sell is not None:
        aapl.submit_order(-args.sell) # negative value to sell
    elif args.cancel is not None:
        # Initialize the Alpaca API
        api = tradeapi.REST(API_KEY, SECRET_KEY, base_url='https://paper-api.alpaca.markets', api_version='v2')
   
        try:
            # Attempt to cancel the specified order
            api.cancel_order(args.cancel)
            print(f'Order {args.cancel} has been cancelled.')
        except tradeapi.rest.APIError as e:
            print(f'Error: {e}')
            
    elif args.show_orders:
        # Initialize the Alpaca API
        api = tradeapi.REST(API_KEY, SECRET_KEY, base_url='https://paper-api.alpaca.markets', api_version='v2')
        
        # Get a list of all your orders
        orders = api.list_orders()
        
        # Create a DataFrame to display the orders as a table
        orders_df = pd.DataFrame({
            'Order ID': [order.id for order in orders],
            'Symbol': [order.symbol for order in orders],
            'Quantity': [order.qty for order in orders],
            'Order Type': [order.type for order in orders],
            'Side': [order.side for order in orders],
            'Status': [order.status for order in orders],
        })
        
        print(orders_df)
    else:
        print('Please provide valid options. Use --show-position to display your current position, --buy to specify the number of shares to buy, --sell to specify the number of shares to sell, --cancel to specify the order ID to cancel, or --show-orders to display your current orders.')