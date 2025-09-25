sales = [120, 80, 150, 200, 50]  

total_sales = sum(sales)
average_sales = total_sales / len(sales)
min_sales = min(sales)
max_sales = max(sales)

print("---- Integers ----")
print("Total Sales:", total_sales)
print("Average Sales:", average_sales)
print("Min Sales:", min_sales)
print("Max Sales:", max_sales)
print()
print("---- Lists ----")
print("Original List:", sales)
sales.append(95)
sales = [s for s in sales if s >= 60]

sales.sort()

print("Modified List:", sales)
print()