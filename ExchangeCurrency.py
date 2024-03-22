import tkinter as tk
from forex_python.converter import CurrencyRates

def convert_currency():
    currency_rates = CurrencyRates()
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()
    amount = float(amount_entry.get())
    converted_amount = currency_rates.convert(from_currency, to_currency, amount)
    result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

# Create the main window
root = tk.Tk()
root.title("Currency Converter")

# Create entry for amount
amount_label = tk.Label(root, text="Amount:")
amount_label.grid(row=0, column=0, padx=5, pady=5)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1, padx=5, pady=5)

# Create dropdown for from currency
from_currency_var = tk.StringVar()
from_currency_var.set("USD")
from_currency_label = tk.Label(root, text="From Currency:")
from_currency_label.grid(row=1, column=0, padx=5, pady=5)
from_currency_menu = tk.OptionMenu(root, from_currency_var, "USD", "EUR", "GBP", "JPY", "AUD")
from_currency_menu.grid(row=1, column=1, padx=5, pady=5)

# Create dropdown for to currency
to_currency_var = tk.StringVar()
to_currency_var.set("EUR")
to_currency_label = tk.Label(root, text="To Currency:")
to_currency_label.grid(row=2, column=0, padx=5, pady=5)
to_currency_menu = tk.OptionMenu(root, to_currency_var, "USD", "EUR", "GBP", "JPY", "AUD")
to_currency_menu.grid(row=2, column=1, padx=5, pady=5)

# Create button to convert currency
convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Create label to display result
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Run the main event loop
root.mainloop()
