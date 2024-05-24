#  A supermarket maintains a pricing format for all its products. A value N is printed on each product. When the scanner reads the value N on the item, the product of all the digits in the value N is the price of the item. The task here is to design the software such that given the code of any item N the product (multiplication) of all the digits of value should be computed(price).

def compute_price(n):
    product = 1
    for digit in str(n):
        product *= int(digit)
    print(f'The price of product is: {product}')

price = int(input("enter the price printed on the item: "))
compute_price(price)
