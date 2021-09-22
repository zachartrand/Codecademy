"""
Page Visits Funnel
Cool T-Shirts Inc. has asked you to analyze data on visits to their website. Your job is to build a funnel, which is a description of how many people continue to the next step of a multi-step process.

In this case, our funnel is going to describe the following process:

    1. A user visits CoolTShirts.com
    2. A user adds a t-shirt to their cart
    3. A user clicks “checkout”
    4. A user actually purchases a t-shirt
"""

import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

# 1. Inspect the DataFrames using print and head:
#       visits lists all of the users who have visited the website
#       cart lists all of the users who have added a t-shirt to their cart
#       checkout lists all of the users who have started the checkout
#       purchase lists all of the users who have purchased a t-shirt
print(visits.head(), cart.head(), checkout.head(), purchase.head())

# 2. Combine visits and cart using a left merge.
visits_cart = visits.merge(cart, how='left')
print(visits_cart)

# 3. How long is your merged DataFrame?
print(len(visits_cart))
# 2000

# 4. How many of the timestamps are null for the column cart_time?
null_times = visits_cart[visits_cart.cart_time.isnull()]
print(len(null_times))
# 1652
#    What do these null rows mean?
# The users of these rows visited the website but didn't add items to their shopping cart.

# 5. What percent of users who visited Cool T-Shirts Inc. ended up not placing
# a t-shirt in their cart?
# Note: To calculate percentages, it will be helpful to turn either the
# numerator or the denominator into a float, by using float(), with the number to
# convert passed in as input. Otherwise, Python will use integer division,
# which truncates decimal points.
print(1652.0 / 2000 * 100)
# 82.6%

# 6. Repeat the left merge for cart and checkout and count null values.
# What percentage of users put items in their cart, but did not proceed to checkout?
cart_checkout = cart.merge(checkout, how='left')
total = len(cart_checkout)
null_count = len(cart_checkout[cart_checkout.checkout_time.isnull()])
no_checkout_percent = float(null_count) / total * 100
print(no_checkout_percent)
# 25.3112033195%

# 7. Merge all four steps of the funnel, in order, using a series of left merges.
#    Save the results to the variable all_data.
#    Examine the result using print and head.
kwargs = dict(how='left')
all_data = visits.merge(cart, **kwargs).merge(checkout, **kwargs).merge(purchase, **kwargs)
print(all_data.head())

# 8. What percentage of users proceeded to checkout, but did not purchase a t-shirt?
checkout_no_purchase = all_data[
    all_data.purchase_time.isnull() & ~all_data.checkout_time.isnull()]
checkout_count = all_data[~all_data.checkout_time.isnull()]
percent_checkout_no_purchase = 100.0 * len(checkout_no_purchase) / len(checkout_count)
print(percent_checkout_no_purchase)
# 16.889632107%

# 9. Which step of the funnel is weakest (i.e., has the highest percentage of
#    users not completing it)?
# People who visit the site but don't add a t-shirt to their cart.
#
#    How might Cool T-Shirts Inc. change their website to fix this problem?
# Better advertising, better pricing, put some of their products on sale, better products.

## Average Time to Purchase ##
# 10. Using the giant merged DataFrame all_data that you created, let's calculate
#     the average time from initial visit to final purchase.
all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time

# 11. Examine the results.
print(all_data.time_to_purchase)

# 12. Calculate the average time to purchase.
print(all_data.time_to_purchase.mean())
