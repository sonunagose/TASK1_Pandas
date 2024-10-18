#DataFrame students
#+-------------+--------+
#| Column Name | Type   |
#+-------------+--------+
#| id          | int    |
#| first       | object |
#| last        | object |
#| age         | int    |
#+-------------+--------+
#Write a solution to rename the columns as follows:

#id to student_id
#first to first_name
#last to last_name
#age to age_in_years
#The result format is in the following example.

 

#Example 1:
#Input:
#+----+---------+----------+-----+
#| id | first   | last     | age |
#+----+---------+----------+-----+
#| 1  | Mason   | King     | 6   |
#| 2  | Ava     | Wright   | 7   |
#| 3  | Taylor  | Hall     | 16  |
#| 4  | Georgia | Thompson | 18  |
#| 5  | Thomas  | Moore    | 10  |
#+----+---------+----------+-----+
#Output:
#+------------+------------+-----------+--------------+
#| student_id | first_name | last_name | age_in_years |
#+------------+------------+-----------+--------------+
#| 1          | Mason      | King      | 6            |
#| 2          | Ava        | Wright    | 7            |
#| 3          | Taylor     | Hall      | 16           |
#| 4          | Georgia    | Thompson  | 18           |
#| 5          | Thomas     | Moore     | 10           |
#+------------+------------+-----------+--------------+
#Explanation: 
#The column names are changed accordingly.



students = [
    {
        'id':1,
        'first':'Mason',
        'last':'King',
        'age':6
    },
    {
        'id':2,
        'first':'Ava',
        'last':'Wright',
        'age':7 
    },
    {
        'id':3,
        'first':'Taylor',
        'last':'Hall',
        'age':16
    },
    {
        'id':4,
        'first':'Georgia',
        'last':'Thompson',
        'age':18
    },
    {
        'id':5,
        'first':'Thomas',
        'last':'Moore',
        'age':10
    }
]

print(students)

import pandas as pd

students = {
    'id': [1, 2, 3, 4, 5],
    'first': ['Mason', 'Ava', 'Taylor', 'Georgia', 'Thomas'],
    'last': ['King', 'Wright', 'Hall', 'Thompson', 'Moore'],
    'age': [6, 7, 16, 18, 10]
}

students = pd.DataFrame(students)

stud_renamed= students.rename(columns={
    'id': 'student_id',
    'first': 'first_name',
    'last': 'last_name',
    'age': 'age_in_years'
})

print(stud_renamed)