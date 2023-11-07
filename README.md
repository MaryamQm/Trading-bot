# Trading Bot Project

## Overview

The Trading Bot Project is a simple yet functional Python-based trading bot that allows users to interact with financial markets, specifically stocks. This bot is designed to demonstrate basic trading functionalities, such as buying and selling shares, viewing a portfolio, and displaying orders, using the Alpaca Paper Trading API. Please note that this project is for educational purposes and should not be used for real financial trading.

## Features

- Buy and sell shares of a specific stock.
- View your current portfolio holdings.
- Display your order history.

## Prerequisites

Before you get started with this project, you'll need the following:

- Python 3.x installed on your machine.
- Alpaca API keys for paper trading. You can sign up for a free account at [Alpaca](https://alpaca.markets/).
- The required Python libraries, as specified in the project's dependencies.

## Installation

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/your-username/trading-bot.git
   ```

2. Create a `keys.py` file in the project directory with your Alpaca API keys:

   ```python
   API_KEY = "your-api-key"
   SECRET_KEY = "your-secret-key"
   ```

3. Install the project dependencies:

   ```shell
   pip install -r requirements.txt
   ```

## Usage

1. Run the trading bot script to start the bot:

   ```shell
   python trading_bot.py
   ```

   The bot will execute in the console, and you can interact with it via the command line.

2. Optionally, run the GUI script to interact with the bot through a graphical user interface:

   ```shell
   python gui.py
   ```

   The GUI provides an easy way to buy and sell shares and view order history.

## License

This project is provided under the MIT License. Please review the [LICENSE](LICENSE) file for details.

## Disclaimer

This project is for educational purposes only. Do not use this trading bot for real trading. Always use caution and conduct thorough research before making any financial decisions.

## Acknowledgments

- Special thanks to [Alpaca](https://alpaca.markets/) for providing a paper trading platform and API.
- This project is inspired by educational resources and tutorials on algorithmic trading.

## Contributors

- [Maryam Ekhtiari] https://github.com/MaryamQm) - Project Lead
- [Maryam Ekhtiari](https://github.com/MaryamQm) - GUI Development
- [Maryam Ekhtiari](https://github.com/MaryamQm) - Documentation
