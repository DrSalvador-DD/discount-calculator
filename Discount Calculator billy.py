import tkinter as tk

def calculate_discount():
    # Get raw text from entry fields
    price_text = entry_price.get()
    discount_text = entry_discount.get()

    # Check if fields are empty
    if not price_text or not discount_text:
        label_result.config(text="Please fill in all fields.")
        return

    try:
        # Convert text to numbers
        price = float(price_text)
        discount = float(discount_text)

        # Check for negative values
        if price < 0 or discount < 0:
            label_result.config(text="Values must be positive numbers.")
            return

        # Calculate final price
        final_price = price - (price * discount / 100)

        # Display result
        label_result.config(text=f"Final Price: Rp. {final_price:.2f}")

    except ValueError:
        label_result.config(text="Please enter valid numbers only.")

# Create main window
window = tk.Tk()
window.title("Discount Calculator")
window.geometry("300x250")

# Original Price Label & Entry
label_price = tk.Label(window, text="Original Price:")
label_price.pack()

entry_price = tk.Entry(window)
entry_price.pack()

# Discount Label & Entry
label_discount = tk.Label(window, text="Discount (%):")
label_discount.pack()

entry_discount = tk.Entry(window)
entry_discount.pack()

# Calculate Button
button_calculate = tk.Button(window, text="Calculate", command=calculate_discount)
button_calculate.pack(pady=10)

# Result Label
label_result = tk.Label(window, text="Final Price:")
label_result.pack()

window.mainloop()
