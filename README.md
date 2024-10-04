<img src="icons/app_icon.png" alt="CryptoPay app icon" />

# CryptoPay


A modern, user-friendly desktop application that allows users to quickly and easily convert between USD and various cryptocurrencies. Built with Python and PySide6, this application provides real-time cryptocurrency price data and additional market information, making it an invaluable tool for crypto enthusiasts, investors, and anyone interested in tracking cryptocurrency values. Want to get paid in crypto but don't know how much to ask for? CryptoPay is the perfect solution!
<br><br>
**Remember:** Crypto values are constantly changing, second-by-second. Use this information with caution.

## Features

- **Real-time Conversion**: Convert USD to multiple cryptocurrencies using up-to-date market data.
- **High Precision**: Display crypto values with up to 8 decimal places for more accurate conversions.
- **Customizable Currency List**: Add or remove cryptocurrencies to tailor the app to your needs.
- **Market Information**: View additional details such as the cryptocurrency's name and market capitalization.
- **User-friendly Interface**: Clean and intuitive GUI design for ease of use.
- **Error Handling**: Robust error checking and user feedback for a smooth experience.

## Benefits

- **Stay Informed**: Keep track of cryptocurrency values by manually performing the conversion. (Auto mode is on the [TODO list](TODO/TODO.md)
- **Make Informed Decisions**: Access market cap information to gauge the size and stability of different cryptocurrencies.
- **Save Time**: Quickly perform currency conversions without the need for web searches or complex calculations.
- **Flexibility**: Customize the list of cryptocurrencies to focus on the ones that matter to you.
- **Accuracy**: High-precision calculations ensure accurate conversions, even for small amounts.

## Installation

### Requirements

- Python 3.7 or higher
- PySide6
- yfinance

### Steps

1. Clone the repository:
   ```
   git clone https://github.com/endorpheus/CryptoPay.git
   cd CryptoPay
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:<br>
If requirements.txt doesn't exist, just watch for error messages and install the unmet dependencies manually.
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python CryptoPay.py
   ```

## Usage

1. Launch the application.
2. Select a cryptocurrency from the dropdown menu.
3. Enter the USD amount you wish to convert.
4. Click "Update Price" to see the conversion result and additional information.
5. Use the File menu to add or remove cryptocurrencies from the list.

## Contributing

Contributions are welcome!

## Acknowledgments

- Built with [PySide6](https://wiki.qt.io/Qt_for_Python)
- Cryptocurrency data provided by [yfinance](https://github.com/ranaroussi/yfinance)
- Media assets: [Media Attribution](Media_Attribution.md)

## Support

If you encounter any problems or have any questions, please open an issue on the GitHub repository.

---

Happy crypto converting!<br><br><br>
Ryon Shane Hall
