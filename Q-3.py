sales_data = [
    {"product_id": 101, "product_name": "Smartphone", "sale_amount": 500},
    {"product_id": 102, "product_name": "Laptop", "sale_amount": 300},
    {"product_id": 101, "product_name": "Smartphone", "sale_amount": 400},
    {"product_id": 103, "product_name": "Smartwatch", "sale_amount": 700}
]
total = 0
for rec in sales_data:
    total += rec["sale_amount"]

average = total / len(sales_data)

highest_total = 0
highest_product = {}

for rec in sales_data:
    pid = rec["product_id"]
    pname = rec["product_name"]

    product_total = 0
    for other in sales_data:
        if other["product_id"] == pid:
            product_total += other["sale_amount"]

    if product_total > highest_total:
        highest_total = product_total
        highest_product = {
            "product_id": pid,
            "product_name": pname
        }
analyz_data = {
    "Total Sales": total,
    "Average Sales": average,
    "Highest-Selling Product": highest_product
}

print(analyz_data)
