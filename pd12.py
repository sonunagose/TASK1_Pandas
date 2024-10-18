#DataFrame df1
#+-------------+--------+
#| Column Name | Type   |
#+-------------+--------+
#| student_id  | int    |
#| name        | object |
#| age         | int    |
#+-------------+--------+

#DataFrame df2
#+-------------+--------+
#| Column Name | Type   |
#+-------------+--------+
#| student_id  | int    |
#| name        | object |
#| age         | int    |
#+-------------+--------+

#Write a solution to concatenate these two DataFrames vertically into one DataFrame.

#The result format is in the following example.

 

#Example 1:

#Input:
#df1
#+------------+---------+-----+
#| student_id | name    | age |
#+------------+---------+-----+
#| 1          | Mason   | 8   |
#| 2          | Ava     | 6   |
#| 3          | Taylor  | 15  |
#| 4          | Georgia | 17  |
#+------------+---------+-----+
#df2
#+------------+------+-----+
#| student_id | name | age |
#+------------+------+-----+
#| 5          | Leo  | 7   |
#| 6          | Alex | 7   |
#+------------+------+-----+
#Output:
#+------------+---------+-----+
#| student_id | name    | age |
#+------------+---------+-----+
#| 1          | Mason   | 8   |
#| 2          | Ava     | 6   |
#| 3          | Taylor  | 15  |
#| 4          | Georgia | 17  |
#| 5          | Leo     | 7   |
#| 6          | Alex    | 7   |
#+------------+---------+-----+
#Explanation:
#The two DataFramess are stacked vertically, and their rows are combined.


df1 =  {
    'student_id': [1, 2, 3, 4],
    'name': ['Mason', 'Ava', 'Taylor', 'Georgia'],
    'age': [8, 6, 15, 17]
}

df2 = {
    'student_id': [5, 6],
    'name': ['Leo', 'Alex'],
    'age': [7, 7]
}

print(df1)
print()
print(df2)

import pandas as pd 

df1 = pd.DataFrame(df1)
df2 = pd.DataFrame(df2)


vertical_concat = pd.concat([df1, df2], axis=0)
print(vertical_concat)