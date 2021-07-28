from data import data

# list of dictionaries
products = data


def test1():
    print("Print each Product title:")

    for prod in products:
        print(prod["title"])

# test 2
#  print the sum of all prices


def test2():
    sum = 0
    print("Total value in inventory:")
    for prod in products:
        total = (prod["price"])
        sum += total
    print(f"the TOTAL is : {sum}")


# test 3
# print the title of products with price > 6


def test3():
    print("Print each Product price: GREATER THAN 6")
    for prod in products:
        price = (prod["price"])

        if(price >= 6):
            print(prod["title"])

# test4
# print the total stock value (price * stock)


def test4():
    sum = 0
    print("Total value in inventory:")
    for prod in products:
        total = (prod["price"] * prod["stock"])
        sum += total
    print(f"the TOTAL is : {sum}")

# test 5
# get the lsit of unique categories
# print each string in  the list


def test5():
    cat = []
    print("-------UNIQUE Categories------")
    for prod in products:
        uni = (prod["category"])
        if uni not in cat:
            cat.append(uni)
            print(uni)


def run_test():
    print("Starting tests....")
    # test1()
    # test2()
    # test3()
    # test4()
    test5()


run_test()