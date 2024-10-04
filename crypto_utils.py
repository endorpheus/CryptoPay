import os
import json
import yfinance as yf
import logging
from typing import Tuple, List, Optional
from decimal import Decimal, getcontext

# Set a high precision for Decimal calculations
getcontext().prec = 28

# Setup logging
LOG_FILE = "logs/output.log"

# Delete the existing log file if it exists
if os.path.exists(LOG_FILE):
    try:
        os.remove(LOG_FILE)
    except Exception as e:
        print(f"Error deleting existing log file: {e}")

os.makedirs("logs", exist_ok=True)
logging.basicConfig(filename=LOG_FILE, level=logging.ERROR, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

TICKERS_FILE = "tickers_list.json"

def load_tickers() -> List[str]:
    """Load tickers from a JSON file or use default values."""
    try:
        if os.path.exists(TICKERS_FILE):
            with open(TICKERS_FILE, "r") as file:
                return json.load(file)
    except Exception as e:
        logging.error(f"Error loading tickers: {e}")
    return ["BTC-USD", "ETH-USD", "SOL-USD"]  # Default tickers

def save_tickers(tickers: List[str]) -> None:
    """Save current tickers to a JSON file."""
    try:
        with open(TICKERS_FILE, "w") as file:
            json.dump(tickers, file, indent=4)
    except Exception as e:
        logging.error(f"Error saving tickers: {e}")

def get_crypto_data(crypto_ticker: str) -> Tuple[Optional[Decimal], Optional[str]]:
    """Fetch the current price and information of the selected crypto ticker."""
    try:
        crypto = yf.Ticker(crypto_ticker)
        data = crypto.history(period="1d")
        if data.empty:
            raise ValueError(f"No data available for {crypto_ticker}")
        
        # Convert to Decimal for higher precision
        price = Decimal(str(data['Close'].iloc[-1]))
        
        market_cap = crypto.info.get('marketCap', 'N/A')
        if isinstance(market_cap, (int, float)):
            market_cap = f"${market_cap:,.0f}"
        
        info = f"Name: {crypto.info.get('name', 'N/A')}, Market Cap: {market_cap}"
        return price, info
    except Exception as e:
        logging.error(f"Error fetching crypto data for {crypto_ticker}: {e}")
        return None, None
