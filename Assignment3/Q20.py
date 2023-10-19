def generate_discount_table(prices):
    print("Original Price   |   Discount Amount   |   New Price")
    print("-" * 50)
    
    discount_rate = 0.60
    
    for price in prices:
        discount_amount = price * discount_rate
        new_price = price - discount_amount
        
        print(f"${price:.2f}              |   ${discount_amount:.2f}               |   ${new_price:.2f}")

# List of original prices
prices = [4.95, 9.95, 14.95, 19.95, 24.95]

# Generate the discount table
generate_discount_table(prices)
