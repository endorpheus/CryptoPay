import sys
from PySide6.QtWidgets import (QApplication, QVBoxLayout, QHBoxLayout, QComboBox, QLineEdit, 
                               QLabel, QPushButton, QWidget, QMessageBox, QInputDialog, QMenuBar, 
                               QSpacerItem, QSizePolicy, QMainWindow)
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import Qt
from decimal import Decimal
from crypto_utils import load_tickers, save_tickers, get_crypto_data

# Define version
VERSION = "1.0"

class CryptoConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"Crypto Converter v{VERSION}")
        self.setGeometry(100, 100, 500, 182)
        self.center_on_screen()

        # Set custom icon for the app
        self.setWindowIcon(QIcon("icons/app_icon.png"))

        # Load tickers from file or use defaults
        self.tickers = load_tickers()

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Create menu bar
        self.create_menus()

        # Crypto Dropdown with Menu for adding/removing currencies
        self.crypto_dropdown = QComboBox()
        self.crypto_dropdown.addItems(self.tickers)
        dropdown_layout = QHBoxLayout()
        dropdown_layout.addWidget(QLabel("Select Cryptocurrency:"))
        dropdown_layout.addWidget(self.crypto_dropdown)

        main_layout.addLayout(dropdown_layout)

        # Input for USD
        usd_layout = QHBoxLayout()
        usd_layout.addWidget(QLabel("Enter USD amount:"))
        self.usd_input = QLineEdit()
        self.usd_input.setPlaceholderText("Enter USD amount")
        usd_layout.addWidget(self.usd_input)

        main_layout.addLayout(usd_layout)

        # Button to Update Price
        self.update_button = QPushButton("Update Price")
        self.update_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.update_button.clicked.connect(self.update_crypto_price)
        main_layout.addWidget(self.update_button)

        # Labels for displaying results
        self.result_label = QLabel("Equivalent Crypto Amount: N/A")
        self.result_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.result_label)

        self.info_label = QLabel("Crypto Info: N/A")
        self.info_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.info_label)

        self.crypto_value_label = QLabel("Crypto Value: N/A")
        self.crypto_value_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.crypto_value_label)

        # Add a spacer
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

    def center_on_screen(self):
        frame_gm = self.frameGeometry()
        screen = QApplication.primaryScreen().availableGeometry().center()
        frame_gm.moveCenter(screen)
        self.move(frame_gm.topLeft())

    def create_menus(self):
        # Create "File" menu
        file_menu = self.menuBar().addMenu("File")
        
        add_currency_action = QAction("Add Currency", self)
        add_currency_action.triggered.connect(self.add_currency)
        file_menu.addAction(add_currency_action)

        remove_currency_action = QAction("Remove Currency", self)
        remove_currency_action.triggered.connect(self.remove_currency)
        file_menu.addAction(remove_currency_action)

        # Create "About" menu
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)
        self.menuBar().addAction(about_action)

    def show_about(self):
        QMessageBox.about(
            self, 
            "About CryptoPay",
            f"CryptoPay v{VERSION}\n\n"
            "A modern cryptocurrency converter app.\n"
            "Built with Python and PySide6.\n"
            "Data from Yahoo Finance (yfinance).\n"
            "by Ryon Shane Hall\n"
            "endorpheus@gmail.com\n"
            "https://github.com/endorpheus\n"
            "https://github.com/endorpheus/CryptoPay"
        )

    def update_crypto_price(self):
        usd_amount = self.usd_input.text()
        crypto_ticker = self.crypto_dropdown.currentText()

        if not usd_amount:
            QMessageBox.warning(self, "Input Error", "Please enter a valid USD amount.")
            return

        try:
            usd_amount = float(usd_amount)
        except ValueError:
            QMessageBox.warning(self, "Input Error", "USD amount must be a number.")
            return

        crypto_price, crypto_info = get_crypto_data(crypto_ticker)
        if crypto_price:
            crypto_amount = Decimal(str(usd_amount)) / crypto_price
            self.result_label.setText(f"Equivalent Crypto Amount: {crypto_amount:.8f} {crypto_ticker.split('-')[0]}")
            self.info_label.setText(f"Crypto Info: {crypto_info}")
            self.crypto_value_label.setText(f"Crypto Value: {crypto_price:.8f} USD")
        else:
            QMessageBox.warning(self, "Data Error", f"Unable to fetch data for {crypto_ticker}")

    def add_currency(self):
        currency, ok = QInputDialog.getText(self, "Add Currency", "Enter currency ticker (e.g., BTC-USD):")
        if ok and currency:
            if currency not in self.tickers:
                self.tickers.append(currency)
                self.crypto_dropdown.addItem(currency)
                save_tickers(self.tickers)
                QMessageBox.information(self, "Currency Added", f"{currency} has been added to the list.")
            else:
                QMessageBox.warning(self, "Duplicate Currency", f"{currency} is already in the list.")

    def remove_currency(self):
        current_currency = self.crypto_dropdown.currentText()
        index = self.crypto_dropdown.currentIndex()
        if index != -1:
            self.tickers.remove(current_currency)
            self.crypto_dropdown.removeItem(index)
            save_tickers(self.tickers)
            QMessageBox.information(self, "Currency Removed", f"{current_currency} has been removed from the list.")
        else:
            QMessageBox.warning(self, "Remove Error", "No currency selected to remove.")

# Main application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CryptoConverter()
    window.show()
    sys.exit(app.exec())
