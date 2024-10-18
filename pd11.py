#DataFrame products
#+-------------+--------+
#| Column Name | Type   |
#+-------------+--------+
#| name        | object |
#| quantity    | int    |
#| price       | int    |
#+-------------+--------+
#Write a solution to fill in the missing value as 0 in the quantity column.

#The result format is in the following example.

 

#Example 1:
#Input:+-----------------+----------+-------+
#| name            | quantity | price |
#+-----------------+----------+-------+
#| Wristwatch      | None     | 135   |
#| WirelessEarbuds | None     | 821   |
#| GolfClubs       | 779      | 9319  |
#| Printer         | 849      | 3051  |
#+-----------------+----------+-------+
#Output:
#+-----------------+----------+-------+
#| name            | quantity | price |
#+-----------------+----------+-------+
#| Wristwatch      | 0        | 135   |
#| WirelessEarbuds | 0        | 821   |
#| GolfClubs       | 779      | 9319  |
#| Printer         | 849      | 3051  |
#+-----------------+----------+-------+
#Explanation: 
#The quantity for Wristwatch and WirelessEarbuds are filled by 0.

products = [
    {
        'name': 'Wristwatch',
        'quantity':'None',
        'price': 135
    },
    {
        'name': 'WirelessEarbuds',
        'quantity':'None',
        'price': 821
    },
    {
        'name': 'GolfClubs',
        'quantity':'779',
        'price': 9319
    },
    {
        'name': 'Printer',
        'quantity':'849',
        'price': 3051
    }
]

print(products)

import pandas as pd

products = {
    'name': ['Wristwatch', 'WirelessEarbuds', 'GolfClubs', 'Printer'],
    'quantity': [None, None, 779, 849],
    'price': [135, 821, 9319, 3051]
}
products = pd.DataFrame(products)

products['quantity'] = products['quantity'].fillna(0)
print(products)