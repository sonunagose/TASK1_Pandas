#DataFrame customers
#+-------------+--------+
#| Column Name | Type   |
#+-------------+--------+
#| customer_id | int    |
#| name        | object |
#| email       | object |
#+-------------+--------+
#There are some duplicate rows in the DataFrame based on the email column.

#Write a solution to remove these duplicate rows and keep only the first occurrence.

#The result format is in the following example.

 

#Example 1:
##Input:
#+-------------+---------+---------------------+
#| customer_id | name    | email               |
#+-------------+---------+---------------------+
#| 1           | Ella    | emily@example.com   |
#| 2           | David   | michael@example.com |
#| 3           | Zachary | sarah@example.com   |
#| 4           | Alice   | john@example.com    |
#| 5           | Finn    | john@example.com    |
#| 6           | Violet  | alice@example.com   |
#+-------------+---------+---------------------+
#Output:  
#+-------------+---------+---------------------+
#| customer_id | name    | email               |
#+-------------+---------+---------------------+
#| 1           | Ella    | emily@example.com   |
#| 2           | David   | michael@example.com |
#| 3           | Zachary | sarah@example.com   |
#| 4           | Alice   | john@example.com    |
#| 6           | Violet  | alice@example.com   |
#+-------------+---------+---------------------+
#Explanation:
#Alic (customer_id = 4) and Finn (customer_id = 5) both use john@example.com, so only the first occurrence of this email is retained.

data = [
    {
        'customer_id': 1,
        'name': 'Ella',
        'email':'emily@example.com '
    },
    {
        'customer_id': 2,
        'name': 'David',
        'email':'michael@example.com'
    },
    {
        'customer_id': 3,
        'name': 'Zachary',
        'email':'sarah@example.com'
    },
    {
        'customer_id': 4,
        'name': 'Alice',
        'email':'john@example.com '
    },
    {
        'customer_id': 5,
        'name': 'Finn',
        'email':'john@example.com '
    },
    {
        'customer_id': 6,
        'name': 'Violet',
        'email':'alice@example.com '
    }  
]

print(data)


import pandas as pd

data = {
    'customer_id': [1, 2, 3, 4, 5, 6],
    'name': ['Ella', 'David', 'Zachary', 'Alice', 'Finn', 'Violet'],
    'email': ['emily@example.com', 'michael@example.com', 'sarah@example.com', 'john@example.com', 'john@example.com', 'alice@example.com']
}


customers = pd.DataFrame(data)

customers_data= customers.drop_duplicates(subset='email', keep='first')
print(customers_data)