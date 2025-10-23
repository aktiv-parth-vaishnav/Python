class Store:
    def __init__(self):
        # dictionary to store all shelf and their products
        self.shelfs = {}
        # dictionary to store product categories
        self.categories = {}

    def create_shelf(self, shelf_name):
       """
         This Method to create a new shelf.
       """
       if shelf_name not in self.shelfs:
            self.shelfs[shelf_name] = {}
            print(f"shelf '{shelf_name}' created successfully.\n")
       else:
            print(f"shelf '{shelf_name}' already exists.\n")

    def add_product(self, shelf, product, month, cost_list, percent):
        """
          This Method Add Product in Shelf If Not Available Then first
          add shelf

          return none
        """
        if shelf not in self.shelfs:
            self.shelfs[shelf] = {}
        if product not in self.shelfs[shelf]:
            self.shelfs[shelf][product] = {'cost': {}, 'sale': {}}
        # Sale price = cost + (cost * percent / 100)
        sale_list = [c + (c * percent / 100) for c in cost_list]
        self.shelfs[shelf][product]['cost'][month] = cost_list
        self.shelfs[shelf][product]['sale'][month] = sale_list

    def update_sale_price(self, shelf, product, month, percent):
        """
        update price with given percentage
        """
        if shelf in self.shelfs and product in self.shelfs[shelf]:
            if month in self.shelfs[shelf][product]['cost']:
                cp_list = self.shelfs[shelf][product]['cost'][month]
                new_sale = [c + (c * percent / 100) for c in cp_list]
                self.shelfs[shelf][product]['sale'][month] = new_sale
                print(f"Sale price updated for {product} in {shelf} ({month}).\n")

    def update_sale_price_shelf(self, shelf, percent):
        """
        update shelf price with given percentage  
        """
        
        if shelf in self.shelfs:
            for prod, data in self.shelfs[shelf].items():
                for month, cost_list in data['cost'].items():
                    new_sale = [c + (c * percent / 100) for c in cost_list]
                    self.shelfs[shelf][prod]['sale'][month] = new_sale
            print(f"All sale prices updated for {shelf} by {percent}%.\n")

    def set_category(self, product, category):
        """
        This Method to set a category for a given product.

        return none
        """
        self.categories[product] = category
        print(f"Category '{category}' set for {product}.\n")

    def reset_cost(self, shelf, product, month):
        """
        This Method to reset cost price with 0 for a given shelf, product, and month.
        return none
        """
        if shelf in self.shelfs and product in self.shelfs[shelf]:
            if month in self.shelfs[shelf][product]['cost']:
                n = len(self.shelfs[shelf][product]['cost'][month])
                self.shelfs[shelf][product]['cost'][month] = [0] * n
                self.shelfs[shelf][product]['sale'][month] = [0] * n
                print(f"Cost and sale reset for {product} in {shelf} ({month}).\n")

    def get_price_info(self, product, mode='max'):
        """

        """
        found = False
        for shelf, pdata in self.shelfs.items():
            if product in pdata:
                for month, sale_list in pdata[product]['sale'].items():
                    if sale_list:
                        price = max(sale_list) if mode == 'max' else min(sale_list)
                        print(f"{mode.title()} price for {product} is {price} in {shelf} ({month})")
                        found = True
        if not found:
            print(f"No data found for {product}.\n")

    def avg_by_shelf(self, shelf, month):
        total_cost = 0
        total_sale = 0
        count = 0
        if shelf in self.shelfs:
            for prod, pdata in self.shelfs[shelf].items():
                if month in pdata['cost']:
                    total_cost += sum(pdata['cost'][month])
                    total_sale += sum(pdata['sale'][month])
                    count += len(pdata['cost'][month])
        if count > 0:
            avg_cost = total_cost / count
            avg_sale = total_sale / count
            profit = avg_sale - avg_cost
            print(f"shelf: {shelf}, Month: {month}")
            print(f"Average Cost = {avg_cost:.2f}, Average Sale = {avg_sale:.2f}, Profit = {profit:.2f}\n")
        else:
            print(f"No data found for {shelf} in {month}.\n")

    def avg_by_product(self, product, month):
        total_cost = 0
        total_sale = 0
        count = 0
        for shelf, pdata in self.shelfs.items():
            if product in pdata:
                if month in pdata[product]['cost']:
                    total_cost += sum(pdata[product]['cost'][month])
                    total_sale += sum(pdata[product]['sale'][month])
                    count += len(pdata[product]['cost'][month])
        if count > 0:
            avg_cost = total_cost / count
            avg_sale = total_sale / count
            profit = avg_sale - avg_cost
            print(f"Product: {product}, Month: {month}")
            print(f"Average Cost = {avg_cost:.2f}, Average Sale = {avg_sale:.2f}, Profit = {profit:.2f}\n")
        else:
            print(f"No data found for {product} in {month}.\n")


store = Store()

# shelf 1
store.create_shelf("shelf-1")
store.add_product("shelf-1", "Product 1", "January", [10, 30, 45, 50], 20)
store.add_product("shelf-1", "Product 1", "February", [60, 64, 68], 30)

# shelf 2
store.create_shelf("shelf-2")
store.add_product("shelf-2", "Product 1", "January", [206, 220, 225], 10)
store.add_product("shelf-2", "Product 1", "March", [180, 170, 165], 15)

# shelf 3
print("/////////create self")
store.create_shelf("shelf-3")

print("//////////add product")
store.add_product("shelf-3", "Product 2", "March", [55, 59, 61], 10)
store.add_product("shelf-3", "Product 2", "April", [53, 54, 55], 10)
print("//////////////set category")
store.set_category("Product 1", "Electronics")
print("////////////update sale price ")
store.update_sale_price("shelf-1", "Product 1", "January", 25)
store.update_sale_price_shelf("shelf-2", 12)
print("///////////reset cost")
store.reset_cost("shelf-1", "Product 2", "February")
print("///////////Show price pf product")
store.get_price_info("Product 4", "max")
print("///////////Avg By Shelf For Particular Month ")
store.avg_by_shelf("shelf-1", "January")
print("////////////Avg By Product For Particular Month")
store.avg_by_product("Product 1", "January")
