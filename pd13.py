#DataFrame weather
#+-------------+--------+
#| Column Name | Type   |
#+-------------+--------+
#| city        | object |
#| month       | object |
#| temperature | int    |
#+-------------+--------+
#Write a solution to pivot the data so that each row represents temperatures for a specific month, and each city is a separate column.

#The result format is in the following example.

 

#Example 1:
#Input:
#+--------------+----------+-------------+
#| city         | month    | temperature |
#+--------------+----------+-------------+
#| Jacksonville | January  | 13          |
#| Jacksonville | February | 23          |
#| Jacksonville | March    | 38          |
#| Jacksonville | April    | 5           |
#| Jacksonville | May      | 34          |
#| ElPaso       | January  | 20          |
#| ElPaso       | February | 6           |
#| ElPaso       | March    | 26          |
#| ElPaso       | April    | 2           |
#| ElPaso       | May      | 43          |
#+--------------+----------+-------------+
#Output:
#+----------+--------+--------------+
#| month    | ElPaso | Jacksonville |
#+----------+--------+--------------+
#| April    | 2      | 5            |
#| February | 6      | 23           |
#| January  | 20     | 13           |
#| March    | 26     | 38           |
#| May      | 43     | 34           |
#+----------+--------+--------------+
#Explanation:
#The table is pivoted, each column represents a city, and each row represents a specific month.

weather = [
    {
        'city': 'Jacksonville',
        'month': 'January',
        'temperature':13
    },
    {
        'city': 'Jacksonville',
        'month': 'Febuary',
        'temperature':23
    },
    {
        'city': 'Jacksonville',
        'month': 'March',
        'temperature':38
    },
    {
        'city': 'Jacksonville',
        'month': 'April',
        'temperature':5
    },
    {
        'city': 'Jacksonville',
        'month': 'May',
        'temperature':34
    },
    {
        'city': 'Elpaso',
        'month': 'January',
        'temperature':20
    },
    {
        'city': 'Elpaso',
        'month': 'February',
        'temperature':6
    },
    {
        'city': 'Elpaso',
        'month': 'March',
        'temperature':26
    },
    {
        'city': 'Elpaso',
        'month': 'April',
        'temperature':2
    },
    {
        'city': 'Elpaso',
        'month': 'May',
        'temperature':2
    }
]

print(weather)


import pandas as pd 

df = pd.DataFrame(weather)

#print("Original Dataframe:\n", df)


pivot_weather = df.pivot(index='month', columns='city', values='temperature')
print("Reshaped DataFrame:\n", pivot_weather)