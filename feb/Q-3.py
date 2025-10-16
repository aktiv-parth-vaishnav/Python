def analyze_sales_data(sales_data):
    """this method calculate highest selling product of the day
    and total sales per day

    return dict
    """

    total_sales_per_day = {}

    for sale in sales_data:
        date = sale["sale_date"]
        amount = sale["sale_amount"]
        total_sales_per_day[date] = total_sales_per_day.get(date, 0) + amount

    highest_selling_day = max(total_sales_per_day, key=total_sales_per_day.get)

    return {
        "Total Sales Per Day": total_sales_per_day,
        "Highest-Selling Day": highest_selling_day
    }


sales_data = [
    {"product_id": 101, "product_name": "Smartphone", "sale_amount": 500, "sale_date": "2025-01-01"},
    {"product_id": 102, "product_name": "Laptop", "sale_amount": 300, "sale_date": "2025-01-01"},
    {"product_id": 101, "product_name": "Smartphone", "sale_amount": 400, "sale_date": "2025-01-02"},
    {"product_id": 103, "product_name": "Smartwatch", "sale_amount": 700, "sale_date": "2025-01-02"},
]

result = analyze_sales_data(sales_data)

# Result Output
print(result)
