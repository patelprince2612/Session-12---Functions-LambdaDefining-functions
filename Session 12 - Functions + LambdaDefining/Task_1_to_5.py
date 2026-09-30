# Task 1: Define a function called get_discounted_price that takes price and discount_percent as arguments and returns the final price after applying the discount. Test it with a price of 500 and a discount of 10%.
def get_discounted_price(price, discount_percent):
    discount_amount = price * (discount_percent / 100)
    return price - discount_amount

print(get_discounted_price(500, 10))

# Task 2: Write a function called format_follower_count that takes a number and returns it in Instagram-style format (e.g., 1500 as '1.5K', 1200000 as '1.2M').
def format_follower_count(num):
    if num >= 1000000:
        return f"{num / 1000000:.1f}M"
    elif num >= 1000:
        return f"{num / 1000:.1f}K"
    else:
        return str(num)

print(format_follower_count(1500))
print(format_follower_count(1200000))

# Task 3: Given a list of song durations in minutes, use a lambda function with the map() function to convert all durations to seconds and print the resulting list.
durations_in_minutes = [3.5, 4.2, 5.0, 2.5]
durations_in_seconds = list(map(lambda mins: mins * 60, durations_in_minutes))
print(durations_in_seconds)

# Task 4: Use a lambda function with the filter() function to get all product names from a Flipkart-style list that start with the letter 'M'. Example list: ['Mobile', 'Mouse', 'Laptop', 'Monitor', 'Keyboard'].
products = ['Mobile', 'Mouse', 'Laptop', 'Monitor', 'Keyboard']
m_products = list(filter(lambda item: item.startswith('M'), products))
print(m_products)

# Task 5: Using reduce() and a lambda function, calculate the total bill amount for a Swiggy order given a list of item prices: [120, 80, 150, 60].
from functools import reduce

prices = [120, 80, 150, 60]
total_bill = reduce(lambda x, y: x + y, prices)
print(total_bill)