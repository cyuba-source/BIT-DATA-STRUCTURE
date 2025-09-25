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
sales_records = [
    {"id": 1, "name": "Paracetamol", "value": 120},
    {"id": 2, "name": "Amoxicillin", "value": 80},
    {"id": 3, "name": "Ibuprofen", "value": 150},
]

print("---- Dictionaries ----")
print("Original Records:", sales_records)

sales_records[0]["value"] = 130
del sales_records[1]
sales_records.append({"id": 4, "name": "Cough Syrup", "value": 90})
total_value = sum(item["value"] for item in sales_records)

print("Modified Records:", sales_records)
print("Total Value:", total_value)