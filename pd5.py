#DataFrame employees
#+-------------+--------+
#| Column Name | Type.  |
#+-------------+--------+
#| name        | object |
#| salary      | int.   |
#+-------------+--------+
#A company plans to provide its employees with a bonus.

#Write a solution to employees = {create a new column name bonus that contains the doubled values of the salary column.

#The result format is in the following example.

 

#Example 1:

#Input:
#DataFrame employees
#+---------+--------+
#| name    | salary |
#+---------+--------+
#| Piper   | 4548   |
#| Grace   | 28150  |
#| Georgia | 1103   |
#| Willow  | 6593   |
#| Finn    | 74576  |
#| Thomas  | 24433  |
#+---------+--------+
#Output:
#+---------+--------+--------+
#| name    | salary | bonus  |
#+---------+--------+--------+
#| Piper   | 4548   | 9096   |
#| Grace   | 28150  | 56300  |
#| Georgia | 1103   | 2206   |
#| Willow  | 6593   | 13186  |
#| Finn    | 74576  | 149152 |
#| Thomas  | 24433  | 48866  |
#+---------+--------+--------+
#Explanation: 
#A new column bonus is created by doubling the value in the column salary.


employees = [
    {
        'name': 'Piper',
        'salary':4548
    },
    {
         'name': 'Grace',
        'salary':28150
    },
   {
        'name': 'Georgia',
        'salary':1103
    },
    {
         'name': 'Willow',
        'salary':6593
    },
    {
         'name': 'Finn',
        'salary':74576
    },
    {
         'name': 'Thomas',
        'salary':24433
    },  
]

print(employees)


import pandas as pd
employees = {
    'name': ['Piper', 'Grace', 'Georgia', 'Willow', 'Finn', 'Thomas'],
    'salary': [4548, 28150, 1103, 6593, 74576, 24433]
}

employees = pd.DataFrame(employees)

employees['bonus'] = employees['salary']* 2
print(employees)