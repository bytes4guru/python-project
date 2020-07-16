#!/usr/bin/env python
# -*- coding: utf-8 -*-

# checkout.py

            # OBJECTIVES: #
#
# Checkout Class that maintains a list of items
# that are being checked out.
# 
# Checkout Class provides interfaces for:
#   - Setting the price of individual items.
#   - Adding the individual items to the check out.
#   - The current total cost for all the items added.
#   - Add an 'apply discount' on select items when N 
#     number of that item are purchased

class Checkout:

    class Discount:
        def __init__(self, item_count, price):
            self.item_count = item_count
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}


    def addDiscount(self, item, number_of_items, price):
        discount = self.Discount(number_of_items, price)
        self.discounts[item] = discount


    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        if item not in self.prices:
            raise Exception("Error! Item not priced!")

        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    # The calculateTotal method iterates over all of 
    # the counts in the items dictionary, and 
    # calculate the total by multiplying the total 
    # number of items added by each item's price, 
    # and returning that value.
    def calculateTotal(self):
        total = 0
        for item, count in self.items.items():
            total += self.calculateItemTotal(item, count)
        return total

    def calculateItemTotal(self, item, count):
        total = 0
        # For each item in the items dictionary,
        # search in the discounts map to see 
        # if there's a discount for that item.
        if item in self.discounts:
            discount = self.discounts[item]
            if count >= discount.item_count:
                total += self.calculateItemDiscountedTotal(item, count, discount)
            else:
                total += self.prices[item] * count
        else:
            total += self.prices[item] * count
        
        return total
    
    def calculateItemDiscountedTotal(self, item, count, discount):
        total = 0
        number_of_discounts = count / discount.item_count
        total += number_of_discounts * discount.price
        remaining = count % discount.item_count
        total += remaining * self.prices[item]
        return total