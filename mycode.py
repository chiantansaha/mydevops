import math 
import statistics
'''
orders = []
order = input("What would you like to order? (Q to Quit)")

while (order.upper() != 'Q'):
    # Find the order and add it
    found = menu.get(order)
    if found:
        orders.append(order)
    else:
        print("Menu item doesn't exist")
        order = input("Anything else? (Q to Quit)")
        print(orders)

numbers = [4,5,65,98,3]

avg = statistics.mean(numbers)
print(avg)

'''

import random


def lotto_numbers():
    lotto_nums = []
    for i in range(5):
        lotto_nums.append(random.randint(1, 53))

    return lotto_nums

if __name__ == "__main__":
    i = lotto_numbers()
    print(i)
