import tkinter as tk


# Function to perform currency exchange calculation
def exchange_money():
    # Get the amount entered by the user as USD
    amount_usd = float(entry.get())

    # Convert the USD amount to CAD using the exchange rate
    amount_cad = amount_usd * 1.13

    # Update the result label with the converted amount
    result_label.config(text=f"${amount_usd:.2f} USD is equivalent to ${amount_cad:.2f} CAD")


# Create the main window
root = tk.Tk()
root.title("Currency Exchange")

# Create a canvas to hold the widgets
canvas = tk.Canvas(root, width=400, height=200)
canvas.pack()

# Load the background image
background_image = tk.PhotoImage(file="background.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Create an entry widget for the user to enter the amount in USD
entry = tk.Entry(root, width=10)
entry.pack()

# Create a button to trigger the currency exchange calculation
exchange_button = tk.Button(root, text="Exchange", command=exchange_money)
exchange_button.pack()

# Create a label to display the result of the currency exchange calculation
result_label = tk.Label(root, text="")
result_label.pack()

# Start the Tkinter event loop
root.mainloop()
