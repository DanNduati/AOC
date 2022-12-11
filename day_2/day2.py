"""
Encrypted strategy guide
------------------------

| Opponent     	| Me           	|
|--------------	|--------------	|
| A - Rock     	| X - Rock     	|
| B - Paper    	| Y - Paper    	|
| C - Scissors 	| Z - Scissors 	|

Scores
------
- Total score = sum of scores for each round
- Score for single round = shape(1 for Rock, 2 for Paper, and 3 for Scissors) + Outcome(0 if you lost, 3 if the round was a draw, and 6 if you won)
"""
opponent_dict = {"A": "Rock", "B": "Paper", "C": "Scissors"}
me_dict = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}
total_score = total_score_2 = 0
with open("input.txt", "r") as fp:
    for opp, me in map(str.split, fp.read().splitlines()):
        opp, me = ord(opp) - ord("A"), ord(me) - ord("X")
        total_score += 1 + me + (me - opp + 1) % 3 * 3
        total_score_2 += 1 + me + (me + opp - 1) % 3
print(total_score)
print(total_score_2)
