#DataFrame students
#+-------------+--------+
#| Column Name | Type   |
#+-------------+--------+
#| student_id  | int    |
#| name        | object |
#| age         | int    |
#+-------------+--------+

#Write a solution to select the name and age of the student with student_id = 101.

#The result format is in the following example.

 

#Example 1:
#Input:
#+------------+---------+-----+
#| student_id | name    | age |
#+------------+---------+-----+
#| 101        | Ulysses | 13  |
#| 53         | William | 10  |
#| 128        | Henry   | 6   |
#| 3          | Henry   | 11  |
#+------------+---------+-----+
#Output:
#+---------+-----+
#| name    | age | 
#+---------+-----+
#| Ulysses | 13  |
#+---------+-----+
#Explanation:
#Student Ulysses has student_id = 101, we select the name and age.

students = [
    {
        'student_id': 101,
        'name': 'Ulysses',
        'age': 13
    },
    {
         'student_id': 53,
        'name': 'William',
        'age': 10
    },
    {
         'student_id': 128,
        'name': 'Henry',
        'age': 6
    },
    {
         'student_id': 3,
        'name': 'Henry',
        'age': 11
    }
]

print(students)

import pandas as pd

students = {
    'student_id': [101, 53, 128, 3],
    'name': ['Ulysses', 'William', 'Henry', 'Henry'],
    'age': [13, 10, 6, 11]
}

students = pd.DataFrame(students)

output = students[students['student_id'] == 101][['name', 'age']]

print(output)