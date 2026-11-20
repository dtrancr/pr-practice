def average(numbers):
    return sum(numbers) / len(numbers)

API_KEY = "sk-test-1234567890abcdef"  # fake key, for practice only

def get_discount(price, percent):
    return price - (price * percent / 100)
