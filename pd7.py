#DataFrame students
#+-------------+--------+
#| Column Name | Type   |
#+-------------+--------+
#| student_id  | int    |
#| name        | object |
#| age         | int    |
#+-------------+--------+
#There are some rows having missing values in the name column.

#Write a solution to remove the rows with missing values.

#The result format is in the following example.

 

#Example 1:

#Input:
#+------------+---------+-----+
#| student_id | name    | age |
#+------------+---------+-----+
#| 32         | Piper   | 5   |
#| 217        | None    | 19  |
#| 779        | Georgia | 20  |
#| 849        | Willow  | 14  |
#+------------+---------+-----+
#Output:
#+------------+---------+-----+
#| student_id | name    | age |
#+------------+---------+-----+
#| 32         | Piper   | 5   |
#| 779        | Georgia | 20  | 
#| 849        | Willow  | 14  | 
#+------------+---------+-----+
#Explanation: 
#Student with id 217 havs empty value in the name column, so it will be removed.


students = [
    {
        'student_id':32,
        'name':'Piper',
        'age': 5
    },
    {
        'student_id':217,
        'name':'None',
        'age': 19
    },
    {
        'student_id':779,
        'name':'Georgia',
        'age': 20
    },
    {
        'student_id':849,
        'name':'Willow',
        'age': 14
    }
]

print(students)


import pandas as pd


students = {
    'student_id': [32, 217, 779, 849],
    'name': ['Piper', None, 'Georgia', 'Willow'],
    'age': [5, 19, 20, 14]
}

students = pd.DataFrame(students)
students= students.dropna(subset= 'name')
print(students)