class ItemToPurchase:
    def __init__(self, item_name = 'none', item_price = float(0), item_quantity = int(0)):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
    
    def print_item_cost(self):
        item_total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${item_total}")
        return item_total
        
shopping_list = []
number_of_items = int(input("How many items are on the list: "))
for i in range(number_of_items):
    item_name = str(input(f'What is the name of item number {i + 1}: '))
    item_price = float(input(f'What is the price of item number {i + 1}: '))
    item_quantity = int(input(f'What is the quantity of item number {i + 1}: '))
    item = ItemToPurchase(item_name, item_price, item_quantity)
    shopping_list.append(item)
print('TOTAL COST')
total = 0
for item in shopping_list:
    total = total + item.print_item_cost()
print('Total: $' + str(total))