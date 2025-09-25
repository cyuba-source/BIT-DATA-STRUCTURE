sales = [120, 80, 150, 200, 50]  

total_sales = sum(sales)
average_sales = total_sales / len(sales)
min_sales = min(sales)
max_sales = max(sales)
report = f"Pharmacy Sales Report:\nTotal = {total_sales}, Average = {average_sales:.2f}\n"
summary = f"Lowest = {min_sales}, Highest = {max_sales}"
print("---- Strings ----")
print(report + summary)
print()