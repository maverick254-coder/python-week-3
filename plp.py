def calculate_discount(price, discount_percent):
    """Calculates the final price after applying a discount if it is 20% or higher."""
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    return price  # Return original price if discount is less than 20%

# Get user input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Print the result
if discount_percent >= 20:
    print(f"The final price after a {discount_percent}% discount is: {final_price:.2f}")
else:
    print(f"No discount applied. The original price remains: {price:.2f}")
