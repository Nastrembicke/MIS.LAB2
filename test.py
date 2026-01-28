#constraints
bouquet_cost = 17.00
extraflowers_Cost = 0.35
tip_expense = .15
sales_tax = 0.18

#Declare Variables 
total_topping_cost = 0
total_bouquet_cost = 0

#input
number_of_bouquets = int(input("Enter the number of bouquets that have been purchased: "))
extra_flowers = int(input("Enter the number of extra flowrs that have been purchased: "))

#processing
total_bouquet_cost = bouquet_cost * number_of_bouquets

total_extra_flower_cost = extraflowers_Cost * extra_flowers

total_order_cost = (1 + tip_expense) * (total_bouquet_cost + total_extra_flower_cost) + (number_of_bouquets * sales_tax)

#output
print(total_order_cost)
