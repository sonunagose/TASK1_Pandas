#DataFrame animals
#+-------------+--------+
#| Column Name | Type   |
#+-------------+--------+
#| name        | object |
#| species     | object |
#| age         | int    |
#| weight      | int    |
#+-------------+--------+
#Write a solution to list the names of animals that weigh strictly more than 100 kilograms.

#Return the animals sorted by weight in descending order.

#The result format is in the following example.

 

#Example 1:

#Input: 
#DataFrame animals:
#+----------+---------+-----+--------+
#| name     | species | age | weight |
#+----------+---------+-----+--------+
#| Tatiana  | Snake   | 98  | 464    |
#| Khaled   | Giraffe | 50  | 41     |
#| Alex     | Leopard | 6   | 328    |
#| Jonathan | Monkey  | 45  | 463    |
#| Stefan   | Bear    | 100 | 50     |
#| Tommy    | Panda   | 26  | 349    |
#+----------+---------+-----+--------+
#Output: 
#+----------+
#| name     |
#+----------+
#| Tatiana  |
#| Jonathan |
#| Tommy    |
#| Alex     |
#+----------+
#Explanation: 
#All animals weighing more than 100 should be included in the results table.
#Tatiana's weight is 464, Jonathan's weight is 463, Tommy's weight is 349, and Alex's weight is 328.
#The results should be sorted in descending order of weight.
 

#In Pandas, method chaining enables us to perform operations on a DataFrame without breaking up each operation into a separate line or creating multiple temporary variables. 

#Can you complete this task in just one line of code using method chaining?


animals = [
    {
        'name': 'Tatiana',
        'species':'Snake',
        'age':98,
        'weight':464
    },
    {
         'name': 'Khaled',
        'species':'Giraffe',
        'age':50,
        'weight':41
    },
    {
         'name': 'Alex',
        'species':'Leopard',
        'age':6,
        'weight':328
    },
    {
         'name': 'Jonathan',
        'species':'Monkey',
        'age':45,
        'weight':463
    },
    {
         'name': 'Stefan',
        'species':'Bear',
        'age':100,
        'weight':50
    },
    {
         'name': 'Tommy',
        'species':'Panda',
        'age':26,
        'weight':349
    }
]

print(animals)

import pandas as pd

animals = {
    'name': ['Tatiana', 'Khaled', 'Alex', 'Jonathan', 'Stefan', 'Tommy'],
    'species': ['Snake', 'Giraffe', 'Leopard', 'Monkey', 'Bear', 'Panda'],
    'age': [98, 50, 6, 45, 100, 26],
    'weight': [464, 41, 328, 463, 50, 349]
}

animals = pd.DataFrame(animals)

output = animals[animals['weight'] > 100].sort_values(by='weight', ascending=False)['name']
print(output)