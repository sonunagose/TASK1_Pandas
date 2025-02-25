#DataFrame players:
#+-------------+--------+
#| Column Name | Type   |
#+-------------+--------+
#| player_id   | int    |
#| name        | object |
#| age         | int    |
#| position    | object |
#| ...         | ...    |
#+-------------+--------+
#Write a solution to calculate and display the number of rows and columns of players.

#Return the result as an array:

#[number of rows, number of columns]

#The result format is in the following example.

 

#Example 1:

#Input:
#+-----------+----------+-----+-------------+--------------------+
#| player_id | name     | age | position    | team               |
#+-----------+----------+-----+-------------+--------------------+
#| 846       | Mason    | 21  | Forward     | RealMadrid         |
#| 749       | Riley    | 30  | Winger      | Barcelona          |
#| 155       | Bob      | 28  | Striker     | ManchesterUnited   |
#| 583       | Isabella | 32  | Goalkeeper  | Liverpool          |
#| 388       | Zachary  | 24  | Midfielder  | BayernMunich       |
#| 883       | Ava      | 23  | Defender    | Chelsea            |
#| 355       | Violet   | 18  | Striker     | Juventus           |
#| 247       | Thomas   | 27  | Striker     | ParisSaint-Germain |
#| 761       | Jack     | 33  | Midfielder  | ManchesterCity     |
#| 642       | Charlie  | 36  | Center-back | Arsenal            |
#+-----------+----------+-----+-------------+--------------------+
#Output:
#[10, 5]
#Explanation:
#This DataFrame contains 10 rows and 5 columns.


#Soln-

import pandas as pd

players = [
    {
       'player_id':846,
       'name': 'Mason',
       'age':21,
       'position': 'Forward',
       'team': 'RealMadrid'
    },
    {
       'player_id':749,
       'name': 'Riley',
       'age':30,
       'position': 'Winger',
       'team': 'Barcelona'
    },
    {
       'player_id':155,
       'name': 'Bob',
       'age':28,
       'position': 'Striker',
       'team': 'ManchesterUnited'
    },
    {
       'player_id':583,
       'name': 'Isabella',
       'age':32,
       'position': 'Goalkeeper',
       'team': 'Liverpool'
    },
    {
        'player_id':388,
       'name': 'Zachary',
       'age':24,
       'position': 'Midfielder',
       'team': 'BayernMunich'
    },
    {
        'player_id':883,
       'name': 'Ava',
       'age':23,
       'position': 'Defender',
       'team': 'Chelsea'
    },
    {
        'player_id':355,
       'name': 'Violet',
       'age':18,
       'position': 'Striker',
       'team': 'Juventus'
    },
    {
        'player_id':247,
       'name': 'Thomas',
       'age':27,
       'position': 'Striker',
       'team': 'ParisSaint-Germain'
    },
    {
        'player_id':761,
       'name': 'Jack',
       'age':33,
       'position': 'Midfielder',
       'team': 'ManchesterCity'
    },
    {
        'player_id':642,
       'name': 'Charlie',
       'age':36,
       'position': 'Center-back',
       'team': 'Arsenal'
    }
]

#print('players',players)



import pandas as pd


players = {
    'player_id': [846, 749, 155, 583, 388, 883, 355, 247, 761, 642],
    'name': ['Mason', 'Riley', 'Bob', 'Isabella', 'Zachary', 'Ava', 'Violet', 'Thomas', 'Jack', 'Charlie'],
    'age': [21, 30, 28, 32, 24, 23, 18, 27, 33, 36],
    'position': ['Forward', 'Winger', 'Striker', 'Goalkeeper', 'Midfielder', 'Defender', 'Striker', 'Striker', 'Midfielder', 'Center-back'],
    'team': ['RealMadrid', 'Barcelona', 'ManchesterUnited', 'Liverpool', 'BayernMunich', 'Chelsea', 'Juventus', 'ParisSaint-Germain', 'ManchesterCity', 'Arsenal']
}

players = pd.DataFrame(players)


num_rows, num_columns = players.shape


result = [num_rows, num_columns]
print(result)