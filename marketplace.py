from time import sleep
from product import Products


product_list = []
shopping_bag = []


def main():
    menu()


def menu():
    print('1 - Register product')
    print('2 - Show all products')
    print('3 - Purchase product')
    print('4 - Visualize bag')
    print('5 - Checkout')
    print('6 - Exit the system')

    option = int(input('Chose an option above: '))
    options = {1: registerProduct, 2: showAllProduct, 3: purchaseProduct, 4: visualizeBag, 5: checkout, 6: exit}
    function = options[option]
    function()
    menu()


def registerProduct():
    print('Register product')
    name = input('Enter the product name: ')
    price = float(input('Enter the product price: '))
    product = Products(name, price)
    product_list.append(product)
    print(f' The product was registered successfully!')
    sleep(1)
    menu()


def showAllProduct():
    if len(product_list) > 0:
        for product in product_list:
            print(product)
            sleep(1)
    print("There are no registered products.")
    menu()


def purchaseProduct():
    if len(product_list) > 0:
        print('Products available:')
        for product in product_list:
            print(product)

        code = int(input('Enter the product code: '))
        product = visualizeProductByTheCode(code)

        if product:
            if len(shopping_bag) > 0:
                product_in_bag = False

                for item in shopping_bag:
                    quantity = item.get(product)
                    if quantity:
                        item[product] = quantity + 1
                        print(f'The product{product.name} now has {quantity + 1}units in the bag.')
                        product_in_bag = True
                        sleep(2)
                        menu()

                if not product_in_bag:
                    prod = {product: 1}
                    shopping_bag.append(prod)
                    print(f'The product {product.name} was added to the bag')
                    sleep(2)
                    menu()

            else:
                item = {product: 1}
                shopping_bag.append(item)
                print(f'The product {product.name} was added to the bag.')
                sleep(2)
                menu()

        else:
            print(f'The product with code {code} was not found.')
            sleep(2)
            menu()

    else:
        print('There are no products available.')
    sleep(2)
    menu()


def visualizeBag():
    if len(shopping_bag) > 0:
        for item in shopping_bag:
            for data in item.items():
                print(data[0])
                print(f'Quantity: {data[1]}')
            sleep(1)
    else:
        print("Bag empty")
    sleep(2)
    menu()


def checkout():
    if len(shopping_bag) > 0:
        purchase_price = 0
        for item in shopping_bag:
            for data in item.items():
                purchase_price += data[0].price * data[1]
                sleep(1)
        print(f'The purchase price is {purchase_price}')
        shopping_bag.clear()
        sleep(2)
    else:
        print(f'There are no products in the bag.')
    sleep(2)
    menu()


def visualizeProductByTheCode(code):
    product = None
    for item in product_list:
        if item.code == code:
            product = item
    return product


if __name__ == '__main__':
    main()
