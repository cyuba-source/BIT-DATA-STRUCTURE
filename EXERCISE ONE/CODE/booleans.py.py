
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
threshold = 100
if average_sales > threshold and max_sales > 180:
    status = "Above Standard"
else:
    status = "Below Standard"

print("---- Booleans ----")
print("Status:", status)
print()