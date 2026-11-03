#exersise 1
def calculate_tax(price, rate):
    return price * rate

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")

#exercise 2
def apply_discount(price, tier):
    if tier == "gold":
        return price * .85
    elif tier == "silver":
        return price * .9
    elif tier == "bronze":
        return price * .95
    else:
        return price 

original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier)}")


#exercise 3

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

print(f"final_price(200, 0.07, 'gold) = ${final_price(200, 0.07, 'gold'):.2f}")

#exercise 4

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

rate = 0.07
for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Price: ${price} | teir: {tier} | Total: ${total:.2f}")

#ex 6
x = 100

def double_it():
    x = 999
    return x * 2

print(x)
print(double_it())
print(x)

#self-assesment1
#the first error I spotted in exercise 5 was the missing colon at the end of the loop. I spotted this durring the rubber duck debugging. this tells me that I can spot very simple errors in a simple thing of code.

#self-assesment2
#the line of code apply_discount(price, tier) means that the function apply_discount is being called with the arguments price and tier. The function will then calculate the discounted price based on the tier and return it. it's imputs are the price and tier, and its output is the discounted price. Then the code returns the discounted price to the caller, which can then use it for further calculations or display it to the user.

#slef- assesment3
#I used AI to help me with the debugging of the code. I used it to help me find the errors in the code and to help me understand what the code was doing. I also used it to help me understand how to fix the errors in the code. I found it very helpful in understanding the code and how to fix it.